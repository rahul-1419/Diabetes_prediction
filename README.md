# Diabetes Prediction 🩺

## Project Overview  
This is an end-to-end machine learning project that builds a predictive model to determine whether a person has diabetes based on health metrics. The project covers data preprocessing, exploratory data analysis, model training, evaluation, and deployment.

## Features & Highlights  
- Data preprocessing: handled missing values, scaling, outlier detection, feature engineering.  
- Model building: trained models (e.g., Logistic Regression, Random Forest) and selected the best performing one.  
- Evaluation: used metrics such as accuracy, ROC-AUC, confusion matrix to assess model performance.  
- Deployment: packaged the best model and set up a simple web app (via `app.py`) for inference.  
- Reproducible pipeline: all steps documented and versioned; model saved as `.pkl`.

## Tech Stack  
- **Language:** Python  
- **Libraries:** Pandas, NumPy, scikit-learn, Matplotlib / Seaborn  
- **Web App / Deployment:** Flask (or whichever you used)  
- **Model Serialization:** Pickle (or joblib)  
- **Versioning / Environment:** requirements.txt for dependencies  
- **Dataset:** [Describe dataset, e.g., “Pima Indians Diabetes Dataset”]

## Installation & Setup  
1. **Clone the repository**  
 git clone https://github.com/rahul-1419/Diabetes_prediction.git
 cd Diabetes_prediction

2. **Create a virtual environment (optional but recommended)**
python3 -m venv venv 
source venv/bin/activate

3. **Install dependencies**
pip install -r requirements.txt

4. **Run the notebook or web app**
To explore the analysis and modelling: open NoteBook/Script.ipynb in Jupyter.

To run the web app:
python app.py

## Usage

Input relevant patient health metrics (e.g., glucose level, BMI, age) in the web form.

Submit to get a prediction (Diabetic / Non-Diabetic) along with probability (if implemented).

Use the model for batch inference by loading best_logistic_regression_model.pkl in your own scripts.

## Model Performance

| Model               | Accuracy | ROC-AUC | Notes                               |
| ------------------- | -------- | ------- | ----------------------------------- |
| Logistic Regression | XX%      | X.XX    | Chosen model for deployment         |
| Random Forest       | XX%      | X.XX    | Higher variance but slightly better |
