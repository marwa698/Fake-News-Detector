from app.credibility.source_checker import check_source

def score_credibility(url: str = None, text: str = None) -> dict:
    """
    يجمع كل عوامل المصداقية في score واحد
    """
    result = {
        "has_url": False,
        "source_score": 0.5,
        "has_author": False,
        "has_citations": False,
        "final_credibility_score": 0.5,
        "details": {}
    }

    # فحص الرابط
    if url and url.strip():
        result["has_url"] = True
        source_info = check_source(url)
        result["source_score"] = source_info["final_score"]
        result["details"]["source"] = source_info

    # فحص النص
    if text:
        # وجود كاتب
        author_indicators = [
            "بقلم", "كتب", "أفاد", "by ", "author:", "written by",
            "reporter:", "correspondent"
        ]
        result["has_author"] = any(
            ind.lower() in text.lower() for ind in author_indicators
        )

        # وجود مصادر داعمة
        citation_indicators = [
            "وفقاً", "بحسب", "أشار", "صرّح", "أعلن",
            "according to", "sources say", "officials said",
            "confirmed by", "reported by"
        ]
        result["has_citations"] = any(
            ind.lower() in text.lower() for ind in citation_indicators
        )

    # الـ score النهائي
    score = result["source_score"] * 0.5
    score += 0.20 if result["has_author"]    else 0.0
    score += 0.30 if result["has_citations"] else 0.0

    result["final_credibility_score"] = round(score, 3)
    return result