from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv
import os
import time

def scrape_to_csv(html):
    soup = BeautifulSoup(html, 'html.parser')

    if "No results found." in soup.get_text():
        return None

    data = []

    # Iterate through each course info section in the HTML
    course_info_blocks = soup.find_all('div', class_='courseInfo')
    for course_info in course_info_blocks:
        prof = course_info.find('strong').text.strip()
        details_text = course_info.get_text(" ", strip=True)
        
        # Adjust splitting logic based on the actual format of details_text
        time_taken = ' '.join(details_text.split()[1:3])
        index = details_text.split('index #')[1].split()[0]
        enrollment = details_text.split('Enrollment=')[1].split(',')[0].strip()

        # Extract questions and section scores
        table = course_info.find_next('tbody')
        if table:
            questions = table.find_all('td', class_='qText')
            sections = table.find_all('td', class_='mono stats mQuestion section')
            scores = []

            for question, section in zip(questions[-2:], sections[-2:]):
                question_text = question.text.strip()
                section_score = section.text.strip()
                scores.append(section_score)
            
        professor_info = {
            'Professor': prof,
            'Time': time_taken,
            'Index': index,
            'Enrollment': enrollment,
            'Scores': scores
        }
        
        data.append(professor_info)

    # Convert to pandas DataFrame
    return data

def get_prof_json_by_course(courses):
    # Initialize Selenium WebDriver
    driver = webdriver.Edge()

    url = "https://sirs.rutgers.edu/index.php"

    # Navigate to the website
    driver.get(url)
    wait = WebDriverWait(driver, 20)

    # Log in
    username = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password = driver.find_element(By.ID, "password")

    # Loading th dot_env to securely log in to CAS
    load_dotenv()

    username.send_keys(os.getenv('RUTGERS_USERNAME'))
    password.send_keys(os.getenv('RUTGERS_PASSWORD'))
    password.send_keys(Keys.RETURN)

    # Wait for and handle additional steps, e.g., two-factor authentication
    wait.until(EC.element_to_be_clickable((By.ID, "trust-browser-button"))).click()

    # Select school and department
    time.sleep(8)


    professors = []
    
    for course in courses:
        split_course = course.split(":")
        
        time.sleep(2)
        school = Select(driver.find_element(By.ID, "school"))
        school.select_by_value(split_course[0])

        time.sleep(1)
        dept = Select(driver.find_element(By.ID, "dept"))
        dept.select_by_value(split_course[1])

        # Enter course and search
        course = driver.find_element(By.NAME, "survey[course]")
        course.send_keys(split_course[2])
        driver.find_element(By.XPATH, "//button[contains(text(), 'Search by subject code')]").click()
        
        
        html = driver.page_source

        df = scrape_to_csv(html)
        professors.append(df)
        driver.get(url)
    
    driver.quit()
    
    return professors[0]
                  

if __name__ == "__main__": 

    courses= ["01:198:111", "01:198:112", "01:198:205"]

    profs = get_prof_json_by_course(courses)
    
    print(profs)