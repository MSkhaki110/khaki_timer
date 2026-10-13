import streamlit as st
import time

# ----------------- PAGE CONFIG -----------------
st.set_page_config(page_title="Login Timer App", page_icon="🔐")

# ----------------- SESSION -----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ----------------- ALARM -----------------
def play_alarm():
    st.markdown("""
        <audio autoplay>
            <source src="https://actions.google.com/sounds/v1/alarms/alarm_clock.ogg" type="audio/ogg">
        </audio>
    """, unsafe_allow_html=True)

# ----------------- LOGIN PAGE -----------------
def login():

    st.markdown("""
        <style>
        .stApp {
            background-color: #FFD700;  /* Gold */
        }

        h1 {
            text-align: center;
            color: white;
        }

        label {
            color: white !important;
            font-weight: bold;
        }

        /* Center input fields */
        .center {
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1>🔐 Login Page</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username == "admin" and password == "1234":
                st.session_state.logged_in = True
                st.success("Login Successful 🎉")
                st.rerun()
            else:
                st.error("Invalid Username or Password")

# ----------------- TIMER PAGE -----------------
def timer_app():

    st.markdown("""
        <style>
        .stApp {
            background-color: #FFD700;
        }

        html, body, [class*="css"] {
            color: white !important;
        }

        .timer-box {
            background-color: #2E8B57;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            color: white;
            font-size: 28px;
            font-weight: bold;
            margin-top: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("⏱️ Timer Dashboard")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    seconds = st.number_input("Enter time in seconds:", min_value=1, step=1)
    start = st.button("Start Timer")

    box = st.empty()

    if start:
        for i in range(int(seconds), 0, -1):
            mins, secs = divmod(i, 60)
            timer = f"{mins:02d}:{secs:02d}"

            box.markdown(f"""
            <div class="timer-box">
                ⏳ Time Left: {timer}
            </div>
            """, unsafe_allow_html=True)

            time.sleep(1)

        box.markdown("""
        <div class="timer-box">
            🎉 Time's Up!
        </div>
        """, unsafe_allow_html=True)

        play_alarm()
        st.success("Alarm Finished 🔔")

# ----------------- MAIN -----------------
if st.session_state.logged_in:
    timer_app()
else:
    login()