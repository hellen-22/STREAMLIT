import streamlit as st
import pandas as pd
import pandas_profiling
#pip install streamlit_pandas_profiling
from streamlit_pandas_profiling import st_profile_report

st.header('UNITS DETERMINANT')
"""
units_data = pd.read_csv('dashboard_data/Aggregated_Metrics_By_Country_And_Subscriber_Status.csv')
profile = units_data.profile_report()
st_profile_report(profile)

"""

#Implementing streamlit selctbox
school_selectbox = st.selectbox("Select your school",(
    "School of Computing",
    "School of Nursing",
    "School of Disaster Management",
    "School of Business and Economics",
    "School of Education"
))

if school_selectbox == "School of Computing":
    st.selectbox("Select your department",(
        "Information Technology",
        "Computer Science"
    ))


elif school_selectbox == "School of nursing":
    st.selectbox("Select your department",(
        "Nursing",
        "Technology"
    ))

elif school_selectbox == "School of Disaster Management":
    st.selectbox("Select your department",(
        "Disaster",
        "Management"
    ))


elif school_selectbox == "School of Business and Economics":
    st.selectbox("Select your department",(
        "Business Management",
        "Maths and economics"
    ))


elif school_selectbox == "School of Education":
    st.selectbox("Select your department",(
        "Arts",
        "Science",
        "Mathematics"
    ))

#Implementing streamlit slider
year_of_study = st.slider("Pick year of study", 1, 4, 2)
if year_of_study == 1:
    st.write("I'm in First Year")
elif year_of_study == 2:
    st.write("I'm in Second Year")
elif year_of_study == 3:
    st.write("I'm in Third Year")
elif year_of_study == 4:
    st.write("I'm in Fourth Year")

average_units = st.slider("How many units are offered in a semester", 0, 10,(5, 6))
st.write("We have an average of ", average_units, "units" )

#Implementing streamlit multiselect
st.multiselect("Select your fields of interest",["Networking", "Programming", "Security", "Hardware", "Database"],["Networking", "Database"])

#Implementing streamlit checkbox
st.write("How did you hear about us")
st.checkbox("Twitter")
st.checkbox("Whatsapp")
st.checkbox("A friend")
st.checkbox("Website")

#Implementing streamlit text input
search_text = st.text_input("Choice")


#Implementing streamlit button
recommend_button = st.button('SUBMIT')

#st.latex-for mathematical formulas

uploaded_file = st.file_uploader("Choose a csv file")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')