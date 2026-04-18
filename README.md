# Data Analysis Internship Project

This repository contains internship deliverables across four core data science tasks:

1. Big Data Analysis (PySpark)
2. Machine Learning (scikit-learn)
3. Interactive Dashboard (Dash)
4. Sentiment Analysis (NLTK + scikit-learn)

It also includes a small standalone Snake game in `snake/`.

## Repository Structure

```text
Data-Analysis-Internship/
|-- data/
|   |-- IPL.csv
|-- notebooks/
|   |-- Task1_BigData.ipynb
|   |-- Task2_ML.ipynb
|   `-- task2_ml_model.ipynb
|-- snake/
|   |-- index.html
|   |-- styles.css
|   `-- game.js
|-- README.md
`-- requirements.txt
```

## Setup

### 1) Create and activate virtual environment (recommended)

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Launch Jupyter

```bash
jupyter notebook
```

Open notebooks from the `notebooks/` folder.

## Task Guide

## Task 1: Big Data Analysis
- Use PySpark to load/simulate large data.
- Perform cleaning and transformations.
- Run EDA aggregations and summarize insights.
- Demonstrate scalability with partitioning/caching/timing.

## Task 2: Machine Learning
- Load dataset (e.g., sklearn built-in).
- Preprocess features and perform feature selection.
- Train classification or regression model.
- Report metrics (accuracy/F1/ROC-AUC or suitable alternatives).

## Task 3: Dashboard (Dash)
- Build an interactive dashboard with filters and plots.
- Show meaningful dataset insights.

If your dashboard script is `dashboard_app.py`, run:

```bash
python dashboard_app.py
```

Then open `http://127.0.0.1:8050`.

## Task 4: Sentiment Analysis
- Load tweet/review text dataset.
- Apply text preprocessing (cleaning/tokenization/stopword handling).
- Train or apply sentiment model.
- Report performance and key insights.

## Optional: Snake Game

Run directly:
- Open `snake/index.html` in your browser.

Or serve the repository root and navigate to:
- `/snake/`

## Notes for Submission

- Keep notebook cells clean and well-commented.
- Add markdown explanations before major code blocks.
- Include final insights/conclusion section per task.
- Ensure all code runs top-to-bottom without errors in a fresh environment.
