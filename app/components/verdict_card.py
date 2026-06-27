import streamlit as st

def render_verdict_card(label: str, confidence: float,
                         credibility_score: float, language: str):
    """
    بيعرض النتيجة النهائية
    """
    # الـ weighted final score
    final_score = (confidence * 0.6) + (credibility_score * 0.4)

    if label == "FAKE":
        verdict     = "❌ خبر مزيف"
        color       = "#ff4b4b"
        bg          = "#fff0f0"
    elif label == "REAL":
        verdict     = "✅ خبر حقيقي"
        color       = "#00c853"
        bg          = "#f0fff4"
    else:
        verdict     = "⚠️ غير محدد"
        color       = "#ffa500"
        bg          = "#fff8f0"

    lang_display = "🇸🇦 عربي" if language == "ar" else "🇺🇸 إنجليزي"

    st.markdown(f"""
    <div style="
        background:{bg};
        border:2px solid {color};
        border-radius:12px;
        padding:24px;
        text-align:center;
        margin:16px 0;
    ">
        <h1 style="color:{color}; margin:0">{verdict}</h1>
        <p style="color:#666; margin:8px 0">اللغة المكتشفة: {lang_display}</p>
        <hr style="border-color:{color}; opacity:0.3">
        <div style="display:flex; justify-content:space-around; margin-top:12px">
            <div>
                <h3 style="color:{color}">{confidence:.0%}</h3>
                <p style="color:#888; margin:0">ثقة النموذج</p>
            </div>
            <div>
                <h3 style="color:{color}">{credibility_score:.0%}</h3>
                <p style="color:#888; margin:0">مصداقية المصدر</p>
            </div>
            <div>
                <h3 style="color:{color}">{final_score:.0%}</h3>
                <p style="color:#888; margin:0">النتيجة النهائية</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)