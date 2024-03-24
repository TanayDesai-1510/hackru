import flask
from flask import (
    Flask,
    jsonify,
    request
)
import json
import random
import pandas as pd

app = Flask(__name__)

@app.route("/classtrial")
def hello():
    return jsonify({
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
            "class": "Cognitive Science: A   Multidisciplinary Introduction",
            "id": "01:185:201",
            "dept": "Cognitive Science",
            "school": "School of Arts and Sciences",
            "credits": 4
        },
    })
    
@app.route("/classtrial/<int:id>")
def get_class(id):
    return jsonify({
        "class": "Introduction to Computer Science",
        "id": "01:198:111",
        "dept": "Computer Science",
        "school": "School of Arts and Sciences",
        "credits": 4
    })
    
@app.route("/proftrial")
def get_prof():
    return jsonify({
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
    
FINAL = pd.read_csv("backend/more/final_student_course_records.csv")

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