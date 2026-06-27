import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ─── Page Config (لازم يكون أول حاجة) ─────────────────
st.set_page_config(
    page_title="كاشف الأخبار المزيفة",
    page_icon="🔍",
    layout="wide",
)

# ─── Session State ─────────────────────────────────────
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False
if "lang" not in st.session_state:
    st.session_state.lang = "ar"

# ─── Translations ──────────────────────────────────────
T = {
    "ar": {
        "title": "كاشف الأخبار المزيفة 🔍",
        "subtitle": "نظام ذكاء اصطناعي ثنائي اللغة للكشف عن الأخبار المزيفة",
        "analyze": "🔍 تحليل",
        "input_label": "أدخل الخبر للفحص",
        "input_type": "نوع الإدخال:",
        "text_input": "نص مباشر",
        "url_input": "رابط مقال",
        "text_placeholder": "الصق نص الخبر هنا...",
        "url_placeholder": "https://example.com/article",
        "warning": "⚠️ من فضلك أدخل نص أو رابط!",
        "extracting": "جاري استخراج النص من الرابط...",
        "analyzing": "🤖 جاري التحليل...",
        "tab1": "📊 تحليل النص",
        "tab2": "🔎 فحص المصدر",
        "tab3": "ℹ️ عن النظام",
        "words_title": "الكلمات المؤثرة في القرار",
        "about": """
### عن النظام
- **نموذج العربي:** AraBERT
- **نموذج الإنجليزي:** RoBERTa
- **Explainability:** LIME
- **فحص المصدر:** Domain + عمر الموقع + كاتب

### كيف يعمل؟
1. يكشف لغة النص تلقائياً
2. يوجهه للنموذج المناسب
3. يفحص مصداقية المصدر
4. يدمج النتيجتين في score نهائي
5. يشرح القرار بتلوين الكلمات
        """
    },
    "en": {
        "title": "Fake News Detector 🔍",
        "subtitle": "Bilingual AI system for fake news detection",
        "analyze": "🔍 Analyze",
        "input_label": "Enter News to Check",
        "input_type": "Input type:",
        "text_input": "Direct text",
        "url_input": "Article URL",
        "text_placeholder": "Paste the news text here...",
        "url_placeholder": "https://example.com/article",
        "warning": "⚠️ Please enter text or URL!",
        "extracting": "Extracting text from URL...",
        "analyzing": "🤖 Analyzing...",
        "tab1": "📊 Text Analysis",
        "tab2": "🔎 Source Check",
        "tab3": "ℹ️ About",
        "words_title": "Words that influenced the decision",
        "about": """
### About
- **Arabic Model:** AraBERT
- **English Model:** RoBERTa
- **Explainability:** LIME
- **Source Check:** Domain + Age + Author

### How it works?
1. Auto-detects language
2. Routes to the right model
3. Checks source credibility
4. Combines scores
5. Highlights influential words
        """
    }
}

# ─── Theme ─────────────────────────────────────────────
dark = st.session_state.dark_mode
lang = st.session_state.lang
t    = T[lang]
direction = "rtl" if lang == "ar" else "ltr"

if dark:
    bg         = "#0e1117"
    card_bg    = "#1e2130"
    text_color = "#fafafa"
    border     = "#444444"
    btn_bg     = "#2d2d2d"
else:
    bg         = "#f8f9fa"
    card_bg    = "#ffffff"
    text_color = "#0e1117"
    border     = "#dddddd"
    btn_bg     = "#ffffff"

st.markdown(f"""
<style>
/* اتجاه الصفحة */
html, body, .stApp {{
    direction: {direction};
    background-color: {bg} !important;
    color: {text_color} !important;
}}

/* إخفاء عناصر Streamlit الافتراضية */
#MainMenu, footer, header {{ visibility: hidden; }}

/* الـ text area */
.stTextArea textarea {{
    background-color: {card_bg} !important;
    color: {text_color} !important;
    border: 1px solid {border} !important;
    border-radius: 10px !important;
    font-size: 16px !important;
}}

/* الـ text input */
.stTextInput > div > div > input {{
    background-color: {card_bg} !important;
    color: {text_color} !important;
    border: 1px solid {border} !important;
    border-radius: 10px !important;
}}

/* زرار التحليل الرئيسي */
.stButton > button[kind="primary"] {{
    background-color: #ff4b4b !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-size: 18px !important;
    padding: 12px !important;
}}

/* أزرار الثيم واللغة */
.stButton > button:not([kind="primary"]) {{
    background-color: {btn_bg} !important;
    color: {text_color} !important;
    border: 1px solid {border} !important;
    border-radius: 8px !important;
    font-size: 16px !important;
    padding: 6px 12px !important;
}}

/* الـ radio buttons */
.stRadio label {{
    color: {text_color} !important;
}}

/* الـ markdown */
.stMarkdown p, .stMarkdown h1, .stMarkdown h2, 
.stMarkdown h3, .stMarkdown li {{
    color: {text_color} !important;
}}

/* الـ tabs */
.stTabs [data-baseweb="tab"] {{
    color: {text_color} !important;
}}

/* card style */
.custom-card {{
    background-color: {card_bg};
    border: 1px solid {border};
    border-radius: 12px;
    padding: 20px;
    margin: 10px 0;
}}
</style>
""", unsafe_allow_html=True)

# ─── Header ────────────────────────────────────────────
col_title, col_btns = st.columns([8, 2])

with col_title:
    st.markdown(f"## {t['title']}")
    st.markdown(f"*{t['subtitle']}*")

with col_btns:
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
    b1, b2 = st.columns(2)
    with b1:
        if st.button("🌙" if not dark else "☀️", key="theme_btn", help="تغيير الثيم"):
            st.session_state.dark_mode = not st.session_state.dark_mode
            st.rerun()
    with b2:
        if st.button("EN" if lang == "ar" else "ع", key="lang_btn", help="تغيير اللغة"):
            st.session_state.lang = "en" if lang == "ar" else "ar"
            st.rerun()

st.markdown("---")

# ─── Load Models ───────────────────────────────────────
@st.cache_resource
def load_router():
    from app.nlp.classifier_router import ClassifierRouter
    router = ClassifierRouter()
    router.load_models()
    return router

router = load_router()

# ─── Input ─────────────────────────────────────────────
st.markdown(f"### 📝 {t['input_label']}")

input_type = st.radio(t["input_type"], [t["text_input"], t["url_input"]], horizontal=True)

text_input = ""
url_input  = ""

if input_type == t["text_input"]:
    text_input = st.text_area("", placeholder=t["text_placeholder"], height=200, label_visibility="collapsed")
else:
    url_input = st.text_input("", placeholder=t["url_placeholder"], label_visibility="collapsed")

analyze_btn = st.button(t["analyze"], type="primary", use_container_width=True)

# ─── Analysis ──────────────────────────────────────────
if analyze_btn:
    text = text_input.strip()
    url  = url_input.strip()

    if not text and not url:
        st.warning(t["warning"])
        st.stop()

    if url and not text:
        with st.spinner(t["extracting"]):
            try:
                from newspaper import Article
                article = Article(url)
                article.download()
                article.parse()
                text = article.text
                if not text:
                    st.error("❌ مش قادر أستخرج النص من الرابط ده")
                    st.stop()
            except Exception as e:
                st.error(f"❌ خطأ: {e}")
                st.stop()

    with st.spinner(t["analyzing"]):
        from app.credibility.credibility_scorer import score_credibility
        from app.explainability.lime_explainer import LimeExplainer

        prediction  = router.predict(text)
        credibility = score_credibility(url=url, text=text)
        explainer   = LimeExplainer(
            predict_fn=lambda tx: router.predict(tx),
            lang=prediction["language"]
        )
        explanation = explainer.explain(text)

    st.markdown("---")

    # Verdict Card
    from app.components.verdict_card import render_verdict_card
    render_verdict_card(
        label=prediction["label"],
        confidence=prediction["confidence"],
        credibility_score=credibility["final_credibility_score"],
        language=prediction["language"]
    )

    st.markdown("---")

    tab1, tab2, tab3 = st.tabs([t["tab1"], t["tab2"], t["tab3"]])

    with tab1:
        st.markdown(f"### {t['words_title']}")
        from app.components.highlighted_text import render_highlighted_text
        render_highlighted_text(text, explanation)

    with tab2:
        from app.components.source_report import render_source_report
        render_source_report(credibility)

    with tab3:
        st.markdown(t["about"])