import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_course_data(url):
    # Fetch the HTML content
    response = requests.get(url)
    html_content = response.text

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract course data
    courses = []
    for container in soup.find_all("div", class_="item-container"):
        course_id_element = container.find("span", class_="course-annotation")
        course_id = course_id_element.text.strip() if course_id_element else None
        
        course_title_element = container.find("span", class_="course-title")
        course_title = course_title_element.text.strip() if course_title_element else None
        
        course_desc_element = container.find("span", class_="course-desc")
        course_desc = course_desc_element.text.strip() if course_desc_element else None
        
        # Course prerequisites are optional
        course_prereq_element = container.find("span", class_="course-prereq")
        course_prereq = course_prereq_element.text.strip() if course_prereq_element else None

        courses.append({
            "Course ID": course_id,
            "Course Title": course_title,
            "Course Description": course_desc,
            "Course Prerequisites": course_prereq
        })

    return pd.DataFrame(courses)

def save_to_csv(df, filename):
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    url = "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20763.html"
    df = extract_course_data(url)
    save_to_csv(df, "backend/Women's and Gender Studies 988 Courses.csv")
    
    url2 = "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20398.html"
    df2 = extract_course_data(url2)
    save_to_csv(df2, "backend/Computer Science 198 Courses.csv")