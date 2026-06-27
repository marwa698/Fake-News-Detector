import lime
import lime.lime_text
import numpy as np
from typing import Callable

class LimeExplainer:
    def __init__(self, predict_fn: Callable, lang: str = "ar"):
        self.lang = lang
        self.explainer = lime.lime_text.LimeTextExplainer(
            class_names=["REAL", "FAKE"],
            bow=False
        )
        self.predict_fn = predict_fn

    def explain(self, text: str, num_features: int = 10) -> dict:
        """
        يرجع الكلمات اللي أثّرت على القرار
        """
        def predict_proba(texts):
            results = []
            for t in texts:
                pred = self.predict_fn(t)
                conf = pred["confidence"]
                if pred["label"] == "FAKE":
                    results.append([1 - conf, conf])
                else:
                    results.append([conf, 1 - conf])
            return np.array(results)

        try:
            exp = self.explainer.explain_instance(
                text,
                predict_proba,
                num_features=num_features,
                num_samples=100
            )

            words = exp.as_list()
            positive = [(w, s) for w, s in words if s > 0]
            negative = [(w, s) for w, s in words if s < 0]

            return {
                "top_fake_words": positive[:5],
                "top_real_words": negative[:5],
                "all_words": words
            }
        except Exception as e:
            return {"error": str(e), "top_fake_words": [], "top_real_words": []}