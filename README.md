
## **Overview**
This project implements an **error recommendation system** using a recommendation engine based on user data. It generates error categories for users and provides an API endpoint to fetch the top `n` errors for a given user.

## **Steps Involved**

1. **Generating Data**:  
   We create user profiles using a random method in JSON format. These profiles are stored in a CSV file (`user_profiles.csv`).
   
2. **Recommendation System**:  
   The system recommends errors based on a user’s past error data, including error category, sub-category, and frequency.
   
3. **API Endpoint**:  
   An endpoint is created using Flask, where users can query their errors by `user_id` and retrieve the top `n` errors based on frequency.

## **File Descriptions**

1. **`Reccomendation_system.ipynb`**:  
   This notebook generates random user profiles in JSON format and saves them as `user_profiles.csv`. Each user has error categories such as **Grammar**, **Vocabulary**, **Pronunciation**, and **Fluency** along with sub-categories and frequencies.
   
2. **`user_profiles.csv`**:  
   A CSV file containing user data generated by the notebook. Each row represents a user's error profile.
   
3. **`app.py`**:  
   A Flask-based web application that reads from `user_profiles.csv`. It provides an API to fetch error recommendations for a user based on their historical error patterns.

## **API Usage**

### 1. **Home Route**
- **`GET /`**
- This renders a simple HTML form for inputting `user_id` and the number of recommended errors (`n`).

### 2. **Generate Error Recommendations**
- **`POST /generate-exercise`**
- **Parameters**:
  - `user_id`: ID of the user.
  - `n`: The number of top error recommendations to return (default is 3).
  
#### **Example Request**:

```bash
POST /generate-exercise
Content-Type: application/x-www-form-urlencoded

user_id=1&n=3
```
## **Running the Project**

**Ensure you have the necessary libraries installed:**

```bash
pip install pandas flask

```
**Run the Flask app:**

```bash
python app.py
```
**The app will be accessible at http://127.0.0.1:5000/. You can use the HTML form or make POST requests to the /generate-exercise endpoint.**
