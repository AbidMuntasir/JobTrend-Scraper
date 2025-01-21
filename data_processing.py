import pandas as pd

def load_and_process_data():
   # Load data
    job_df = pd.read_csv("data/job_data.csv") 

    # Processing Top Companies
    most_jobs_cmp = job_df.groupby('Company Name')['Job Link'].count().sort_values(ascending=False).head(20)
    most_jobs_cmp = most_jobs_cmp.reset_index()
    most_jobs_cmp.columns = ['Company Name', 'Number of Jobs']

    # Processing Top Skills
    skills = job_df['Skills'].str.split(', ', expand=True).stack().value_counts().head(20)
    skills = skills.reset_index()
    skills.columns = ['Skill', 'Count']

    # Processing Job Hotspots
    hotspots = job_df['Location'].value_counts().head(20)
    hotspots = hotspots.reset_index()
    hotspots.columns = ['Location', 'Count']
    hotspots = hotspots[hotspots['Location'] != ""]

    # Processing Job Types
    top_roles = job_df['Job Type'].value_counts().head(20)
    top_roles = top_roles.reset_index()
    top_roles.columns = ['Job Type', 'Count']

    return most_jobs_cmp, skills, hotspots, top_roles
