import streamlit as st
from visualizations import create_figures  # Import the figure generation function

# Create figures by calling the function
fig1, fig2, fig3, fig4 = create_figures()

# Streamlit Dashboard
st.title("Job Analysis Dashboard")

# Section 1: Top Companies
st.header("1. Top 20 Companies with Most Jobs")
st.plotly_chart(fig1)

# Section 2: Skills
st.header("2. Top 20 Skills Required")
st.plotly_chart(fig2)

# Section 3: Job Hotspots
st.header("3. Top 20 Job Hotspots")
st.plotly_chart(fig3)

# Section 4: Job Roles
st.header("4. Top 20 Job Roles")
st.plotly_chart(fig4)
# Key Insights
st.markdown("### Key Insights")
st.write("""
- **Top Locations:** Bangalore and Mumbai lead with the highest number of job postings.
- **Top Skills:** Security, Communication Skills, and Production are in high demand.
- **Top Companies:** Accenture and Walmart India are the biggest recruiters.
- **Top Job Roles:** Warehouse Logistics, Project Manager and  HR Manager are the most sought after roles.
""")

