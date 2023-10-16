import pandas as pd
# from flask import Flask
# from flask import request
import json
import  Preprocess
import Predict
import Utils
# import ML_Pipeline.Preprocess
# import ML_Pipeline.Predict
# import ML_Pipeline.Utils
from datetime import datetime
from fastapi import FastAPI,Request
import uvicorn
app = FastAPI()

# app = Flask(__name__)

model_path = '../output/dnn-model'
ml_model, columns = Utils.load_model(model_path)

@app.get('/')
def checl_status():
    return f"Yaayy! I'm working fine with Fastapi on a Uvicorn Server. Time is {str(datetime.now())}"

@app.post("/get_license_status")
async def get_license_status(request: Request):
    items = await request.json()
    test_df = pd.DataFrame([items], columns=items.keys())
    processed_df = Preprocess.apply(test_df)
    prediction = list(Predict.init(processed_df, ml_model, columns)[0])
    max_value = max(prediction)
    max_index = prediction.index(max_value)
    output = {"status": Utils.TARGET[max_index]}
    print(output)
    return output


if __name__ == '__main__':
    uvicorn.run("deploy:app", host="0.0.0.0", port=5000, log_level="info")

