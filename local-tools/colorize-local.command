#!/bin/bash
# ============================================================
# 007.gallery — أداة التلوين المحلية (Local Photo Colorizer)
# تشغّل colorize_local.py (نموذج DDColor · ONNX) على جهازك.
# انقر نقراً مزدوجاً، أو اسحب صوراً/مجلداً فوق أيقونتها.
# ============================================================
set -uo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
PY="$DIR/colorize_local.py"

B=$'\033[1m'; G=$'\033[0;32m'; Y=$'\033[0;33m'; C=$'\033[0;36m'; R=$'\033[0;31m'; N=$'\033[0m'
clear 2>/dev/null || true
echo "${C}${B}"
echo "   ╔══════════════════════════════════════════╗"
echo "   ║        007.gallery · تلوين الصور          ║"
echo "   ║        Local AI Colorizer (DDColor)       ║"
echo "   ╚══════════════════════════════════════════╝"
echo "${N}"

# تحقق من بايثون
if ! command -v python3 >/dev/null 2>&1; then
  echo "${R}✗ لا يوجد python3 على جهازك.${N}  ثبّت Python 3 من python.org ثم أعد المحاولة."
  read -r -p "اضغط Enter… " _; exit 1
fi
# تحقق من الحزم (وتثبيتها إن لزم)
if ! python3 -c "import numpy,PIL,onnxruntime" >/dev/null 2>&1; then
  echo "${Y}تثبيت الحزم المطلوبة لأول مرة (numpy · pillow · onnxruntime)…${N}"
  python3 -m pip install --quiet numpy pillow onnxruntime || {
    echo "${R}تعذّر التثبيت. جرّب يدوياً: pip3 install numpy pillow onnxruntime${N}"
    read -r -p "اضغط Enter… " _; exit 1; }
fi
echo "${G}✓ البيئة جاهزة${N}"
echo

# اجمع المدخلات
INPUTS=()
if [ "$#" -gt 0 ]; then
  INPUTS=("$@")
else
  echo "${Y}اسحب صورة أو مجلداً إلى هذه النافذة ثم اضغط Enter:${N}"
  read -r -e LINE
  eval "INPUTS=($LINE)"
fi
if [ "${#INPUTS[@]}" -eq 0 ]; then
  echo "${R}لم تُحدَّد أي صور.${N}"; read -r -p "اضغط Enter… " _; exit 1
fi

echo "${C}ملاحظة:${N} أول تشغيل سيُنزّل نموذج DDColor (~912MB) مرة واحدة ويُخزَّن."
echo "${B}جارٍ التلوين…${N}"
echo
python3 "$PY" "${INPUTS[@]}"

echo
read -r -p "اضغط Enter للإغلاق… " _
