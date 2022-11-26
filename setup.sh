#!/usr/bin/env bash
git clone https://github.com/ultralytics/yolov5
apt-get update
apt-get install libgl1-mesa-dev
pip3 install -r requirements.txt
pip3 install -r yolov/requirements.txt
conda create --name animal-collector-server --python=3.10
conda activate animal-collector-server
uvicorn main:app --reload
