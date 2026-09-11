#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
007.gallery — مولّد صفحات المقالات
© 2026 Artist Altayeb Amer / الفنان الطيب عامر

يحوّل بيانات المقالات إلى صفحات HTML ثابتة (أفضل لمحركات البحث)
+ ملف data/articles.json لفهرسة القائمة (تستخدمه لوحة التحكم لاحقاً).

الاستخدام:  python3 build-articles.py
"""
import json, os, html
from datetime import date

SITE = "https://007.gallery"
EN_NAME = "Artist Altayeb Amer"
AR_NAME = "الفنان الطيب عامر"

# ════════════════════════════════════════════════════════════
#  المقالات — أضف مقالاً جديداً بإضافة عنصر هنا
# ════════════════════════════════════════════════════════════
ARTICLES = [
{
 "slug":"remove-background-free",
 "date":"2026-08-20",
 "tool":"services/background-removal.html",
 "tool_ar":"جرّب أداة إزالة الخلفية","tool_en":"Try the background remover",
 "icon":"✂️",
 "title_ar":"كيف تزيل خلفية أي صورة مجاناً وبدون برامج",
 "title_en":"How to Remove Any Image Background Free — No Software",
 "desc_ar":"دليل عملي لإزالة خلفية الصور بالذكاء الاصطناعي داخل المتصفح، بدون تثبيت برامج وبدون رفع صورك لأي خادم.",
 "desc_en":"A practical guide to removing image backgrounds with AI inside your browser — no installs, no uploads.",
 "body_ar":"""
<p>إزالة خلفية الصورة من أكثر المهام طلباً: صور المنتجات للمتاجر، الصور الشخصية للسير الذاتية، التصاميم التي تحتاج عنصراً معزولاً. الطريقة التقليدية تعني فتح فوتوشوب وقضاء دقائق في التحديد اليدوي — وهذا مرهق لغير المتخصصين.</p>

<h2>لماذا صار الأمر أسهل اليوم؟</h2>
<p>ظهرت نماذج ذكاء اصطناعي متخصصة في «تجزئة الصور» (Image Segmentation) تفهم أين ينتهي الموضوع وأين تبدأ الخلفية. أشهرها نموذج <strong>RMBG</strong> الذي يعزل الأشخاص والمنتجات والحيوانات بدقة عالية خلال ثوانٍ.</p>
<p>الأهم: هذه النماذج صارت تعمل <strong>داخل المتصفح مباشرة</strong> بفضل تقنيتَي WebAssembly وWebGPU — أي على جهازك أنت، لا على خادم بعيد.</p>

<h2>لماذا يهمّك أن تكون المعالجة محلية؟</h2>
<ul>
  <li><strong>الخصوصية:</strong> صورتك لا تُرفع لأي مكان. مهم جداً لصور العائلة أو المستندات أو منتجات لم تُطلق بعد.</li>
  <li><strong>السرعة:</strong> لا وقت رفع ولا تنزيل — الصورة موجودة أصلاً على جهازك.</li>
  <li><strong>بلا حدود:</strong> لا قيود على عدد الصور، ولا اشتراك شهري.</li>
</ul>

<h2>خطوات الإزالة</h2>
<ol>
  <li>افتح أداة إزالة الخلفية وأفلت صورتك.</li>
  <li>انتظر تحميل النموذج (مرة واحدة فقط، ثم يُخزَّن في متصفحك).</li>
  <li>ستظهر النتيجة بخلفية شفافة — يمكنك المقارنة بين «قبل» و«بعد».</li>
  <li>اختر خلفية بديلة (أبيض، أسود، ملوّنة) أو أبقِها شفافة.</li>
  <li>نزّل الصورة بصيغة PNG لتحافظ على الشفافية.</li>
</ol>

<h2>نصائح للحصول على أفضل نتيجة</h2>
<ul>
  <li><strong>التباين مهم:</strong> كلما اختلف الموضوع عن الخلفية لوناً وإضاءة، كانت الحواف أدق.</li>
  <li><strong>الشعر والفراء:</strong> أصعب الحالات. استخدم صورة عالية الدقة لنتيجة أنظف.</li>
  <li><strong>احفظ PNG لا JPG:</strong> صيغة JPG لا تدعم الشفافية وستضع خلفية بيضاء تلقائياً.</li>
  <li><strong>للمتاجر الإلكترونية:</strong> خلفية بيضاء موحّدة تجعل صفحة منتجاتك أكثر احترافية.</li>
</ul>

<h2>ماذا لو لم تكن النتيجة مثالية؟</h2>
<p>لا يوجد نموذج مثالي 100%. إن كانت الحواف غير دقيقة، جرّب صورة بإضاءة أوضح أو خلفية أبسط. وللحالات المعقّدة جداً (شعر متطاير على خلفية مزدحمة) قد تحتاج تصحيحاً يدوياً بسيطاً بعد الإزالة الآلية.</p>
""",
 "body_en":"""
<p>Removing an image background is one of the most requested tasks: product photos for stores, headshots for CVs, design assets that need an isolated subject. The traditional route means opening Photoshop and spending minutes on manual selection — exhausting for non-designers.</p>

<h2>Why it got easier</h2>
<p>Specialised AI models for <em>image segmentation</em> now understand where a subject ends and the background begins. The best known is <strong>RMBG</strong>, which isolates people, products and animals accurately within seconds.</p>
<p>More importantly, these models now run <strong>directly inside the browser</strong> thanks to WebAssembly and WebGPU — on your own machine, not a remote server.</p>

<h2>Why local processing matters</h2>
<ul>
  <li><strong>Privacy:</strong> your image is never uploaded. Critical for family photos, documents, or unreleased products.</li>
  <li><strong>Speed:</strong> no upload or download wait — the file is already on your device.</li>
  <li><strong>No limits:</strong> no image caps, no monthly subscription.</li>
</ul>

<h2>The steps</h2>
<ol>
  <li>Open the background remover and drop your image.</li>
  <li>Wait for the model to download (once only — it is then cached in your browser).</li>
  <li>The result appears with a transparent background; compare "before" and "after".</li>
  <li>Pick a replacement background (white, black, colour) or keep it transparent.</li>
  <li>Download as PNG to preserve transparency.</li>
</ol>

<h2>Tips for the best result</h2>
<ul>
  <li><strong>Contrast matters:</strong> the more the subject differs from the background in colour and lighting, the cleaner the edges.</li>
  <li><strong>Hair and fur:</strong> the hardest cases — use a higher-resolution image.</li>
  <li><strong>Save PNG, not JPG:</strong> JPG has no transparency and will add a white background.</li>
  <li><strong>For e-commerce:</strong> a consistent white background makes your product page look far more professional.</li>
</ul>

<h2>If the result isn't perfect</h2>
<p>No model is 100% perfect. If edges look rough, try a photo with clearer lighting or a simpler background. Very complex cases (flyaway hair over a busy background) may still need a light manual touch-up afterwards.</p>
"""
},
{
 "slug":"webp-vs-png-vs-jpg",
 "date":"2026-08-20",
 "tool":"services/convert-compress.html",
 "tool_ar":"جرّب أداة التحويل والضغط","tool_en":"Try the converter",
 "icon":"🗂️",
 "title_ar":"WebP أم PNG أم JPG؟ دليل اختيار صيغة الصورة الصحيحة",
 "title_en":"WebP vs PNG vs JPG: Choosing the Right Image Format",
 "desc_ar":"شرح واضح للفروق بين صيغ الصور الثلاث الأشهر، ومتى تستخدم كل واحدة لتوفير الحجم دون خسارة الجودة.",
 "desc_en":"A clear comparison of the three most common image formats and when to use each to cut file size without losing quality.",
 "body_ar":"""
<p>اختيار صيغة الصورة قرار يؤثر مباشرة على سرعة موقعك وجودة تصميمك. إليك الفروق بلا تعقيد.</p>

<h2>JPG — للصور الفوتوغرافية</h2>
<p>الأقدم والأوسع انتشاراً. يستخدم ضغطاً «فاقداً» (lossy) يتخلّص من تفاصيل لا تلاحظها العين لتصغير الحجم.</p>
<ul>
  <li>✅ ممتاز للصور الواقعية والمناظر والوجوه.</li>
  <li>✅ حجم صغير ودعم شامل في كل جهاز.</li>
  <li>❌ <strong>لا يدعم الشفافية</strong> إطلاقاً.</li>
  <li>❌ يفقد جودة مع كل حفظ متكرر.</li>
</ul>

<h2>PNG — للشفافية والحدّة</h2>
<p>ضغط «غير فاقد» (lossless) يحافظ على كل بكسل كما هو.</p>
<ul>
  <li>✅ يدعم <strong>الشفافية</strong> — ضروري للشعارات والأيقونات.</li>
  <li>✅ حواف حادة مثالية للنصوص ولقطات الشاشة والرسومات.</li>
  <li>❌ حجم كبير جداً للصور الفوتوغرافية.</li>
</ul>

<h2>WebP — الخيار الحديث</h2>
<p>طوّرته جوجل ليجمع مزايا الاثنين. يدعم الضغط الفاقد وغير الفاقد <strong>والشفافية معاً</strong>.</p>
<ul>
  <li>✅ أصغر من JPG بنحو <strong>25–35%</strong> بنفس الجودة تقريباً.</li>
  <li>✅ أصغر من PNG بفارق كبير مع الحفاظ على الشفافية.</li>
  <li>✅ مدعوم في كل المتصفحات الحديثة.</li>
  <li>❌ برامج قديمة جداً قد لا تفتحه.</li>
</ul>

<h2>الخلاصة العملية</h2>
<table>
  <tr><th>الحالة</th><th>الصيغة</th></tr>
  <tr><td>موقع إلكتروني (أي صورة)</td><td><strong>WebP</strong></td></tr>
  <tr><td>شعار أو أيقونة بشفافية</td><td>PNG أو WebP</td></tr>
  <tr><td>صورة للطباعة</td><td>PNG</td></tr>
  <tr><td>إرسال عبر واتساب/بريد</td><td>JPG</td></tr>
  <tr><td>لقطة شاشة فيها نص</td><td>PNG أو WebP</td></tr>
</table>

<h2>ما مستوى الجودة المناسب؟</h2>
<p>عند الضغط، قيمة الجودة <strong>80</strong> هي نقطة التوازن المثالية في معظم الحالات: توفير كبير في الحجم وفرق بصري لا يكاد يُلاحظ. انزل إلى 60–70 للصور الخلفية الكبيرة، وارفع إلى 90 للصور التي تحتاج تفاصيل دقيقة.</p>

<h2>لماذا يهمّ حجم الصورة؟</h2>
<p>الصور تشكّل غالباً أكثر من نصف حجم صفحة الويب. تقليلها 30% يعني تحميلاً أسرع، وتجربة أفضل للزائر، وترتيباً أعلى في جوجل — فسرعة الصفحة عامل ترتيب معلَن.</p>
""",
 "body_en":"""
<p>Picking an image format directly affects your site speed and design quality. Here are the differences, without the jargon.</p>

<h2>JPG — for photographs</h2>
<p>The oldest and most widely supported. It uses <em>lossy</em> compression, discarding detail your eye won't notice to shrink the file.</p>
<ul>
  <li>✅ Excellent for realistic photos, landscapes and faces.</li>
  <li>✅ Small size, universal support.</li>
  <li>❌ <strong>No transparency</strong> at all.</li>
  <li>❌ Loses quality every time you re-save.</li>
</ul>

<h2>PNG — for transparency and sharpness</h2>
<p><em>Lossless</em> compression that preserves every pixel exactly.</p>
<ul>
  <li>✅ Supports <strong>transparency</strong> — essential for logos and icons.</li>
  <li>✅ Crisp edges, ideal for text, screenshots and graphics.</li>
  <li>❌ Very large files for photographs.</li>
</ul>

<h2>WebP — the modern choice</h2>
<p>Developed by Google to combine both. It supports lossy and lossless compression <strong>plus transparency</strong>.</p>
<ul>
  <li>✅ Roughly <strong>25–35% smaller</strong> than JPG at similar quality.</li>
  <li>✅ Far smaller than PNG while keeping transparency.</li>
  <li>✅ Supported in every modern browser.</li>
  <li>❌ Very old software may not open it.</li>
</ul>

<h2>Practical summary</h2>
<table>
  <tr><th>Use case</th><th>Format</th></tr>
  <tr><td>Website (any image)</td><td><strong>WebP</strong></td></tr>
  <tr><td>Logo or icon with transparency</td><td>PNG or WebP</td></tr>
  <tr><td>Image for print</td><td>PNG</td></tr>
  <tr><td>Sending via WhatsApp/email</td><td>JPG</td></tr>
  <tr><td>Screenshot containing text</td><td>PNG or WebP</td></tr>
</table>

<h2>What quality level should you use?</h2>
<p>When compressing, a quality value of <strong>80</strong> is the sweet spot in most cases: large size savings with a barely noticeable visual difference. Drop to 60–70 for large background images, and raise to 90 for images needing fine detail.</p>

<h2>Why file size matters</h2>
<p>Images often make up more than half a web page's weight. Cutting them by 30% means faster loading, a better visitor experience, and better Google rankings — page speed is a stated ranking factor.</p>
"""
},
{
 "slug":"upscale-image-without-losing-quality",
 "date":"2026-08-20",
 "tool":"services/upscale.html",
 "tool_ar":"جرّب أداة التكبير","tool_en":"Try the upscaler",
 "icon":"🔍",
 "title_ar":"كيف تكبّر صورة صغيرة دون أن تفقد جودتها",
 "title_en":"How to Enlarge a Small Image Without Losing Quality",
 "desc_ar":"لماذا تتشوّه الصور عند التكبير، وكيف يحلّ الذكاء الاصطناعي هذه المشكلة القديمة داخل متصفحك.",
 "desc_en":"Why images break when enlarged, and how AI solves this old problem right inside your browser.",
 "body_ar":"""
<p>لديك صورة قديمة صغيرة أو لقطة بدقة منخفضة، وتحتاجها بحجم أكبر. تكبّرها فتظهر مشوّشة ومربّعة. لماذا؟</p>

<h2>المشكلة: البكسلات المفقودة</h2>
<p>الصورة شبكة من النقاط (البكسلات). صورة 200×200 تحوي 40 ألف نقطة. عند تكبيرها إلى 800×800 تحتاج 640 ألف نقطة — أي <strong>600 ألف نقطة غير موجودة</strong>.</p>
<p>البرامج التقليدية تخمّن هذه النقاط بحساب متوسط جيرانها (Interpolation). النتيجة: صورة أكبر لكن <strong>ضبابية</strong>، لأن التخمين الحسابي لا يخترع تفاصيل حقيقية.</p>

<h2>الحل: الذكاء الاصطناعي</h2>
<p>نماذج التكبير الفائق (Super-Resolution) دُرِّبت على ملايين أزواج الصور: نسخة صغيرة ونسخة كبيرة من الصورة نفسها. فتعلّمت كيف تبدو التفاصيل الحقيقية عادةً.</p>
<p>لذا حين تعطيها صورة صغيرة، فهي <strong>لا تخمّن حسابياً</strong> بل تعيد بناء الحواف والملامس بناءً على ما تعلّمته. النتيجة أوضح بكثير.</p>

<h2>متى تنجح ومتى تفشل؟</h2>
<ul>
  <li>✅ <strong>ينجح ممتازاً:</strong> الصور الواضحة لكن الصغيرة الحجم.</li>
  <li>✅ <strong>جيد:</strong> الصور المضغوطة بشدة (آثار JPG).</li>
  <li>⚠️ <strong>محدود:</strong> الصور شديدة الضبابية أصلاً — لا يمكن استعادة ما لم يُسجَّل قط.</li>
  <li>❌ <strong>خرافة الأفلام:</strong> «كبّر وحسّن» لوحة سيارة من كاميرا مراقبة بعيدة — مستحيل. النموذج يخترع تفاصيل معقولة، لا يستعيد الحقيقة.</li>
</ul>

<h2>نصائح عملية</h2>
<ul>
  <li><strong>ابدأ بأفضل نسخة متاحة:</strong> لا تكبّر صورة سبق تكبيرها أو ضغطها مراراً.</li>
  <li><strong>لا تبالغ:</strong> ×2 أو ×4 نتائجها ممتازة؛ ما فوق ذلك يبدأ بالاصطناعية.</li>
  <li><strong>للوجوه:</strong> نماذج ترميم الوجوه المتخصصة أفضل من التكبير العام.</li>
  <li><strong>احفظ PNG:</strong> لئلا تضيف صيغة JPG ضغطاً جديداً فوق العمل.</li>
</ul>

<h2>هل يعمل هذا في المتصفح؟</h2>
<p>نعم. بفضل WebGPU صار بالإمكان تشغيل نماذج التكبير على كرت الشاشة داخل المتصفح. الصور لا تُرفع لأي خادم، والمعالجة تتم على جهازك. على الأجهزة القديمة يعمل على المعالج — أبطأ لكنه ينجح.</p>
""",
 "body_en":"""
<p>You have an old small photo or a low-resolution screenshot and need it bigger. You enlarge it and it turns blurry and blocky. Why?</p>

<h2>The problem: missing pixels</h2>
<p>An image is a grid of dots. A 200×200 image holds 40,000 of them. Enlarging it to 800×800 requires 640,000 — meaning <strong>600,000 dots that do not exist</strong>.</p>
<p>Traditional software guesses them by averaging neighbours (interpolation). The result is a bigger but <strong>blurry</strong> image, because mathematical guessing cannot invent real detail.</p>

<h2>The solution: AI</h2>
<p>Super-resolution models were trained on millions of image pairs — a small and a large version of the same picture — learning what genuine detail usually looks like.</p>
<p>So when you give one a small image, it <strong>doesn't guess arithmetically</strong>; it reconstructs edges and textures based on what it learned. The result is far sharper.</p>

<h2>When it works and when it doesn't</h2>
<ul>
  <li>✅ <strong>Works very well:</strong> images that are sharp but simply small.</li>
  <li>✅ <strong>Good:</strong> heavily compressed images with JPG artefacts.</li>
  <li>⚠️ <strong>Limited:</strong> images that were already very blurry — you cannot recover what was never recorded.</li>
  <li>❌ <strong>The movie myth:</strong> "enhance" a licence plate from distant CCTV — impossible. The model invents plausible detail; it does not recover truth.</li>
</ul>

<h2>Practical tips</h2>
<ul>
  <li><strong>Start from the best copy you have:</strong> don't upscale an image that was already upscaled or repeatedly compressed.</li>
  <li><strong>Don't overdo it:</strong> ×2 or ×4 gives excellent results; beyond that it starts to look artificial.</li>
  <li><strong>For faces:</strong> dedicated face-restoration models beat general upscaling.</li>
  <li><strong>Save as PNG</strong> so JPG compression isn't layered on top of the work.</li>
</ul>

<h2>Does this work in a browser?</h2>
<p>Yes. Thanks to WebGPU, upscaling models can run on your graphics card inside the browser. Images are never uploaded, and processing happens on your device. On older machines it falls back to the CPU — slower, but it still works.</p>
"""
},
{
 "slug":"extract-text-from-image-ocr-arabic",
 "date":"2026-08-20",
 "tool":"services/ocr.html",
 "tool_ar":"جرّب أداة استخراج النص","tool_en":"Try the text extractor",
 "icon":"📝",
 "title_ar":"استخراج النص من الصور بالعربية: دليل OCR الكامل",
 "title_en":"Extracting Text from Images in Arabic: A Complete OCR Guide",
 "desc_ar":"كيف تحوّل صورة أو مستنداً ممسوحاً إلى نص قابل للتحرير والنسخ — بالعربية والإنجليزية ومجاناً.",
 "desc_en":"How to turn an image or scanned document into editable, copyable text — in Arabic and English, for free.",
 "body_ar":"""
<p>لديك صورة لصفحة كتاب، أو لقطة شاشة فيها نص، أو فاتورة ممسوحة — وتحتاج النص مكتوباً لا مصوّراً. هنا يأتي دور <strong>OCR</strong> (التعرّف الضوئي على الحروف).</p>

<h2>كيف يعمل OCR؟</h2>
<p>البرنامج يحلّل الصورة ويبحث عن أشكال تشبه الحروف، ثم يطابقها مع نماذج تعلّمها مسبقاً، ويجمعها كلمات وجُملاً. النتيجة نص عادي يمكنك نسخه وتحريره والبحث فيه.</p>

<h2>لماذا العربية أصعب؟</h2>
<p>العربية تمثّل تحدياً حقيقياً لأنظمة OCR لأسباب بنيوية:</p>
<ul>
  <li><strong>الحروف متصلة</strong> ولا تُكتب منفصلة كالإنجليزية — فصعوبة تحديد أين ينتهي حرف ويبدأ آخر.</li>
  <li><strong>شكل الحرف يتغيّر</strong> حسب موقعه (أول، وسط، آخر، منفرد) — الحرف الواحد له أربع صور.</li>
  <li><strong>النقاط والتشكيل</strong> تفرّق بين حروف متشابهة (ب/ت/ث)، وأي ضبابية تُربك التمييز.</li>
</ul>
<p>لهذا تكون دقة OCR العربي عادةً أقل من الإنجليزي — وهذا طبيعي وليس عيباً في الأداة.</p>

<h2>كيف تحصل على أفضل دقة؟</h2>
<ul>
  <li><strong>دقة عالية:</strong> كلما كانت الصورة أوضح كانت النتيجة أدق. تجنّب الصور المصغّرة.</li>
  <li><strong>استقامة:</strong> صوّر الصفحة مستقيمة لا مائلة. الميل يربك التعرّف كثيراً.</li>
  <li><strong>إضاءة متساوية:</strong> تجنّب الظلال والانعكاسات ووهج الفلاش.</li>
  <li><strong>تباين واضح:</strong> نص أسود على خلفية بيضاء هو المثالي.</li>
  <li><strong>اختر اللغة الصحيحة:</strong> إن كان النص عربياً فقط، اختر «العربية فقط» — يعطي دقة أعلى من الوضع المختلط.</li>
  <li><strong>الخطوط الواضحة أفضل:</strong> خطوط الطباعة العادية أدق بكثير من الخطوط الزخرفية أو خط اليد.</li>
</ul>

<h2>استخدامات عملية</h2>
<ul>
  <li>تحويل صفحات كتاب مصوّرة إلى نص للبحث والاقتباس.</li>
  <li>نسخ نص من لقطة شاشة لا تسمح بالتحديد.</li>
  <li>أرشفة الفواتير والمستندات الورقية بشكل قابل للبحث.</li>
  <li>استخراج نص من صورة لترجمته.</li>
</ul>

<h2>الخصوصية</h2>
<p>مستنداتك غالباً حساسة — عقود، فواتير، أوراق شخصية. لهذا يهمّ كثيراً أن يعمل OCR <strong>داخل متصفحك</strong> بدل رفع المستند إلى خادم مجهول. أداتنا تعمل محلياً بالكامل: يُحمَّل المحرّك مرة واحدة، ثم لا يغادر ملفك جهازك أبداً.</p>

<h2>راجع النتيجة دائماً</h2>
<p>لا يوجد OCR بدقة 100%، خصوصاً في العربية. اعتبر الناتج <strong>مسوّدة ممتازة</strong> توفّر عليك 90% من وقت الكتابة، ثم راجعها سريعاً — خاصة الأرقام والأسماء.</p>
""",
 "body_en":"""
<p>You have a photo of a book page, a screenshot containing text, or a scanned invoice — and you need the text as text, not as a picture. That's where <strong>OCR</strong> (Optical Character Recognition) comes in.</p>

<h2>How does OCR work?</h2>
<p>The software analyses the image, looks for letter-like shapes, matches them against patterns it has learned, and assembles them into words and sentences. The result is plain text you can copy, edit and search.</p>

<h2>Why is Arabic harder?</h2>
<p>Arabic poses genuine structural challenges for OCR systems:</p>
<ul>
  <li><strong>Letters connect</strong> rather than standing apart as in English — so it's hard to tell where one letter ends and the next begins.</li>
  <li><strong>Letter shapes change</strong> by position (initial, medial, final, isolated) — one letter has four forms.</li>
  <li><strong>Dots and diacritics</strong> distinguish similar letters (ب/ت/ث), and any blur confuses the distinction.</li>
</ul>
<p>This is why Arabic OCR accuracy is typically lower than English — that's expected, not a flaw in the tool.</p>

<h2>Getting the best accuracy</h2>
<ul>
  <li><strong>High resolution:</strong> the clearer the image, the better the result. Avoid thumbnails.</li>
  <li><strong>Keep it straight:</strong> photograph the page square-on, not at an angle. Skew badly hurts recognition.</li>
  <li><strong>Even lighting:</strong> avoid shadows, reflections and flash glare.</li>
  <li><strong>Strong contrast:</strong> black text on a white background is ideal.</li>
  <li><strong>Pick the right language:</strong> if the text is Arabic only, choose "Arabic only" — it beats mixed mode.</li>
  <li><strong>Clean fonts win:</strong> ordinary print fonts are far more accurate than decorative faces or handwriting.</li>
</ul>

<h2>Practical uses</h2>
<ul>
  <li>Turning photographed book pages into searchable, quotable text.</li>
  <li>Copying text from a screenshot that doesn't allow selection.</li>
  <li>Archiving invoices and paper documents in a searchable form.</li>
  <li>Extracting text from an image in order to translate it.</li>
</ul>

<h2>Privacy</h2>
<p>Your documents are often sensitive — contracts, invoices, personal papers. That's why it matters that OCR runs <strong>inside your browser</strong> rather than uploading the document to an unknown server. Our tool works entirely locally: the engine downloads once, and your file never leaves your device.</p>

<h2>Always review the output</h2>
<p>No OCR is 100% accurate, especially in Arabic. Treat the output as an <strong>excellent draft</strong> that saves you 90% of the typing, then proofread quickly — particularly numbers and names.</p>
"""
},
{
 "slug":"free-qr-code-with-logo",
 "date":"2026-08-20",
 "tool":"services/qr.html",
 "tool_ar":"جرّب مولّد QR","tool_en":"Try the QR generator",
 "icon":"🔳",
 "title_ar":"كيف تصنع رمز QR احترافياً بشعارك وألوانك",
 "title_en":"How to Make a Professional QR Code With Your Logo",
 "desc_ar":"دليل عملي لإنشاء رموز QR أنيقة تعمل بموثوقية — مع شرح مستويات تصحيح الخطأ وأخطاء شائعة تُفسد الرمز.",
 "desc_en":"A practical guide to elegant QR codes that actually scan — error-correction levels and the mistakes that break them.",
 "body_ar":"""
<p>رمز QR جسر بين المطبوع والرقمي: بطاقة عمل، قائمة طعام، ملصق، عبوة منتج. لكن كثيراً من الرموز المصمَّمة بذوق <strong>تفشل في المسح</strong>. إليك كيف تصنع رمزاً جميلاً وموثوقاً معاً.</p>

<h2>كيف يعمل رمز QR؟</h2>
<p>الرمز شبكة من المربّعات السوداء والبيضاء تمثّل بيانات ثنائية. المربّعات الكبيرة في ثلاث زوايا تُسمّى «أنماط التموضع» — بها تعرف الكاميرا اتجاه الرمز حتى لو كان مائلاً أو مقلوباً.</p>

<h2>تصحيح الخطأ: أهم إعداد يجهله الناس</h2>
<p>يحتوي رمز QR على بيانات زائدة تسمح بقراءته حتى لو تلف جزء منه. أربعة مستويات:</p>
<ul>
  <li><strong>L</strong> — يتحمّل تلف 7%</li>
  <li><strong>M</strong> — 15%</li>
  <li><strong>Q</strong> — 25%</li>
  <li><strong>H</strong> — 30% ✅ <em>اختر هذا عند إضافة شعار</em></li>
</ul>
<p>لماذا؟ لأن وضع شعار في المنتصف <strong>يحجب بيانات فعلية</strong>. المستوى H يوفّر فائضاً يعوّض ما حجبه الشعار، فيُقرأ الرمز رغم ذلك.</p>

<h2>قواعد الشعار في المنتصف</h2>
<ul>
  <li><strong>لا تتجاوز 25%</strong> من عرض الرمز. الأأمان حوالي 20%.</li>
  <li>ضع <strong>خلفية صلبة</strong> خلف الشعار (بلون خلفية الرمز) لفصله بوضوح.</li>
  <li><strong>لا تغطِّ الزوايا الثلاث</strong> إطلاقاً — تغطيتها تُفشل المسح تماماً.</li>
</ul>

<h2>الألوان: قاعدة واحدة حاسمة</h2>
<p>الكاميرا تقرأ <strong>التباين</strong> لا اللون. لذا:</p>
<ul>
  <li>✅ <strong>الرمز داكن والخلفية فاتحة</strong> — هذا هو الأصل.</li>
  <li>⚠️ العكس (فاتح على داكن) يعمل في معظم الهواتف الحديثة لكن ليس كلها. اختبره.</li>
  <li>❌ لونان متقاربان في الإضاءة (أصفر على أبيض) = فشل شبه مؤكّد.</li>
  <li>❌ تدرّجات لونية معقّدة تربك القراءة.</li>
</ul>

<h2>الحجم والطباعة</h2>
<p>القاعدة العملية: <strong>عرض الرمز ≥ عُشر مسافة المسح</strong>. للمسح من متر واحد، اجعل الرمز 10سم على الأقل. وللطباعة صدّر بدقة عالية (1024px فأكثر) أو استخدم <strong>SVG</strong> — فهو متجهي يُطبع بأي حجم بلا تحبّب.</p>

<h2>أخطاء شائعة</h2>
<ul>
  <li><strong>عدم الاختبار:</strong> اختبر بهاتفين مختلفين قبل الطباعة. الطباعة خطأ مكلفة.</li>
  <li><strong>إلغاء الهامش:</strong> يحتاج الرمز إطاراً فارغاً حوله ليعزله عن محيطه.</li>
  <li><strong>رابط طويل جداً:</strong> يجعل المربّعات دقيقة وصعبة القراءة. اختصر الرابط.</li>
  <li><strong>نسيان اختبار الرابط:</strong> تأكد أن الصفحة تعمل وتناسب الجوال.</li>
</ul>
""",
 "body_en":"""
<p>A QR code bridges print and digital: business cards, menus, posters, packaging. Yet many beautifully designed codes <strong>fail to scan</strong>. Here's how to make one that is both attractive and reliable.</p>

<h2>How does a QR code work?</h2>
<p>It is a grid of black and white squares representing binary data. The large squares in three corners are "position patterns" — they tell the camera the code's orientation even if it is tilted or upside down.</p>

<h2>Error correction: the setting most people miss</h2>
<p>A QR code carries redundant data so it still reads when partly damaged. There are four levels:</p>
<ul>
  <li><strong>L</strong> — tolerates 7% damage</li>
  <li><strong>M</strong> — 15%</li>
  <li><strong>Q</strong> — 25%</li>
  <li><strong>H</strong> — 30% ✅ <em>choose this when adding a logo</em></li>
</ul>
<p>Why? Because placing a logo in the middle <strong>covers real data</strong>. Level H provides enough redundancy to compensate, so the code still scans.</p>

<h2>Rules for a centre logo</h2>
<ul>
  <li><strong>Never exceed 25%</strong> of the code's width. Around 20% is safest.</li>
  <li>Put a <strong>solid backing</strong> behind the logo (in the code's background colour) to separate it cleanly.</li>
  <li><strong>Never cover the three corners</strong> — doing so breaks scanning entirely.</li>
</ul>

<h2>Colour: one decisive rule</h2>
<p>Cameras read <strong>contrast</strong>, not colour. So:</p>
<ul>
  <li>✅ <strong>Dark code on a light background</strong> — this is the norm.</li>
  <li>⚠️ Inverted (light on dark) works on most modern phones but not all. Test it.</li>
  <li>❌ Two colours of similar brightness (yellow on white) will almost certainly fail.</li>
  <li>❌ Complex gradients confuse readers.</li>
</ul>

<h2>Size and printing</h2>
<p>Rule of thumb: <strong>code width ≥ one tenth of the scanning distance</strong>. To scan from one metre, make it at least 10cm. For print, export at high resolution (1024px or more) or use <strong>SVG</strong> — being vector, it prints at any size without pixelation.</p>

<h2>Common mistakes</h2>
<ul>
  <li><strong>Not testing:</strong> test with two different phones before printing. Print mistakes are expensive.</li>
  <li><strong>Removing the margin:</strong> the code needs empty quiet space around it.</li>
  <li><strong>Very long URLs:</strong> they make the squares tiny and hard to read. Shorten the link.</li>
  <li><strong>Not checking the link:</strong> make sure the page works and is mobile-friendly.</li>
</ul>
"""
},
{
 "slug":"protect-images-watermark-guide",
 "date":"2026-08-20",
 "tool":"services/watermark.html",
 "tool_ar":"جرّب أداة العلامة المائية","tool_en":"Try the watermark studio",
 "icon":"🛡️",
 "title_ar":"كيف تحمي صورك على الإنترنت: دليل العلامة المائية",
 "title_en":"How to Protect Your Images Online: A Watermarking Guide",
 "desc_ar":"متى تستخدم العلامة المائية وكيف تصمّمها بحيث تحمي عملك دون أن تُفسد جماله.",
 "desc_en":"When to watermark, and how to design one that protects your work without ruining it.",
 "body_ar":"""
<p>تنشر صورك على الإنترنت فتُسرق وتُنسب لغيرك. العلامة المائية أقدم حل وأبسطه — لكن استخدامها الخاطئ يُفسد عملك أكثر مما يحميه.</p>

<h2>ما الذي تفعله العلامة المائية فعلاً؟</h2>
<p>لنكن صادقين: <strong>لا توجد حماية مطلقة</strong> لأي صورة منشورة. العلامة المائية تفعل ثلاثة أشياء واقعية:</p>
<ul>
  <li><strong>تردع السرقة السهلة</strong> — أغلب السارقين كسالى، ووجود علامة يجعلهم ينتقلون لصورة أخرى.</li>
  <li><strong>تنسب العمل إليك</strong> — حتى لو انتشرت الصورة، اسمك معها.</li>
  <li><strong>تسوّق لك</strong> — كل مشاركة تحمل اسمك أو موقعك.</li>
</ul>

<h2>الموازنة الصعبة</h2>
<p>علامة خفيفة جداً = تُقصّ أو تُزال بسهولة. علامة ثقيلة جداً = تُفسد الصورة وتنفّر المشاهد. الحل يعتمد على غرضك:</p>
<table>
  <tr><th>الغرض</th><th>الأسلوب</th></tr>
  <tr><td>عرض أعمالك (بورتفوليو)</td><td>علامة صغيرة في زاوية · شفافية 30–40%</td></tr>
  <tr><td>صور معاينة قبل البيع</td><td>علامة مكرّرة على كامل الصورة</td></tr>
  <tr><td>صور للعملاء</td><td>بلا علامة (النسخة النهائية المدفوعة)</td></tr>
  <tr><td>وسائل التواصل</td><td>اسم الحساب في زاوية · شفافية 40%</td></tr>
</table>

<h2>قواعد تصميم علامة جيدة</h2>
<ul>
  <li><strong>الشفافية 30–45%:</strong> أقل تكاد تُرى، وأكثر تُزعج.</li>
  <li><strong>تجنّب الزوايا وحدها:</strong> أسهل ما يُقصّ. للحماية الجادة ضعها قرب المنتصف أو كرّرها.</li>
  <li><strong>خط بسيط وواضح:</strong> الخطوط الزخرفية تصعُب قراءتها بحجم صغير.</li>
  <li><strong>أضف ظلاً خفيفاً:</strong> ليبقى النص مقروءاً على الخلفيات الفاتحة والداكنة معاً.</li>
  <li><strong>الحجم 5–10%</strong> من ارتفاع الصورة يناسب معظم الحالات.</li>
</ul>

<h2>التكرار: الأقوى للمعاينات</h2>
<p>عند بيع صورك، النمط المكرّر بزاوية مائلة عبر الصورة كلها هو الأصعب على الإزالة — لأن إزالته تتطلب إعادة بناء أجزاء كثيرة. استخدم شفافية منخفضة (20–30%) ليبقى المحتوى مفهوماً وقابلاً للتقييم.</p>

<h2>وسيلة أخرى: البيانات الوصفية</h2>
<p>يمكن دفن اسمك وحقوقك <strong>داخل ملف الصورة</strong> نفسه (حقول Author وCopyright). لا تُرى ولا تُفسد التصميم، وتسافر مع الملف. ليست حماية بصرية، لكنها دليل ملكية عملي.</p>

<h2>إخفاء معلومة حساسة</h2>
<p>أحياناً تريد العكس: إخفاء رقم أو وجه أو عنوان قبل النشر. الطمس أو البكسلة على المنطقة يحلّ هذا. <strong>تحذير مهم:</strong> بكسلة خفيفة على نص قد تُعكس أحياناً — استخدم شدّة عالية على المعلومات الحسّاسة حقاً.</p>
""",
 "body_en":"""
<p>You publish your images online and they get stolen and credited to someone else. Watermarking is the oldest and simplest answer — but done badly it ruins your work more than it protects it.</p>

<h2>What does a watermark actually do?</h2>
<p>Let's be honest: <strong>there is no absolute protection</strong> for any published image. A watermark does three realistic things:</p>
<ul>
  <li><strong>Deters lazy theft</strong> — most thieves are lazy; a watermark sends them to another image.</li>
  <li><strong>Attributes the work to you</strong> — even if the image spreads, your name travels with it.</li>
  <li><strong>Markets you</strong> — every share carries your name or website.</li>
</ul>

<h2>The difficult balance</h2>
<p>Too light and it's cropped or removed easily. Too heavy and it ruins the image. The answer depends on your purpose:</p>
<table>
  <tr><th>Purpose</th><th>Approach</th></tr>
  <tr><td>Portfolio display</td><td>Small corner mark · 30–40% opacity</td></tr>
  <tr><td>Previews before purchase</td><td>Tiled across the whole image</td></tr>
  <tr><td>Client deliverables</td><td>No watermark (the paid final)</td></tr>
  <tr><td>Social media</td><td>Handle in a corner · 40% opacity</td></tr>
</table>

<h2>Design rules for a good watermark</h2>
<ul>
  <li><strong>Opacity 30–45%:</strong> less is barely visible, more is intrusive.</li>
  <li><strong>Don't rely on corners alone:</strong> they are the easiest to crop. For serious protection place it near the centre or tile it.</li>
  <li><strong>Use a simple, legible typeface:</strong> decorative fonts are hard to read small.</li>
  <li><strong>Add a subtle shadow</strong> so the text stays readable over both light and dark areas.</li>
  <li><strong>Size at 5–10%</strong> of the image height suits most cases.</li>
</ul>

<h2>Tiling: strongest for previews</h2>
<p>When selling images, a repeated pattern angled across the whole frame is hardest to remove, because removing it means rebuilding large areas. Use low opacity (20–30%) so the content stays understandable and reviewable.</p>

<h2>Another approach: metadata</h2>
<p>You can bury your name and rights <strong>inside the image file</strong> itself (Author and Copyright fields). It is invisible, doesn't harm the design, and travels with the file. Not visual protection, but practical proof of ownership.</p>

<h2>Hiding sensitive information</h2>
<p>Sometimes you want the opposite: hiding a number, face or address before publishing. Blurring or pixelating that region solves it. <strong>Important warning:</strong> light pixelation over text can sometimes be reversed — use high strength on genuinely sensitive information.</p>
"""
},
{
 "slug":"why-browser-ai-tools-are-safer",
 "date":"2026-08-20",
 "tool":"index.html",
 "tool_ar":"تصفّح الأدوات المجانية","tool_en":"Browse the free tools",
 "icon":"🔒",
 "title_ar":"لماذا أدوات الذكاء الاصطناعي في المتصفح أكثر أماناً؟",
 "title_en":"Why Browser-Based AI Tools Are Safer for Your Privacy",
 "desc_ar":"الفرق بين المعالجة المحلية والسحابية، وماذا يحدث لصورك حين ترفعها إلى موقع مجاني.",
 "desc_en":"The difference between local and cloud processing, and what really happens when you upload to a free site.",
 "body_ar":"""
<p>حين ترفع صورة إلى موقع تحرير مجاني، هل سألت نفسك: <strong>أين تذهب صورتك؟ ومن يراها؟ وكم تبقى محفوظة؟</strong></p>

<h2>ماذا يحدث في المواقع السحابية؟</h2>
<p>الطريقة التقليدية: صورتك تُرفع إلى خادم، تُعالَج هناك، ثم تُعاد إليك. هذا يعني عملياً:</p>
<ul>
  <li>نسخة من صورتك <strong>موجودة على جهاز لا تملكه</strong>.</li>
  <li>مدة الاحتفاظ بها تعتمد على سياسة الموقع — وكثير منها غامض.</li>
  <li>موظفو الخدمة قد يستطيعون الوصول إليها تقنياً.</li>
  <li>أي اختراق للخادم يعرّض صور كل المستخدمين.</li>
  <li>بعض الخدمات تستخدم صور المستخدمين <strong>لتدريب نماذجها</strong>.</li>
</ul>
<p>هذا مقلق خصوصاً مع المستندات الرسمية، صور العائلة والأطفال، تصاميم لم تُنشر بعد، أو صور منتجات قبل الإطلاق.</p>

<h2>البديل: المعالجة داخل المتصفح</h2>
<p>ظهرت تقنيتان غيّرتا المعادلة:</p>
<ul>
  <li><strong>WebAssembly:</strong> تشغيل كود عالي الأداء داخل المتصفح بسرعة قريبة من البرامج الأصلية.</li>
  <li><strong>WebGPU:</strong> وصول المتصفح إلى كرت الشاشة — أي تشغيل نماذج الذكاء الاصطناعي محلياً.</li>
</ul>
<p>النتيجة: يُنزَّل <strong>النموذج</strong> إلى جهازك مرة واحدة، ثم تُعالَج صورك عندك. الصورة لا تغادر الجهاز إطلاقاً.</p>

<h2>كيف تتحقّق بنفسك؟</h2>
<p>اختبار بسيط وحاسم: افتح الأداة وانتظر تحميلها، ثم <strong>اقطع الإنترنت</strong> وجرّب معالجة صورة. إن نجحت العملية فالمعالجة محلية بالتأكيد — لأن لا اتصال أصلاً.</p>

<h2>المقارنة</h2>
<table>
  <tr><th></th><th>محلي (المتصفح)</th><th>سحابي</th></tr>
  <tr><td>الخصوصية</td><td>كاملة</td><td>تعتمد على الثقة</td></tr>
  <tr><td>وقت الرفع</td><td>لا يوجد</td><td>يزيد مع حجم الملف</td></tr>
  <tr><td>حدود الاستخدام</td><td>بلا حدود</td><td>غالباً محدود</td></tr>
  <tr><td>التكلفة</td><td>مجاني عادةً</td><td>اشتراك غالباً</td></tr>
  <tr><td>القوة القصوى</td><td>محدودة بجهازك</td><td>عالية جداً</td></tr>
</table>

<h2>متى تبقى السحابة أفضل؟</h2>
<p>لنكن منصفين: المهام الثقيلة جداً (توليد فيديو، نماذج بمليارات المعاملات) تحتاج عتاداً لا يملكه معظم الناس. القاعدة العملية:</p>
<ul>
  <li>✅ <strong>محلي</strong> للمهام اليومية: إزالة خلفية، ضغط، تحويل، OCR، تكبير.</li>
  <li>☁️ <strong>سحابي</strong> للمهام الثقيلة — وعندها اقرأ سياسة الخصوصية أولاً.</li>
</ul>

<h2>خلاصة</h2>
<p>القاعدة الذهبية: <strong>ما لا يغادر جهازك لا يمكن تسريبه</strong>. كلما وجدت أداة محلية تؤدي الغرض، فضّلها — خصوصاً للملفات التي تهمّك.</p>
""",
 "body_en":"""
<p>When you upload an image to a free editing site, have you asked yourself: <strong>where does it go? Who sees it? How long is it kept?</strong></p>

<h2>What happens on cloud sites?</h2>
<p>The traditional model: your image is uploaded to a server, processed there, and sent back. In practice this means:</p>
<ul>
  <li>A copy of your image <strong>exists on a machine you don't own</strong>.</li>
  <li>Retention depends on the site's policy — and many are vague.</li>
  <li>Staff may technically be able to access it.</li>
  <li>Any server breach exposes every user's images.</li>
  <li>Some services use user images <strong>to train their models</strong>.</li>
</ul>
<p>That's especially concerning for official documents, family and children's photos, unpublished designs, or pre-launch product shots.</p>

<h2>The alternative: processing inside the browser</h2>
<p>Two technologies changed the equation:</p>
<ul>
  <li><strong>WebAssembly:</strong> running high-performance code in the browser at near-native speed.</li>
  <li><strong>WebGPU:</strong> browser access to the graphics card — meaning AI models can run locally.</li>
</ul>
<p>The result: the <strong>model</strong> downloads to your device once, then your images are processed on your machine. The image never leaves it.</p>

<h2>How to verify it yourself</h2>
<p>A simple, decisive test: open the tool, let it load, then <strong>disconnect the internet</strong> and try processing an image. If it still works, processing is definitely local — there is no connection to send anything over.</p>

<h2>The comparison</h2>
<table>
  <tr><th></th><th>Local (browser)</th><th>Cloud</th></tr>
  <tr><td>Privacy</td><td>Complete</td><td>Based on trust</td></tr>
  <tr><td>Upload time</td><td>None</td><td>Grows with file size</td></tr>
  <tr><td>Usage limits</td><td>Unlimited</td><td>Usually capped</td></tr>
  <tr><td>Cost</td><td>Usually free</td><td>Often subscription</td></tr>
  <tr><td>Maximum power</td><td>Limited by your device</td><td>Very high</td></tr>
</table>

<h2>When is the cloud still better?</h2>
<p>To be fair: very heavy tasks (video generation, billion-parameter models) need hardware most people don't have. The practical rule:</p>
<ul>
  <li>✅ <strong>Local</strong> for everyday tasks: background removal, compression, conversion, OCR, upscaling.</li>
  <li>☁️ <strong>Cloud</strong> for heavy tasks — and there, read the privacy policy first.</li>
</ul>

<h2>Bottom line</h2>
<p>The golden rule: <strong>what never leaves your device cannot be leaked</strong>. Whenever a local tool does the job, prefer it — especially for files that matter to you.</p>
"""
},
{
 "slug":"compress-image-without-uploading",
 "date":"2026-09-11",
 "tool":"services/convert-compress.html",
 "tool_ar":"جرّب أداة الضغط","tool_en":"Try the compressor",
 "icon":"\U0001F4E6",
 "title_ar":"تصغير حجم الصورة أونلاين بدون رفعها لأي موقع",
 "title_en":"Compress an Image Online Without Uploading It Anywhere",
 "desc_ar":"كيف تقلّل حجم صورك بنسبة تصل إلى 70٪ دون خسارة ملحوظة في الجودة — وبدون إرسالها إلى خادم أحد.",
 "desc_en":"How to cut image file size by up to 70% with no visible quality loss — and without sending your photos to anyone's server.",
 "body_ar":"""
<p>الصور الكبيرة تبطئ موقعك، وتملأ مساحة تخزينك، وتفشل في الرفع على المنصات التي تحدّ الحجم. لكن معظم أدوات الضغط المجانية تطلب رفع صورتك أولاً — وهذا يعني أن نسخة منها صارت على جهاز لا تملكه.</p>

<h2>لماذا تكون الصورة كبيرة أصلاً؟</h2>
<p>ثلاثة أسباب، وكل واحد له حلّ مختلف:</p>
<ul>
  <li><strong>أبعاد ضخمة:</strong> كاميرا الجوال تصوّر بـ12 ميغابكسل. صفحة الويب لا تحتاج أكثر من 1920 بكسل عرضاً. تصغير الأبعاد وحده قد يوفّر 80٪.</li>
  <li><strong>صيغة غير مناسبة:</strong> حفظ صورة فوتوغرافية بصيغة PNG يضاعف حجمها بلا فائدة.</li>
  <li><strong>جودة مبالغ فيها:</strong> الفرق بين جودة 100 وجودة 80 لا تراه العين، لكن الحجم ينخفض للنصف.</li>
</ul>

<h2>الترتيب الصحيح للضغط</h2>
<p>هذا الترتيب يعطي أفضل نتيجة:</p>
<ol>
  <li><strong>صغّر الأبعاد أولاً</strong> إلى ما تحتاجه فعلاً. هذه أكبر مكسب على الإطلاق.</li>
  <li><strong>اختر الصيغة الصحيحة:</strong> WebP للويب، JPG للإرسال، PNG للشفافية فقط.</li>
  <li><strong>اضبط الجودة على 80.</strong> انزل إلى 65 للصور الخلفية الكبيرة التي لا يدقّق فيها أحد.</li>
</ol>
<p>لو عكست الترتيب — ضغطت بجودة منخفضة ثم صغّرت الأبعاد — ستحصل على صورة أسوأ بنفس الحجم.</p>

<h2>ما الفرق بين «الضغط» و«تغيير الحجم»؟</h2>
<p>خلط شائع يستحق التوضيح:</p>
<ul>
  <li><strong>تغيير الحجم (Resize):</strong> يقلّل عدد البكسلات. صورة 4000×3000 تصير 1920×1440.</li>
  <li><strong>الضغط (Compress):</strong> يُبقي عدد البكسلات ويقلّل البيانات المستخدمة لوصفها.</li>
</ul>
<p>الأقوى هو استخدام الاثنين معاً — وهذا ما تفعله الأداة في خطوة واحدة.</p>

<h2>متى لا تضغط؟</h2>
<ul>
  <li><strong>الصور المعدّة للطباعة:</strong> تحتاج كل بكسل. اطبع من الأصل.</li>
  <li><strong>الصور التي ستحرّرها لاحقاً:</strong> كل ضغط يفقد بيانات لا تعود. احتفظ بنسخة أصلية دائماً.</li>
  <li><strong>الرسومات ذات الحواف الحادة:</strong> الشعارات والمخططات تتشوّه بالضغط الفاقد. استخدم PNG أو WebP غير الفاقد.</li>
</ul>

<h2>لماذا يهمّ ألا تُرفع الصورة؟</h2>
<p>الضغط عملية حسابية بحتة لا تحتاج خادماً — متصفحك قادر عليها تماماً. فإذا كان الرفع غير ضروري تقنياً، فلماذا تقبله؟ خصوصاً مع صور العائلة، أو لقطات مستندات، أو تصاميم لم تُنشر بعد.</p>
""",
 "body_en":"""
<p>Large images slow your site, fill your storage, and fail to upload on platforms with size limits. Yet most free compression tools require uploading your image first — meaning a copy now sits on a machine you do not own.</p>

<h2>Why is the image large in the first place?</h2>
<p>Three causes, each with a different fix:</p>
<ul>
  <li><strong>Huge dimensions:</strong> a phone camera shoots 12 megapixels. A web page rarely needs more than 1920px wide. Resizing alone can save 80%.</li>
  <li><strong>Wrong format:</strong> saving a photograph as PNG doubles its size for no benefit.</li>
  <li><strong>Excessive quality:</strong> you cannot see the difference between quality 100 and 80, but the file halves.</li>
</ul>

<h2>The correct order</h2>
<p>This sequence gives the best result:</p>
<ol>
  <li><strong>Resize first</strong> to what you actually need. This is by far the biggest win.</li>
  <li><strong>Pick the right format:</strong> WebP for web, JPG for sending, PNG only for transparency.</li>
  <li><strong>Set quality to 80.</strong> Drop to 65 for large background images nobody inspects closely.</li>
</ol>
<p>Reverse the order — compress hard then resize — and you get a worse image at the same size.</p>

<h2>Compress vs resize — what's the difference?</h2>
<ul>
  <li><strong>Resize:</strong> reduces the pixel count. A 4000×3000 image becomes 1920×1440.</li>
  <li><strong>Compress:</strong> keeps the pixel count and reduces the data used to describe it.</li>
</ul>
<p>The strongest approach uses both together — which is what the tool does in a single pass.</p>

<h2>When not to compress</h2>
<ul>
  <li><strong>Images destined for print:</strong> they need every pixel. Print from the original.</li>
  <li><strong>Images you will edit later:</strong> every compression discards data permanently. Always keep an original.</li>
  <li><strong>Graphics with hard edges:</strong> logos and diagrams degrade under lossy compression. Use PNG or lossless WebP.</li>
</ul>

<h2>Why does avoiding upload matter?</h2>
<p>Compression is pure arithmetic that needs no server — your browser handles it perfectly. So if uploading is technically unnecessary, why accept it? Especially for family photos, document scans, or unreleased designs.</p>
"""
},
{
 "slug":"convert-png-to-webp",
 "date":"2026-09-11",
 "tool":"services/convert-compress.html",
 "tool_ar":"جرّب أداة التحويل","tool_en":"Try the converter",
 "icon":"\U0001F504",
 "title_ar":"تحويل PNG إلى WebP: لماذا ومتى وكيف",
 "title_en":"Convert PNG to WebP: Why, When and How",
 "desc_ar":"دليل عملي لتحويل صور PNG إلى WebP مع الحفاظ على الشفافية — وتوفير يتجاوز نصف الحجم أحياناً.",
 "desc_en":"A practical guide to converting PNG images to WebP while keeping transparency — often saving more than half the file size.",
 "body_ar":"""
<p>PNG صيغة ممتازة لكنها مسرفة. WebP تعطيك نفس المزايا تقريباً بحجم أصغر بكثير. إليك متى يستحق التحويل ومتى لا.</p>

<h2>كم ستوفّر فعلاً؟</h2>
<p>التوفير يعتمد على نوع الصورة:</p>
<ul>
  <li><strong>لقطات الشاشة والواجهات:</strong> توفير 40–60٪ بضغط غير فاقد.</li>
  <li><strong>الشعارات والأيقونات البسيطة:</strong> توفير 25–45٪ مع الحفاظ الكامل على الشفافية.</li>
  <li><strong>الصور الفوتوغرافية المحفوظة خطأً كـPNG:</strong> توفير يتجاوز <strong>80٪</strong> — هذه أكبر مكسب.</li>
</ul>

<h2>هل تبقى الشفافية؟</h2>
<p>نعم، تماماً. هذه أهم نقطة يخشاها الناس. WebP يدعم قناة ألفا الكاملة مثل PNG بالضبط — لن تفقد الشفافية ولن تظهر خلفية بيضاء.</p>
<p>الفارق الوحيد: WebP يدعم <strong>نمطين</strong> — فاقد وغير فاقد. للشعارات والرسومات استخدم غير الفاقد للحفاظ على الحواف الحادة؛ وللصور الفوتوغرافية استخدم الفاقد بجودة 80.</p>

<h2>هل يدعمه الجميع؟</h2>
<p>كل المتصفحات الحديثة تدعمه منذ سنوات: Chrome وEdge وFirefox وSafari. المشكلة الوحيدة في برامج سطح مكتب قديمة جداً، أو بعض أدوات التصميم التي لم تُحدَّث.</p>
<p><strong>القاعدة العملية:</strong> استخدم WebP لكل ما ينشر على الويب. واحتفظ بنسخة PNG للأرشيف أو للتسليم لعميل قد يفتحها ببرنامج قديم.</p>

<h2>متى تبقى على PNG؟</h2>
<ul>
  <li>ملف تسلّمه لعميل أو مطبعة — إلا إن طلب WebP صراحةً.</li>
  <li>صورة ستمرّ بدورات تحرير متكرّرة — الأصل غير الفاقد أأمن.</li>
  <li>أيقونة تطبيق أو أصل تصميم داخل نظامك الفني.</li>
</ul>

<h2>الخطوات</h2>
<ol>
  <li>أفلت ملفات PNG — أو مجلداً كاملاً بمجلداته الفرعية.</li>
  <li>اختر WebP، واضبط الجودة على 80 (أو اتركها أعلى للرسومات الحادة).</li>
  <li>حدّد أقصى عرض إن أردت تصغير الأبعاد في الوقت نفسه.</li>
  <li>نزّل الملفات فردياً أو كلها في ZIP واحد.</li>
</ol>
<p>ستظهر لك نسبة التوفير لكل صورة — مؤشر مفيد لتعرف أي الصور كانت تستنزف موقعك.</p>
""",
 "body_en":"""
<p>PNG is an excellent but wasteful format. WebP gives you nearly the same benefits at a far smaller size. Here is when converting is worth it, and when it isn't.</p>

<h2>How much will you actually save?</h2>
<p>Savings depend on the image type:</p>
<ul>
  <li><strong>Screenshots and UI captures:</strong> 40–60% with lossless compression.</li>
  <li><strong>Simple logos and icons:</strong> 25–45% with transparency fully preserved.</li>
  <li><strong>Photographs mistakenly saved as PNG:</strong> over <strong>80%</strong> — the single biggest win.</li>
</ul>

<h2>Does transparency survive?</h2>
<p>Yes, completely. This is the point people worry about most. WebP supports a full alpha channel exactly like PNG — you will not lose transparency and no white background will appear.</p>
<p>The one difference: WebP has <strong>two modes</strong> — lossy and lossless. For logos and graphics use lossless to keep hard edges crisp; for photographs use lossy at quality 80.</p>

<h2>Is it universally supported?</h2>
<p>Every modern browser has supported it for years: Chrome, Edge, Firefox and Safari. The only friction is very old desktop software, or design tools that were never updated.</p>
<p><strong>Practical rule:</strong> use WebP for everything published on the web. Keep a PNG copy for archiving or for delivering to a client who may open it in older software.</p>

<h2>When to stay with PNG</h2>
<ul>
  <li>A file you deliver to a client or a printer — unless they explicitly ask for WebP.</li>
  <li>An image that will go through repeated editing rounds — a lossless original is safer.</li>
  <li>An app icon or a design asset inside your own system.</li>
</ul>

<h2>The steps</h2>
<ol>
  <li>Drop your PNG files — or an entire folder including subfolders.</li>
  <li>Choose WebP and set quality to 80 (or higher for sharp graphics).</li>
  <li>Set a max width if you want to resize at the same time.</li>
  <li>Download files individually or all together as a ZIP.</li>
</ol>
<p>You will see the saving percentage for each image — a useful signal for spotting which files were draining your site.</p>
"""
},
{
 "slug":"product-photos-white-background",
 "date":"2026-09-11",
 "tool":"services/background-removal.html",
 "tool_ar":"جرّب إزالة الخلفية","tool_en":"Try background removal",
 "icon":"\U0001F6CD",
 "title_ar":"صور المنتجات بخلفية بيضاء: دليل المتاجر الإلكترونية",
 "title_en":"Product Photos on a White Background: An E-commerce Guide",
 "desc_ar":"كيف تحوّل صور منتجاتك إلى خلفية بيضاء موحّدة تلبّي شروط أمازون ونون وتزيد ثقة المشتري.",
 "desc_en":"How to put your product photos on a clean white background that meets marketplace rules and builds buyer trust.",
 "body_ar":"""
<p>الخلفية البيضاء ليست ذوقاً بل <strong>شرطاً</strong> في معظم المتاجر الكبرى. أمازون مثلاً يشترط خلفية بيضاء نقية للصورة الرئيسية، ويرفض أو يخفض ترتيب المنتجات المخالفة.</p>

<h2>لماذا تزيد المبيعات؟</h2>
<ul>
  <li><strong>تركيز كامل على المنتج</strong> بلا مشتّتات بصرية.</li>
  <li><strong>اتساق الصفحة:</strong> صفحة منتجات بخلفيات متباينة تبدو غير احترافية وتقلّل الثقة.</li>
  <li><strong>ملفات أخف:</strong> الخلفية الموحّدة تُضغط أفضل بكثير، فتتحسّن سرعة متجرك.</li>
</ul>

<h2>التصوير أهم من المعالجة</h2>
<p>لا تعتمد على البرنامج لإصلاح تصوير سيئ. اتبع هذه القواعد وسيصبح العزل شبه تلقائي:</p>
<ul>
  <li><strong>باعد المنتج عن الخلفية</strong> نصف متر على الأقل — يمنع انعكاس الظلال عليها.</li>
  <li><strong>إضاءة من جهتين</strong> لتقليل الظلال الحادة التي يصعب عزلها.</li>
  <li><strong>خلفية مختلفة عن لون المنتج:</strong> منتج أبيض على خلفية بيضاء أصعب حالة على أي نموذج.</li>
  <li><strong>ثبّت الكاميرا</strong> وصوّر بأعلى دقة متاحة.</li>
</ul>

<h2>سير العمل الكامل</h2>
<ol>
  <li>أزل الخلفية بالذكاء الاصطناعي — ستحصل على خلفية شفافة.</li>
  <li>اختر الخلفية البيضاء من لوحة الألوان بدل الشفافة.</li>
  <li>نزّل الصورة، ثم مرّرها على أداة التحويل لضغطها بصيغة WebP أو JPG.</li>
  <li>وحّد الأبعاد لكل منتجاتك — المربع 1:1 هو المعيار الأكثر قبولاً.</li>
</ol>

<h2>المنتجات الصعبة</h2>
<ul>
  <li><strong>الزجاج والشفافيات:</strong> أصعب حالة إطلاقاً. صوّرها على خلفية داكنة ثم عالجها، أو استعن بتصحيح يدوي.</li>
  <li><strong>المجوهرات والتفاصيل الدقيقة:</strong> صوّر بأعلى دقة ممكنة — التفاصيل الصغيرة أول ما يضيع.</li>
  <li><strong>الأقمشة والفراء:</strong> الحواف الناعمة تحتاج تباينًا قويًا مع الخلفية.</li>
</ul>

<h2>ميزة المعالجة المحلية للتجار</h2>
<p>صور منتجاتك قبل الإطلاق <strong>معلومة تجارية حسّاسة</strong>. رفعها إلى خدمة مجانية يعني أن منتجك صار على خادم طرف ثالث قبل أن تعلنه. المعالجة داخل المتصفح تلغي هذا القلق تماماً — ولا حدّ على عدد الصور مهما كبر كتالوجك.</p>
""",
 "body_en":"""
<p>A white background is not a matter of taste — it is a <strong>requirement</strong> on most major marketplaces. Amazon, for instance, demands a pure white background for the main image and will reject or down-rank listings that break it.</p>

<h2>Why does it increase sales?</h2>
<ul>
  <li><strong>Full focus on the product</strong> with no visual distraction.</li>
  <li><strong>Page consistency:</strong> a catalogue with mismatched backgrounds looks unprofessional and erodes trust.</li>
  <li><strong>Lighter files:</strong> a uniform background compresses far better, improving your store's speed.</li>
</ul>

<h2>Shooting matters more than editing</h2>
<p>Do not rely on software to rescue a bad shot. Follow these rules and isolation becomes almost automatic:</p>
<ul>
  <li><strong>Separate the product from the backdrop</strong> by at least half a metre — this prevents shadows falling on it.</li>
  <li><strong>Light from two sides</strong> to reduce hard shadows that are difficult to cut out.</li>
  <li><strong>Use a backdrop that differs from the product colour:</strong> a white product on white is the hardest case for any model.</li>
  <li><strong>Stabilise the camera</strong> and shoot at the highest resolution available.</li>
</ul>

<h2>The full workflow</h2>
<ol>
  <li>Remove the background with AI — you get a transparent result.</li>
  <li>Pick the white background from the colour swatches instead of transparent.</li>
  <li>Download, then run it through the converter to compress as WebP or JPG.</li>
  <li>Standardise dimensions across your catalogue — a 1:1 square is the most widely accepted.</li>
</ol>

<h2>Difficult products</h2>
<ul>
  <li><strong>Glass and transparent items:</strong> the hardest case by far. Shoot against a dark backdrop, then process, or expect manual touch-up.</li>
  <li><strong>Jewellery and fine detail:</strong> shoot at maximum resolution — small details are the first thing lost.</li>
  <li><strong>Fabric and fur:</strong> soft edges need strong contrast against the backdrop.</li>
</ul>

<h2>Why local processing matters for sellers</h2>
<p>Pre-launch product photos are <strong>commercially sensitive</strong>. Uploading them to a free service puts your product on a third party's server before you announce it. In-browser processing removes that worry entirely — with no cap on image count, however large your catalogue.</p>
"""
},
{
 "slug":"image-sizes-social-media",
 "date":"2026-09-11",
 "tool":"services/convert-compress.html",
 "tool_ar":"جرّب أداة تغيير الحجم","tool_en":"Try the resizer",
 "icon":"\U0001F4F1",
 "title_ar":"مقاسات الصور الصحيحة لوسائل التواصل الاجتماعي",
 "title_en":"The Right Image Sizes for Social Media",
 "desc_ar":"جدول مرجعي بأبعاد الصور لكل منصة، ولماذا تفقد صورك جودتها عند النشر وكيف تمنع ذلك.",
 "desc_en":"A reference table of image dimensions for every platform, why your posts lose quality, and how to prevent it.",
 "body_ar":"""
<p>ترفع صورة عالية الجودة فتظهر باهتة أو مقصوصة. السبب ليس المنصة وحدها — بل عدم مطابقة الأبعاد والحجم لما تتوقّعه.</p>

<h2>لماذا تفقد صورك جودتها؟</h2>
<p>كل منصة <strong>تعيد ضغط</strong> ما ترفعه. فإذا رفعت صورة بأبعاد خاطئة، تحدث عمليتان ضارتان: إعادة تحجيم ثم إعادة ضغط. والنتيجة صورة أسوأ مما لو رفعتها بالمقاس الصحيح من البداية.</p>
<p><strong>القاعدة الذهبية:</strong> ارفع بالأبعاد الدقيقة التي تتوقّعها المنصة، وبجودة عالية (85–90)، ودع المنصة تضغط مرة واحدة فقط.</p>

<h2>جدول الأبعاد</h2>
<table>
  <tr><th>المنصة والنوع</th><th>الأبعاد</th><th>النسبة</th></tr>
  <tr><td>إنستغرام — منشور مربع</td><td>1080×1080</td><td>1:1</td></tr>
  <tr><td>إنستغرام — عمودي</td><td>1080×1350</td><td>4:5</td></tr>
  <tr><td>إنستغرام — ستوري وريلز</td><td>1080×1920</td><td>9:16</td></tr>
  <tr><td>فيسبوك — منشور</td><td>1200×630</td><td>1.91:1</td></tr>
  <tr><td>فيسبوك — غلاف</td><td>1640×856</td><td>—</td></tr>
  <tr><td>إكس (تويتر) — منشور</td><td>1600×900</td><td>16:9</td></tr>
  <tr><td>لينكدإن — منشور</td><td>1200×627</td><td>1.91:1</td></tr>
  <tr><td>يوتيوب — صورة مصغّرة</td><td>1280×720</td><td>16:9</td></tr>
  <tr><td>بنترست</td><td>1000×1500</td><td>2:3</td></tr>
  <tr><td>واتساب — حالة</td><td>1080×1920</td><td>9:16</td></tr>
</table>

<h2>النسبة أهم من الأبعاد</h2>
<p>لو اضطررت للاختيار، فالنسبة أهم. صورة بنسبة صحيحة وأبعاد أصغر تظهر سليمة؛ أما النسبة الخاطئة فتعني <strong>قصّاً تلقائياً</strong> قد يقطع رأس شخص أو نصف شعارك.</p>

<h2>أخطاء شائعة</h2>
<ul>
  <li><strong>رفع صورة الكاميرا كما هي:</strong> 12 ميغابكسل بنسبة 4:3 — ستُقصّ وتُضغط بعنف.</li>
  <li><strong>نص قرب الحافة:</strong> اترك هامشاً آمناً 10٪ من كل جهة؛ الواجهات تغطّي الأطراف بأزرار.</li>
  <li><strong>إعادة رفع صورة نُزّلت من منصة أخرى:</strong> ضغط فوق ضغط — أسوأ نتيجة ممكنة. ارفع من الأصل دائماً.</li>
  <li><strong>استخدام PNG لصورة فوتوغرافية:</strong> ملف ضخم بلا فائدة، وبعض المنصات تحوّله إلى JPG بجودة أقل.</li>
</ul>

<h2>سير عمل سريع</h2>
<ol>
  <li>حدّد المنصة والمقاس من الجدول أعلاه.</li>
  <li>غيّر أبعاد الصورة إلى المقاس المطلوب.</li>
  <li>احفظ بصيغة JPG بجودة 85–90 (أو PNG إن كان فيها نص حادّ أو شفافية).</li>
  <li>ارفع — ودع المنصة تضغط مرة واحدة فقط.</li>
</ol>
""",
 "body_en":"""
<p>You upload a high-quality image and it appears washed out or cropped. The platform is not solely to blame — your dimensions and file size did not match what it expects.</p>

<h2>Why do your images lose quality?</h2>
<p>Every platform <strong>re-compresses</strong> what you upload. If you upload at the wrong dimensions, two damaging operations occur: resampling, then re-compression. The result is worse than if you had uploaded at the correct size to begin with.</p>
<p><strong>Golden rule:</strong> upload at the exact dimensions the platform expects, at high quality (85–90), and let it compress only once.</p>

<h2>Dimensions table</h2>
<table>
  <tr><th>Platform and type</th><th>Dimensions</th><th>Ratio</th></tr>
  <tr><td>Instagram — square post</td><td>1080×1080</td><td>1:1</td></tr>
  <tr><td>Instagram — portrait</td><td>1080×1350</td><td>4:5</td></tr>
  <tr><td>Instagram — Story &amp; Reels</td><td>1080×1920</td><td>9:16</td></tr>
  <tr><td>Facebook — post</td><td>1200×630</td><td>1.91:1</td></tr>
  <tr><td>Facebook — cover</td><td>1640×856</td><td>—</td></tr>
  <tr><td>X (Twitter) — post</td><td>1600×900</td><td>16:9</td></tr>
  <tr><td>LinkedIn — post</td><td>1200×627</td><td>1.91:1</td></tr>
  <tr><td>YouTube — thumbnail</td><td>1280×720</td><td>16:9</td></tr>
  <tr><td>Pinterest</td><td>1000×1500</td><td>2:3</td></tr>
  <tr><td>WhatsApp — status</td><td>1080×1920</td><td>9:16</td></tr>
</table>

<h2>Ratio matters more than size</h2>
<p>If you must choose, prioritise the ratio. A correct ratio at smaller dimensions still displays properly; a wrong ratio means <strong>automatic cropping</strong> that may cut off someone's head or half your logo.</p>

<h2>Common mistakes</h2>
<ul>
  <li><strong>Uploading the camera file as-is:</strong> 12 megapixels at 4:3 — it will be cropped and heavily compressed.</li>
  <li><strong>Text near the edge:</strong> leave a 10% safe margin on every side; interfaces cover the edges with buttons.</li>
  <li><strong>Re-uploading an image downloaded from another platform:</strong> compression on top of compression — the worst possible result. Always upload from the original.</li>
  <li><strong>Using PNG for a photograph:</strong> a huge file for no benefit, and some platforms convert it to a lower-quality JPG anyway.</li>
</ul>

<h2>Quick workflow</h2>
<ol>
  <li>Pick the platform and size from the table above.</li>
  <li>Resize your image to those dimensions.</li>
  <li>Save as JPG at quality 85–90 (or PNG if it contains sharp text or transparency).</li>
  <li>Upload — and let the platform compress just once.</li>
</ol>
"""
}
]

# ════════════════════════════════════════════════════════════
TPL = """<!DOCTYPE html>
<!--
  ════════════════════════════════════════════════════════════
   007.gallery
   Creator : {EN_NAME}
   المبتكر  : {AR_NAME}
   Source  : {SITE}
   © 2026 {EN_NAME} — All rights reserved.
  ════════════════════════════════════════════════════════════
-->
<html lang="ar" dir="rtl" data-creator="{EN_NAME}" data-creator-ar="{AR_NAME}" data-source="{SITE}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title_ar} — 007.gallery</title>
<meta name="description" content="{desc_ar}">
<link rel="stylesheet" href="../assets/brand.css">
<link rel="icon" href="../favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="../assets/icon-32.png">
<link rel="apple-touch-icon" href="../assets/icon-180.png">
<link rel="manifest" href="../manifest.webmanifest">
<meta name="theme-color" content="#0a0b0f">
<link rel="canonical" href="{SITE}/articles/{slug}.html">
<meta property="og:type" content="article">
<meta property="og:site_name" content="007.gallery">
<meta property="og:title" content="{title_ar}">
<meta property="og:description" content="{desc_ar}">
<meta property="og:url" content="{SITE}/articles/{slug}.html">
<meta property="og:image" content="{SITE}/assets/og-cover.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="author" content="{EN_NAME}">
<meta name="creator" content="{EN_NAME}">
<meta name="copyright" content="© 2026 {EN_NAME}">
<link rel="author" href="../humans.txt">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Article",
"headline":{headline_json},
"description":{desc_json},
"datePublished":"{date}","dateModified":"{date}",
"inLanguage":["ar","en"],
"image":"{SITE}/assets/og-cover.png",
"author":{{"@type":"Person","name":"{EN_NAME}","alternateName":"{AR_NAME}"}},
"publisher":{{"@type":"Organization","name":"007.gallery","url":"{SITE}"}},
"mainEntityOfPage":"{SITE}/articles/{slug}.html"}}
</script>
<style>
  .art{{max-width:760px;margin:0 auto;padding:34px 0 20px}}
  .art .kicker{{display:flex;align-items:center;gap:10px;font-size:13px;color:var(--txt-mute);margin-bottom:14px;flex-wrap:wrap}}
  .art .kicker .ico{{font-size:22px}}
  .art h1{{font-size:clamp(24px,4.2vw,36px);font-weight:900;line-height:1.3;letter-spacing:-.3px}}
  .art .lede{{color:var(--txt-dim);font-size:16px;margin-top:12px;line-height:1.9}}
  .art h2{{font-size:20px;font-weight:800;color:var(--gold-2);margin:32px 0 10px}}
  .art p,.art li{{color:var(--txt-dim);font-size:15.5px;line-height:2}}
  .art ul,.art ol{{padding-inline-start:22px;margin:10px 0}}
  .art li{{margin-bottom:8px}}
  .art strong{{color:var(--txt)}}
  .art em{{color:var(--txt);font-style:italic}}
  .art table{{width:100%;border-collapse:collapse;margin:16px 0;font-size:14.5px}}
  .art th,.art td{{padding:11px 12px;border-bottom:1px solid var(--line);text-align:start;color:var(--txt-dim)}}
  .art th{{color:var(--gold-2);font-weight:800}}
  .cta-tool{{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;
    background:linear-gradient(135deg,var(--gold-soft),transparent);border:1px solid rgba(212,175,55,.28);
    border-radius:16px;padding:20px 22px;margin:34px 0}}
  .cta-tool p{{margin:0;color:var(--txt);font-weight:700;font-size:15px}}
  .art-en{{display:none}}
  html[lang=en] .art-ar{{display:none}}
  html[lang=en] .art-en{{display:block}}
  .backlink{{display:inline-flex;align-items:center;gap:7px;font-size:13.5px;color:var(--gold-2);font-weight:700;margin-bottom:6px}}
</style>
<script src="../assets/guardian.js" defer></script>
<script src="../assets/ads.js" defer></script>
</head>
<body>
<header class="site-header"><div class="wrap nav">
  <a class="brand" href="../index.html"><span class="logo">007</span><span>007<b>.gallery</b></span></a>
  <div class="nav-actions">
    <button class="btn btn-lang" id="langBtn" onclick="toggleLang()">EN</button>
    <a class="btn btn-ghost" href="index.html"><span data-ar>كل المقالات</span><span data-en>All articles</span></a>
  </div>
</div></header>

<main class="wrap">
 <article class="art">
  <a class="backlink" href="index.html"><span data-ar>← المقالات</span><span data-en>← Articles</span></a>

  <!-- عربي -->
  <div class="art-ar">
    <div class="kicker"><span class="ico">{icon}</span><span>{date_ar}</span> · <span>007.gallery</span></div>
    <h1>{title_ar}</h1>
    <p class="lede">{desc_ar}</p>
    {body_ar}
    <div class="cta-tool">
      <p>جرّب الأداة مجاناً الآن — تعمل في متصفحك بلا رفع.</p>
      <a class="btn btn-primary" href="../{tool}">{tool_ar} ←</a>
    </div>
  </div>

  <!-- English -->
  <div class="art-en">
    <div class="kicker"><span class="ico">{icon}</span><span>{date_en}</span> · <span>007.gallery</span></div>
    <h1>{title_en}</h1>
    <p class="lede">{desc_en}</p>
    {body_en}
    <div class="cta-tool">
      <p>Try the tool free — it runs in your browser, nothing uploaded.</p>
      <a class="btn btn-primary" href="../{tool}">{tool_en} →</a>
    </div>
  </div>

  <div data-ad-slot="leaderboard"></div>
 </article>
</main>

<footer class="site-footer"><div class="wrap foot">
  <a class="brand" href="../index.html"><span class="logo">007</span><span>007<b>.gallery</b></span></a>
  <p>© 2026 007.gallery · <span data-ar>كل الحقوق محفوظة</span><span data-en>All rights reserved</span>
     · <a href="../privacy.html" style="color:var(--gold-2)"><span data-ar>سياسة الخصوصية</span><span data-en>Privacy</span></a></p>
</div></footer>

<script>
"use strict";
function toggleLang(){{
  const h=document.documentElement, en=h.getAttribute('lang')==='en';
  h.setAttribute('lang', en?'ar':'en');
  h.setAttribute('dir',  en?'rtl':'ltr');
  document.getElementById('langBtn').textContent = en?'EN':'ع';
  try{{ localStorage.setItem('gallery_lang', en?'ar':'en'); }}catch(e){{}}
}}
try{{ if(localStorage.getItem('gallery_lang')==='en') toggleLang(); }}catch(e){{}}
</script>
</body>
</html>
"""

AR_MONTHS = {1:"يناير",2:"فبراير",3:"مارس",4:"أبريل",5:"مايو",6:"يونيو",
             7:"يوليو",8:"أغسطس",9:"سبتمبر",10:"أكتوبر",11:"نوفمبر",12:"ديسمبر"}
EN_MONTHS = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",
             7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}

def fmt_date(d, ar=True):
    y, m, day = map(int, d.split("-"))
    return f"{day} {(AR_MONTHS if ar else EN_MONTHS)[m]} {y}"

def build():
    here = os.path.dirname(os.path.abspath(__file__))
    outdir = os.path.join(here, "articles")
    os.makedirs(outdir, exist_ok=True)
    index = []
    for a in ARTICLES:
        page = TPL.format(
            SITE=SITE, EN_NAME=EN_NAME, AR_NAME=AR_NAME,
            slug=a["slug"], date=a["date"], icon=a["icon"],
            date_ar=fmt_date(a["date"], True), date_en=fmt_date(a["date"], False),
            title_ar=html.escape(a["title_ar"]), title_en=html.escape(a["title_en"]),
            desc_ar=html.escape(a["desc_ar"]), desc_en=html.escape(a["desc_en"]),
            headline_json=json.dumps(a["title_ar"], ensure_ascii=False),
            desc_json=json.dumps(a["desc_ar"], ensure_ascii=False),
            body_ar=a["body_ar"].strip(), body_en=a["body_en"].strip(),
            tool=a["tool"], tool_ar=a["tool_ar"], tool_en=a["tool_en"],
        )
        with open(os.path.join(outdir, a["slug"] + ".html"), "w", encoding="utf-8") as f:
            f.write(page)
        index.append({k: a[k] for k in
                      ("slug","date","icon","title_ar","title_en","desc_ar","desc_en","tool")})
        print("  ✓ articles/" + a["slug"] + ".html")

    index.sort(key=lambda x: x["date"], reverse=True)
    os.makedirs(os.path.join(here, "data"), exist_ok=True)
    with open(os.path.join(here, "data", "articles.json"), "w", encoding="utf-8") as f:
        json.dump({"updated": date.today().isoformat(), "articles": index},
                  f, ensure_ascii=False, indent=2)
    print(f"  ✓ data/articles.json ({len(index)} مقالات)")

if __name__ == "__main__":
    build()
