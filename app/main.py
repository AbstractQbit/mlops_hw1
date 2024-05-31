import catboost
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import FileResponse, HTMLResponse, Response

from app.preprocessing import import_data
from app.scorer import score

model = catboost.CatBoostClassifier().load_model("app/cbmodel.cbm")
cat_features = ["регион", "использование", "pack"]

app = FastAPI()


@app.get("/")
async def root():
    return FileResponse("app/index.html")


@app.post("/process_csv")
async def process_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(
            status_code=415,
            detail="Unsupported media type. Must be a `.csv` file.",
        )

    file_bytes = await file.read()
    input_df = import_data(file_bytes)

    res_csv = score(input_df)

    return Response(
        content=res_csv,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=predictions.csv"},
    )
