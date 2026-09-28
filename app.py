import streamlit as st
import pandas as pd
import urllib.parse
from pathlib import Path
from openpyxl import load_workbook

st.set_page_config(
    page_title="GNCIPL Data Analytics Internship",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------------
# FILE CONFIGURATION
# ---------------------------------------------------------

BASE_DIR = Path(__file__).parent

GITHUB_RAW = (
    "https://github.com/prastuti0511/"
    "Data-Analytics-GNCIPL-/raw/refs/heads/main/"
)

PROJECTS = {
    "Week 1": {
        "title": "McDonald's Menu Nutrition Analysis",
        "description": "Analysis of calories, protein, fat, carbohydrates, sugar and sodium across McDonald's menu items.",
        "excel": "GNCIPL WEEK 1 EXCEL(2).xlsx",
        "powerbi": "GNCIPL WEEK 1 POWER BI(1).pbix",
        "sheet": "Table1",
        "usecols": "A:N"
    },

    "Week 2": {
        "title": "Bug Tracking & Software Quality Analysis",
        "description": "Analysis of software bugs based on severity, priority, status, modules and resolution time.",
        "excel": "GNCIPL WEEK 2 EXCEL(1).xlsx",
        "powerbi": "GNCIPL WEEK 2 POWER BI(1).pbix",
        "sheet": "Table1",
        "usecols": "A:M"
    },

    "Week 3": {
        "title": "Glacier Ice Melt Monitoring",
        "description": "Analysis of glacier ice loss, temperature, snowfall, precipitation and regional risk.",
        "excel": "GNCIPL WEEK 3 EXCEL(1).xlsx",
        "powerbi": "GNCIPL WEEK 3 POWER BI(1).pbix",
        "sheet": "glacier_ice_melt_monitoring_syn",
        "usecols": "A:U"
    },

    "Week 4": {
        "title": "Water Usage & Resource Analysis",
        "description": "Analysis of water usage, rainfall, population and state-wise water consumption.",
        "excel": "GNCIPL WEEK 4 EXCEL(1).xlsx",
        "powerbi": "GNCIPL WEEK 4 POWER BI(1).pbix",
        "sheet": "Water_Data",
        "usecols": "A:O"
    },

    "Week 5": {
        "title": "AI-Enhanced Robotics Data Analytics",
        "description": "Analysis of robotics productivity, AI accuracy, efficiency, maintenance and production.",
        "excel": "GNCIPL WEEK 5 EXCEL(1).xlsx",
        "powerbi": "GNCIPL WEEK 5 POWER BI(1).pbix",
        "sheet": "Robotics_Data",
        "usecols": "A:Z"
    },

    "Week 6": {
        "title": "Employment Trends & Workforce Analysis",
        "description": "Analysis of employment trends, salaries, employability, skills and workforce gaps.",
        "excel": "GNCIPL WEEK 6 EXCEL(1).xlsx",
        "powerbi": "GNCIPL WEEK 6 POWER BI(1).pbix",
        "sheet": "Employee_Data",
        "usecols": "A:AZ"
    }
}


# ---------------------------------------------------------
# HELPER FUNCTIONS
# ---------------------------------------------------------

def excel_col_number(col_range):
    """Convert A:AZ into the ending column number."""
    end_col = col_range.split(":")[-1]

    number = 0
    for char in end_col:
        number = number * 26 + ord(char.upper()) - ord("A") + 1

    return number


def clean_columns(df):
    """Remove completely empty columns."""
    df = df.dropna(axis=1, how="all")

    valid_columns = []

    for col in df.columns:
        if col is None:
            continue

        name = str(col).strip()

        if name == "":
            continue

        if name.lower().startswith("column"):
            continue

        valid_columns.append(col)

    return df[valid_columns]


@st.cache_data(show_spinner=False)
def load_excel(filename, sheet_name, usecols):
    """
    Reads only the required columns using openpyxl read-only mode.
    This prevents the huge-memory problem caused by Weeks 3 and 4.
    """

    path = BASE_DIR / filename

    if not path.exists():
        raise FileNotFoundError(
            f"File not found: {filename}"
        )

    max_col = excel_col_number(usecols)

    workbook = load_workbook(
        path,
        read_only=True,
        data_only=True
    )

    worksheet = workbook[sheet_name]

    rows = worksheet.iter_rows(
        min_row=1,
        max_col=max_col,
        values_only=True
    )

    header = next(rows)

    data = list(rows)

    workbook.close()

    df = pd.DataFrame(data, columns=header)

    return clean_columns(df)


def numeric_column(df, names):
    """Find the first matching numeric column."""
    for name in names:
        if name in df.columns:
            return name
    return None


# ---------------------------------------------------------
# KPI SECTION
# ---------------------------------------------------------

def show_kpis(df, week):

    if week == "Week 1":

        calories = numeric_column(df, ["Calories"])
        protein = numeric_column(df, ["Protien", "Protein"])
        sugar = numeric_column(df, ["Sugar"])

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Menu Items", len(df))

        if calories:
            c2.metric(
                "Average Calories",
                f"{pd.to_numeric(df[calories], errors='coerce').mean():.0f}"
            )

        if protein:
            c3.metric(
                "Average Protein",
                f"{pd.to_numeric(df[protein], errors='coerce').mean():.1f} g"
            )

        if sugar:
            c4.metric(
                "Average Sugar",
                f"{pd.to_numeric(df[sugar], errors='coerce').mean():.1f} g"
            )

    elif week == "Week 2":

        severity = numeric_column(df, ["Severity"])

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Total Bugs", len(df))

        if "Status" in df.columns:
            c2.metric("Statuses", df["Status"].nunique())

        if "Module" in df.columns:
            c3.metric("Modules", df["Module"].nunique())

        if "Severity" in df.columns:
            c4.metric("Severity Levels", df["Severity"].nunique())

    elif week == "Week 3":

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Records", f"{len(df):,}")

        if "Region" in df.columns:
            c2.metric("Regions", df["Region"].nunique())

        if "Glacier_ID" in df.columns:
            c3.metric("Glaciers", df["Glacier_ID"].nunique())

        if "Risk_Level" in df.columns:
            c4.metric("Risk Levels", df["Risk_Level"].nunique())

    elif week == "Week 4":

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Records", f"{len(df):,}")

        if "State" in df.columns:
            c2.metric("States", df["State"].nunique())

        if "Region" in df.columns:
            c3.metric("Regions", df["Region"].nunique())

        if "Year" in df.columns:
            c4.metric("Years", df["Year"].nunique())

    elif week == "Week 5":

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Records", f"{len(df):,}")

        if "Robot_ID" in df.columns:
            c2.metric("Robots", df["Robot_ID"].nunique())

        if "Robot_Type" in df.columns:
            c3.metric("Robot Types", df["Robot_Type"].nunique())

        if "Plant" in df.columns:
            c4.metric("Plants", df["Plant"].nunique())

    elif week == "Week 6":

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Employee Records", f"{len(df):,}")

        if "Industry" in df.columns:
            c2.metric("Industries", df["Industry"].nunique())

        if "Year" in df.columns:
            c3.metric("Years", df["Year"].nunique())

        if "Gender" in df.columns:
            c4.metric("Gender Categories", df["Gender"].nunique())


# ---------------------------------------------------------
# CHARTS
# ---------------------------------------------------------

def show_charts(df, week):

    st.subheader("📊 Interactive Analysis")

    if week == "Week 1":

        col1, col2 = st.columns(2)

        with col1:

            if "Menu" in df.columns and "Calories" in df.columns:

                chart_data = (
                    df.groupby("Menu")["Calories"]
                    .mean()
                    .sort_values(ascending=False)
                )

                st.write("**Average Calories by Menu Category**")
                st.bar_chart(chart_data)

        with col2:

            if "Item" in df.columns and "Calories" in df.columns:

                chart_data = (
                    df[["Item", "Calories"]]
                    .copy()
                )

                chart_data["Calories"] = pd.to_numeric(
                    chart_data["Calories"],
                    errors="coerce"
                )

                chart_data = (
                    chart_data
                    .dropna()
                    .sort_values("Calories", ascending=False)
                    .head(10)
                    .set_index("Item")
                )

                st.write("**Top 10 Items by Calories**")
                st.bar_chart(chart_data)

        if all(
            col in df.columns
            for col in ["Calories", "Total Fat", "Carbohydrates", "Sugar", "Sodium"]
        ):

            nutrition = df[
                ["Calories", "Total Fat", "Carbohydrates", "Sugar", "Sodium"]
            ].apply(pd.to_numeric, errors="coerce").mean()

            st.write("**Average Nutrition Metrics**")
            st.bar_chart(nutrition)

    elif week == "Week 2":

        col1, col2 = st.columns(2)

        with col1:

            if "Severity" in df.columns:

                severity_count = df["Severity"].value_counts()

                st.write("**Bug Count by Severity**")
                st.bar_chart(severity_count)

        with col2:

            if "Module" in df.columns and "Resolution Time (Days)" in df.columns:

                resolution = df.copy()

                resolution["Resolution Time (Days)"] = pd.to_numeric(
                    resolution["Resolution Time (Days)"],
                    errors="coerce"
                )

                resolution = (
                    resolution
                    .groupby("Module")["Resolution Time (Days)"]
                    .mean()
                    .sort_values(ascending=False)
                )

                st.write("**Average Resolution Time by Module**")
                st.bar_chart(resolution)

        if "Status" in df.columns:

            st.write("**Bug Status Distribution**")
            st.bar_chart(df["Status"].value_counts())

    elif week == "Week 3":

        col1, col2 = st.columns(2)

        with col1:

            if "Year" in df.columns and "Ice_Loss_km2" in df.columns:

                temp = df.copy()

                temp["Ice_Loss_km2"] = pd.to_numeric(
                    temp["Ice_Loss_km2"],
                    errors="coerce"
                )

                trend = (
                    temp.groupby("Year")["Ice_Loss_km2"]
                    .mean()
                    .sort_index()
                )

                st.write("**Average Ice Loss by Year**")
                st.line_chart(trend)

        with col2:

            if "Region" in df.columns and "Ice_Loss_km2" in df.columns:

                region = df.copy()

                region["Ice_Loss_km2"] = pd.to_numeric(
                    region["Ice_Loss_km2"],
                    errors="coerce"
                )

                region = (
                    region.groupby("Region")["Ice_Loss_km2"]
                    .mean()
                    .sort_values(ascending=False)
                )

                st.write("**Average Ice Loss by Region**")
                st.bar_chart(region)

        if "Risk_Level" in df.columns:

            st.write("**Risk Level Distribution**")
            st.bar_chart(df["Risk_Level"].value_counts())

    elif week == "Week 4":

        col1, col2 = st.columns(2)

        with col1:

            if "Year" in df.columns and "Water_Usage_Million_m3" in df.columns:

                temp = df.copy()

                temp["Water_Usage_Million_m3"] = pd.to_numeric(
                    temp["Water_Usage_Million_m3"],
                    errors="coerce"
                )

                trend = (
                    temp.groupby("Year")["Water_Usage_Million_m3"]
                    .mean()
                    .sort_index()
                )

                st.write("**Average Water Usage by Year**")
                st.line_chart(trend)

        with col2:

            if "State" in df.columns and "Water_Usage_Million_m3" in df.columns:

                temp = df.copy()

                temp["Water_Usage_Million_m3"] = pd.to_numeric(
                    temp["Water_Usage_Million_m3"],
                    errors="coerce"
                )

                state = (
                    temp.groupby("State")["Water_Usage_Million_m3"]
                    .mean()
                    .sort_values(ascending=False)
                    .head(15)
                )

                st.write("**Average Water Usage by State**")
                st.bar_chart(state)

        if "Region" in df.columns and "Rainfall_mm" in df.columns:

            temp = df.copy()

            temp["Rainfall_mm"] = pd.to_numeric(
                temp["Rainfall_mm"],
                errors="coerce"
            )

            rainfall = (
                temp.groupby("Region")["Rainfall_mm"]
                .mean()
                .sort_values(ascending=False)
            )

            st.write("**Average Rainfall by Region**")
            st.bar_chart(rainfall)

    elif week == "Week 5":

        col1, col2 = st.columns(2)

        with col1:

            if "Robot_Type" in df.columns and "Units_Produced" in df.columns:

                temp = df.copy()

                temp["Units_Produced"] = pd.to_numeric(
                    temp["Units_Produced"],
                    errors="coerce"
                )

                production = (
                    temp.groupby("Robot_Type")["Units_Produced"]
                    .sum()
                    .sort_values(ascending=False)
                )

                st.write("**Units Produced by Robot Type**")
                st.bar_chart(production)

        with col2:

            if "Plant" in df.columns and "Overall_Efficiency" in df.columns:

                temp = df.copy()

                temp["Overall_Efficiency"] = pd.to_numeric(
                    temp["Overall_Efficiency"],
                    errors="coerce"
                )

                efficiency = (
                    temp.groupby("Plant")["Overall_Efficiency"]
                    .mean()
                    .sort_values(ascending=False)
                )

                st.write("**Average Efficiency by Plant**")
                st.bar_chart(efficiency)

        if "Robot_Status" in df.columns:

            st.write("**Robot Status Distribution**")
            st.bar_chart(df["Robot_Status"].value_counts())

    elif week == "Week 6":

        col1, col2 = st.columns(2)

        with col1:

            if "Year" in df.columns and "Employability" in df.columns:

                temp = df.copy()

                temp["Employability"] = pd.to_numeric(
                    temp["Employability"],
                    errors="coerce"
                )

                employability = (
                    temp.groupby("Year")["Employability"]
                    .mean()
                    .sort_index()
                )

                st.write("**Average Employability by Year**")
                st.line_chart(employability)

        with col2:

            if "Industry" in df.columns and "Salary" in df.columns:

                temp = df.copy()

                temp["Salary"] = pd.to_numeric(
                    temp["Salary"],
                    errors="coerce"
                )

                salary = (
                    temp.groupby("Industry")["Salary"]
                    .mean()
                    .sort_values(ascending=False)
                    .head(15)
                )

                st.write("**Average Salary by Industry**")
                st.bar_chart(salary)

        if "Skill_Gap" in df.columns:

            st.write("**Skill Gap Distribution**")
            st.bar_chart(df["Skill_Gap"].value_counts())


# ---------------------------------------------------------
# MAIN APP
# ---------------------------------------------------------

st.title("📊 GNCIPL Data Analytics Internship Portfolio")

st.write(
    "Interactive six-week portfolio containing Excel datasets, "
    "data analysis and Power BI projects."
)

st.sidebar.header("📚 Select Internship Week")

week = st.sidebar.selectbox(
    "Choose a project:",
    list(PROJECTS.keys())
)

project = PROJECTS[week]

st.header(project["title"])

st.write(project["description"])

# ---------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------

try:

    with st.spinner(f"Loading {week} data..."):

        df = load_excel(
            project["excel"],
            project["sheet"],
            project["usecols"]
        )

except Exception as e:

    st.error("Unable to load this week's Excel data.")

    st.code(str(e))

    st.stop()


# ---------------------------------------------------------
# KPI
# ---------------------------------------------------------

show_kpis(df, week)

st.divider()

# ---------------------------------------------------------
# CHARTS
# ---------------------------------------------------------

show_charts(df, week)

st.divider()

# ---------------------------------------------------------
# DATA TABLE
# ---------------------------------------------------------

st.subheader("📋 Dataset")

st.write(
    f"Showing the first 100 rows of {len(df):,} total records."
)

st.dataframe(
    df.head(100),
    use_container_width=True,
    height=450
)

# ---------------------------------------------------------
# DOWNLOADS
# ---------------------------------------------------------

st.subheader("📥 Project Files")

col1, col2 = st.columns(2)

with col1:

    excel_path = BASE_DIR / project["excel"]

    if excel_path.exists():

        with open(excel_path, "rb") as file:

            st.download_button(
                label="⬇️ Download Excel Dataset",
                data=file,
                file_name=project["excel"],
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

with col2:

    encoded_pbix = urllib.parse.quote(project["powerbi"])

    pbix_url = GITHUB_RAW + encoded_pbix

    st.link_button(
        "⬇️ Download Power BI File",
        pbix_url
    )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.divider()

st.subheader("📁 Six-Week Internship Portfolio")

for project_name, project_info in PROJECTS.items():

    st.write(
        f"**{project_name}:** {project_info['title']}"
    )

st.success(
    "GNCIPL Data Analytics Internship Portfolio loaded successfully."
)
