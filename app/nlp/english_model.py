from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

class EnglishModel:
    def __init__(self, model_path: str = "models/roberta_english"):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"EnglishModel using: {self.device}")
        
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_path)
            self.model = AutoModelForSequenceClassification.from_pretrained(model_path)
            self.model.to(self.device)
            self.model.eval()
            self.loaded = True
        except Exception as e:
            print(f"[WARNING] English model not found at {model_path}: {e}")
            print("Using placeholder - train the model first via Kaggle notebook.")
            self.loaded = False

    def predict(self, text: str) -> dict:
        if not self.loaded:
            return {"label": "UNKNOWN", "confidence": 0.0}
        
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            max_length=512,
            padding=True
        ).to(self.device)
        
        with torch.no_grad():
            outputs = self.model(**inputs)
            probs = torch.softmax(outputs.logits, dim=-1)
            pred = torch.argmax(probs, dim=-1).item()
            confidence = probs[0][pred].item()
        
        label = "FAKE" if pred == 1 else "REAL"
        return {"label": label, "confidence": round(confidence, 4)}