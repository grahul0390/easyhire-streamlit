import streamlit as st
import time

st.set_page_config(page_title="AI Recruiter for SMBs", layout="wide")

st.title("🤖 EasyHire AI – Your AI Recruiter for SMBs")
st.markdown("Just say what you need. We'll hire for you!")

st.markdown("---")
st.subheader("📍 Step 1: Describe Your Hiring Need")

user_input = st.text_input("Enter requirement (e.g., 'Need a delivery guy with bike in Bangalore')")

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
    if st.button("🎯 Show Matched Candidates"):
        with st.spinner("Matching candidates from LinkedIn..."):
            time.sleep(2)
            st.markdown("### 👥 Top Matched Candidates")
            candidates = [
                {
                    "Name": "Rahul Sharma",
                    "Match": 92,
                    "Suitability": "Owns bike, 1.5 yrs experience delivering in Bangalore, speaks Kannada, lives 2 km from job location."
                },
                {
                    "Name": "Arjun Mehta",
                    "Match": 85,
                    "Suitability": "Has bike, 2 yrs experience, lives in Koramangala, familiar with Rajajinagar area."
                }
            ]
            for c in candidates:
                st.markdown(f"**{c['Name']}** – Match Score: {c['Match']}%  \n> _{c['Suitability']}_")

        st.markdown("---")
        if st.button("📲 Initiate Candidate Outreach"):
            with st.spinner("Starting AI-driven WhatsApp/LinkedIn conversation..."):
                time.sleep(2)
                st.markdown("### 💬 Sample AI Conversation")
                chat = [
                    ("AI", "Hi Rahul! We have a delivery job in Rajajinagar. Interested?"),
                    ("Rahul", "Yes, sounds good."),
                    ("AI", "Do you own a bike and know the area well?"),
                    ("Rahul", "Yes, I have a bike and I live nearby."),
                    ("AI", "Great! Can you start within 2 days?"),
                    ("Rahul", "Absolutely."),
                    ("AI", "Perfect. Let’s schedule your interview.")
                ]
                for speaker, msg in chat:
                    st.markdown(f"**{speaker}**: {msg}")
                st.success("✅ Candidate qualified via AI pre-screening.")

            st.markdown("---")
            st.markdown("### 🗓️ Interview Scheduling Options")
            selected = st.radio("Choose a suggested interview slot:", ["Today 3 PM", "Today 5 PM", "Tomorrow 10 AM"])
            custom_time = st.text_input("Or propose a new time (e.g., Tomorrow 4 PM):")

            if st.button("✅ Confirm or Reschedule Interview"):
                final_time = custom_time if custom_time else selected
                with st.spinner("Reaching out to candidate to confirm new time..."):
                    time.sleep(2)
                    st.markdown(f"**AI**: Rahul, the recruiter has scheduled your interview at **{final_time}**. Please confirm.")
                    time.sleep(1.5)
                    st.markdown("**Rahul**: Confirmed! Looking forward to it.")
                    st.success(f"🎉 Interview confirmed for {final_time}")
