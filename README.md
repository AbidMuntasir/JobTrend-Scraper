
# **JobTrend Scraper**

## **Overview**

JobTrend Scraper is a Python-based project that scrapes job postings from TimesJobs, a leading career platform, to gather insights into the job market. The project focuses on extracting key details from job listings, such as companies, roles, locations, and required skills. The data is then analyzed and visualized using interactive plots and static charts to help job seekers, recruiters, and businesses understand current trends in job markets, roles, and skills demand.

## **Project Features**

- **Web Scraping:**  
  The core of this project is web scraping, which collects job-related data from TimesJobs. This includes extracting details like company names, job titles, locations, required skills, job types, and posting dates.
  
- **Data Analysis:**  
  The scraped data is cleaned, processed, and analyzed to gain insights into job trends. Key areas of analysis include the most popular companies, top job roles, in-demand skills, and job hotspots.

- **Data Visualization:**  
  Interactive and static visualizations are provided to better interpret the analysis. These visualizations help in identifying the most frequent job roles, companies with the highest number of openings, and the most common job locations.

## **Project Structure**
```
/Sales-Data-Analysis
├── Data/
│   ├── raw_data.csv        # Original data
│   ├── job_data.csv 
├── data_processing.py
├── visualizations.py
├── web_scraping.py
├── job_analysis_dashboard.py
├──job_analysis_static.ipynb
├── README.md                     # Project documentation
├── requirements.txt              # Dependencies
```


## **Technologies Used**

- **Python**
- **Pandas** for data manipulation and analysis
- **Matplotlib** and **Seaborn** for static data visualization
- **Plotly** for interactive visualizations
- **Streamlit** for deploying an interactive dashboard

## **Features of the Dashboard**

- **Top Companies:**  
  Displays the top 20 companies with the highest number of job postings.

- **Skills Insights:**  
  Visualizes the top 20 skills in demand based on job postings.

- **Job Locations:**  
  Highlights the top 20 locations where the most job opportunities are available.

- **Job Roles:**  
  Shows the top 20 job roles by frequency across the scraped data.

## **Getting Started**

### **Prerequisites**
To get started with this project, you'll need to have Python installed, along with the following libraries:

- **streamlit**
- **pandas**
- **matplotlib**
- **seaborn**
- **plotly**
- **beautifulsoup4**
- **requests**

You can install the necessary dependencies using the following command:

```bash
pip install streamlit pandas matplotlib seaborn plotly beautifulsoup4 requests
```
### Steps to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/AbidMuntasir/JobTrend-Scraper.git
   cd JobTrend-Scraper
   ```
### **Running the Project**

1. **Scraping Data:**  
   The first step in this project is scraping job data from TimesJobs using `BeautifulSoup` and `requests`. This step runs automatically when you run the script.

2. **Interactive Dashboard:**  
   The interactive dashboard is built using Streamlit and Plotly. To run the dashboard locally, navigate to the project directory in your terminal and use the following command:

   ```bash
   streamlit run job_analysis_dashboard.py
   ```

   This will open a local server where you can interact with the dashboard.

3. **Static Visualizations:**  
   You can also view the static visualizations (e.g., bar charts) directly in Jupyter notebooks or Python scripts.

## **Live Streamlit Dashboard**

To interact with the live version of the Streamlit dashboard, visit the link below:

[JobTrend Scraper Dashboard](<https://jobtrend-scraper-dashboard.streamlit.app/>)

## **How to Use the Dashboard**

Once the dashboard is up and running, you can explore the following:

- **View the Top 20 Companies** with the highest number of job postings.
- **Explore the Most In-Demand Skills** by looking at the top 20 skills required for jobs.
- **Discover the Most Popular Job Locations** across the country.
- **Analyze the Most Frequent Job Roles** available in the job market.

## **Sample Visuals**

Here are some of the interactive visualizations included in the dashboard:

- **Top 20 Companies with Most Job Postings**
- **Top 20 In-Demand Skills**
- **Top 20 Job Hotspots (Locations)**
- **Top 20 Job Roles**

## **Conclusion**

This project provides valuable insights into the current job market by scraping and analyzing data from TimesJobs. The interactive dashboard helps users explore trends in job openings, locations, skills, and roles. By integrating data analysis with interactive visualizations, this project makes it easier for businesses and job seekers to make informed decisions.


## **License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

## **Contact**
For inquiries or collaboration:
- **Email**: abidmuntasir.am@gmail.com
- **GitHub**: [AbidMuntasir](https://github.com/AbidMuntasir)


---

