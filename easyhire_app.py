
import streamlit as st
import time

st.set_page_config(page_title="AI Recruiter for SMBs", layout="wide")

st.title("🤖 EasyHire AI – Your AI Recruiter for SMBs")
st.markdown("Just say what you need. We'll hire for you!")

st.markdown("---")
st.subheader("📍 Step 1: Describe Your Hiring Need")

user_input = st.text_input("Voice/Text Input:", "")

if user_input:
    st.success("Received: " + user_input)
    with st.spinner("🤖 Parsing your requirement..."):
        time.sleep(2)
        st.markdown("### ✅ AI Parsed Job Intent")
        st.json({
            "Role Title": "Delivery Executive",
            "Location": "Bangalore",
            "Requirements": ["Owns bike", "Local knowledge"],
            "Language": "Any",
            "Experience": "0–2 years"
        })

    with st.spinner("🔍 Matching candidates from LinkedIn..."):
        time.sleep(2)
        st.markdown("### 🎯 Top Matched Candidates")
        candidates = [
            {"Name": "Rahul Sharma", "Match": 92},
            {"Name": "Arjun Mehta", "Match": 85},
            {"Name": "Sameer Rao", "Match": 73}
        ]
        for c in candidates:
            st.markdown(f"- **{c['Name']}** – Match Score: {c['Match']}%")

    with st.spinner("📲 Engaging candidates via WhatsApp..."):
        time.sleep(2)
        st.markdown("### 💬 Candidate Conversations")
        chat = [
            ("AI", "Hi Rahul, job available near you. Interested?"),
            ("Rahul", "Yes! I can start tomorrow."),
            ("AI", "Do you know the area?"),
            ("Rahul", "Yes, very well.")
        ]
        for speaker, msg in chat:
            st.markdown(f"**{speaker}**: {msg}")
        st.success("✅ Screening passed.")

    with st.spinner("📅 Scheduling Interview..."):
        time.sleep(2)
        st.markdown("### 🗓️ Interview Confirmed")
        st.markdown("- **Candidate:** Rahul Sharma")
        st.markdown("- **Time:** Today at 3 PM")
        st.markdown("- **Mode:** Phone call")
        st.balloons()
        st.success("🎉 Candidate successfully scheduled for interview!")
