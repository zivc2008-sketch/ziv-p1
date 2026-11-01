import streamlit as st

# עיצוב מותאם אישית ב-CSS בתוך מחרוזת פייתון תקינה
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

st.title("🏀 משחק ניחוש נקודות NBA")
st.subheader("הזן גובה ומשקל ונסה להנחש את כמות הנקודות המחושבת!")

# קלט מהמשתמש לגובה ומשקל
height = st.number_input("Enter height:", min_value=0, step=1)
weight = st.number_input("Enter weight:", min_value=0, step=1)

# משקולות המודל
w1 = -0.07072934956142785
w2 = 0.03051940672845106
b = 19.337737482061055

# חישוב התוצאה ועיגול למספר שלם
prediction = height * w1 + weight * w2 + b
expected_points = round(prediction)

# שדה להזנת הניחוש של המשתמש
user_guess = st.number_input("מה הניחוש שלך למספר הנקודות?", step=1, value=0)

if st.button("בדוק ניחוש"):
    if user_guess == expected_points:
        st.balloons()
        st.success(f"כל הכבוד! צדקת בול! התוצאה המחושבת היא {expected_points}.")
    else:
        st.error(f"לא מדויק. הניחוש שלך היה {user_guess}, אך לפי המודל התוצאה היא {expected_points} (לפני עיגול: {prediction:.2f}).")
