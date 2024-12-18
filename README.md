# House Price Prediction

## Features
- A trained Linear Regression model to predict house prices.
- A REST API built with Flask.
- A simple frontend to submit input data and view predictions.
- Dockerized for easy deployment.

## Setup and Usage

#### 1. Clone the Repository
Clone this repository to your local machine.

#### 2. Build and Run the App

##### Step 1: Build the Docker Image
Use this command `docker-compose build`

##### Step 2: Start the Container
Use this command `docker-compose up`
The app will be accessible at the port you mentioned

##### Step 3: Stop and Remove the Container
use this command `docker-compose down`

## Test API
#### Use Postman for testing the api
##### 1.Open Postman and create a new POST request.
##### 2.Go to the "Body" tab, select "raw," and choose JSON as the format.
##### 3.Write the Json Data and press Send
##### 4.Get the predicted price as the response 
