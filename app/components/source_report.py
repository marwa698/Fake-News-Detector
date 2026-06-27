import streamlit as st

def render_source_report(credibility_result: dict):
    """
    تقرير فحص المصدر
    """
    st.markdown("### 🔎 تقرير المصدر")

    col1, col2, col3 = st.columns(3)

    with col1:
        icon = "✅" if credibility_result.get("has_author") else "❌"
        st.metric("كاتب محدد", icon)

    with col2:
        icon = "✅" if credibility_result.get("has_citations") else "❌"
        st.metric("مصادر داعمة", icon)

    with col3:
        score = credibility_result.get("final_credibility_score", 0.5)
        st.metric("نقاط المصداقية", f"{score:.0%}")

    # تفاصيل الدومين لو في رابط
    if credibility_result.get("has_url") and "source" in credibility_result.get("details", {}):
        source = credibility_result["details"]["source"]
        st.markdown("---")
        col1, col2, col3 = st.columns(3)

        with col1:
            status = source.get("domain_status", "unknown")
            icons  = {"trusted": "✅", "untrusted": "❌", "unknown": "⚠️"}
            st.metric("سمعة الدومين", icons.get(status, "⚠️"))

        with col2:
            age = source.get("age_years")
            st.metric("عمر الموقع", f"{age} سنة" if age else "غير معروف")

        with col3:
            st.metric("الدومين", source.get("domain", "-"))