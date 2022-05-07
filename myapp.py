import streamlit as st

st.header('UNITS DETERMINANT')

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


search_text = st.text_input("Choice")

recommend_button = st.button('SUBMIT')