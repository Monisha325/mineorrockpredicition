# Rock vs Mine Prediction

A Machine Learning and Deep Learning-based classification project to distinguish between underwater rocks and mines using sonar signal data. Deployed as an interactive web app with real-time prediction capability using Streamlit.

---

## 1. Project Overview
Sonar signals are used in **underwater exploration**, **robotics**, and **naval defense**.  
This project builds **multiple classification models** (**ML + Deep Learning**) to distinguish between **rocks and mines** and provides an **interactive web interface** for easy predictions.

---

## 2. Project Structure
```bash
rock-vs-mine-prediction/
├── README.md
├── Rock Vs Mine.py
├── Rock_vs_Mine_Prediction.ipynb
├── header_image.jpg
├── predictive_system.py
├── requirements.txt
└── trained_model.sav

```
---

## 3. Dataset
- **Source:** UCI Machine Learning Repository  
- **Samples:** 208 sonar reflections  
- **Features:** 60 numerical attributes per sample  
- **Target Classes:**  
  - `R` → Rock  
  - `M` → Mine  

---

## 4. Technologies Used
- **Language:** Python 3.11+  
- **Libraries:**  
  - **Data Handling:** NumPy, Pandas  
  - **ML Models:** Scikit-learn (Logistic Regression, Random Forest)  
  - **Deep Learning:** TensorFlow / Keras  
  - **Visualization:** Matplotlib  
  - **Deployment:** Streamlit  

---

## 5. Models Implemented
### 1. Logistic Regression
Baseline binary classification model.

### 2. Random Forest
An ensemble model for improved handling of complex data.

### 3. Deep Neural Network (Keras)
- **Input layer:** 60 features  
- **Hidden layers:** 2 Dense layers (ReLU activation)  
- **Output layer:** Sigmoid activation (binary classification)  

---

## 6. How to Run
### Step 1: Clone the repository
```bash
git clone https://github.com/Monisha325/RockVsMinePredicition.git
cd RockVsMinePredicition
```

###Step 2: Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit app
```bash
streamlit run app.py
```

## 7. Results
Model	Training Accuracy	Test Accuracy
Logistic Regression	83.42%	76.19%
Random Forest	100%	76.19%
Deep Neural Network	96%	80–82%

## 8.Working Web Application model
The Streamlit app interface correctly classifies an object as a Rock based on sonar inputs.
<img width="1153" height="948" alt="image" src="https://github.com/user-attachments/assets/ac2d322a-9f06-4606-a6d5-67a7d174b604" />

## 8. Future Enhancements
Add hyperparameter tuning for better performance
Use SHAP/LIME for interpretability (understanding model decisions)


## 9. Author
Monisha Patnana
(Machine Learning & Deep Learning Enthusiast)

