import pandas as pd
from flask import Flask, request, jsonify, render_template_string
import logging
logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

df = pd.read_csv('user_profiles.csv')

@app.route('/')
def home():
    return render_template_string("""
    <h1>Exercise Recommendation System</h1>
    <p>Use the /generate-exercise endpoint with a POST request to get exercise recommendations.</p>
    <form action="/generate-exercise" method="post">
        <label for="user_id">User ID:</label>
        <input type="number" id="user_id" name="user_id" required><br><br>
        <label for="n">Number of recommendations:</label>
        <input type="number" id="n" name="n" value="3"><br><br>
        <input type="submit" value="Get Recommendations">
    </form>
    """)

@app.route('/generate-exercise', methods=['POST'])
def generate_exercise():
    try:
        user_id = int(request.form['user_id'])
        n = int(request.form.get('n', 3)) 

        
        user_data = df[df['user_id'] == user_id]
        if user_data.empty:
            return jsonify({"error": "User not found"}), 404

        
        categories = {
            'Grammar': ['Prepositions', 'Tenses'],
            'Vocabulary': ['Word Choice'],
            'Pronunciation': ['Intonation'],
            'Fluency': ['Sentence Structure']
        }

        error_list = []

       
        for main_category, sub_categories in categories.items():
           
            main_error_count = int(user_data[main_category].sum())
            if main_error_count > 0:
                for sub_category in sub_categories:
                    
                    sub_error_count = int(user_data[sub_category].sum())
                    if sub_error_count > 0:
                        error_list.append({
                            "errorCategory": main_category,
                            "errorSubCategory": sub_category,
                            "errorFrequency": sub_error_count
                        })

        
        sorted_errors = sorted(error_list, key=lambda x: x['errorFrequency'], reverse=True)[:n]

        return jsonify({
            "top_errors": sorted_errors
        })

    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return jsonify({"error": f"An internal server error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
