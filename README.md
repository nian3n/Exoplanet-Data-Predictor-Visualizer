# exoplanet_data_predictor_visualizer

A web app for **predicting and visualizing exoplanet data** using ML. Built with **Streamlit** for frontend, the website allows users to upload datasets, visualize featured relationships, and evaluate a pretrained model’s performance all in an interactive interface.

---

## 🚀 Features

- **🪐 Interactive Frontend**  
  Upload your exoplanet dataset (CSV) and explore it directly in the browser.

- **📊 Data Visualization Dashboard**  
  Generate scatterplots, histograms, and correlation heatmaps for any numeric features.

- **🤖 ML Model Prediction**  
  Automatically classifies each exoplanet entry into:
  - `CONFIRMED`
  - `CANDIDATE`
  - `FALSE POSITIVE`

- **📈 Model Testing**  
  Shows accuracy metrics (training, validation, and test performance) and evaluation results in real time.


---

## 🧩 Tech Stack

| Component | Description |
|------------|-------------|
| **Frontend** | Streamlit |
| **Modeling** | Scikit-learn / LightGBM / XGBoost |
| **Data Handling** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Deployment** | Streamlit Cloud / Local Run |

---

## 🧠 How It Works

1. **Upload a dataset** (`.csv`) with Kepler-style features (e.g. orbital period, planet radius, transit depth).  
2. The app preprocesses and validates the data to match the trained model’s features.  
3. The ML pipeline predicts the exoplanet type for each record.  
4. The dashboard displays:
   - Prediction results
   - Model accuracy
   - Interactive charts for deeper insights

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/exoplanet_data_predictor_visualizer.git
cd exoplanet_data_predictor_visualizer

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

pip install -r requirements.txt
streamlit run home.py

exoplanet_data_predictor_visualizer/
│
├── pages/
│   ├── About.py                #about the authors
│   ├── data_exploration.py     # Data visualization page
│   ├── model_testing.py        # Model accuracy display
│   ├── Exoplanet_predictor.py       #prediction
│
├── to be uploaded.pkl        # Pretrained ML model
├── home.py                     # Main Streamlit entry page
├── theme.py                    # Custom theming and UI styling
├── assets/                     # Backgrounds and icons
└── requirements.txt


