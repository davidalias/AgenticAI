import pandas as pd
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import FileResponse

from classify import classify

app = FastAPI()

@app.post("/classify")
async def classify_logs(file: UploadFile):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code = 400, detail = "File must be a csv")
    
    try:
        #Read the uploaded csv
        df = pd.read_csv(file.file)
        if "source" not in df.columns or "log_message" not in df.columns:
            raise HTTPException(status_code = 400, detail = "CSV must contain 'source' and 'log_message' columns")