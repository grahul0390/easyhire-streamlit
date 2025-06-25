import streamlit as st
import time

# Set up the app
st.set_page_config(page_title="AI Recruiter for SMBs", layout="wide")
st.title("🤖 SMBHire AI – Your AI Recruiter for SMBs")
st.markdown("Just say what you need. We'll hire for you!")

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 1
if "user_input" not in st.session_state:
    st.session_state.user_input = ""
if "shortlisted" not in st.session_state:
    st.session_state.shortlisted = []
if "engaged" not in st.session_state:
    st.session_state.engaged = []

# Mock candidate data
candidates_data = [
    {
        "Name": "Rahul Sharma",
        "Match": 92,
        "Location": "Bangalore",
        "Experience": "2 years",
        "Skills": ["Owns bike", "Local knowledge", "Customer Service"],
    },
    {
        "Name": "Arjun Mehta",
        "Match": 85,
        "Location": "Bangalore",
        "Experience": "1.5 years",
        "Skills": ["Owns bike", "Delivery"],
    },
    {
        "Name": "Sameer Rao",
        "Match": 73,
        "Location": "Mysore",
        "Experience": "3 years",
        "Skills": ["Logistics", "Driving"],
    },
]

# Step 1: Get user input
if st.session_state.step == 1:
    st.subheader("📍 Step 1: Describe Your Hiring Need")
    st.session_state.user_input = st.text_input("Voice/Text Input:", " ")
    if st.session_state.user_input:
        if st.button("🔍 Parse Requirement with AI"):
            st.session_state.step = 2

# Step 2: Parsed requirement
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

# Step 3: Show candidates with actions
if st.session_state.step == 3:
    st.markdown("### 🎯 Top Matched Candidates")
    for i, c in enumerate(candidates_data):
        with st.container():
            st.markdown(f"#### 👤 {c['Name']} ({c['Match']}% Match)")
            st.markdown(f"- 📍 Location: {c['Location']}\n- 🧑‍💼 Experience: {c['Experience']}\n- 🛠️ Skills: {', '.join(c['Skills'])}")
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"✅ Shortlist {c['Name']}", key=f"shortlist_{i}"):
                    st.session_state.shortlisted.append(c)
                    st.success(f"{c['Name']} shortlisted.")
            with col2:
                if st.button(f"❌ Reject {c['Name']}", key=f"reject_{i}"):
                    st.warning(f"{c['Name']} rejected.")

    if st.session_state.shortlisted:
        if st.button("📲 Engage Shortlisted Candidates via WhatsApp"):
            st.session_state.engaged = st.session_state.shortlisted.copy()
            st.session_state.step = 4

# Step 4: Simulated conversation and screening
if st.session_state.step == 4:
    st.markdown("### 💬 AI Conversation with Candidates")
    for i, c in enumerate(st.session_state.engaged):
        with st.container():
            st.subheader(f"📲 {c['Name']}")
            chat = [
                ("AI", f"Hi {c['Name'].split()[0]}, we found a delivery job near you. Are you interested?"),
                (c['Name'], "Yes, I’m looking for something local."),
                ("AI", "Do you have your own bike?"),
                (c['Name'], "Yes, I do."),
                ("AI", "Can you join within 2 days?"),
                (c['Name'], "Yes."),
                ("AI", "Great! Do you know the local area well?"),
                (c['Name'], "Yes, very well."),
            ]
            for speaker, msg in chat:
                st.markdown(f"**{speaker}**: {msg}")

            st.markdown("**🧾 Pre-Screening Summary:**")
            st.markdown("- Has Bike: ✅\n- Can Join Quickly: ✅\n- Knows Local Area: ✅")

    if st.button("📅 Proceed to Interview Scheduling"):
        st.session_state.step = 5

# Step 5: Interview scheduling
if st.session_state.step == 5:
    st.markdown("### 🗓️ Schedule Interviews")
    for i, c in enumerate(st.session_state.engaged):
        with st.expander(f"Schedule Interview with {c['Name']}"):
            slot = st.selectbox("Select Time Slot", ["Today 3 PM", "Today 5 PM", "Tomorrow 10 AM", "Tomorrow 2 PM"], key=f"slot_{i}")
            if st.button(f"📩 Confirm Interview with {c['Name']}", key=f"confirm_{i}"):
                with st.spinner("Scheduling..."):
                    time.sleep(1)
                st.success(f"Interview with {c['Name']} scheduled at {slot}!")
                st.balloons()
