# Created By Alliance82
# Created On 1/13/2024
# This project is an introudction to Webscraping using requests and BeautifulSoup
# Follows the project from Real Python at https://realpython.com/beautiful-soup-web-scraper-python/
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import sys
import os

# Full URL
URL = "https://realpython.github.io/fake-jobs/" 

# Calls the URL and returns the full webpage code
page = requests.get(URL) 
print(page.text)

# Converts the webpage into a beautifulsoup object
soup = BeautifulSoup(page.content, "html.parser")

# Finds the id that has the job elements within it and cleans it up
results = soup.find(id="ResultsContainer")
print(results.prettify())
job_elements = results.find_all("div", class_="card-content")

# Finds the heading within the div that has the information that we are interested in that are specifically python jobs
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

# Pulls the great grandparent element and makes a list of those job elements that had python in the job name
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

# Loops through each element to capture the job information and link to apply
for job_element in python_job_elements:
    # Sets the Job Title, Hiring Company, and Job Location to the corresponding html headers/paragraphs
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    
    # Prints the Job Title, Hiring Company, and Job Location
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    
    # Looks specifically for the Apply link anchor, as there were two (Learn and Apply)
    links = job_element.find_all("a", text="Apply")
    for link in links:
        link_url = link['href']
        print(f"Apply here: {link_url}")
    print()