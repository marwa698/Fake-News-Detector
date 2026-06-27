import streamlit as st

def render_input_panel() -> dict:
    """
    الـ panel اللي المستخدم بيدخل فيه النص أو الرابط
    """
    st.markdown("### 📝 أدخل الخبر للفحص")

    input_type = st.radio(
        "نوع الإدخال:",
        ["نص مباشر", "رابط مقال"],
        horizontal=True
    )

    text_input = ""
    url_input  = ""

    if input_type == "نص مباشر":
        text_input = st.text_area(
            "النص:",
            placeholder="الصق نص الخبر هنا...",
            height=200
        )
    else:
        url_input = st.text_input(
            "الرابط:",
            placeholder="https://example.com/article"
        )

    analyze_btn = st.button("🔍 تحليل", type="primary", use_container_width=True)

    return {
        "text": text_input,
        "url": url_input,
        "analyze": analyze_btn,
        "input_type": input_type
    }