from app.nlp.language_detector import detect_language

class ClassifierRouter:
    """
    يستقبل النص ويوجهه للنموذج الصح (AraBERT أو RoBERTa)
    """
    def __init__(self):
        self.arabic_model = None
        self.english_model = None
        self._models_loaded = False

    def load_models(self):
        """تحميل النماذج - بيتعمل مرة واحدة بس"""
        from app.nlp.arabic_model import ArabicModel
        from app.nlp.english_model import EnglishModel
        
        print("Loading AraBERT...")
        self.arabic_model = ArabicModel()
        
        print("Loading RoBERTa...")
        self.english_model = EnglishModel()
        
        self._models_loaded = True
        print("Models loaded successfully!")

    def predict(self, text: str) -> dict:
        """
        Returns:
            {
                "language": "ar" or "en",
                "label": "FAKE" or "REAL",
                "confidence": 0.0 - 1.0
            }
        """
        if not self._models_loaded:
            self.load_models()
        
        lang = detect_language(text)
        
        if lang == "ar":
            result = self.arabic_model.predict(text)
        elif lang == "en":
            result = self.english_model.predict(text)
        else:
            # default للإنجليزي لو مش واضح
            lang = "en"
            result = self.english_model.predict(text)
        
        result["language"] = lang
        return result