# Health Insurance Cost Prediction

I built this project to explore whether information about a person’s age, health, and lifestyle can help estimate their health insurance payment. It combines data analysis, machine learning, and a small Streamlit app so the work can be explored as both a notebook project and an interactive demo.

The estimate is generated from patterns in the data. It is not an actual insurance quote, and it should not be used to make decisions about a person’s coverage or cost.

## What the project explores

The analysis investigates how the available input features relate to the insurance payment recorded in the dataset. These include:

- **Age**
- **Gender**
- **BMI**
- **Blood pressure**
- **Diabetes status**
- **Number of children**
- **Smoking status**

The precise meaning, units, and collection method for each field depend on the dataset. Check the dataset documentation before interpreting the values or comparing them with real-world insurance costs.

## Project workflow

The project follows a typical supervised-learning workflow:

1. **Prepare the data** — inspect the dataset, check its columns and data types, and prepare the fields for analysis.
2. **Explore patterns** — use summaries and visualizations to understand the data and look for relationships between features and the target payment.
3. **Prepare model inputs** — encode categorical fields and scale numeric fields where needed. The same fitted preprocessing objects are saved and reused by the app.
4. **Train and compare models** — evaluate regression approaches such as Linear Regression, Polynomial Regression, Support Vector Regression, Random Forest, and XGBoost.
5. **Evaluate predictions** — use metrics including R², MAE, and RMSE. These describe performance on the data used for evaluation; they do not guarantee accuracy for other people or datasets.
6. **Try the model interactively** — enter sample details in the Streamlit app and view an estimated payment.

The notebooks contain the analysis and training work. The Streamlit app loads the saved model and preprocessing files to make predictions from its form inputs.

## Repository contents

- `NoteBooks/` — notebooks for data exploration and model development
- `NoteBooks/src/app.py` — Streamlit prediction interface
- `Data/` — dataset files, if included in the repository
- `NoteBooks/src/*.pkl` — saved model, scaler, and encoders required by the app, if included

The app expects these files alongside `app.py`:

- `best_model.pkl`
- `scaler.pkl`
- `label_encoder_gender.pkl`
- `label_encoder_diabetic.pkl`
- `label_encoder_smoker.pkl`

The model and preprocessing files must come from the same training process and match the input columns and their order. If they are missing, the app cannot make predictions.

## Run the app on Windows

From the repository root, install the dependencies listed in `Requirements.txt` into your virtual environment:

```bash
./.venv/Scripts/python.exe -m pip install -r Requirements.txt
```

Then launch Streamlit:

```bash
./.venv/Scripts/python.exe -m streamlit run "DataApps/Health Insurance Cost/NoteBooks/src/app.py"
```

Open the local URL printed in the terminal, usually `http://localhost:8501`. To stop the app, press **Ctrl+C** in that terminal.

## Interpreting the results

A model can learn associations in its training data without identifying what causes a payment to be higher or lower. Its estimates may reflect the dataset’s size, source, missing information, and limitations. The model may perform differently on people or data not represented during training.

The app currently formats the displayed estimate with a Ghana cedi (`₵`) symbol. Confirm that this matches the dataset’s currency and units before interpreting the amount.

## Limitations and responsible use

This is a learning project, not a pricing system or professional insurance tool. Health and demographic information is sensitive, and model outputs can be inaccurate or unfair. Do not use the app to determine someone’s eligibility, set premiums, or make decisions about their healthcare or coverage.

When sharing or extending the project, avoid publishing private personal information, credentials, or data you are not authorized to distribute.
