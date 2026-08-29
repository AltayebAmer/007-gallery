# نشر 007.gallery

موقع ثابت بالكامل (HTML/CSS/JS) — لا يحتاج خادماً ولا قاعدة بيانات.

## ما يُرفع وما لا يُرفع

**ارفع:** `index.html` · `privacy.html` · `404.html` · `robots.txt` · `sitemap.xml`
· `manifest.webmanifest` · `favicon.ico` · `_headers` · `assets/` · `services/`

**لا ترفع:** `local-tools/` (أدوات سطر مكتب خاصة بك) · `DEPLOY.md`

> `services/_diagnostics.html` صفحة فحص داخلية — محجوبة عن الفهرسة بـ `noindex` و`robots.txt`.
> يمكنك حذفها قبل النشر إن أردت.

---

## الخيار الأول: Cloudflare Pages (موصى به)

يدعم ملف `_headers` مباشرةً — وهو مهم لتسريع الذكاء الاصطناعي.

1. ادخل [dash.cloudflare.com](https://dash.cloudflare.com) → **Workers & Pages** → **Create** → **Pages** → **Upload assets**.
2. اسحب محتويات مجلد المشروع (وليس المجلد نفسه).
3. سمِّ المشروع `007-gallery` ثم **Deploy**.
4. **Custom domains** → أضف `007.gallery` و`www.007.gallery`.
5. إن كان النطاق مُدارًا في Cloudflare فالتوجيه تلقائي؛ وإلا اتبع تعليمات DNS المعروضة.

## الخيار الثاني: Netlify

1. [app.netlify.com/drop](https://app.netlify.com/drop) — اسحب محتويات المجلد.
2. **Domain settings** → **Add custom domain** → `007.gallery`.
3. يدعم `_headers` و`404.html` تلقائياً.

## الخيار الثالث: GitHub Pages

يعمل، لكن **لا يدعم `_headers`** → لن تحصل على تسريع تعدّد الخيوط في أدوات الذكاء الاصطناعي.

---

## بعد النشر

1. **تحقّق من HTTPS** — يجب أن يعمل الموقع على `https://007.gallery`.
2. **Google Search Console** → أضف الموقع → أرسل `https://007.gallery/sitemap.xml`.
3. **اختبر بطاقة المشاركة** عبر [opengraph.xyz](https://www.opengraph.xyz) — يجب أن تظهر صورة `og-cover.png`.
4. **افحص الذكاء الاصطناعي** على `/services/_diagnostics.html` — تأكد أن `crossOriginIsolated` أصبح `true`
   (يعني أن ترويسات `_headers` عملت والمعالجة ستكون أسرع).

## الإعلانات (رد المعروف)

مساحات الإعلانات حالياً **عناصر نائبة** بلا كود فعلي. لتفعيل AdSense:

1. سجّل في [adsense.google.com](https://adsense.google.com) وأضف نطاق `007.gallery`
   (سياسة الخصوصية جاهزة في `/privacy.html` وهي شرط للقبول).
2. بعد الموافقة، ضع كود AdSense مكان كل عنصر:
   ```html
   <div class="ad"> … </div>
   ```
3. لا ترفع أي صورة للمستخدم إلى المعلنين — الأدوات محلية بالكامل وهذه ميزتك التسويقية.

## تحديث الموقع لاحقاً

عدّل الملفات محلياً ثم أعد رفعها بنفس الطريقة (أو اربط المشروع بمستودع Git للنشر التلقائي).
