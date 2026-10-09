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
st.text("המודל קיבל את נתוני השחקנים - הגובה והנקודות למשחק ואיתם התאמן עד שמצא את המודל הטוב ביותר")
st.text("הלוס עבור הבייסליין: 4.777328250434676")
st.text("הלוס עבור המודל: 4.764889016829812")
st.text("המודל טוב רק במעט מאוד מהבייסליין - ניתן להסיק מכאן שגובה של שחקן הוא לא מדד טוב בשביל לחזות נקודות שלו למשחק")
