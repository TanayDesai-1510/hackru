import pandas as pd

FINAL = pd.read_csv("backend/more/final_student_course_records.csv")

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
        
    return {
        "NetID": netid,
        "Name": name,
        "Major": major,
        "Year": year,
        "GPA": gpa,
        "Courses": courses
    }

if __name__ == "__main__":
    print(FINAL.head())
    print(find_all_data("dt358"))