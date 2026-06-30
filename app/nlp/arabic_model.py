from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

class ArabicModel:
    def __init__(self, model_path: str = "models/arabert_arabic"):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"ArabicModel using: {self.device}")
        
        # لو الموديل مش موجود محلياً، حمّله من HuggingFace
        import os
        if not os.path.exists(model_path) or not os.path.exists(f"{model_path}/config.json"):
            print("Local model not found, loading from HuggingFace...")
            model_path = "Marwa-yosry/arabert-arabic-fake-news"
        
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_path)
            self.model = AutoModelForSequenceClassification.from_pretrained(model_path)
            self.model.to(self.device)
            self.model.eval()
            self.loaded = True
        except Exception as e:
            print(f"[WARNING] Arabic model error: {e}")
            self.loaded = False

    def predict(self, text: str) -> dict:
        if not self.loaded:
            return {"label": "UNKNOWN", "confidence": 0.0}
        
        inputs = self.tokenizer(
            text, return_tensors="pt", truncation=True,
            max_length=512, padding=True
        ).to(self.device)
        
        with torch.no_grad():
            outputs = self.model(**inputs)
            probs = torch.softmax(outputs.logits, dim=-1)
            pred = torch.argmax(probs, dim=-1).item()
            confidence = probs[0][pred].item()
        
        return {"label": "FAKE" if pred == 1 else "REAL", "confidence": round(confidence, 4)}