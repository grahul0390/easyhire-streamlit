
import streamlit as st

st.set_page_config(page_title="AI Recruiter for SMBs", layout="wide")

st.title("🤖 EasyHire AI – Your AI Recruiter for SMBs")
st.markdown("Just say what you need. We'll hire for you!")

st.markdown("---")
st.subheader("📊 Hiring Progress Summary")

col1, col2, col3, col4 = st.columns(4)
col1.metric("🎯 Matched", "0")
col2.metric("📞 Engaged", "0")
col3.metric("✅ Shortlisted", "0")
col4.metric("📅 Scheduled", "0")

st.markdown("---")
st.subheader("Step 1: Enter Hiring Need")

user_input = st.text_input("Type your hiring need:", "")

if user_input:
    st.success("Hiring need received.")
    st.markdown("---")
    st.subheader("Step 2: AI Parsed Job Intent")
    st.json({
        "Role Title": "Delivery Executive",
        "Location": "Bangalore",
        "Requirements": ["Owns bike", "Local knowledge"],
        "Language": "Any",
        "Experience": "0–2 years"
    })

    show_step3 = st.button("➡️ Show AI-Matched Candidates")

    if show_step3:
        st.markdown("---")
        st.subheader("Step 3: AI-Matched Candidates")
        candidates = [
            {"Name": "Rahul Sharma", "Match": 92},
            {"Name": "Arjun Mehta", "Match": 85},
            {"Name": "Sameer Rao", "Match": 73}
        ]
        for c in candidates:
            st.markdown(f"- **{c['Name']}** – Match Score: {c['Match']}%")

        show_step4 = st.button("➡️ Show WhatsApp Chat Previews")

        if show_step4:
            st.markdown("---")
            st.subheader("Step 4: WhatsApp Chat Engagement")

            chat = [
                ("AI", "Hi Rahul, job available near you. Interested?"),
                ("Rahul", "Yes! I can start tomorrow."),
                ("AI", "Do you know the area?"),
                ("Rahul", "Yes, very well.")
            ]
            for speaker, msg in chat:
                st.markdown(f"**{speaker}**: {msg}")

            st.markdown("✅ Screening Passed")

            show_step5 = st.button("➡️ Show Pre-Screen Summary & Interview")

            if show_step5:
                st.markdown("---")
                st.subheader("Step 5: Screening Summary & Actions")
                st.markdown("- Own Bike: ✅")
                st.markdown("- Knows Area: ✅")
                st.markdown("- Can Join in 2 Days: ✅")

                st.selectbox("📅 Select Interview Time", ["Today 3 PM", "Today 5 PM", "Tomorrow 10 AM"])
                st.button("📩 Confirm Interview")
