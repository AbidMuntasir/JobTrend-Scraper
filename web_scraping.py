import requests as req
from bs4 import BeautifulSoup
import pandas as pd

def scrape_jobs():
    industry_url = 'https://www.timesjobs.com/candidate/job-search.html'
    html = req.get(industry_url).text
    soup = BeautifulSoup(html, 'html.parser')
    industries = soup.find('ul', class_='browse-ind').find_all('a')

    urls = []
    for url in industries:
        html = req.get(f'https://www.timesjobs.com{url["href"]}&sequence=1&postWeek=7').text
        soup = BeautifulSoup(html, 'html.parser')
        pagination = soup.find('div', class_='srp-pagination clearfix')
        if pagination:
            page_numbers = pagination.find_all('em')
            if len(page_numbers) >= 2:
                max_page = int(page_numbers[-2].text)
            else:
                max_page = 1
        else:
            max_page = 1
        for pages in range(1, max_page + 1):
            urls.append(f'https://www.timesjobs.com{url["href"]}&sequence={pages}&postWeek=7'.replace(" ", "+"))

    # Collect job data
    job_df = {'Company Name': [], 'Skills': [], 'Posted Date': [], 'Location': [], 'Job Type': [], 'Job Link': []}
    for url in urls:
        html = req.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
        for job in jobs:
            posted_date = job.find('span', class_='sim-posted').text
            company_name = job.find('h3', class_='joblist-comp-name').text.strip()
            location = job.find('li', class_='srp-zindex location-tru').text.strip()
            skills_html = job.find_all('div', class_='more-skills-sections')
            skills = [skill.text.strip() for skill in skills_html[0].find_all('span')] if skills_html else []
            job_type = job.find('h2', class_='heading-trun').text.strip()
            job_link = job.a['href']
            job_df['Job Link'].append(job_link)
            job_df['Job Type'].append(job_type)
            job_df['Location'].append(location)
            job_df['Posted Date'].append(posted_date.strip())
            job_df['Company Name'].append(company_name)
            job_df['Skills'].append(', '.join(skills))

    # Save to CSV
    df = pd.DataFrame(job_df)
    job_df = df[df.duplicated(subset=['Job Link'],keep='first') == False]
    job_df.to_csv('data/job_data.csv', index=False)
    df.to_csv('data/raw_data.csv', index=False)
    print("Scraping completed and data saved to 'data/raw_data.csv'.")
    print("Duplicate job entries removed and data saved to 'data/job_data.csv'.")
    

if __name__ == "__main__":
    scrape_jobs()
