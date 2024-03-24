import flask
from flask import (
    Flask,
    jsonify,
    request,
    redirect
)
import json
import random
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

#FINAL = pd.read_csv("more/final_student_course_records.csv")
FINAL = 1

@app.route('/class', methods=['POST', 'OPTIONS'])
def handle_form_submission():
    if request.method == 'OPTIONS':
        # The actual server should handle preflight request automatically,
        # but you can customize the response here if needed.
        return _build_cors_preflight_response()

    # Assuming POST request handling below
    data = request.json

    # Process the data (here we are just printing it)
    major = data.get('major')
    year = data.get('year')
    gpa = data.get('gpa')

    print(f"Major: {major}, Year: {year}, GPA: {gpa}")

    return jsonify({"status": "success", "message": "Form data received"}), 200

def _build_cors_preflight_response():
    response = jsonify({"status": "success", "message": "CORS preflight"})
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type")
    return response


@app.route("/classtrial")
def hello():
    reply = jsonify({
        0 : {
            "class": "Introduction to Computer Science",
            "id": "01:198:111",
            "dept": "Computer Science",
            "school": "School of Arts and Sciences",
            "credits": 4
        },
        1 : {
            "class": "Data Structures",
            "id": "01:198:112",
            "dept": "Computer Science",
            "school": "School of Arts and Sciences",
            "credits": 4
        },
        2 : {
            "class": "Introduction to Discrete Structures I",
            "id": "01:198:205",
            "dept": "School of Arts and Sciences",
            "school": "School of Arts and Sciences",
            "credits": 4            
        },
        3 : {
            "class": "Caclulus I for Mathematical Sciences",
            "id": "01:640:151",
            "dept": "Mathematics",
            "school": "School of Arts and Sciences",
            "credits": 4                     
        },
        4 : {
            "class": "Cognitive Science: A Multidisciplinary Introduction",
            "id": "01:185:201",
            "dept": "Cognitive Science",
            "school": "School of Arts and Sciences",
            "credits": 4
        },
    })
    reply.headers.add('Access-Control-Allow-Origin', '*')
    return reply
    
    
@app.route("/classtrial/<int:id>")
def get_class(id):
    reply = jsonify({
        "class": "Introduction to Computer Science",
        "id": "01:198:111",
        "dept": "Computer Science",
        "school": "School of Arts and Sciences",
        "credits": 4
    })
    reply.headers.add('Access-Control-Allow-Origin', '*')
    return reply
    
@app.route("/proftrial")
def get_prof():
    reply = jsonify({
        0 : {
            "professor": "Kostas Bekris",
            "dept": "Computer Science",
            "school": "School of Arts and Sciences",
            "ratings": [4.5, 3.9, 3,8]
        },
        1 : {
            "professor": "Sesh Venugopal",
            "dept": "Computer Science",
            "school": "School of Arts and Sciences",
            "rating": 4.2
        },
        2 : {
            "professor": "Suneeta Ramaswami",
            "dept": "Computer Science",
            "school": "School of Arts and Sciences",
            "rating": 4.0
        },
        3 : {
            "professor": "Kostas Bekris",
            "dept": "Computer Science",
            "school": "School of Arts and Sciences",
            "rating": 4.5
        },
        4 : {
            "professor": "Sesh Venugopal",
            "dept": "Computer Science",
            "school": "School of Arts and Sciences",
            "rating": 4.2
        },
    })
    reply.headers.add('Access-Control-Allow-Origin', '*')
    return reply
    

@app.route("/dashboard")
def find_all_data(netid="jm288", final=FINAL):
    if netid == "":
        return None
    if len(final[final['NetID'] == netid]) == 0 or len(final[final['NetID'] == netid]) == None:
        return None
    tmp_df = final[final['NetID'] == netid]
    netid = tmp_df['NetID'].values[0]
    name = tmp_df['Name'].values[0]
    major = tmp_df['Major'].values[0]
    year = tmp_df['Year'].values[0]
    gpa = tmp_df['GPA'].values[0]
    courses = {}
    for index, row in tmp_df.iterrows():
        course_id = row['Course ID']
        course_name = row['Course Title']
        grade = row['Grade']
        courses[course_id] = [course_name, grade]
        
    return {
        "NetID": netid,
        "Name": name,
        "Major": major,
        "Year": year,
        "GPA": gpa,
        "Courses": courses
    }

if __name__ == "__main__":
    app.run(debug=True)