import requests


url = 'http://127.0.0.1/predict'

data = {
    "sepal_length": 5.1,
    "sepal_width": 3.3,
    "petal_length": 4.4,
    "petal_width": 2.3
}

response = requests.post(url, json=data)

if response.status_code == 200:
    prediction = response.json()["prediction"]
    print("Predicted species:", prediction)
else:
    print("Error:", response.text)
