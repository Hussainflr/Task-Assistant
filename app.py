import streamlit as st
from agents.orchestrator import run_multi_agent

# -----------------------------
# Session State
# -----------------------------
if "logs" not in st.session_state:
    st.session_state.logs = []

if "plan" not in st.session_state:
    st.session_state.plan = ""

if "work" not in st.session_state:
    st.session_state.work = ""

if "final" not in st.session_state:
    st.session_state.final = ""


# -----------------------------
# UI
# -----------------------------
st.title(" Multi-Agent Task Assistant")

user_input = st.text_input("Enter your task:")

if st.button("Run"):

    if not user_input:
        st.warning("Please enter a task")
    else:
        st.session_state.logs.clear()

        plan, work, final = run_multi_agent(
            user_input,
            st.session_state.logs
        )

        st.session_state.plan = plan
        st.session_state.work = work
        st.session_state.final = final


# -----------------------------
# Display
# -----------------------------
st.subheader(" Plan")
st.write(st.session_state.plan)

st.subheader("Execution")
st.write(st.session_state.work)

st.subheader("Final Answer")
st.write(st.session_state.final)

st.subheader("Logs")
for log in st.session_state.logs:
    st.text(log)