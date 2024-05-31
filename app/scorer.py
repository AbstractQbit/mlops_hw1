import catboost
import pandas as pd
from app.preprocessing import preprocess

model = catboost.CatBoostClassifier().load_model("app/cbmodel.cbm")

def score(df: pd.DataFrame):
    df["pred_probas"] = model.predict_proba(preprocess(df))[:, 1]
    df["preds"] = (df["pred_probas"] > 0.5).astype(int)
    result_csv = df.set_index("client_id")["preds"].to_csv()
    return result_csv