#!/bin/bash
# ============================================================
# 007.gallery — أداة التكبير المحلية (Local Upscaler)
# تعتمد على محرّك Upscayl (Real-ESRGAN NCNN/Vulkan) المثبّت على جهازك.
# انقر نقراً مزدوجاً، أو اسحب صوراً/مجلداً فوق أيقونتها.
# ============================================================
set -euo pipefail

UP="/Applications/Upscayl.app/Contents/Resources"
BIN="$UP/bin/upscayl-bin"
MODELS="$UP/models"

# ---------- ألوان ----------
B=$'\033[1m'; G=$'\033[0;32m'; Y=$'\033[0;33m'; C=$'\033[0;36m'; R=$'\033[0;31m'; N=$'\033[0m'

clear 2>/dev/null || true
echo "${C}${B}"
echo "   ╔══════════════════════════════════════════╗"
echo "   ║        007.gallery · التكبير المحلي        ║"
echo "   ║        Local AI Upscaler (Upscayl)        ║"
echo "   ╚══════════════════════════════════════════╝"
echo "${N}"

# ---------- تحقق من وجود Upscayl ----------
if [ ! -x "$BIN" ]; then
  echo "${R}✗ لم يُعثر على Upscayl في /Applications/Upscayl.app${N}"
  echo "  ثبّت Upscayl من upscayl.org ثم أعد المحاولة."
  echo; read -r -p "اضغط Enter للإغلاق… " _; exit 1
fi
echo "${G}✓ محرّك Upscayl جاهز${N}  (Real-ESRGAN · Vulkan)"
echo

# ---------- اجمع ملفات الإدخال ----------
INPUTS=()
if [ "$#" -gt 0 ]; then
  INPUTS=("$@")                                  # مسحوبة فوق الأيقونة
else
  echo "${Y}اسحب صورة أو مجلداً إلى هذه النافذة ثم اضغط Enter"
  echo "(أو اسحب عدة عناصر):${N}"
  read -r -e LINE
  # فكّ المسارات المفصولة بمسافات مع دعم علامات التنصيص/الهروب
  eval "INPUTS=($LINE)"
fi
if [ "${#INPUTS[@]}" -eq 0 ]; then
  echo "${R}لم تُحدَّد أي صور.${N}"; read -r -p "اضغط Enter… " _; exit 1
fi

# ---------- الخيارات ----------
echo
echo "${B}معامل التكبير:${N}  1) 2x    2) 3x    4) 4x ${C}(افتراضي)${N}"
read -r -p "اختر [Enter=4x]: " S
case "${S:-}" in 1) SCALE=2;; 2) SCALE=3;; 3) SCALE=4;; *) SCALE=4;; esac

echo
echo "${B}النموذج:${N}"
echo "  1) realesrgan-x4plus       ${C}(عام · افتراضي)${N}"
echo "  2) realesrgan-x4plus-anime (رسوم/أنمي)"
echo "  3) realesrgan-x4fast       (أسرع)"
echo "  4) ultrasharp              (حِدّة عالية)"
echo "  5) remacri                 (واقعي ناعم)"
read -r -p "اختر [Enter=1]: " M
case "${M:-}" in 2) MODEL=realesrgan-x4plus-anime;; 3) MODEL=realesr-animevideov3;; 4) MODEL=ultrasharp;; 5) MODEL=remacri;; *) MODEL=realesrgan-x4plus;; esac

echo
echo "${B}صيغة الإخراج:${N}  1) png ${C}(افتراضي)${N}   2) jpg   3) webp"
read -r -p "اختر [Enter=png]: " F
case "${F:-}" in 2) FMT=jpg;; 3) FMT=webp;; *) FMT=png;; esac

# ---------- عالِج ----------
shopt -s nullglob nocaseglob
count=0; ok=0; fail=0
process_one () {
  local in="$1" outdir="$2"
  local base; base="$(basename "$in")"; base="${base%.*}"
  local out="$outdir/${base}_x${SCALE}.${FMT}"
  count=$((count+1))
  printf "  ${C}⏳${N} %s → x%s …\n" "$(basename "$in")" "$SCALE"
  if "$BIN" -i "$in" -o "$out" -s "$SCALE" -n "$MODEL" -m "$MODELS" -f "$FMT" >/dev/null 2>&1; then
    printf "     ${G}✓ %s${N}\n" "$(basename "$out")"; ok=$((ok+1))
  else
    printf "     ${R}✗ فشل${N}\n"; fail=$((fail+1))
  fi
}

echo
echo "${B}جارٍ التكبير…${N}"
for item in "${INPUTS[@]}"; do
  [ -e "$item" ] || { echo "  ${Y}تخطّي (غير موجود): $item${N}"; continue; }
  if [ -d "$item" ]; then
    OUT="$item/upscaled"; mkdir -p "$OUT"
    for f in "$item"/*.{png,jpg,jpeg,webp}; do [ -e "$f" ] && process_one "$f" "$OUT"; done
  else
    OUT="$(dirname "$item")/upscaled"; mkdir -p "$OUT"
    process_one "$item" "$OUT"
  fi
done

echo
echo "${G}${B}تمّ.${N}  الناتج: ${ok}  ·  الفشل: ${fail}  ·  الإجمالي: ${count}"
echo "الصور المكبّرة في مجلد ${B}upscaled${N} بجانب صورك الأصلية."
echo
read -r -p "اضغط Enter للإغلاق… " _
