import streamlit as st
import pandas as pd
import os

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="GNCIPL Data Analytics Internship",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# PROJECT INFORMATION
# --------------------------------------------------

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

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("📊 GNCIPL Data Analytics Internship")

st.subheader("Six-Week Data Analytics Portfolio")

st.write(
    "This application presents the Excel datasets and Power BI dashboards "
    "developed during the six-week internship."
)

st.divider()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("📁 Internship Projects")

selected_week = st.sidebar.selectbox(
    "Select a Week",
    list(projects.keys())
)

project = projects[selected_week]

# --------------------------------------------------
# PROJECT INFORMATION
# --------------------------------------------------

st.header(f"{selected_week}: {project['title']}")

st.write(project["description"])

st.divider()

# --------------------------------------------------
# FILE PATHS
# --------------------------------------------------

excel_path = project["excel"]
powerbi_path = project["powerbi"]

# --------------------------------------------------
# DOWNLOAD SECTION
# --------------------------------------------------

col1, col2 = st.columns(2)

# --------------------------------------------------
# EXCEL DOWNLOAD
# --------------------------------------------------

with col1:

    st.subheader("📗 Excel Dataset")

    if os.path.exists(excel_path):

        with open(excel_path, "rb") as file:

            st.download_button(
                label="⬇️ Download Excel File",
                data=file,
                file_name=excel_path,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                width="stretch"
            )

    else:

        st.error(
            f"Excel file not found: {excel_path}"
        )

# --------------------------------------------------
# POWER BI DOWNLOAD
# --------------------------------------------------

with col2:

    st.subheader("📊 Power BI Dashboard")

    if os.path.exists(powerbi_path):

        with open(powerbi_path, "rb") as file:

            st.download_button(
                label="⬇️ Download Power BI File",
                data=file,
                file_name=powerbi_path,
                mime="application/octet-stream",
                width="stretch"
            )

    else:

        st.error(
            f"Power BI file not found: {powerbi_path}"
        )

# --------------------------------------------------
# EXCEL PREVIEW
# --------------------------------------------------

st.divider()

st.header("📋 Excel Data Preview")

if os.path.exists(excel_path):

    try:

        # Read Excel workbook
        excel_file = pd.ExcelFile(excel_path)

        # Get worksheet names
        sheet_names = excel_file.sheet_names

        # Worksheet selector
        selected_sheet = st.selectbox(
            "Select Worksheet",
            sheet_names
        )

        # Read selected worksheet
        df = pd.read_excel(
            excel_path,
            sheet_name=selected_sheet
        )

        # Display row and column counts
        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Number of Rows",
                df.shape[0]
            )

        with col2:

            st.metric(
                "Number of Columns",
                df.shape[1]
            )

        # --------------------------------------------------
        # FIX FOR STREAMLIT / PYARROW MIXED DATA TYPES
        # --------------------------------------------------

        display_df = df.copy()

        for column in display_df.columns:

            display_df[column] = display_df[column].astype(str)

        # Display dataframe
        st.dataframe(
            display_df,
            width="stretch"
        )

    except Exception as e:

        st.warning(
            f"Excel preview could not be displayed: {e}"
        )

else:

    st.info(
        "The Excel file is not available for preview."
    )

# --------------------------------------------------
# INTERNSHIP PROJECT SUMMARY
# --------------------------------------------------

st.divider()

st.header("📚 Six-Week Internship Projects")

summary = {
    "Week 1": "Nutrition Analysis of McDonald’s Menu",
    "Week 2": "Software Bug Tracker Analysis",
    "Week 3": "Climate Change – Glacier Ice-Melt Analysis",
    "Week 4": "Water Consumption Dashboard",
    "Week 5": "AI-Enhanced Robotics Data Analytics",
    "Week 6": "Employment Data Analysis and Skill Gap Identification"
}

for week, title in summary.items():

    st.markdown(
        f"**{week}:** {title}"
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "GNCIPL Data Analytics Internship | Excel & Power BI Portfolio"
)
