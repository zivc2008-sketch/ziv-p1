import streamlit as st
st.title("NBA")
st.header("Enter height to see the expacted points")
height = st.number_input("enter height:", min_value=0, step=1)


w= -0.03650734467294015
b= 15.534315785648516

prediction = height * w +b

st.subheader(f"result: {prediction}")

st.text("המודל הזה מחשב את ממוצי הנקודות של שחקן בגובה מסוים רק לפי גובהו")
st.text("אם בודקים לפי גובה - השיפוע דווקא יוצא שלילי ככל ששחקן יותר גבוה כך הממוצא יורד")
