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
    
import pandas as pd

# Assuming the extract_course_data function is already defined

list_of_urls = {
    ("Africana Studies", "013"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20311.html",
    ("Africana Studies", "014"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20312.html",
    ("American Studies", "050"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20323.html",
    ("Anthropology", "070"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20328.html",
    ("Art History", "082"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20342.html",
    ("Asian Studies", "098"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20350.html",
    ("Astrophysics", "105"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20355.html",
    ("Catalan", "145"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20357.html",
    ("Cognitive Science", "185"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20385.html",
    ("Computer Science", "198"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20398.html",
    ("Economics", "220"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg22953.html",
    ("History", "506"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20500.html",
    ("Mathematics", "640"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20606.html",
    ("Statistics", "960"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20744.html",
    ("Women's and Gender Studies", "988"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20763.html",
    ("Cinema Studies", "175"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20373.html",
}

def create_mega_dataframe(url_dict):
    mega_df = pd.DataFrame()

    for (department, department_id), url in url_dict.items():
        df = extract_course_data(url)
        df['Department'] = department
        df['Department ID'] = department_id
        mega_df = pd.concat([mega_df, df], ignore_index=True)

    mega_df.reset_index(inplace=True)
    mega_df.rename(columns={'index': 'ID'}, inplace=True)

    return mega_df

# Now call the function to create the mega dataframe
mega_df = create_mega_dataframe(list_of_urls)
save_to_csv(mega_df, "backend/mega_courses.csv")


if __name__ == "__main__":
    url = "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20763.html"
    df = extract_course_data(url)
    save_to_csv(df, "backend/Women's and Gender Studies 988 Courses.csv")
    
    url2 = "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20398.html"
    df2 = extract_course_data(url2)
    save_to_csv(df2, "backend/Computer Science 198 Courses.csv")