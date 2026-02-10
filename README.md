# 🎬 Movie Recommender System

A content-based movie recommender system built with Python, scikit-learn, and Streamlit.

**🔗 Live Demo:** [https://recommendermovies.streamlit.app/](https://recommendermovies.streamlit.app/)

## 📅 Project Timeline (Day by Day)

### **Day 1: Project Setup**
- Initialized the repository.
- Gathered the dataset (`movies_final.csv`).

### **Day 2: Exploratory Data Analysis (EDA)**
- **File:** `EDA_Day2.ipynb`
- Analyzed the dataset structure.
- Cleaned and preprocessed the data.
- Visualized key features.

### **Day 3: Feature Engineering**
- **File:** `Day3.ipynb`
- Extracted relevant text features.
- Created tags for content-based filtering.

### **Day 4: Model Building**
- **File:** `Model_Building_Day4.ipynb`
- Vectorized text data using `TF-IDF`.
- Calculated cosine similarity.
- Saved the model artifacts (`movies.pkl`, `neighbors.pkl`, `tfidf_vectorizer.pkl`).

### **Day 5: Evaluation & Refinement**
- **File:** `day 5.ipynb`
- Tested the recommender logic.
- Refined the recommendation function.

### **Day 6: Application & Deployment**
- **Files:** `app.py` (FastAPI), `streamlit_app.py` (Streamlit)
- Built a FastAPI backend for API access.
- Created an interactive **Streamlit Frontend**.
- Deployed the application to **Streamlit Cloud**.

## 🚀 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Shiivu13/Project-1-Recommender.git
    cd Project-1-Recommender
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Streamlit App:**
    ```bash
    streamlit run streamlit_app.py
    ```

4.  **Run the FASTAPI Backend (Optional):**
    ```bash
    uvicorn app:app --reload
    ```
