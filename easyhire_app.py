import streamlit as st
import time

# Set up the app
st.set_page_config(page_title="AI Recruiter for SMBs", layout="wide")
st.title("🤖 EasyHire AI – Your AI Recruiter for SMBs")
st.markdown("Just say what you need. We'll hire for you!")

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 1
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Step 1: Get user input
if st.session_state.step == 1:
    st.subheader("📍 Step 1: Describe Your Hiring Need")
    st.session_state.user_input = st.text_input("Voice/Text Input:", "")
    if st.session_state.user_input:
        if st.button("🔍 Parse Requirement with AI"):
            st.session_state.step = 2

# Step 2: AI Parses the requirement
if st.session_state.step == 2:
    with st.spinner("🤖 Parsing your requirement..."):
        time.sleep(2)
    st.markdown("### ✅ AI Parsed Job Intent")
    parsed_output = {
        "Role Title": "Delivery Executive",
        "Location": "Bangalore",
        "Requirements": ["Owns bike", "Local knowledge"],
        "Language": "Any",
        "Experience": "0–2 years"
    }
    st.json(parsed_output)
    if st.button("🎯 Find Matching Candidates"):
        st.session_state.step = 3

# Step 3: Show matched candidates
if st.session_state.step == 3:
    with st.spinner("🔍 Matching candidates from LinkedIn..."):
        time.sleep(2)
    st.markdown("### 🎯 Top Matched Candidates")
    st.session_state.candidates = [
        {"Name": "Rahul Sharma", "Match": 92},
        {"Name": "Arjun Mehta", "Match": 85},
        {"Name": "Sameer Rao", "Match": 73}
    ]
    for c in st.session_state.candidates:
        st.markdown(f"**👤 {c['Name']}** – Match Score: **{c['Match']}%**")
    if st.button("📲 Engage Top Candidate via WhatsApp"):
        st.session_state.step = 4

# Step 4: Simulate WhatsApp conversation
if st.session_state.step == 4:
    with st.spinner("📲 Engaging candidates via WhatsApp..."):
        time.sleep(2)
    st.markdown("### 💬 Candidate Conversation with Rahul Sharma")
    chat = [
        ("AI", "Hi Rahul, job available near you. Interested?"),
        ("Rahul", "Yes! I can start tomorrow."),
        ("AI", "Do you know the area?"),
        ("Rahul", "Yes, very well.")
    ]
    for speaker, msg in chat:
        st.markdown(f"**{speaker}**: {msg}")
    st.success("✅ Screening passed.")
    if st.button("📅 Schedule Interview"):
        st.session_state.step = 5

# Step 5: Schedule interview
if st.session_state.step == 5:
    st.markdown("### 🗓️ Interview Scheduling")
    slot = st.selectbox("Select Interview Time", [
        "Today at 3 PM", "Today at 5 PM", "Tomorrow at 10 AM", "Tomorrow at 2 PM"
    ])
    if st.button("📩 Confirm Interview"):
        with st.spinner("Scheduling..."):
            time.sleep(2)
        st.markdown("### ✅ Interview Confirmed")
        st.markdown("- **Candidate:** Rahul Sharma")
        st.markdown(f"- **Time:** {slot}")
        st.markdown("- **Mode:** Phone call")
        st.balloons()
        st.success("🎉 Candidate successfully scheduled for interview!")
