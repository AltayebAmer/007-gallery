/* ════════════════════════════════════════════════════════════
   007.gallery — شريط معرض الفنان الطيب عامر  v1.0
   © 2026 Artist Altayeb Amer / الفنان الطيب عامر
   ────────────────────────────────────────────────────────────
   يعرض ٧ خانات تربط بالتخصصات الفنية السبعة على altayebamer.com
   الاستخدام:  <div data-art-gallery></div>
   البيانات :  data/artgallery.json  (أضف img لعرض لوحة حقيقية)
   ════════════════════════════════════════════════════════════ */
(function (global) {
  "use strict";

  const T = () => document.documentElement.getAttribute("lang") === "en";

  const CSS = `
  .ag-wrap{margin:44px 0}
  .ag-head{text-align:center;margin-bottom:22px}
  .ag-head h2{font-size:clamp(20px,3vw,27px);font-weight:900;letter-spacing:-.3px}
  .ag-head h2 em{font-style:normal;background:linear-gradient(120deg,var(--gold),var(--gold-2));
    -webkit-background-clip:text;background-clip:text;color:transparent}
  .ag-head p{color:var(--txt-dim);font-size:14.5px;margin-top:9px;max-width:560px;margin-inline:auto;line-height:1.85}
  .ag-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:12px}
  @media(max-width:1000px){.ag-grid{grid-template-columns:repeat(4,1fr)}}
  @media(max-width:680px){.ag-grid{grid-template-columns:repeat(2,1fr)}}
  .ag-tile{position:relative;border-radius:15px;overflow:hidden;aspect-ratio:3/4;
    border:1px solid var(--line);display:block;transition:.24s;text-decoration:none;
    background-size:cover;background-position:center}
  .ag-tile:hover{transform:translateY(-6px);border-color:var(--gold);
    box-shadow:0 14px 34px rgba(0,0,0,.45)}
  .ag-tile .ag-veil{position:absolute;inset:0;
    background:linear-gradient(180deg,transparent 30%,rgba(0,0,0,.78) 100%)}
  .ag-tile .ag-ico{position:absolute;top:12px;inset-inline-start:12px;font-size:22px;
    filter:drop-shadow(0 2px 6px rgba(0,0,0,.6))}
  .ag-tile .ag-txt{position:absolute;inset-inline:0;bottom:0;padding:14px 12px;text-align:center}
  .ag-tile h3{font-size:13.5px;font-weight:900;color:#fff;line-height:1.35;
    text-shadow:0 2px 8px rgba(0,0,0,.7)}
  .ag-tile p{font-size:11px;margin-top:4px;line-height:1.5;opacity:.92}
  .ag-foot{text-align:center;margin-top:20px}
  .ag-foot a{display:inline-flex;align-items:center;gap:8px;font-size:14px;font-weight:800;
    color:var(--gold-2);border:1px solid var(--line-2);padding:11px 22px;border-radius:12px;transition:.16s}
  .ag-foot a:hover{border-color:var(--gold);background:var(--gold-soft)}
  `;

  function injectCss() {
    if (document.getElementById("ag-css")) return;
    const st = document.createElement("style");
    st.id = "ag-css"; st.textContent = CSS;
    document.head.appendChild(st);
  }

  function tile(it, en) {
    const bg = it.img
      ? `background-image:linear-gradient(180deg,transparent,rgba(0,0,0,.2)),url('${it.img}')`
      : `background-image:linear-gradient(150deg, ${it.c1}, ${it.c2})`;
    return `<a class="ag-tile" href="${it.url}" target="_blank" rel="noopener"
       style="${bg}" data-art="${it.id}">
      <span class="ag-veil"></span>
      <span class="ag-ico">${it.icon}</span>
      <span class="ag-txt">
        <h3>${en ? it.title_en : it.title_ar}</h3>
        <p style="color:${it.accent}">${en ? it.desc_en : it.desc_ar}</p>
      </span>
    </a>`;
  }

  let DATA = null;

  function paint() {
    if (!DATA) return;
    const en = T();
    document.querySelectorAll("[data-art-gallery]").forEach(host => {
      host.innerHTML =
        `<div class="ag-wrap">
           <div class="ag-head">
             <h2>${en ? "From the studio of <em>Altayeb Amer</em>"
                      : "من مرسم <em>الطيب عامر</em>"}</h2>
             <p>${en ? "Seven artistic disciplines by the creator of this site — step inside the gallery."
                     : "سبعة تخصصات فنية لمبتكر هذا الموقع — تفضّل بزيارة المعرض."}</p>
           </div>
           <div class="ag-grid">${DATA.items.map(i => tile(i, en)).join("")}</div>
           <div class="ag-foot">
             <a href="${DATA.site}" target="_blank" rel="noopener">
               ${en ? "Visit the full gallery →" : "زُر المعرض كاملاً ←"}
             </a>
           </div>
         </div>`;
    });
  }

  function load() {
    if (!document.querySelector("[data-art-gallery]")) return;
    injectCss();
    // اعثر على مسار البيانات نسبةً إلى عمق الصفحة
    const depth = (location.pathname.replace(/\/[^/]*$/, "/").match(/\//g) || []).length - 1;
    const base = depth > 0 ? "../".repeat(depth) : "";
    fetch(base + "data/artgallery.json")
      .then(r => r.json())
      .then(j => { DATA = j; paint(); })
      .catch(() => {});
  }

  global.ARTGALLERY = { paint, load, get data() { return DATA; } };

  if (document.readyState === "loading")
    document.addEventListener("DOMContentLoaded", load);
  else load();
})(typeof window !== "undefined" ? window : globalThis);
