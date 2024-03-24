import flask
from flask import (
    Flask,
    jsonify,
    request
)
import json
import random
import pandas as pd

from scrap import get_prof_json_by_course
from more.hackru import (
    generate_course_advice,
    generate_course_advice_generic,
    get_list_from_response
)

app = Flask(__name__)

FINAL = pd.read_csv("C:\\Users\\tanay\\OneDrive\\Desktop\\hackru\\hackru\\backend\\more\\final_student_course_records.csv")

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
            "class": "Cognitive Science: A   Multidisciplinary Introduction",
            "id": "01:185:201",
            "dept": "Cognitive Science",
            "school": "School of Arts and Sciences",
            "credits": 4
        },
    })
    reply.headers.add('Access-Control-Allow-Origin', '*')
    return reply
    
@app.route("/class-anon/major/<string:major>/gpa/<float:gpa>/year/<string:year>/interests/<string:interests>", methods=["OPTIONS", "GET"])
def get_class_rec_anon(major, gpa, year, interests, key=KEY):
    data = generate_course_advice_generic(major[:len(major) - 6], gpa, year, interests, openai_api_key=key)
    reply_df = get_list_from_response(data.choices[0].message.content)
    reply = {}
    
    if reply_df is not None:
        for index, row in reply_df.iterrows():
            # Updated the reply dictionary
            reply[index] = {
                "class": row['Course Title'],
                "id": row['Course ID'],
                "description": row['Course Description'],
                "school": "School of Arts and Sciences",
            }
            print(row['Course Title'])
            print(row['Course Description'])
            print(row['Course ID'])
        
        reply = jsonify(reply)
        reply.headers.add('Access-Control-Allow-Origin', '*')
        return reply    
    
    else:
        reply = jsonify({
            "error": "No courses found."
        })
        reply.headers.add('Access-Control-Allow-Origin', '*')
        return reply
            
    # except Exception as e:
    #     reply = jsonify({
    #         "error": "NetID not found.",
    #         "exception": e
    #     })
    #     reply.headers.add('Access-Control-Allow-Origin', '*')
    #     return reply
    
# @app.route("/class-anon/<string:id>")
# def get_class(id, key=KEY):
#     try:
#         mydict = {}
#         data = generate_course_advice_generic(mydict["major"], mydict["gpa"], mydict["year"], mydict["interests"], openai_api_key=key)
#         reply_df = get_list_from_response(data.choices[0].message.content)
        
#         for index, row in reply_df.iterrows():
#             # Updated the reply dictionary
#             reply[index] = {
#                 "class": row['Course Title'],
#                 "id": row['Course ID'],
#                 "description": row['Course Description'],
#                 "school": "School of Arts and Sciences",
#             }
#             print(row['Course Title'])
#             print(row['Course Description'])
#             print(row['Course ID'])
        
#         reply = jsonify(reply)
#         reply.headers.add('Access-Control-Allow-Origin', '*')
#         return reply    
        
#     except Exception as e:
#         reply = jsonify({
#             "error": "NetID not found.",
#             "exception": e
#         })
#         reply.headers.add('Access-Control-Allow-Origin', '*')
#         return reply
    
@app.route("/prof/<string:courseid>")
def professors(courseid):
    professors = dict()
    data = get_prof_json_by_course([courseid])
    
    reply = {}
    
    for index, row in enumerate(data):
        reply[index] = {
            "name": row["Professor"],
            "rating1": row["Scores"][0],
            "rating2": row["Scores"][1],
        }
    
    reply = jsonify(reply)
    reply.headers.add('Access-Control-Allow-Origin', '*')
    print(reply)
    return reply
    
@app.route("/class-netid/<string:id>")
def get_class(id, key=KEY):
    
    # try:
    reply = {}
    
    response_from_openai = generate_course_advice(id, openai_api_key=key) # Gets AI recommendation
    print(response_from_openai.choices[0].message.content)
    reply_df = get_list_from_response(response_from_openai.choices[0].message.content) # Converts into PD DF
    for index, row in reply_df.iterrows():
        # Updated the reply dictionary
        reply[index] = {
            "class": row['Course Title'],
            "id": row['Course ID'],
            "description": row['Course Description'],
            "school": "School of Arts and Sciences",
        }
        print(row['Course Title'])
        print(row['Course Description'])
        print(row['Course ID'])
    
    reply = jsonify(reply)
    reply.headers.add('Access-Control-Allow-Origin', '*')
    return reply

    # except Exception as e:
    #     reply = jsonify({
    #         "error": "NetID not found.",
    #         "exception": e
    #     })
    #     reply.headers.add('Access-Control-Allow-Origin', '*')
    #     return reply
    
@app.route("/proftrial")
def get_prof_trial():
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
    
@app.route("/prof/<string:id>")
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
            "rating": [4.2, 3.7]
        },
        2 : {
            "professor": "Suneeta Ramaswami",
            "dept": "Computer Science",
            "school": "School of Arts and Sciences",
            "rating": [4.0]
        },
    })
    reply.headers.add('Access-Control-Allow-Origin', '*')
    return reply


@app.route("/dashboard/<string:netid>")
def find_all_data(netid, final=FINAL):
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
        
    reply = jsonify({
        "NetID": netid,
        "Name": name,
        "Major": major,
        "Year": year,
        "GPA": gpa,
        "Courses": courses
    })
    reply.headers.add('Access-Control-Allow-Origin', '*')
    return reply

if __name__ == "__main__":
    app.run(debug=True)