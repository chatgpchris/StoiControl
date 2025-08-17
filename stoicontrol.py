import streamlit as st
import datetime
import random


# ✅ Import questions and messages
from how_much_stoic_have_you_been import questions, status_messages


# ---------------------------
# Data handling
# ---------------------------

def calculate_score(user_answers):
    total = 0
    count = 0
    for q_num, idx in user_answers.items():
        score = questions[q_num]["answers"][idx]["score"]
        if score is not None:
            total += score
            count += 1
    if count == 0:
        return 0
    max_score = count * 3
    return round((total / max_score) * 100)


def get_status_message(score):
    if score <= 39:
        key = "0-39"
    elif score <= 59:
        key = "40-59"
    elif score <= 79:
        key = "60-79"
    elif score <= 94:
        key = "80-94"
    elif score <= 99:
        key = "95-99"
    else:
        key = "100"
    return random.choice(status_messages[key])


# ---------------------------
# Streamlit UI
# ---------------------------
st.set_page_config(page_title="StoiControl", page_icon="🦅", layout="centered")

st.title("🦅 StoiControl")
st.markdown(
    """
    <style>
    div.stButton > button {
        font-size: 18px;
        padding: 10px 15px;
        text-align: left;
    }
    </style>
    """, unsafe_allow_html=True
)
st.markdown(
    """
    <p style="font-size:20px; line-height:1.6;">
    They say life's a mess. We say, let's clean it up!<br><br>
    Welcome to the ultimate self-mastery challenge!<br><br>
    Your mind is the only kingdom you can truly rule, so start regaining your inner control 
    and learn to handle whatever chaos the universe throws at you!<br><br>
    Let's test how much Stoic you have recently been.
    </p>
    """, unsafe_allow_html=True
)
# Initialize session state
if "started" not in st.session_state:
    st.session_state.started = False
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}

# Intro page
if not st.session_state.started:
    if st.button("➡️ Take the Stoic Self-Test"):
        st.session_state.started = True
        st.rerun()
    st.stop()

# ---------------------------
# Question flow
# ---------------------------
q_keys = list(questions.keys())
q_num = st.session_state.current_question

if q_num < len(q_keys):
    q_data = questions[q_keys[q_num]]


    st.header(f"Question {q_num + 1} of {len(q_keys)}")
    st.markdown(f"<p style='font-size:22px; font-weight:bold;'>{q_data['text']}</p>", unsafe_allow_html=True)

    choice = None  # initialize

    for idx, opt in enumerate(q_data["answers"]):
    # Use st.button for each option
        if st.button(opt["text"], key=f"q{q_num}_{idx}"):
            choice = idx
            st.session_state.user_answers[q_keys[q_num]] = choice
            st.session_state.current_question += 1
            st.rerun()


# ---------------------------
# Results
# ---------------------------
else:
    user_answers = st.session_state.user_answers
    score = calculate_score(user_answers)
    message = get_status_message(score)
    today = datetime.date.today().strftime("%d %B, %Y")

    st.success(f"### Your Stoic Score on {today}: {score}%")

    st.markdown(
    f"""
    <div style="
        display:block;
        background-color:#e6f4fc;
        color:#0f4c81;
        padding:15px 20px;
        border-radius:6px;
        font-size:20px;
        line-height:1.5;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border: 1px solid #cce6f5;
    ">
        <div style="font-weight:bold; font-size:22px; margin-bottom:8px;">Assessment</div>
        <div style="font-size:20px; line-height:1.5;">{message}</div>
    </div>
    """,
    unsafe_allow_html=True
)


    # Retake option
    if st.button("🔄 Retake Test"):
        st.session_state.started = False
        st.session_state.current_question = 0
        st.session_state.user_answers = {}
        for key in list(st.session_state.keys()):
            if key.startswith("q"):
                del st.session_state[key]
        st.rerun()

