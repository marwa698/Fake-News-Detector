#  Bilingual Fake News Detector | كاشف الأخبار المزيفة

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-2.1.0-red?logo=pytorch)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28-ff4b4b?logo=streamlit)
![Transformers](https://img.shields.io/badge/🤗_Transformers-4.40-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

**A bilingual AI system for fake news detection supporting Arabic and English**

[Demo](#demo) • [Features](#features) • [Installation](#installation) • [Usage](#usage) • [Model Performance](#model-performance)

</div>

---

##  Overview

A full-stack NLP project that detects fake news in both **Arabic** and **English** using fine-tuned transformer models. The system automatically detects the language, routes to the appropriate model, checks source credibility, and explains its decision using LIME.

---

##  Features

| Feature | Description |
|--------|-------------|
|  **Bilingual** | Supports Arabic and English automatically |
|  **AraBERT** | Fine-tuned on 11K+ Arabic news articles |
|  **RoBERTa** | Fine-tuned on LIAR dataset (8.9K samples) |
|  **LIME Explainability** | Highlights words that influenced the decision |
|  **Source Credibility** | Checks domain reputation, age, author presence |
|  **Dark/Light Mode** | Toggle between themes |
|  **Bilingual UI** | Arabic/English interface switch |

---

##  Project Structure

```
fake-news-detector/
├── app/
│   ├── main.py                    # Streamlit entry point
│   ├── nlp/
│   │   ├── language_detector.py   # Auto language detection
│   │   ├── text_preprocessing.py  # Text cleaning
│   │   ├── arabic_model.py        # AraBERT wrapper
│   │   ├── english_model.py       # RoBERTa wrapper
│   │   └── classifier_router.py   # Routes text to correct model
│   ├── credibility/
│   │   ├── source_checker.py      # Domain + whois check
│   │   ├── domain_database.py     # Trusted/untrusted domains
│   │   ├── metadata_extractor.py  # Author, citations extractor
│   │   └── credibility_scorer.py  # Combines all factors
│   ├── explainability/
│   │   └── lime_explainer.py      # LIME word highlighting
│   └── components/
│       ├── input_panel.py         # Text/URL input UI
│       ├── verdict_card.py        # Result display
│       ├── highlighted_text.py    # Colored word display
│       └── source_report.py       # Source credibility report
├── models/
│   ├── arabert_arabic/            # Fine-tuned AraBERT weights
│   └── roberta_english/           # Fine-tuned RoBERTa weights
├── data/
│   ├── arabic/                    # Arabic fake news dataset
│   └── english/                   # LIAR dataset
├── notebooks/
│   ├── 01_eda_both_languages.ipynb
│   ├── 02_finetune_roberta.ipynb
│   └── 03_finetune_arabert.ipynb
└── requirements.txt
```

---

##  System Pipeline

```
Input (Text or URL)
        ↓
Language Detection (langdetect)
        ↓
    ┌───────────────────────┐
    │                       │
AraBERT               RoBERTa
(Arabic)              (English)
    │                       │
    └──────────┬────────────┘
               ↓
     Text Classification
     (FAKE / REAL + confidence)
               ↓
     Source Credibility Check
     (Domain + Age + Author)
               ↓
     Merge Scores (weighted)
               ↓
     LIME Explainability
               ↓
     Final Report to User
```

---

##  Model Performance

| Model | Dataset | Accuracy | F1 Score |
|-------|---------|----------|----------|
| AraBERT (aubmindlab/bert-base-arabertv02) | Arabic Fake News (~11K) | **99.74%** | **99.74%** |
| RoBERTa (roberta-base) | LIAR Dataset (~8.9K) | **~70%** | **~70%** |

---

##  Installation

```bash
# Clone the repo
git clone https://github.com/marwa698/fake-news-detector.git
cd fake-news-detector

# Create virtual environment
python -m venv venv --without-pip
venv\Scripts\activate  # Windows
python get-pip.py

# Install PyTorch with CUDA
pip install torch==2.1.0 --index-url https://download.pytorch.org/whl/cu118

# Install dependencies
pip install -r requirements.txt
```

>  Models are not included in the repo due to size. Train them using the notebooks or download separately.

---

##  Usage

```bash
streamlit run app/main.py
```

Then open `http://localhost:8501` in your browser.

### Input Options:
- **Direct text**: Paste any Arabic or English news article
- **Article URL**: Paste a URL and the system extracts the text automatically

---

##  Source Credibility Factors

| Factor | Weight | Description |
|--------|--------|-------------|
| Domain Reputation | 35% | Checked against known trusted/untrusted sources |
| Domain Age | 20% | Newer domains are more suspicious |
| Author Presence | 15% | Anonymous articles are flagged |
| Supporting Citations | 30% | Articles with sources score higher |

---

##  Tech Stack

- **Models**: AraBERT, RoBERTa (HuggingFace Transformers)
- **Explainability**: LIME
- **UI**: Streamlit
- **Source Check**: python-whois, BeautifulSoup4
- **Training**: PyTorch, CUDA (RTX 3050)

---

##  Training Details

### Arabic Model (AraBERT)
- Base: `aubmindlab/bert-base-arabertv02`
- Dataset: Arabic Fake and Real News (~46K → balanced to 11.5K)
- Epochs: 3 | Batch size: 8 | LR: 2e-5
- Hardware: RTX 3050 6GB

### English Model (RoBERTa)
- Base: `roberta-base`
- Dataset: LIAR Dataset (~10K → balanced to 9K)
- Epochs: 3 | Batch size: 8 | LR: 2e-5
- Hardware: RTX 3050 6GB

---

##  Author

**Marwa Yosry**  
[![GitHub](https://img.shields.io/badge/GitHub-marwa698-black?logo=github)](https://github.com/marwa698)

---

##  License

MIT License - feel free to use and modify.
