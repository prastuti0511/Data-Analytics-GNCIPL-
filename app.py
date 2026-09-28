import streamlit as st

st.set_page_config(
    page_title="GNCIPL Data Analytics Internship",
    page_icon="📊",
    layout="wide"
)

GITHUB_BASE = "https://github.com/prastuti0511/Data-Analytics-GNCIPL-/blob/main/"

projects = {
    "Week 1": {
        "title": "Nutrition Analysis of McDonald’s Menu",
        "description": "Analysis of calories, protein, fat, carbohydrates, sugar and sodium across McDonald’s menu items.",
        "excel": "GNCIPL%20WEEK%201%20EXCEL%282%29.xlsx",
        "powerbi": "GNCIPL%20WEEK%201%20POWER%20BI%281%29.pbix"
    },
    "Week 2": {
        "title": "Software Bug Tracker Analysis",
        "description": "Analysis of software bugs based on severity, priority, type, status, resolution time and modules.",
        "excel": "GNCIPL%20WEEK%202%20EXCEL%281%29.xlsx",
        "powerbi": "GNCIPL%20WEEK%202%20POWER%20BI%281%29.pbix"
    },
    "Week 3": {
        "title": "Climate Change – Glacier Ice-Melt Analysis",
        "description": "Analysis of glacier ice cover, ice loss, melt rate, temperature and climate risk.",
        "excel": "GNCIPL%20WEEK%203%20EXCEL%281%29.xlsx",
        "powerbi": "GNCIPL%20WEEK%203%20POWER%20BI%281%29.pbix"
    },
    "Week 4": {
        "title": "Water Consumption Dashboard",
        "description": "Analysis of water consumption, rainfall, population, groundwater extraction and regional trends.",
        "excel": "GNCIPL%20WEEK%204%20EXCEL%281%29.xlsx",
        "powerbi": "GNCIPL%20WEEK%204%20POWER%20BI%281%29.pbix"
    },
    "Week 5": {
        "title": "AI-Enhanced Robotics Data Analytics",
        "description": "Analysis of robot productivity, AI detection accuracy, efficiency, downtime, maintenance, energy and cost savings.",
        "excel": "GNCIPL%20WEEK%205%20EXCEL%281%29.xlsx",
        "powerbi": "GNCIPL%20WEEK%205%20POWER%20BI%281%29.pbix"
    },
    "Week 6": {
        "title": "Employment Data Analysis and Skill Gap Identification",
        "description": "Analysis of employment trends, workforce distribution, employability, skill gaps and training requirements.",
        "excel": "GNCIPL%20WEEK%206%20EXCEL%281%29.xlsx",
        "powerbi": "GNCIPL%20WEEK%206%20POWER%20BI%281%29.pbix"
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

st.subheader("📗 Excel Dataset")

excel_url = GITHUB_BASE + project["excel"]

st.link_button(
    "⬇️ Open / Download Excel File",
    excel_url
)

st.subheader("📊 Power BI Dashboard")

powerbi_url = GITHUB_BASE + project["powerbi"]

st.link_button(
    "⬇️ Open / Download Power BI File",
    powerbi_url
)

st.divider()

st.header("📚 Six-Week Internship Projects")

for week, details in projects.items():
    st.markdown(f"**{week}:** {details['title']}")

st.divider()

st.success(
    "All six internship projects are available through the links above."
)

st.caption(
    "GNCIPL Data Analytics Internship | Excel & Power BI Portfolio"
)
