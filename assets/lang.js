/*
  ════════════════════════════════════════════════════════════
   007.gallery — مبدّل اللغة (نسختان مستقلتان AR / EN)
   Creator : Artist Altayeb Amer
   المبتكر  : الفنان الطيب عامر
   © 2026 Artist Altayeb Amer — All rights reserved.
  ════════════════════════════════════════════════════════════

  قبل فصل /en/ كان زر اللغة يقلب الـ CSS داخل نفس الصفحة.
  الآن لكل لغة رابط مستقل، فالزر يجب أن *ينتقل* لا أن يقلب:
  العربية في الجذر (x-default) والإنجليزية تحت /en/.

  يُحمَّل بـ defer فيعمل بعد السكربتات المضمّنة في كل صفحة،
  ومن ثم يستبدل toggleLang() القديمة المعرّفة داخلها.
*/
(function (global) {
  "use strict";

  var doc = global.document;

  /* مسار النسخة المقابلة للصفحة الحالية */
  function counterpart(path) {
    if (path === "/en" || path === "/en/") return "/";
    if (path.indexOf("/en/") === 0) return path.slice(3);
    return path === "/" ? "/en/" : "/en" + path;
  }

  function isEnglish() {
    return doc.documentElement.getAttribute("lang") === "en";
  }

  /* يستبدل النسخة المضمّنة في الصفحة */
  global.toggleLang = function () {
    var loc = global.location;
    loc.href = counterpart(loc.pathname) + loc.search + loc.hash;
  };

  function label() {
    var btn = doc.getElementById("langBtn");
    if (!btn) return;
    var en = isEnglish();
    btn.textContent = en ? "ع" : "EN";
    btn.setAttribute("lang", en ? "ar" : "en");
    btn.setAttribute("title", en ? "اقرأ بالعربية" : "Read in English");
    btn.setAttribute("aria-label", en ? "التبديل إلى العربية" : "Switch to English");
  }

  /* يُصحّح اللغة إن قلبتها نسخة مضمّنة قديمة قبل تحميل هذا الملف */
  function enforce() {
    var h = doc.documentElement;
    var en = global.location.pathname.indexOf("/en") === 0;
    h.setAttribute("lang", en ? "en" : "ar");
    h.setAttribute("dir", en ? "ltr" : "rtl");
    label();
  }

  global.I18N = { counterpart: counterpart };

  if (doc.readyState === "loading")
    doc.addEventListener("DOMContentLoaded", enforce);
  else enforce();
})(typeof window !== "undefined" ? window : globalThis);
