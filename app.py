import streamlit as st
import pandas as pd

from statistics import compute_mean_and_std
from grading_policy import get_relative_grading_policy
from grading_engine import assign_grade
from input_layer import extract_marks_from_csv



st.set_page_config(
    page_title="Grade Calculator",
    layout="centered"
)

st.title("📊 Grade Calculator")
st.caption("Relative grading using official Mean & Standard Deviation policy")

policy = get_relative_grading_policy()



mode = st.selectbox(
    "Choose grading mode",
    [
        "Single Student (Known Mean & SD)",
        "CSV (Full Class)",
        "Manual Entry (Full Class)",
        
    ]
)

st.divider()



if mode == "Single Student (Known Mean & SD)":
    st.subheader("🎓 Single Student Grading")

    mean = st.number_input("Class Mean", min_value=0.0, max_value=100.0, step=0.1)
    std_dev = st.number_input("Class Standard Deviation", min_value=0.0, step=0.1)
    marks = st.number_input("Student Marks", min_value=0.0, max_value=100.0, step=0.5)

    if st.button("Calculate Grade"):
        grade, points = assign_grade(marks, mean, std_dev, policy)

        st.success(f"Grade: {grade}")
        st.info(f"Grade Points: {points}")



elif mode == "CSV (Full Class)":
    st.subheader("📂 CSV Upload (Full Class)")

    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file:
        try:
            marks = extract_marks_from_csv(uploaded_file)
            mean, std_dev = compute_mean_and_std(marks)

            st.write(f"**Class Mean:** {mean:.2f}")
            st.write(f"**Standard Deviation:** {std_dev:.2f}")

            results = []
            for i, m in enumerate(marks, start=1):
                grade, points = assign_grade(m, mean, std_dev, policy)
                results.append({
                    "Student": i,
                    "Marks": round(m, 2),
                    "Grade": grade,
                    "Points": points
                })

            df = pd.DataFrame(results)
            st.subheader("Grades")
            st.dataframe(df, use_container_width=True)

        except Exception as e:
            st.error(str(e))



elif mode == "Manual Entry (Full Class)":
    st.subheader("✍️ Manual Entry (Full Class)")

    raw_marks = st.text_area(
        "Enter marks (comma separated)",
        placeholder="78, 85, 90, 66, 72"
    )

    if st.button("Calculate Grades"):
        try:
            marks = [float(x.strip()) for x in raw_marks.split(",") if x.strip()]
            if not marks:
                raise ValueError("No marks provided.")

            mean, std_dev = compute_mean_and_std(marks)

            st.write(f"**Class Mean:** {mean:.2f}")
            st.write(f"**Standard Deviation:** {std_dev:.2f}")

            results = []
            for i, m in enumerate(marks, start=1):
                grade, points = assign_grade(m, mean, std_dev, policy)
                results.append({
                    "Student": i,
                    "Marks": round(m, 2),
                    "Grade": grade,
                    "Points": points
                })

            df = pd.DataFrame(results)
            st.subheader("Grades")
            st.dataframe(df, use_container_width=True)

        except Exception as e:
            st.error(str(e))


# =================================================
# MODE 4: KNOWN MEAN & SD (MULTIPLE STUDENTS)
# =================================================
elif mode == "Known Mean & SD (Multiple Students)":
    st.subheader("📐 Known Mean & SD")

    mean = st.number_input("Class Mean", min_value=0.0, max_value=100.0, step=0.1)
    std_dev = st.number_input("Class Standard Deviation", min_value=0.0, step=0.1)

    raw_marks = st.text_area(
        "Enter student marks (comma separated)",
        placeholder="72, 81, 67"
    )

    if st.button("Calculate Grades"):
        try:
            marks = [float(x.strip()) for x in raw_marks.split(",") if x.strip()]
            if not marks:
                raise ValueError("No marks provided.")

            results = []
            for i, m in enumerate(marks, start=1):
                grade, points = assign_grade(m, mean, std_dev, policy)
                results.append({
                    "Student": i,
                    "Marks": round(m, 2),
                    "Grade": grade,
                    "Points": points
                })

            df = pd.DataFrame(results)
            st.subheader("Grades")
            st.dataframe(df, use_container_width=True)

        except Exception as e:
            st.error(str(e))