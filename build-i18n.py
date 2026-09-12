#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
007.gallery — فاصل اللغتين (AR في الجذر + EN تحت /en/)
© 2026 Artist Altayeb Amer / الفنان الطيب عامر

لماذا هذه البنية تحديداً:
  العربية تبقى في الجذر لأن الجمهور الأساسي عربي، ولأن كل رابط مفهرس
  حالياً (26 رابطاً) لا يتحرّك → صفر إعادة توجيه وصفر خسارة ترتيب.
  الإنجليزية تُولَّد تحت /en/ فيصبح لكل لغة رابط مستقل، وهو شرط hreflang.

ماذا يفعل:
  1. يُصلح ملفات المصدر العربية في مكانها (hreflang, og:locale, lang.js)
     — بعلامات i18n فالتشغيل المتكرر يستبدل ولا يُكرّر.
  2. يُولّد شجرة en/ كاملة من نفس المصدر → مصدر واحد، لا صيانة مزدوجة.
  3. يُعيد بناء sitemap.xml بالنسختين.

مبدأ أمان أساسي:
  لا يُحذف أي وسم داخل <script> أو <style>. فيها نصوص عربية موزّعة على
  أسطر متعددة داخل تسلسل سلاسل ('...' + '...') وأي حذف نصّي يُفسد الـ JS.
  الـ CSS القائم (html[lang=en] [data-ar]{display:none}) يتولّاها وقت
  التشغيل، وهي رسائل حالة لا محتوى فهرسة.

الاستخدام:  python3 build-articles.py && python3 build-i18n.py
"""
import os, re, shutil, json, importlib.util
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://007.gallery"
OUT  = os.path.join(HERE, "en")

# ════════════════════════════════════════════════════════════
#  العناوين والأوصاف الإنجليزية للصفحات المكتوبة يدوياً
#  (العنوان و<meta description> نصّان مفردان لا وسمان ثنائيان،
#   فلا يمكن استخراجهما آلياً — مكتوبة هنا بوعي لاستهداف البحث)
# ════════════════════════════════════════════════════════════
META = {
"index.html": dict(
  title="007.gallery — Free Professional Image Tools, Fully Private",
  desc="Seven free image tools that run entirely inside your browser — background removal, AI upscaling, compression, OCR, QR codes and watermarking. No sign-up, no upload.",
  og_title="007.gallery — Seven Free Image Tools, No Upload",
  og_desc="Background removal, AI upscaling, compression, OCR, QR and watermarking — all running inside your browser, free and completely private."),
"articles/index.html": dict(
  title="Image Editing Guides — 007.gallery",
  desc="Short, practical guides on image editing: removing backgrounds, image formats, AI upscaling and extracting text from images.",
  og_title="Image Editing Guides — 007.gallery",
  og_desc="Practical guides on image editing and browser-based AI."),
"contact.html": dict(
  title="Contact Us — 007.gallery",
  desc="Get in touch with the 007.gallery team — tool ideas, bug reports, partnerships and commissions. Every message is read.",
  og_title="Contact Us — 007.gallery",
  og_desc="Get in touch with the 007.gallery team."),
"projects.html": dict(
  title="Projects by Artist Altayeb Amer — 007.gallery",
  desc="Digital projects by Artist Altayeb Amer: browser image tools, Arabic calligraphy, data analysis and a distraction-free digital Quran.",
  og_title="Projects by Artist Altayeb Amer",
  og_desc="Digital projects in image editing, Arabic calligraphy and AI."),
"privacy.html": dict(
  title="Privacy Policy — 007.gallery",
  desc="Privacy policy for 007.gallery — all image processing happens inside your browser and your images are never uploaded to any server.",
  og_title="Privacy Policy — 007.gallery",
  og_desc="All image processing happens inside your browser — your images are never uploaded."),
"404.html": dict(
  title="Page Not Found — 007.gallery",
  desc="This page could not be found, but all seven free image tools are still here.",
  og_title="Page Not Found — 007.gallery",
  og_desc="This page could not be found."),
"services/background-removal.html": dict(
  title="Remove Image Background Free — No Upload — 007.gallery",
  desc="Remove the background from any image automatically with AI, running locally in your browser via WebGPU. Nothing is uploaded, nothing leaves your device.",
  og_title="Remove Image Background Free — 007.gallery",
  og_desc="Automatic AI background removal inside your browser — no upload, complete privacy."),
"services/convert-compress.html": dict(
  title="Convert & Compress Images — WebP, JPG, PNG — 007.gallery",
  desc="Convert, compress and resize your images between WebP, JPG and PNG in batches — locally in your browser, with no upload.",
  og_title="Convert & Compress Images — 007.gallery",
  og_desc="Convert, compress and resize between WebP, JPG and PNG in one batch — locally, no upload."),
"services/ocr.html": dict(
  title="Extract Text from Images (OCR) — Arabic & English — 007.gallery",
  desc="Turn images and documents into editable text in Arabic and English — processed locally in your browser, free and unlimited.",
  og_title="Extract Text from Images (OCR) — 007.gallery",
  og_desc="Turn images and documents into editable text — Arabic and English, free, in your browser."),
"services/portrait-blur.html": dict(
  title="Portrait Background Blur (Bokeh) — 007.gallery",
  desc="A professional bokeh effect that isolates your subject and blurs the background — running locally in your browser via WebGPU.",
  og_title="Portrait Background Blur — 007.gallery",
  og_desc="A professional bokeh effect that isolates your subject and blurs the background — free, in your browser."),
"services/qr.html": dict(
  title="Pro QR Code Generator with Logo — 007.gallery",
  desc="Create elegant QR codes in your own colours with your logo, at resolutions up to 4096px with SVG export — free, instant, in your browser.",
  og_title="Pro QR Code Generator with Logo — 007.gallery",
  og_desc="Elegant QR codes in your colours with your logo, up to 4096px — free and instant."),
"services/upscale.html": dict(
  title="AI Image Upscaler — Enlarge Without Losing Quality — 007.gallery",
  desc="Double the size and sharpness of your images with AI — running locally in your browser via WebGPU, with no upload.",
  og_title="AI Image Upscaler — 007.gallery",
  og_desc="Double the size and sharpness of your images with AI, locally in your browser — free."),
"services/watermark.html": dict(
  title="Add a Watermark to Images (Batch) — 007.gallery",
  desc="Add your text or logo watermark to many images at once, or blur a region to hide it — processed locally in your browser.",
  og_title="Add a Watermark to Images — 007.gallery",
  og_desc="Watermark many images at once, or blur a region to hide it — free, in your browser."),
}

# صفحات لا تُفهرس ولا تُنسخ
SKIP = {"services/_diagnostics.html"}
# صفحات تُنسخ لكن بلا canonical/hreflang ولا سايت ماب
NOINDEX = {"404.html"}

PRIORITY = {"/": "1.0", "/articles/": "0.9"}


# ════════════════════════════════════════════════════════════
#  أدوات
# ════════════════════════════════════════════════════════════
def clean_url(rel):
    """مسار الملف → الرابط النظيف (Cloudflare Pages يحوّل .html بـ308)"""
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return "/" + rel[:-len("index.html")]
    return "/" + rel[:-len(".html")]


def load_articles():
    """يقرأ بيانات المقالات من المولّد نفسه — مصدر واحد للعنوان الإنجليزي"""
    path = os.path.join(HERE, "build-articles.py")
    spec = importlib.util.spec_from_file_location("ba", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return {a["slug"]: a for a in mod.ARTICLES}


def protect(s):
    """يُخرج <script> و<style> من متناول أي حذف وسوم"""
    store = []
    def keep(m):
        store.append(m.group(0))
        return "\x00%d\x00" % (len(store) - 1)
    s = re.sub(r"<script\b.*?</script>", keep, s, flags=re.S | re.I)
    s = re.sub(r"<style\b.*?</style>",  keep, s, flags=re.S | re.I)
    return s, store


def restore(s, store):
    return re.sub(r"\x00(\d+)\x00", lambda m: store[int(m.group(1))], s)


def strip_balanced(s, open_pat, tag):
    """يحذف عنصراً كاملاً مع محتواه، بعدّ الوسوم المتداخلة من نفس النوع.
       ضروري لأن <span data-ar>مولّد <span>QR</span> احترافي</span>
       يحتوي span داخلياً، والمطابقة غير الجَشِعة تتوقف عند الإغلاق الخطأ."""
    rx_open  = re.compile(open_pat, re.I)
    rx_any   = re.compile(r"<%s\b|</%s\s*>" % (tag, tag), re.I)
    while True:
        m = rx_open.search(s)
        if not m:
            return s
        depth = 0
        end = None
        for t in rx_any.finditer(s, m.start()):
            depth += -1 if t.group(0).startswith("</") else 1
            if depth == 0:
                end = t.end()
                break
        if end is None:            # وسم غير مغلق — لا نلمسه
            return s
        s = s[:m.start()] + s[end:]


def absolutize(s, depth):
    """الأصول المشتركة تصير جذرية، فلا تتأثر بزيادة عمق /en/.
       روابط الصفحات تبقى نسبية كي تبقى داخل شجرة /en/."""
    for asset in ("assets/", "favicon.ico", "manifest.webmanifest", "humans.txt"):
        for pre in ("../../", "../", ""):
            s = s.replace('href="%s%s' % (pre, asset), 'href="/%s' % asset)
            s = s.replace('src="%s%s'  % (pre, asset), 'src="/%s'  % asset)
    # روابط صفحات مكتوبة جذرية أصلاً → داخل /en/
    s = re.sub(r'href="/(services|articles)/', r'href="/en/\1/', s)
    s = re.sub(r'href="/"', 'href="/en/"', s)
    # بيانات المقالات تُقرأ من الجذر
    s = s.replace("'../data/", "'/data/").replace('"../data/', '"/data/')
    return s


HREF_MARK_A = "<!-- i18n:alternates -->"
HREF_MARK_B = "<!-- /i18n:alternates -->"

def alternates(url_ar):
    en = "/en/" if url_ar == "/" else "/en" + url_ar
    return (HREF_MARK_A + "\n"
            '<link rel="alternate" hreflang="ar" href="%s%s">\n'
            '<link rel="alternate" hreflang="en" href="%s%s">\n'
            '<link rel="alternate" hreflang="x-default" href="%s%s">\n'
            % (SITE, url_ar, SITE, en, SITE, url_ar)
            + HREF_MARK_B)


def set_alternates(s, url_ar):
    block = alternates(url_ar)
    if HREF_MARK_A in s:                      # تشغيل متكرر → استبدال
        return re.sub(re.escape(HREF_MARK_A) + r".*?" + re.escape(HREF_MARK_B),
                      lambda m: block, s, flags=re.S)
    # المقالات تحمل hreflang من قالب المولّد أصلاً
    if 'hreflang="x-default"' in s:
        return s
    m = re.search(r'<link rel="canonical"[^>]*>', s)
    if not m:
        return s
    return s[:m.end()] + "\n" + block + s[m.end():]


def ensure_lang_js(s):
    if "/assets/lang.js" in s:
        return s
    m = re.search(r'<script src="(?:\.\./)*assets/guardian\.js" defer></script>', s)
    tag = '<script src="/assets/lang.js" defer></script>'
    if m:
        return s[:m.start()] + tag + "\n" + s[m.start():]
    return s.replace("</head>", tag + "\n</head>", 1)


def kill_lang_memory(s):
    """لكل لغة رابط مستقل الآن، فقلب اللغة من localStorage صار خطأ:
       كان يُظهر الإنجليزية على رابط عربي."""
    return s.replace("localStorage.getItem('gallery_lang')", "/*i18n*/null")


def fix_jsonld_url(s, url):
    return re.sub(r'("url":\s*")https://007\.gallery/[^"]*(")',
                  lambda m: m.group(1) + SITE + url + m.group(2), s)


# ════════════════════════════════════════════════════════════
#  إصلاح المصدر العربي في مكانه
# ════════════════════════════════════════════════════════════
def patch_arabic(rel, url):
    p = os.path.join(HERE, rel)
    s0 = open(p, encoding="utf-8").read()
    s = s0
    if rel not in NOINDEX:
        s = set_alternates(s, url)
        if "og:locale" not in s:
            m = re.search(r'<meta property="og:url"[^>]*>', s)
            if m:
                s = (s[:m.end()] + '\n<meta property="og:locale" content="ar_AR">'
                     '\n<meta property="og:locale:alternate" content="en_US">' + s[m.end():])
        elif "og:locale:alternate" not in s:
            s = s.replace('<meta property="og:locale" content="ar_AR">',
                          '<meta property="og:locale" content="ar_AR">\n'
                          '<meta property="og:locale:alternate" content="en_US">', 1)
        s = fix_jsonld_url(s, url)
    s = ensure_lang_js(s)
    s = kill_lang_memory(s)
    # العدد الصحيح سبع أدوات — كان النص يقول ١٥ أداة
    s = s.replace("١٥ أداة ذكية للصور", "سبع أدوات ذكية للصور")
    if s != s0:
        open(p, "w", encoding="utf-8").write(s)
        return True
    return False


# ════════════════════════════════════════════════════════════
#  توليد النسخة الإنجليزية
# ════════════════════════════════════════════════════════════
def ltr_fixes(s):
    """ما كانت toggleLang() القديمة تضبطه وقت التشغيل صار يجب أن يكون
       صحيحاً في HTML الثابت، لأن الزر لم يعد يقلب الصفحة بل ينتقل.
       والصواب الثابت أفضل على أي حال: لا وميض قبل عمل JS، وصحيح للزاحف."""
    # سهم «افتح الأداة» يتبع اتجاه القراءة
    s = s.replace('<span class="arrow">\u2190</span>', '<span class="arrow">\u2192</span>')
    # سهم الرجوع للرئيسية: SVG يشير يساراً، يُقلب في LTR
    s = s.replace('id="homeArrow">', 'id="homeArrow" style="transform:rotate(180deg)">')
    # حرفا اسم الفنان في الشعار الدائري
    s = s.replace('<div class="avatar">\u0637\u0639</div>', '<div class="avatar">AA</div>')
    # نص <option> يُبنى إنجليزياً مباشرةً بدل الانتظار حتى تُصحّحه
    # syncSelectLabels() — كانت تعرض «\u0623\u0628\u064a\u0636 \u00b7 White» لحظةً قبل عمل JS
    s = re.sub(r'(<option\b[^>]*\bdata-label-en="([^"]*)"[^>]*>)[^<]*(</option>)',
               lambda m: m.group(1) + m.group(2) + m.group(3), s)
    return s


def build_english(rel, url, meta):
    src = open(os.path.join(HERE, rel), encoding="utf-8").read()
    depth = rel.count("/")

    s, store = protect(src)
    # حذف المحتوى العربي — خارج <script> و<style> فقط
    s = strip_balanced(s, r"<span\s+data-ar\s*>", "span")
    # أي <div> يحمل صنفاً ينتهي بـ -ar مهما رافقه من أصناف أخرى.
    # المطابقة الحرفية لا تكفي: الموجود فعلاً class="related art-ar"
    # وclass="guides seo-ar" وclass="doc doc-ar".
    s = strip_balanced(
        s, r'<div[^>]*\bclass="[^"]*\b(?:art|seo|doc|block)-ar\b[^"]*"[^>]*>', "div")
    s = restore(s, store)

    # لغة الصفحة
    s = s.replace('<html lang="ar" dir="rtl"', '<html lang="en" dir="ltr"', 1)

    # الرأس
    if meta:
        s = re.sub(r"<title>.*?</title>",
                   lambda m: "<title>%s</title>" % meta["title"], s, count=1, flags=re.S)
        s = re.sub(r'(<meta name="description" content=")[^"]*(")',
                   lambda m: m.group(1) + meta["desc"] + m.group(2), s, count=1)
        s = re.sub(r'(<meta property="og:title" content=")[^"]*(")',
                   lambda m: m.group(1) + meta["og_title"] + m.group(2), s, count=1)
        s = re.sub(r'(<meta property="og:description" content=")[^"]*(")',
                   lambda m: m.group(1) + meta["og_desc"] + m.group(2), s, count=1)

    en_url = "/en/" if url == "/" else "/en" + url
    if rel not in NOINDEX:
        s = re.sub(r'(<link rel="canonical" href=")[^"]*(")',
                   lambda m: m.group(1) + SITE + en_url + m.group(2), s, count=1)
        s = re.sub(r'(<meta property="og:url" content=")[^"]*(")',
                   lambda m: m.group(1) + SITE + en_url + m.group(2), s, count=1)
        s = set_alternates(s, url)
        s = fix_jsonld_url(s, en_url)
    s = s.replace('<meta property="og:locale" content="ar_AR">',
                  '<meta property="og:locale" content="en_US">')
    s = s.replace('<meta property="og:locale:alternate" content="en_US">',
                  '<meta property="og:locale:alternate" content="ar_AR">')
    s = s.replace('"inLanguage": [\n  "ar",\n  "en"\n ]', '"inLanguage": "en"')
    s = s.replace('"inLanguage":["ar","en"]', '"inLanguage":"en"')

    s = ltr_fixes(s)
    s = absolutize(s, depth)
    s = kill_lang_memory(s)
    s = ensure_lang_js(s)

    dest = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    open(dest, "w", encoding="utf-8").write(s)


# ════════════════════════════════════════════════════════════
def collect():
    pages = []
    for rel in ["index.html", "contact.html", "projects.html", "privacy.html", "404.html",
                "articles/index.html"]:
        pages.append(rel)
    for f in sorted(os.listdir(os.path.join(HERE, "services"))):
        rel = "services/" + f
        if f.endswith(".html") and rel not in SKIP:
            pages.append(rel)
    for f in sorted(os.listdir(os.path.join(HERE, "articles"))):
        if f.endswith(".html") and f != "index.html":
            pages.append("articles/" + f)
    return pages


def sitemap(urls):
    today = date.today().isoformat()
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
             '        xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for u in urls:
        en = "/en/" if u == "/" else "/en" + u
        pr = PRIORITY.get(u, "0.9" if u.startswith("/services/")
                          else "0.8" if u.startswith("/articles/")
                          else "0.4" if u == "/privacy" else "0.6")
        for loc, alt_self in ((u, u), (en, en)):
            lines.append("  <url>")
            lines.append("    <loc>%s%s</loc>" % (SITE, loc))
            lines.append('    <xhtml:link rel="alternate" hreflang="ar" href="%s%s"/>' % (SITE, u))
            lines.append('    <xhtml:link rel="alternate" hreflang="en" href="%s%s"/>' % (SITE, en))
            lines.append('    <xhtml:link rel="alternate" hreflang="x-default" href="%s%s"/>' % (SITE, u))
            lines.append("    <lastmod>%s</lastmod>" % today)
            lines.append("    <changefreq>weekly</changefreq>")
            lines.append("    <priority>%s</priority>" % pr)
            lines.append("  </url>")
    lines.append("</urlset>")
    open(os.path.join(HERE, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    return len(urls) * 2


def main():
    arts = load_articles()
    pages = collect()

    if os.path.isdir(OUT):
        shutil.rmtree(OUT)          # إعادة بناء كاملة → لا بقايا من تشغيل سابق

    patched = 0
    indexed = []
    for rel in pages:
        url = clean_url(rel)
        meta = META.get(rel)
        if meta is None and rel.startswith("articles/"):
            a = arts.get(os.path.basename(rel)[:-5])
            if a:
                meta = dict(title=a["title_en"] + " — 007.gallery", desc=a["desc_en"],
                            og_title=a["title_en"], og_desc=a["desc_en"])
        if patch_arabic(rel, url):
            patched += 1
        build_english(rel, url, meta)
        if rel not in NOINDEX:
            indexed.append(url)

    n = sitemap(indexed)
    print("  ✓ %d صفحة عربية مُصلحة" % patched)
    print("  ✓ %d صفحة إنجليزية في en/" % len(pages))
    print("  ✓ sitemap.xml — %d رابطاً (%d لكل لغة)" % (n, n // 2))


if __name__ == "__main__":
    main()
