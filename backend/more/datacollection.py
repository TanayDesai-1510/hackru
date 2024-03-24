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

megaurldict = {
    ("Africana Studies", "013"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20311.html",
    ("Africana Studies", "014"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20312.html",
    ("American Studies", "050"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20323.html",
    ("Anthropology", "070"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20328.html",
    ("Art History", "082"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20342.html",
    ("Asian Studies", "098"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20350.html",
    ("Astrophysics", "105"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20355.html",
    ("Agriculture and Environmental Science", "015"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg21138.html",
    ("Catalan", "145"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20357.html",
    ("Chinese", "165"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20365.html",
    ("Chinese", "165"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20370.html",
    ("Classical Humanities", "190"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20379.html",
    ("Classics in Ancient Greek", "490"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20381.html",
    ("Classic in Latin", "580"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20382.html",
    ("Criminal Justice", "202"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20403.html",
    ("Dance", "203"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20408.html",
    ("Dance", "206"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20409.html",
    ("East Asia Language and Area Studies", "214"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20414.html",
    ("Education", "300"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20424.html",
    ("English", "350"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20432.html",
    ("English", "353"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20433.html",
    ("English", "354"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20434.html",
    ("English", "355"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20435.html",
    ("European Studies", "360"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20445.html",
    ("Excerise Science and Sport Studies", "377"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20450.html",
    ("French", "420"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20463.html",
    ("French", "420"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20464.html",
    ("Geography", "450"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20472.html",
    ("Geological Sciences", "460"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20473.html",
    ("German", "470"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20488.html",
    ("German", "470"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20489.html",
    ("Modern Greek Studies", "489"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg22963.html",
    ("Modern Greek Studies", "489"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg22960.html",
    ("Marine Sciences", "628"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg21153.html",
    ("Meterology", "670"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg21154.html",
    ("Microbiology", "680"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg21155.html",
    ("Hindi", "505"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20494.html", 
    ("Cognitive Science", "185"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20385.html",
    ("Computer Science", "198"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20398.html",
    ("Economics", "220"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg22953.html",
    ("History", "506"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20500.html",
    ("History", "508"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20501.html",
    ("History", "510"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20502.html",
    ("History", "512"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20503.html",
    ("Hungarian", "535"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20515.html",
    ("Hungarian", "535"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20516.html",
    ("Italian", "560"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20522.html",
    ("Italian", "560"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20523.html",
    ("Japanese", "565"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20537.html",
    ("Japanese", "565"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20538.html",
    ("Mathematics", "640"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20606.html",
    ("Medical Technology", "660"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20609.html",
    ("Labor Studies", "575" ): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20557.html",
    ("Latin American Studies", "590"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20562.html",
    ("Statistics", "960"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20744.html",
    ("Sociology", "960"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20725.html",
    ("Religion", "840"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20700.html",
    ("Philosophy", "790"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20657.html",
    ("Political Science", "790"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20674.html",
    ("Women's and Gender Studies", "988"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20763.html",
    ("Cinema Studies", "175"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20373.html",
    ("Finance", "390"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg21334.html",
    ("Marketing", "630"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg21337.html",
    ("Accounting", "010"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg21331.html",
    ("Management", "620"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg21335.html",
    ("Management Science and Information Systems", "623"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg21336.html",
    ("Information Technology and Informatics", "189"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg21378.html",
    ("Journalism and Media Studies", "567"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg21379.html",
    ("Communication", "192"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg21377.html",
    ("Planning and Public Policy", "762"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg21513.html",
    ("Public Health", "832"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg21514.html",
}

miniurldict = {
    ("Computer Science", "198"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20398.html",
    ("Mathematics", "640"): "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20606.html"
}

def normalize_course_id(df):
    # First, remove quotations from the course_id
    df['Course ID'] = df['Course ID'].str.replace('"', '')

    # Initialize an empty list to hold the new or duplicated rows
    new_rows = []

    # Iterate over the DataFrame rows
    for index, row in df.iterrows():
        course_id = row['Course ID']
        
        try:
            # Check for hyphen or comma in course_id and split accordingly
            if '-' in course_id or ',' in course_id:
                # Split the course_id by hyphen or comma
                parts = course_id.replace('-', ',').split(',')
                                
                # Create a new row for each part
                new_row = row.copy()
                new_row['Course ID'] = f"{course_id[:7]}{parts[1]}"  # Assuming the format is XX:XXX:XXX
                new_rows.append(new_row)
                    
                row['Course ID'] = parts[0]  # Update the course_id in the row
                new_rows.append(row)

            else:
                new_rows.append(row)
                
        except Exception as e:
            print(f"Error processing row {index}: {e}")

    # Create a new DataFrame from the new rows list
    new_df = pd.DataFrame(new_rows).reset_index(drop=True)

    return new_df


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
mini_df = create_mega_dataframe(miniurldict)
mini_df = normalize_course_id(mini_df)
save_to_csv(mini_df, "backend/more/mini_courses.csv")

mega_df = create_mega_dataframe(megaurldict)
mega_df = normalize_course_id(mega_df)
print(mega_df[mega_df['Course ID'].apply(lambda x: len(str(x)) > 10)])
print(len(mega_df[mega_df['Course ID'].apply(lambda x: len(str(x)) > 10)]))

save_to_csv(mega_df, "backend/more/mega_courses.csv")


if __name__ == "__main__":
    # url = "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20763.html"
    # df = extract_course_data(url)
    # save_to_csv(df, "backend/more/Women's and Gender Studies 988 Courses.csv")
    
    # url2 = "https://catalogs.rutgers.edu/generated/nb-ug_0507/pg20398.html"
    # df2 = extract_course_data(url2)
    # save_to_csv(df2, "backend/more/Computer Science 198 Courses.csv")
    
    pass
