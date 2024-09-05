import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("externalcss.css")

def show_home():
    st.markdown("<h1 style='text-align: center; color: white;'>What do 100,000 reviewers tell about ChatGPT?</h1>", unsafe_allow_html=True)
    st.info(' ')
    gif_url = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmsxNXdqZmM5cHZnanFqdHN6Z3lhN3BoZno1ZWJ2d2toZDVvcWFhcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/iiSb58oATiANL65Dd2/giphy.gif"
    st.markdown(f"""
        <div style="display: flex; justify-content: center;">
            <img src="{gif_url}" style="max-width: 100%; height: auto;">
        </div>
    """, unsafe_allow_html=True)
    st.info(' ')
    st.markdown("<h1 style='text-align: center; color: white;'>Analyzing ChatGPT reviews</h1>", unsafe_allow_html=True)
    st.write("such an easy project. hehe")
    st.info(" ")

def show_docs():
    st.markdown("<h1 style='text-align: center; color: white;'>Documentation</h1>", unsafe_allow_html=True)
    st.write("The following modules were used")
    data = [["TextBlob", "NLP Module to generate sentiments"],
        ["Pandas", "Data Preprocessing"],
        ["Streamlit", "Application Framework"],
        ["PowerBI", "Reporting and Visualization"],
        ["DataPrep", "EDA"],
        ["RE", "Text Preprocessing"]]
    df = pd.DataFrame(data, columns=["Module Name", "Usage"])
    html_table = df.to_html(index=False)
    st.markdown(html_table, unsafe_allow_html=True)
    st.write(' ')
    st.write(' ')
    st.write("""
        - **TextBlob**: Used for NLP to generate sentiments from text.
        - **Pandas**: Handles data preprocessing, including cleaning and manipulation.
        - **Streamlit**: Provides an application framework for creating interactive web apps.
        - **PowerBI**: Facilitates reporting and visualization with powerful dashboards.
        - **DataPrep**: Assists in exploratory data analysis (EDA) for summarizing and understanding data.
        - **RE**: Used for text preprocessing to clean and normalize text data.
        """)
    st.write("<h2 style='text-align: center;'><b>Why RE</b></h2>", unsafe_allow_html=True)
    st.write("""
    - **Purpose**: To clean text by removing unwanted characters, managing whitespace, and normalizing the text.
    - **Usage**: Applied during the text preprocessing phase to ensure data consistency and accuracy.

    **Without RE Processing**: 
    - The absence of RE cleaning can lead to the presence of noise and inconsistencies in the text. This can manipulate the analysis performed by tools like TextBlob, resulting in inaccurate sentiment assessments.
    """, unsafe_allow_html=True)

def show_powerbi():
    powerbi_url = "https://app.powerbi.com/view?r=eyJrIjoiYzA5ZjRkMmMtNDQ5My00ZmE4LWFmYjEtMDIwYmRmNzU5ZWYzIiwidCI6IjkzNjIwZTExLTliYzQtNDRiOC05YTVjLWJjMDY2M2I3NDM3NCIsImMiOjEwfQ%3D%3D"
    components.html(f"""
        <div style="text-align: center; width: 100%; height: 0; padding-bottom: 56.25%; position: relative;">
            <iframe src="{powerbi_url}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" allowFullScreen="true"></iframe>
        </div>
    """, height=420)

    overall_findings_data = {
        'Metric': [
            'Average Subjectivity Score',
            'Average Polarity Score',
            'Average Rating'
        ],
        'Value': [
            '0.50 (Moderate level of subjectivity)',
            '0.41 (Slightly positive overall sentiment)',
            '4.45 out of 5 (Generally positive overall rating)'
        ]
    }
    df_overall_findings = pd.DataFrame(overall_findings_data)
    st.markdown("<h1 style='text-align: center;'>Key Findings</h1>", unsafe_allow_html=True)
    st.write(' ')
    st.markdown("<h2 style='text-align: center;'>Overall Findings</h2>", unsafe_allow_html=True)
    st.markdown(
        f"<div style='display: flex; justify-content: center;'>{df_overall_findings.to_html(index=False, header=True, border=0, classes='table table-bordered')}</div>",
        unsafe_allow_html=True
    )

    subjectivity_data = {
        'Subjectivity Level': ['Subjective', 'Mixed', 'Objective'],
        'Average Rating': [4.56, 4.44, 4.17]
    }
    df_subjectivity = pd.DataFrame(subjectivity_data)
    
    st.write(' ')
    st.markdown("<h2 style='text-align: center;'>Subjectivity Findings</h2>", unsafe_allow_html=True)
    st.markdown(
        f"<div style='display: flex; justify-content: center;'>{df_subjectivity.to_html(index=False, header=True, border=0, classes='table table-bordered')}</div>",
        unsafe_allow_html=True
    )

    sentiment_data = {
        'Sentiment': ['Very Positive', 'Positive', 'Neutral', 'Negative', 'Very Negative'],
        'Average Rating': [4.76, 4.56, 4.07, 3.59, 2.79]
    }
    df_sentiment = pd.DataFrame(sentiment_data)
    st.write(' ')
    st.markdown("<h2 style='text-align: center;'>Sentiment Findings</h2>", unsafe_allow_html=True)
    st.markdown(
        f"<div style='display: flex; justify-content: center;'>{df_sentiment.to_html(index=False, header=True, border=0, classes='table table-bordered')}</div>",
        unsafe_allow_html=True
    )

    counts_data = {
        'Type': ['Subjective', 'Mixed', 'Objective', 'Very Positive', 'Positive', 'Neutral', 'Negative', 'Very Negative'],
        'Count': [30067, 17191, 16665, 3867, 26816, 33547, 23647, 2988]
    }
    df_counts = pd.DataFrame(counts_data)
    st.write(' ')
    st.markdown("<h2 style='text-align: center;'>Counts</h2>", unsafe_allow_html=True)
    st.markdown(
        f"<div style='display: flex; justify-content: center;'>{df_counts.to_html(index=False, header=True, border=0, classes='table table-bordered')}</div>",
        unsafe_allow_html=True
    )

# Sidebar navigation
if 'selected_page' not in st.session_state:
    st.session_state.selected_page = "Home"

def show_sidebar_buttons():
    if st.session_state.selected_page == "Home":
        st.sidebar.markdown("""
            <style>
            .sidebar-button {
                display: none;
            }
            </style>
        """, unsafe_allow_html=True)
    else:
        st.sidebar.markdown("""
            <style>
            .sidebar-button {
                display: block;
                margin-bottom: 10px;
            }
            </style>
        """, unsafe_allow_html=True)

    st.sidebar.button('Home', key='home', on_click=lambda: st.session_state.update(selected_page="Home"))
    st.sidebar.button('Documentation', key='docs', on_click=lambda: st.session_state.update(selected_page="Documentation"))
    st.sidebar.button('Reports', key='reports', on_click=lambda: st.session_state.update(selected_page="Reports"))

show_sidebar_buttons()

if st.session_state.selected_page == "Home":
    show_home()
elif st.session_state.selected_page == "Documentation":
    show_docs()
elif st.session_state.selected_page == "Reports":
    show_powerbi()
     
