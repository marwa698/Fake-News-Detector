from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# للحصول على نتائج ثابتة
DetectorFactory.seed = 42

def detect_language(text: str) -> str:
    """
    يحدد لغة النص.
    Returns: 'ar' للعربي، 'en' للإنجليزي، 'unknown' لغير ذلك
    """
    if not text or len(text.strip()) < 10:
        return "unknown"
    
    try:
        lang = detect(text)
        if lang == "ar":
            return "ar"
        elif lang == "en":
            return "en"
        else:
            return "unknown"
    except LangDetectException:
        return "unknown"


if __name__ == "__main__":
    # اختبار سريع
    tests = [
        "This news article claims that scientists discovered...",
        "أعلنت وزارة الصحة اليوم عن اكتشاف علاج جديد",
        "Bonjour le monde",
    ]
    for t in tests:
        print(f"[{detect_language(t)}] {t[:50]}")