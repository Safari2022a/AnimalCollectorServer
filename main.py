import uvicorn
from yolov5.n_detect import run
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from urllib import request

import cv2
import base64
import numpy as np
import io

class DectImageRequest(BaseModel):
    img_base64: str
    width: int
    height: int
    conf: float

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!!"}

@app.post("/animal-detect")
async def create_user(request: DectImageRequest):
    img = decodeImage(request)
    img_path = "temp/request.jpg"
    cv2.imwrite(img_path, img)

    detect_result = run(source=img_path, conf_thres=request.conf)

    return {"params": detect_result}


def decodeImage(request):
    img_binary = base64.b64decode(request.img_base64)
    img = np.frombuffer(img_binary, dtype=np.uint8)
    img = img.reshape([request.height, request.width, 3])

    return img

uvicorn.run(app, host="0.0.0.0", port=3000)
