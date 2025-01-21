import plotly.express as px
from data_processing import load_and_process_data

# Load processed data
most_jobs_cmp, skills, hotspots, top_roles = load_and_process_data()

# Generate Plotly figures
def create_figures():
    fig1 = px.bar(
        most_jobs_cmp,
        x='Number of Jobs',
        y='Company Name',
        orientation='h',
        color='Number of Jobs',
        title='Top 20 Companies with Most Jobs',
        text='Number of Jobs'
    )
    fig1.update_layout(
        xaxis_title='Number of Jobs',
        yaxis_title='Company Name',
        yaxis=dict(categoryorder='total ascending'),
        height=600
    )

    fig2 = px.bar(
        skills,
        x='Count',
        y='Skill',
        orientation='h',
        color='Count',
        title='Top 20 Skills Required',
        text='Count'
    )
    fig2.update_layout(
        xaxis_title='Count',
        yaxis_title='Skill',
        yaxis=dict(categoryorder='total ascending'),
        height=600
    )

    fig3 = px.bar(
        hotspots,
        x='Count',
        y='Location',
        orientation='h',
        color='Count',
        title='Top 20 Job Hotspots',
        text='Count'
    )
    fig3.update_layout(
        xaxis_title='Count',
        yaxis_title='Location',
        yaxis=dict(categoryorder='total ascending'),
        height=600
    )

    fig4 = px.bar(
        top_roles,
        x='Count',
        y='Job Type',
        orientation='h',
        color='Count',
        title='Top 20 Job Roles',
        text='Count'
    )
    fig4.update_layout(
        xaxis_title='Count',
        yaxis_title='Job Type',
        yaxis=dict(categoryorder='total ascending'),
        height=600
    )

    return fig1, fig2, fig3, fig4
