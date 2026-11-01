import streamlit as st

# עיצוב CSS מותאם אישית (עטוף במחרוזת כדי למנוע שגיאות תחביר בפייתון)
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f12a0 0%, #1e1b4b 50%, #0f12a0 100%);
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("NBA")
st.header("Enter height and weight to guess the expected points")

# שדות קלט לגובה ומשקל
height = st.number_input("enter height:", min_value=0, step=1)
weight = st.number_input("enter weight:", min_value=0, step=1)

# משקולות המודל
w1 = -0.07072934956142785
w2 = 0.03051940672845106
b = 19.337737482061055

# חישוב התוצאה המדויקת ועיגול למספר שלם
prediction = height * w1 + weight * w2 + b
expected_points = round(prediction)

# שדה להזנת ניחוש המשתמש
user_guess = st.number_input(
    "Guess the expected points (integer):", step=1, value=0
)

# בדיקת הניחוש
if st.button("Check Guess"):
    if user_guess == expected_points:
        st.balloons()
        st.success(f"Correct! The expected points rounded is {expected_points}.")
    else:
        st.error(
            f"Wrong guess! You guessed {user_guess}, but the calculated value was {expected_points} (exact: {prediction:.2f})."
        )

st.text("(המודל הזה מחשב את ממוצע הנקודות של שחקן בגובה מסוים רק לפי גובה)")
st.text("(אם בודקים לפי גובה - השיפוע דווקא יוצא שלילי ככל ששחקן יותר גבוה כך הממוצע יורד)")
st.text("(המודל קיבל את נתוני השחקנים - הגובה והנקודות למשחק ואותם התאמן עד שמצא את המודל הטוב ביותר)")
st.text("4.777328250434676 :(הלוס עבור הבייסליין)")
st.text("4.764889016829812 :הלוס עבור המודל)")
st.text("(המודל טוב רק במעט מאוד מהבייסליין - ניתן להסיק מכאן שטוב שהוא לא מדד טוב בשביל לחזות נקודות שלו למשחק)")
