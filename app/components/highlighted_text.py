import streamlit as st

def render_highlighted_text(text: str, explanation: dict):
    """
    بيعرض النص مع تلوين الكلمات المؤثرة
    """
    if not explanation or "error" in explanation:
        st.write(text)
        return

    fake_words = {w for w, _ in explanation.get("top_fake_words", [])}
    real_words = {w for w, _ in explanation.get("top_real_words", [])}

    words = text.split()
    highlighted = []

    for word in words:
        clean = word.strip(".,!?؟،")
        if clean in fake_words:
            highlighted.append(
                f'<mark style="background:#ffcccc; padding:2px 4px; '
                f'border-radius:4px">{word}</mark>'
            )
        elif clean in real_words:
            highlighted.append(
                f'<mark style="background:#ccffcc; padding:2px 4px; '
                f'border-radius:4px">{word}</mark>'
            )
        else:
            highlighted.append(word)

    st.markdown(
        f'<div dir="auto" style="line-height:2; font-size:16px">'
        f'{" ".join(highlighted)}</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("🔴 **كلمات تشير للتزوير:**")
        for w, s in explanation.get("top_fake_words", []):
            st.markdown(f"- `{w}` ({s:+.3f})")
    with col2:
        st.markdown("🟢 **كلمات تشير للصحة:**")
        for w, s in explanation.get("top_real_words", []):
            st.markdown(f"- `{w}` ({s:+.3f})")