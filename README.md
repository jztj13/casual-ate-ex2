# casual-ate-ex2
# Stakeholder Engagement Prediction App

This project builds and serves a causal regression model that predicts stakeholder engagement scores based on corporate sustainability spending and participation in a carbon offset program.

---

## 📁 Project Structure

| File/Component       | Purpose |
|----------------------|---------|
| `app.py`             | Starts a Flask server with a `/predict` endpoint that returns predicted engagement scores using the trained model. |
| `regression_model.py`| Trains a linear regression model using the Rubin Causal Model and saves parameters (`α`, `τ`, `β`) to `model_params.json`. |
| `model_params.json`  | Stores the trained model coefficients for use in prediction without retraining. |
| `requirements.txt`   | Lists all required Python packages (`flask`, `pandas`, `statsmodels`, etc.). |
| `Dockerfile`         | Containerizes the app for consistent deployment and reproducibility. |

---

## 🐳 Docker & Codespaces

### 1. Run Model Training

```bash
pip install statsmodels
python regression_model.py
```

### 2. Build Docker Image

```bash
docker build -t my-api .
```

This command:
- Uses the current directory (`.`) as build context
- Reads from the `Dockerfile`
- Tags the image as `my-api` for later reference

---

## 🧪 Using the API

### Run Flask App

```bash
python app.py
```

After running, you may see a browser pop-up — this is expected. Just ignore the "URL not found" message.

### Test with `curl`

```bash
curl -X POST http://127.0.0.1:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"W": 1, "X": 10}'
```

---

## 📊 Model Summary

### Model Equation

\[
Y_i^{\text{obs}} = \alpha + \tau W_i + X_i \beta + \varepsilon_i
\]

### Fit Statistics

| Term              | Value            |
|-------------------|------------------|
| R-squared         | 0.698            |
| Adjusted R²       | 0.662            |
| F-statistic (p)   | 19.61 (p = 3.84e-05) |

### Coefficients

| Term   | Coefficient | Std. Error | t-value | p-value | Interpretation |
|--------|-------------|------------|---------|---------|----------------|
| α (const) | 95.97     | 8.92       | 10.76   | 0.000   | Baseline engagement when W=0 and X=0 |
| τ (W)     | -9.11     | 2.05       | -4.43   | 0.000   | ATE: Program participation lowers engagement by 9.11 pts |
| β (X)     | 1.51      | 0.37       | 4.06    | 0.001   | Each $1,000 in spending increases engagement by 1.51 pts |

✅ **Both predictors are statistically significant (p < 0.05).**

---

## 🎯 Estimated Average Treatment Effect (ATE)

- Estimated \( \hat{\tau} = -9.11 \)
- Indicates that carbon offset program participation **reduces** engagement, holding spending constant.

---

## 📌 Assumptions for Causal Interpretation

For \( \hat{\tau} \) to reflect the **true causal effect**:
- ✅ No unmeasured confounders
- ✅ Correct model specification
- ✅ Ignorability (treatment assignment is as good as random)

---

## ✅ Checklist

- [x] GitHub repo link
- [x] `app.py` with `/predict` route
- [x] `regression_model.py` that creates `model_params.json`
- [x] `requirements.txt`
- [x] `Dockerfile`
- [x] `model_params.json` generated
- [x] This `README.md` explaining all components

---

## 🚀 Improvements (TBD)
_Add suggestions for model or code enhancements here._

