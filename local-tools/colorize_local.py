#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
007.gallery — أداة التلوين المحلية (Local Photo Colorizer)
تعتمد على نموذج DDColor (ONNX) وتعمل بالكامل على جهازك.
Deps: numpy, onnxruntime, Pillow  (كلها موجودة عادةً؛ وإلا: pip3 install numpy onnxruntime pillow)

الاستخدام:
    python3 colorize_local.py صورة.jpg [صورة2.png ...]
    python3 colorize_local.py مجلد/
    python3 colorize_local.py --selftest      # يتحقق من صحة أنابيب الألوان دون النموذج
"""
import sys, os, urllib.request

MODEL_URL = "https://huggingface.co/aimi-models/editor-tools/resolve/main/colorize-ddcolor/ddcolor.onnx"
CACHE_DIR = os.path.expanduser("~/.cache/007-gallery")
MODEL_PATH = os.path.join(CACHE_DIR, "ddcolor.onnx")
EXTS = (".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff")

try:
    import numpy as np
    from PIL import Image
except ImportError as e:
    print("✗ ينقصك حزمة:", e.name, "\n  ثبّتها: pip3 install numpy pillow onnxruntime")
    sys.exit(1)

# ---------------- تحويلات الألوان sRGB <-> CIELAB (D65) ----------------
_D65 = np.array([0.95047, 1.0, 1.08883], dtype=np.float64)
_M   = np.array([[0.4124564, 0.3575761, 0.1804375],
                 [0.2126729, 0.7151522, 0.0721750],
                 [0.0193339, 0.1191920, 0.9503041]], dtype=np.float64)
_Minv = np.linalg.inv(_M)
_EPS, _KAPPA = 216/24389, 24389/27

def rgb_to_lab(rgb):                       # rgb float [0,1] HxWx3 -> Lab
    c = rgb.astype(np.float64)
    lin = np.where(c <= 0.04045, c/12.92, ((c+0.055)/1.055)**2.4)
    xyz = lin @ _M.T / _D65
    t = np.where(xyz > _EPS, np.cbrt(xyz), (_KAPPA*xyz + 16)/116)
    L = 116*t[..., 1] - 16
    a = 500*(t[..., 0] - t[..., 1])
    b = 200*(t[..., 1] - t[..., 2])
    return np.stack([L, a, b], axis=-1)

def lab_to_rgb(lab):                        # Lab -> rgb float [0,1]
    L, a, b = lab[..., 0], lab[..., 1], lab[..., 2]
    fy = (L + 16)/116
    fx = fy + a/500
    fz = fy - b/200
    f = np.stack([fx, fy, fz], axis=-1)
    f3 = f**3
    xyz = np.where(f3 > _EPS, f3, (116*f - 16)/_KAPPA) * _D65
    lin = xyz @ _Minv.T
    srgb = np.where(lin <= 0.0031308, 12.92*lin, 1.055*np.power(np.clip(lin,0,None), 1/2.4) - 0.055)
    return np.clip(srgb, 0, 1)

def _resize(arr, size):                     # arr HxWxC float -> PIL bilinear -> size=(W,H)
    chans = [np.asarray(Image.fromarray(arr[..., i].astype(np.float32), mode="F")
                        .resize(size, Image.BILINEAR), dtype=np.float32)
             for i in range(arr.shape[-1])]
    return np.stack(chans, axis=-1)

# ---------------- أنبوب DDColor ----------------
def preprocess(rgb, in_size):
    """rgb float[0,1] HxWx3 -> (tensor 1x3xSxS, L_original HxWx1)"""
    lab = rgb_to_lab(rgb)
    orig_L = lab[..., :1]
    small = _resize(rgb, (in_size, in_size))
    small_L = rgb_to_lab(small)[..., :1]
    gray_lab = np.concatenate([small_L, np.zeros((in_size, in_size, 2), np.float64)], axis=-1)
    gray_rgb = lab_to_rgb(gray_lab)                       # صورة رمادية 3 قنوات
    tensor = gray_rgb.transpose(2, 0, 1)[None].astype(np.float32)
    return tensor, orig_L

def postprocess(ab_out, orig_L):
    """ab_out 2xSxS  +  L الأصلية HxWx1 -> RGB uint8"""
    H, W = orig_L.shape[:2]
    ab = ab_out.transpose(1, 2, 0).astype(np.float64)     # SxSx2
    ab = _resize(ab, (W, H))
    lab = np.concatenate([orig_L, ab], axis=-1)
    rgb = lab_to_rgb(lab)
    return (rgb*255 + 0.5).clip(0, 255).astype(np.uint8)

# ---------------- الاختبار الذاتي (بدون النموذج) ----------------
def selftest():
    print("• اختبار دورة الألوان sRGB↔Lab …")
    rng = np.random.default_rng(0)
    rgb = rng.random((32, 48, 3))
    back = lab_to_rgb(rgb_to_lab(rgb))
    err = np.abs(back - rgb).max()
    assert err < 1e-4, f"round-trip error too high: {err}"
    print(f"  ✓ دقيقة (أقصى فرق {err:.2e})")

    print("• اختبار الأنبوب كاملاً بمخرَج ab=0 (يجب أن ينتج صورة رمادية بنفس الأبعاد) …")
    img = (rng.random((70, 90, 3)))
    tensor, orig_L = preprocess(img, 256)
    assert tensor.shape == (1, 3, 256, 256), tensor.shape
    fake_ab = np.zeros((2, 256, 256), np.float32)         # لا لون
    out = postprocess(fake_ab, orig_L)
    assert out.shape == (70, 90, 3), out.shape
    # ab=0 => رمادي: القنوات الثلاث متساوية تقريباً
    ch_spread = np.abs(out[..., 0].astype(int) - out[..., 1].astype(int)).mean()
    assert ch_spread < 2.0, f"expected near-gray, spread={ch_spread}"
    print(f"  ✓ الأبعاد صحيحة والناتج رمادي (تشتّت القنوات {ch_spread:.2f})")
    print("\n✅ نجح الاختبار الذاتي — رياضيات الألوان والأنبوب سليمة.")
    print("   (تلوين النموذج الفعلي يتطلب تنزيل DDColor وتشغيله على Chrome/جهازك.)")

# ---------------- التحميل والتشغيل ----------------
def download_model():
    if os.path.exists(MODEL_PATH) and os.path.getsize(MODEL_PATH) > 1_000_000:
        return
    os.makedirs(CACHE_DIR, exist_ok=True)
    print("⬇ تنزيل نموذج DDColor لأول مرة (~912MB) — مرة واحدة فقط…")
    tmp = MODEL_PATH + ".part"
    def hook(b, bs, total):
        if total > 0:
            pct = min(100, 100*b*bs/total)
            print(f"\r   {pct:5.1f}%", end="", flush=True)
    urllib.request.urlretrieve(MODEL_URL, tmp, hook)
    os.replace(tmp, MODEL_PATH)
    print("\n   ✓ اكتمل التنزيل.")

def load_session():
    import onnxruntime as ort
    download_model()
    print("• تحميل النموذج…")
    sess = ort.InferenceSession(MODEL_PATH, providers=["CPUExecutionProvider"])
    inp = sess.get_inputs()[0]
    shp = inp.shape
    in_size = shp[-1] if isinstance(shp[-1], int) and shp[-1] > 0 else 512
    return sess, inp.name, in_size

def colorize_file(sess, in_name, in_size, path, outdir):
    img = Image.open(path).convert("RGB")
    rgb = np.asarray(img, dtype=np.float64) / 255.0
    tensor, orig_L = preprocess(rgb, in_size)
    ab = sess.run(None, {in_name: tensor})[0][0]          # 2xSxS
    out = postprocess(ab, orig_L)
    base = os.path.splitext(os.path.basename(path))[0]
    dst = os.path.join(outdir, f"{base}_color.png")
    Image.fromarray(out).save(dst)
    return dst

def gather(paths):
    files = []
    for p in paths:
        if os.path.isdir(p):
            for f in sorted(os.listdir(p)):
                if f.lower().endswith(EXTS): files.append(os.path.join(p, f))
        elif os.path.isfile(p) and p.lower().endswith(EXTS):
            files.append(p)
    return files

def main():
    args = [a for a in sys.argv[1:] if a]
    if not args:
        print("الاستخدام: python3 colorize_local.py صورة.jpg | مجلد/ | --selftest")
        return
    if args[0] == "--selftest":
        selftest(); return
    files = gather(args)
    if not files:
        print("لم يُعثر على صور صالحة."); return
    sess, in_name, in_size = load_session()
    ok = 0
    for f in files:
        outdir = os.path.join(os.path.dirname(f) or ".", "colorized")
        os.makedirs(outdir, exist_ok=True)
        try:
            dst = colorize_file(sess, in_name, in_size, f, outdir)
            print(f"  ✓ {os.path.basename(dst)}"); ok += 1
        except Exception as e:
            print(f"  ✗ {os.path.basename(f)} — {e}")
    print(f"\nتمّ: {ok}/{len(files)} — الصور الملوّنة في مجلد colorized بجانب أصولها.")

if __name__ == "__main__":
    main()
