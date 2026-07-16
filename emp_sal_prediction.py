import pandas as pd
import joblib
import streamlit as st

def main():
    html_temp="""<h1>Employee Salary Prediction</h1>"""

    model = joblib.load("xgb_model.pkl")
    scaler = joblib.load("scaler.pkl")

    st.markdown(html_temp, unsafe_allow_html=True)
    st.markdown("This app will help you to predict your salary.")

    p1 = st.number_input("Please enter age",18,70,step=1)

    s1 = st.selectbox("Select the Gender",("Female","Male"))
    if s1=='Female':
        p2=0
    elif s1=='Male':
        p2=1
    
    s2 = st.selectbox("Select the Education",("Diploma","Bachelor","Master","PhD"))
    if s2=='Diploma':
        p3=0
    elif s2=='Bachelor':
        p3=1
    elif s2=='Master':
        p3=2
    elif s2=='PhD':
        p3=3

    # Experience Years
    p4 = st.number_input("Please enter Experience Years",0,40,step=1)

# Department
    s3 = st.selectbox("Select the Department",("Operations","IT","Finance","Sales","HR","Marketing"))

    if s3=="Operations":
        p5=0
    elif s3=="IT":
        p5=1
    elif s3=="Finance":
        p5=2
    elif s3=="Sales":
        p5=3
    elif s3=="HR":
        p5=4
    elif s3=="Marketing":
        p5=5

    # Job Level
    s4 = st.selectbox("Select the Job Level",("Junior","Mid","Senior","Lead","Manager"))

    if s4=="Junior":
        p6=1
    elif s4=="Mid":
        p6=2
    elif s4=="Senior":
        p6=3
    elif s4=="Lead":
        p6=4
    elif s4=="Manager":
        p6=5

    # Performance Rating
    p7 = st.selectbox("Select the Performance Rating",(1,2,3,4,5))

    # Certifications
    p8 = st.number_input("Please enter Certifications",0,10,step=1)

    # Overtime Hours
    p9 = st.number_input("Please enter Overtime Hours",0,60,step=1)

    # Remote Work
    s5 = st.selectbox("Select Remote Work",("No","Yes"))

    if s5=="No":
        p10=0
    elif s5=="Yes":
        p10=1

    # City
    s6 = st.selectbox("Select the City",("Hyderabad","Mumbai","Pune","Chennai","Bangalore","Delhi"))

    if s6=="Hyderabad":
        p11=0
    elif s6=="Mumbai":
        p11=1
    elif s6=="Pune":
        p11=2
    elif s6=="Chennai":
        p11=3
    elif s6=="Bangalore":
        p11=4
    elif s6=="Delhi":
        p11=5

    # Company Tenure
    p12 = st.number_input("Please enter Company Tenure",0,15,step=1)

    # Projects Completed
    p13 = st.number_input("Please enter Projects Completed",1,30,step=1)

    # Skill Score
    p14 = st.number_input("Please enter Skill Score",50.0,100.0,step=1.0)


    data_new = pd.DataFrame({
        'Age': [p1],
        'Gender': [p2],
        'Education': [p3],
        'Experience_Years': [p4],
        'Department': [p5],
        'Job_Level': [p6],
        'Performance_Rating': [p7],
        'Certifications': [p8],
        'Overtime_Hours': [p9],
        'Remote_Work': [p10],
        'City': [p11],
        'Company_Tenure': [p12],
        'Projects_Completed': [p13],
        'Skill_Score': [p14]
    }, index=[0])

    if st.button("Predict Salary"):
        data_new_scaled = scaler.transform(data_new)
        pred = model.predict(data_new_scaled)
        st.success("Predicted Annual Salary: {:.2f} LPA".format(pred[0]))

if __name__=='__main__':
    main()