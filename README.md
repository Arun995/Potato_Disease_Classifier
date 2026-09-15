# Potato Disease Classification

An AI-powered web application that classifies potato leaf images into:

- Early Blight
- Late Blight
- Healthy

## Features

- Upload a potato leaf image
- Predict the disease using a CNN model
- Display the predicted class
- Display prediction confidence
- FastAPI backend
- React frontend
- Optional TensorFlow Serving support

## Tech Stack

- Python
- TensorFlow / Keras
- FastAPI
- React
- TensorFlow Serving
- Pillow
- NumPy
- Docker

## Project Structure

potato-disease/
│
├── api/
│   ├── main.py
│   ├── main-tf-serving.py
│   ├── requirements.txt
│   └── test.py
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── .env
│
├── PlantVillage/
├── saved_models/
├── potatoes.keras
├── potatoes.h5
└── models.config

## Model

The model is a Convolutional Neural Network trained using the PlantVillage potato leaf dataset.

### Training Details

- Image size: 256 × 256
- Image channels: 3
- Batch size: 32
- Epochs: 50
- Optimizer: Adam
- Loss function: Sparse Categorical Crossentropy
- Output activation: Softmax
- Number of classes: 3

### Classes

1. Early Blight
2. Late Blight
3. Healthy

## Model Architecture

The CNN contains:

- Image resizing and rescaling
- Multiple Conv2D layers
- ReLU activation
- MaxPooling2D layers
- Flatten layer
- Dense layer
- Softmax output layer

## Performance

The model achieved approximately 96% accuracy during testing.

The exact accuracy may vary depending on the dataset split, training run, and environment.

## Backend

The backend is developed using FastAPI.

### Run the Backend

cd api

pip install -r requirements.txt

uvicorn main:app --reload

The API will run at:

http://127.0.0.1:8000

### API Endpoints

Health Check:

GET /ping

Prediction:

POST /predict

The /predict endpoint accepts an image file and returns the predicted disease and confidence.

### Example Response

{
  "class": "Early Blight",
  "confidence": 0.96
}

## Frontend

The frontend is developed using React.

### Run the Frontend

cd frontend

npm install

npm start

The frontend will run at:

http://localhost:3000

## Prediction Flow

User uploads image
        ↓
React frontend
        ↓
FastAPI backend
        ↓
TensorFlow/Keras model
        ↓
Disease prediction
        ↓
Prediction result displayed

## TensorFlow Serving

The project also includes an optional TensorFlow Serving implementation.

TensorFlow Serving can serve the trained model through a REST API.

TensorFlow Serving endpoint:

http://localhost:8501/v1/models/potatoes_model:predict

## Future Improvements

- Improve model accuracy
- Add more plant diseases
- Add image validation
- Add prediction history
- Add Docker deployment
- Add cloud deployment
- Improve frontend design
- Add model performance monitoring

## Disclaimer

This project is created for educational and demonstration purposes.

The prediction should not be considered a professional agricultural diagnosis.
