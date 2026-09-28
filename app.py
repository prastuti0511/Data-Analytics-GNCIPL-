import streamlit as st
import os

st.set_page_config(
    page_title="GNCIPL Data Analytics Internship",
    page_icon="📊",
    layout="wide"
)

projects = {
    "Week 1": {
        "title": "Nutrition Analysis of McDonald’s Menu",
        "description": "Analysis of calories, protein, fat, carbohydrates, sugar and sodium across McDonald’s menu items.",
        "excel": "GNCIPL WEEK 1 EXCEL(2).xlsx",
        "powerbi": "GNCIPL WEEK 1 POWER BI(1).pbix"
    },
    "Week 2": {
        "title": "Software Bug Tracker Analysis",
        "description": "Analysis of software bugs based on severity, priority, type, status, resolution time and modules.",
        "excel": "GNCIPL WEEK 2 EXCEL(1).xlsx",
        "powerbi": "GNCIPL WEEK 2 POWER BI(1).pbix"
    },
    "Week 3": {
        "title": "Climate Change – Glacier Ice-Melt Analysis",
        "description": "Analysis of glacier ice cover, ice loss, melt rate, temperature and climate risk.",
        "excel": "GNCIPL WEEK 3 EXCEL(1).xlsx",
        "powerbi": "GNCIPL WEEK 3 POWER BI(1).pbix"
    },
    "Week 4": {
        "title": "Water Consumption Dashboard",
        "description": "Analysis of water consumption, rainfall, population, groundwater extraction and regional trends.",
        "excel": "GNCIPL WEEK 4 EXCEL(1).xlsx",
        "powerbi": "GNCIPL WEEK 4 POWER BI(1).pbix"
    },
    "Week 5": {
        "title": "AI-Enhanced Robotics Data Analytics",
        "description": "Analysis of robot productivity, AI detection accuracy, efficiency, downtime, maintenance, energy and cost savings.",
        "excel": "GNCIPL WEEK 5 EXCEL(1).xlsx",
        "powerbi": "GNCIPL WEEK 5 POWER BI(1).pbix"
    },
    "Week 6": {
        "title": "Employment Data Analysis and Skill Gap Identification",
        "description": "Analysis of employment trends, workforce distribution, employability, skill gaps and training requirements.",
        "excel": "GNCIPL WEEK 6 EXCEL(1).xlsx",
        "powerbi": "GNCIPL WEEK 6 POWER BI(1).pbix"
    }
}

st.title("📊 GNCIPL Data Analytics Internship")
st.subheader("Six-Week Data Analytics Portfolio")

st.write(
    "This application presents the Excel datasets and Power BI dashboards "
    "developed during the six-week internship."
)

st.divider()

selected_week = st.sidebar.selectbox(
    "📁 Select Internship Week",
    list(projects.keys())
)

project = projects[selected_week]

st.header(f"{selected_week}: {project['title']}")
st.write(project["description"])

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📗 Excel Dataset")

    if os.path.exists(project["excel"]):
        with open(project["excel"], "rb") as file:
            st.download_button(
                label="⬇️ Download Excel File",
                data=file.read(),
                file_name=project["excel"],
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    else:
        st.error("Excel file not found.")

with col2:
    st.subheader("📊 Power BI Dashboard")

    if os.path.exists(project["powerbi"]):
        with open(project["powerbi"], "rb") as file:
            st.download_button(
                label="⬇️ Download Power BI File",
                data=file.read(),
                file_name=project["powerbi"],
                mime="application/octet-stream"
            )
    else:
        st.error("Power BI file not found.")

st.divider()

st.header("📚 Six-Week Internship Projects")

for week, details in projects.items():
    st.markdown(f"**{week}:** {details['title']}")

st.divider()

st.success(
    "All internship Excel datasets and Power BI dashboards are available for download."
)

st.caption(
    "GNCIPL Data Analytics Internship | Excel & Power BI Portfolio"
)
