
import streamlit as st
from pathlib import Path
import pandas as pd

st.set_page_config(
    page_title="GNCIPL | Six-Week Data Analytics Internship",
    page_icon="📊",
    layout="wide"
)

BASE = Path(__file__).parent / "data"

PROJECTS = {
    1: {
        "title": "Nutrition Analysis of McDonald’s Menu",
        "excel": "GNCIPL WEEK 1 EXCEL(2).xlsx",
        "powerbi": "GNCIPL WEEK 1 POWER BI(1).pbix",
        "description": "Analysis of calories, protein, fat, carbohydrates, sugar and sodium across McDonald’s menu categories."
    },
    2: {
        "title": "Software Bug Tracker Analysis",
        "excel": "GNCIPL WEEK 2 EXCEL(1).xlsx",
        "powerbi": "GNCIPL WEEK 2 POWER BI(1).pbix",
        "description": "Analysis of software bugs by severity, priority, type, status, module and resolution time."
    },
    3: {
        "title": "Climate Change – Glacier Ice-Melt Analysis",
        "excel": "GNCIPL WEEK 3 EXCEL(1).xlsx",
        "powerbi": "GNCIPL WEEK 3 POWER BI(1).pbix",
        "description": "Analysis of glacier ice cover, ice loss, melt rate, temperature and regional climate-risk indicators."
    },
    4: {
        "title": "Water Consumption Dashboard",
        "excel": "GNCIPL WEEK 4 EXCEL(1).xlsx",
        "powerbi": "GNCIPL WEEK 4 POWER BI(1).pbix",
        "description": "Analysis of water consumption, rainfall, per-capita usage and groundwater-related indicators."
    },
    5: {
        "title": "AI-Enhanced Robotics Data Analytics",
        "excel": "GNCIPL WEEK 5 EXCEL(1).xlsx",
        "powerbi": "GNCIPL WEEK 5 POWER BI(1).pbix",
        "description": "Analysis of robot productivity, AI detection accuracy, downtime, maintenance, energy and cost savings."
    },
    6: {
        "title": "Employment Data Analysis and Skill Gap Identification",
        "excel": "GNCIPL WEEK 6 EXCEL(1).xlsx",
        "powerbi": "GNCIPL WEEK 6 POWER BI(1).pbix",
        "description": "Analysis of employment trends, employability, workforce distribution, skill gaps and training requirements."
    },
}

st.title("📊 GNCIPL — Six-Week Data Analytics Internship")
st.caption("Interactive project portfolio | Excel datasets | Power BI dashboards")

with st.sidebar:
    st.header("Projects")
    week = st.radio(
        "Select a week",
        options=list(PROJECTS.keys()),
        format_func=lambda x: f"Week {x} — {PROJECTS[x]['title']}"
    )
    st.divider()
    st.info("Use the download buttons to access the original Excel and Power BI files.")

p = PROJECTS[week]
excel_path = BASE / p["excel"]
pbix_path = BASE / p["powerbi"]

st.header(f"Week {week}: {p['title']}")
st.write(p["description"])

c1, c2 = st.columns(2)
with c1:
    with open(excel_path, "rb") as f:
        st.download_button(
            "⬇️ Download Excel Dataset",
            data=f.read(),
            file_name=p["excel"],
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )
with c2:
    with open(pbix_path, "rb") as f:
        st.download_button(
            "⬇️ Download Power BI Dashboard",
            data=f.read(),
            file_name=p["powerbi"],
            mime="application/octet-stream",
            use_container_width=True
        )

st.divider()
st.subheader("Excel Dataset Preview")

try:
    sheets = pd.ExcelFile(excel_path).sheet_names
    selected_sheet = st.selectbox("Select worksheet", sheets)
    df = pd.read_excel(excel_path, sheet_name=selected_sheet)

    a, b, c = st.columns(3)
    a.metric("Rows", f"{len(df):,}")
    b.metric("Columns", f"{len(df.columns):,}")
    c.metric("Worksheet", selected_sheet)

    st.dataframe(df.head(100), use_container_width=True, height=420)
except Exception as e:
    st.warning(f"Excel preview could not be loaded: {e}")

st.divider()
st.subheader("All Six Projects")
cols = st.columns(3)
for i, (w, info) in enumerate(PROJECTS.items()):
    with cols[i % 3]:
        st.markdown(f"**Week {w}**")
        st.write(info["title"])
        st.caption(info["description"])
