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

    st.markdown("---")
    if st.button("🎯 Show Top Matched Candidates"):
        with st.spinner("🔍 Matching candidates from LinkedIn..."):
            time.sleep(2)
            st.markdown("### 👥 Top Matched Candidates")
            candidates = [
                {
                    "Name": "Rahul Sharma",
                    "Match": 92,
                    "Reason": "Owns a bike, 1.5 years of delivery experience in Bangalore, fluent in Kannada."
                },
                {
                    "Name": "Arjun Mehta",
                    "Match": 85,
                    "Reason": "2 years of experience, lives near Koramangala, familiar with local routes."
                }
            ]
            for c in candidates:
                st.markdown(f"**{c['Name']}** – Match Score: {c['Match']}%  \n> _{c['Reason']}_")

        st.markdown("---")
        if st.button("📲 Reach Out to Candidates"):
            with st.spinner("Starting AI-driven conversation on WhatsApp..."):
                time.sleep(2)
                st.markdown("### 💬 Sample AI Conversation")

                chat = [
                    ("AI", "Hi Rahul, a delivery job is available in your area. Are you interested?"),
                    ("Rahul", "Yes, I'm interested."),
                    ("AI", "Great! Do you own a bike and know the Rajajinagar area?"),
                    ("Rahul", "Yes to both."),
                    ("AI", "Perfect. Can you join in 2 days?"),
                    ("Rahul", "Yes, I can.")
                ]
                for speaker, msg in chat:
                    st.markdown(f"**{speaker}**: {msg}")
                st.success("✅ Candidate pre-screened and eligible")

            st.markdown("---")
            if st.button("📅 Confirm or Reschedule Interview"):
                with st.spinner("Fetching available time slots..."):
                    time.sleep(2)
                    st.markdown("### 🗓️ Interview Scheduling")

                    selected = st.radio("Choose a time slot:", ["Today 3 PM", "Today 5 PM", "Tomorrow 10 AM"])
                    custom_time = st.text_input("Or suggest a new time (e.g., Tomorrow 4 PM)", "")

                    if st.button("✅ Confirm Interview Time"):
                        time_slot = custom_time if custom_time else selected
                        with st.spinner("Notifying candidate..."):
                            time.sleep(2)
                            st.success(f"Interview confirmed at **{time_slot}**.")
                            st.markdown("🎉 AI has notified Rahul and sent a calendar invite.")
