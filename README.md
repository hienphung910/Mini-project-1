# 💰 Salary Prediction using Linear Regression

A simple yet complete **Machine Learning project** that predicts salary based on years of experience using **Linear Regression built from scratch** (without scikit-learn), and an interactive web app powered by **Streamlit**.

---

## 📌 Overview

This project demonstrates:
- How to implement **Linear Regression from scratch** using the **Normal Equation**
- How to evaluate a model using **Mean Squared Error (MSE)**
- How to visualize the regression line with **Matplotlib**
- How to build and deploy a simple **Streamlit web 
app** for real-time salary prediction

---

## 📁 Project Structure

```
salary-prediction-linear-regression/
│
├── Data/
│   └── Salary_dataset.csv       # Dataset: YearsExperience vs Salary
│
├── Source/
│   └── main.py                  # Model training, evaluation & visualization
│
├── app.py                       # Streamlit web app for salary prediction
└── README.md
```

---

## 🧮 Algorithm

The model uses the **Normal Equation** to compute the optimal parameters directly:

$$\theta = (X^T X)^{-1} X^T y$$

Where:
- `w` (weight) = coefficient for Years of Experience
- `b` (bias) = intercept

Resulting regression equation:

```
Salary = 10052.79 × YearsExperience + 22655.57
```

---

## 📊 Dataset

| Column | Description |
|---|---|
| `YearsExperience` | Number of years of work experience |
| `Salary` | Annual salary (USD) |

- **Total samples**: ~30 rows
- **Split**: 80% training / 20% testing

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/salary-prediction-linear-regression.git
cd salary-prediction-linear-regression
```

### 2. Install dependencies

```bash
pip install numpy pandas matplotlib streamlit
```

### 3. Train the model & visualize

```bash
cd Source
python main.py
```

This will:
- Print the regression coefficients (`w`, `b`)
- Display Train/Test MSE scores
- Show a scatter plot with the regression line

### 4. Run the Streamlit web app

```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501` and use the slider to predict salaries!

---

## 📈 Results

| Metric | Value |
|---|---|
| **Equation** | Salary = 10052.79 × YearsExp + 22655.57 |
| **Evaluated with** | Mean Squared Error (MSE) |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **Python** | Core programming language |
| **NumPy** | Matrix operations & Normal Equation |
| **Pandas** | Data loading & manipulation |
| **Matplotlib** | Data visualization |
| **Streamlit** | Interactive web app |

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

