import pandas as pd
import openai

# Load the student records and courses data
STUDENT_RECORDS = pd.read_csv("C:\\Users\\tanay\\OneDrive\\Desktop\\hackru\\hackru\\backend\\more\\final_student_course_records.csv")
ALL_COURSES = pd.read_csv("C:\\Users\\tanay\\OneDrive\\Desktop\\hackru\\hackru\\backend\\more\\mega_courses.csv")

def generate_course_advice(netID, openai_api_key, student_records=STUDENT_RECORDS, all_courses=ALL_COURSES):    
    # Filter records for the specified student
    student_data = student_records[student_records['NetID'] == netID]
    
    # Check if student data is empty
    if student_data.empty:
        return "No records found for this netID."
    
    # Store student's major, GPA, and year
    student_major = student_data['Major'].iloc[0]  # Assuming major, GPA, year are same in all records for a student
    student_gpa = student_data['GPA'].iloc[0]
    student_year = student_data['Year'].iloc[0]
    
    # Get the list of courses the student has taken
    courses_taken = pd.merge(
        student_data,
        all_courses,
        on='Course ID',
        how='left'
    ).drop_duplicates(subset=['Course ID'])
    
    # Fetch all courses offered for the student's major
    offered_courses = all_courses[all_courses['Department'] == student_major]
    
    # Identify courses not yet taken by the student
    remaining_courses = offered_courses[~offered_courses['Course ID'].isin(courses_taken['Course ID'])]

    if student_year == 'Freshman':
        remaining_courses = remaining_courses[remaining_courses['Course ID'].str[7].astype(int) <= 2]
    elif student_year == 'Sophomore':
        remaining_courses = remaining_courses[remaining_courses['Course ID'].str[7].astype(int) <= 3]
    elif student_year == 'Junior':
        remaining_courses = remaining_courses[remaining_courses['Course ID'].str[7].astype(int) <= 4]
    else:  # senior
        remaining_courses = remaining_courses[remaining_courses['Course ID'].str[7].astype(int) > 4]
    
    # Returning a summary dictionary for simplicity
    student_info = {
        'netID': netID,
        'major': student_major,
        'gpa': student_gpa,
        'year': student_year,
        'courses_taken': courses_taken[['Course ID', 'Course Title_x', 'Course Description']].to_dict('records'),
        'remaining_courses': remaining_courses[['Course ID', 'Course Title', 'Course Description']].to_dict('records')
    }

    print(student_info)

    openai.api_key = openai_api_key

    # Construct the prompt with student's data
    prompt = (f'''
        Student ID: {netID}
        Major: {student_info['major']}
        GPA: {student_info['gpa']}
        Year: {student_info['year']}
        Courses Taken: {student_info['courses_taken']}
        Remaining Courses: {student_info['remaining_courses']}
        Based on the above information, recommend five new courses (from the remaining courses) the student should take next, considering their major, academic performance, and interests as implied by past courses.
        This is my conditions:
            1. The student's GPA should be considered when recommending courses. If the student has a high GPA, recommend more challenging courses. If the student has a low GPA, recommend easier courses.
            2. The student's year should be considered when recommending courses. Underclassmen should take easier courses, while upperclassmen should take more challenging courses.
            3. The student's interests should be considered when recommending courses. If the student has taken a lot of courses in a particular area, recommend more courses in that area.
            4. THE COURSES MUST BE FROM THE REMAINING COURSES LISTED ABOVE.
            5. Return only the course IDs, and nothing else. NO DESCRIPTIONS. NO EXPLANATIONS. NO BULLETPOINTS.
        Number four and five is the most important and must always be followed.
        The five new courses should be in a format like this:
        XX:XX:XXX, from the remaining courses
        '''
    )
    
    print(prompt)

    # Call the OpenAI API with the 
    client = openai.OpenAI(
    # This is the default and can be omitted
    api_key=openai_api_key,
    )
    
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
            model="gpt-3.5-turbo",
        )
  
    return chat_completion

def generate_course_advice_generic(student_major, student_gpa, student_year, student_interests, openai_api_key, all_courses=ALL_COURSES):    
    
    # Split the title by the plus, capitalize each word, and join them back with a space
    student_major = " ".join([word.capitalize() for word in student_major.split("+")])
    student_interests = " ".join([word.capitalize() for word in student_major.split("+")])
    student_year = student_year.capitalize()
    
    # Fetch all courses offered for the student's major
    offered_courses = all_courses[all_courses['Department'] == student_major]

    if student_year == 'Freshman':
        remaining_courses = offered_courses[offered_courses['Course ID'].str[7].astype(int) <= 2]
    elif student_year == 'Sophomore':
        remaining_courses = offered_courses[offered_courses['Course ID'].str[7].astype(int) <= 3]
    elif student_year == 'Junior':
        remaining_courses = offered_courses[offered_courses['Course ID'].str[7].astype(int) <= 4]
    else:  # senior
        remaining_courses = offered_courses[offered_courses['Course ID'].str[7].astype(int) > 4]
    
    # Returning a summary dictionary for simplicity
    student_info = {
        'major': student_major,
        'gpa': student_gpa,
        'year': student_year,
        'interests': student_interests,
        'remaining_courses': remaining_courses[['Course ID', 'Course Title', 'Course Description']].to_dict('records')
    }

    print(student_info)

    openai.api_key = openai_api_key

    # Construct the prompt with student's data
    prompt = (f'''
        Major: {student_info['major']}
        GPA: {student_info['gpa']}
        Year: {student_info['year']}
        Interests: {student_info['interests']}
        Remaining Courses: {student_info['remaining_courses']}
        Based on the above information, recommend five courses (from the remaining courses) the student should take next, considering their major, academic performance, and interests.
        This is my conditions:
            1. The student's GPA should be considered when recommending courses. If the student has a high GPA, recommend more challenging courses. If the student has a low GPA, recommend easier courses.
            2. The student's year should be considered when recommending courses. Underclassmen should take easier courses, while upperclassmen should take more challenging courses.
            3. The student's interests should be considered when recommending courses. 
            4. THE COURSES MUST BE FROM THE REMAINING COURSES LISTED ABOVE.
            5. Return only the course IDs, and nothing else. NO DESCRIPTIONS. NO EXPLANATIONS. NO BULLETPOINTS.
        Number four and five are the most important and must always be followed.
        The five new courses should be in a format like this:
        XX:XX:XXX, from the remaining courses
        '''
    )
    
    print(prompt)

    # Call the OpenAI API with the 
    client = openai.OpenAI(
    # This is the default and can be omitted
    api_key=openai_api_key,
    )
    
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
            model="gpt-3.5-turbo",
        )
  
    return chat_completion

def get_course_from_id(id, all_courses=ALL_COURSES):
    course = all_courses[all_courses['Course ID'] == id]
    try:
        print(course['Course Title'].values[0])
        return course[['Course ID', 'Course Title', 'Course Description']].head(1)
    except Exception as e:
        print(f"Course with ID {id} not found because exception {e}.")
        return None

def get_list_from_response(stringbhai):
    # Removes comma  from the string
    stringbhai = stringbhai.replace(",", "")
    # Remove \n from the string
    stringbhai = stringbhai.replace("\n", " ")
    # Splits the string by space
    stringbhai = stringbhai.split(" ")
    # For each part in the string, gets course title and prints it
    tmpdf = []
    for part in stringbhai:
        # Try, if the part has a course id format, like 10 len and 2 colons, it will check for a course, and if it returns a row, then we will add it to temp df
        try:
            if len(part) == 10 and part.count(":") == 2:
                print(part)
                tmp = get_course_from_id(part)
                if tmp is not None and not tmp.empty:
                    tmpdf.append(tmp)
        except Exception as e:
            print(f"Exception {e}")
            
    if len(tmpdf) == 0:
        print("No courses found.")
        return None
    else:
        tmpdf_f = pd.concat(tmpdf, ignore_index=True)
        return tmpdf_f
        
    
# Example usage
if __name__ == "__main__":
    netID = 'dj549'
    result = generate_course_advice(netID, openai_api_key)
    print(result)
    print(result.choices[0].message.content)
    print(type(result.choices[0].message.content))
    print(get_list_from_response(result.choices[0].message.content))
    
    major = "Mathematics"
    gpa = 3.8
    year = "Freshman"
    interests = "calculus, cryptography"
    result = generate_course_advice_generic(major, gpa, year, interests, openai_api_key)
    print(result)
    print(result.choices[0].message.content)
    print(type(result.choices[0].message.content))
    print(get_list_from_response(result.choices[0].message.content))