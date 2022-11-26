#!/usr/bin/env bash
apt-get update
apt-get install libgl1-mesa-dev
pip3 install -r /app/requirements.txt
pip3 install -r /app/yolov5/requirements.txt
conda create --name animal-collector-server --python=3.10
conda activate animal-collector-server
uvicorn main:app --reload
