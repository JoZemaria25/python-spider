from bs4 import BeautifulSoup
import requests
import time

print('What do you not know')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill} ')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').text.replace(' ', '')
        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'Results/{index}.txt', 'w') as f :
                    f.write( f"Company Name: = {company_name.strip()}")
                    f.write(f"Required Skills: = {skills.strip()}")
                    f.write(f'more_info = {more_info}')
                print(f'file saved:{index}!')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting{time_wait} minutes...')
        time.sleep(time_wait * 60)