import re
import unicodedata

def clean_arabic_text(text: str) -> str:
    """تنظيف النص العربي"""
    if not text or not isinstance(text, str):
        return ""
    
    # إزالة الروابط
    text = re.sub(r'http\S+|www\S+', '', text)
    # إزالة الإيميلات
    text = re.sub(r'\S+@\S+', '', text)
    # إزالة الهاشتاقات والمنشنز
    text = re.sub(r'[@#]\S+', '', text)
    # إزالة الأرقام
    text = re.sub(r'[0-9٠-٩]+', '', text)
    # إزالة علامات الترقيم ما عدا العربية
    text = re.sub(r'[^\w\s\u0600-\u06FF]', ' ', text)
    # تطبيع الحروف العربية
    text = re.sub(r'[إأآا]', 'ا', text)
    text = re.sub(r'ة', 'ه', text)
    text = re.sub(r'ى', 'ي', text)
    # إزالة التشكيل
    text = re.sub(r'[\u064B-\u065F]', '', text)
    # إزالة المسافات الزائدة
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text


def clean_english_text(text: str) -> str:
    """تنظيف النص الإنجليزي"""
    if not text or not isinstance(text, str):
        return ""
    
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'[@#]\S+', '', text)
    text = re.sub(r'[^\w\s]', ' ', text)
    text = text.lower()
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text


def preprocess(text: str, lang: str = "ar") -> str:
    """الدالة الرئيسية"""
    if lang == "ar":
        return clean_arabic_text(text)
    else:
        return clean_english_text(text)


if __name__ == "__main__":
    test_ar = "أعلنت #وزارة_الصحة اليوم https://example.com عن اكتشاف علاج جديد!!!"
    test_en = "BREAKING: Scientists at https://example.com discovered a NEW cure!!!"
    
    print("AR:", preprocess(test_ar, "ar"))
    print("EN:", preprocess(test_en, "en"))