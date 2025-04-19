import pandas as pd
import statsmodels.api as sm
import json

data = {
    "Y_obs": [137,118,124,124,120,129,122,142,128,114,
              132,130,130,112,132,117,134,132,121,128],
    "W":     [0,1,1,1,0,1,1,0,0,1,
              1,0,0,1,0,1,0,0,1,1],
    "X":     [19.8,23.4,27.7,24.6,21.5,25.1,22.4,29.3,20.8,20.2,
              27.3,24.5,22.9,18.4,24.2,21.0,25.9,23.2,21.6,22.8]
}

df = pd.DataFrame(data)
X = sm.add_constant(df[["W", "X"]])
y = df["Y_obs"]

model = sm.OLS(y, X).fit()
print(model.summary())

model_params = model.params.to_dict()
print("\nModel Coefficients Saved for API:", model_params)

with open("model_params.json", "w") as f:
    json.dump(model_params, f)
