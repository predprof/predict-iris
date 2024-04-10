import joblib
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import logging


app = FastAPI()
model = joblib.load('./model.joblib')


class IrisSpecies(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.get('/')
def root():
    return {"message": "Welcome to the Iris Species Prediction API"}


@app.post('/predict')
def predict(iris: IrisSpecies):
    """
    Predict the spicies of the iris.

    :param iris: the parameters of iris
    :return: the predicted species of iris
    """
    features = [[
        iris.sepal_length,
        iris.sepal_width,
        iris.petal_length,
        iris.petal_width
    ]]
    logging.info(features)

    prediction = model.predict(features).tolist()[0]
    return {
        "prediction": prediction
    }


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=80)
