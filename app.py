import streamlit as st
st.title("NBA")
st.header("Enter height to see the expacted points")
height = st.number_input("enter height:", min_value=0, step=1)
weight = st.number_input("enter weight:", min_value=0, step=1)


w1= -0.07072934956142785
w2= 0.03051940672845106
b= 19.337737482061055

prediction = height * w1 + weight *w2 +b

st.subheader(f"result: {prediction}")

st.text("המודל הזה מחשב את ממוצי הנקודות של שחקן בגובה מסוים רק לפי גובהו")
st.text("אם בודקים לפי גובה - השיפוע דווקא יוצא שלילי ככל ששחקן יותר גבוה כך הממוצא יורד")
st.text("המודל קיבל את נתוני השחקנים - הגובה והנקודות למשחק ואיתם התאמן עד שמצא את המודל הטוב ביותר")
st.text("הלוס עבור הבייסליין: 4.777328250434676")
st.text("הלוס עבור המודל: 4.764889016829812")
st.text("המודל טוב רק במעט מאוד מהבייסליין - ניתן להסיק מכאן שגובה של שחקן הוא לא מדד טוב בשביל לחזות נקודות שלו למשחק")
