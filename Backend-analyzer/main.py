from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io

from model import model, device  # Load model here
from utils import predict_image, predict_from_comment

app = FastAPI()

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/analyze/")
async def analyze(file: UploadFile = File(...), comment: str = Form(...)):
    image = Image.open(io.BytesIO(await file.read())).convert("RGB")

    ai_pred, ai_conf = predict_image(image, model, device)
    comment_pred = predict_from_comment(comment)

    return {
        "student_comment": comment,
        "comment_prediction": comment_pred,
        "ai_prediction": ai_pred,
        "ai_confidence": ai_conf,
        "prediction_match": (ai_pred == comment_pred["predicted_disease"])
    }
