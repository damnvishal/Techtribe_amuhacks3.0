import requests
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('D:\webscrapper\webscrapperdatasheet-0f49754baaff.json', scope)
client = gspread.authorize(credentials)


sheet = client.open('Job Listings').sheet1

url = 'https://www.naukri.com/jobs-in-bhopal'


response = requests.get(url)


soup = BeautifulSoup(response.content, 'html.parser')


job_listings = soup.find_all('div', class_='job-listing')


for job in job_listings:
    job_title = job.find('h2').text
    job_location = job.find('p', class_='location').text
    job_description = job.find('div', class_='description').text

    
    sheet.append_row([job_title, job_location, job_description])

print("Job listings extracted and stored in Google Sheets.")
