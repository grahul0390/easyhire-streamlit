
import streamlit as st
import random

st.set_page_config(page_title="AI Recruiter for SMBs", layout="wide")

st.title("🤖 EasyHire AI – Your AI Recruiter for SMBs")
st.markdown("Just say what you need. We'll hire for you!")

# Summary Metrics
st.markdown("---")
st.subheader("📊 Hiring Progress Summary")

col1, col2, col3, col4 = st.columns(4)
col1.metric("🎯 Matched Candidates", "3")
col2.metric("📞 Engaged", "2")
col3.metric("✅ Shortlisted", "1")
col4.metric("📅 Interviews Scheduled", "1")
st.markdown("---")

# Role input
st.subheader("Step 1: Enter Hiring Need")
user_input = st.text_input("Type or speak your need:", "Need a delivery guy with bike in Bangalore")

# Parsed output
if user_input:
    st.subheader("Step 2: AI Parsed Job Intent")
    st.json({
        "Role Title": "Delivery Executive",
        "Location": "Bangalore",
        "Requirements": ["Owns bike", "Local knowledge"],
        "Language": "Any",
        "Experience": "0–2 years"
    })

# Candidate Matching
st.markdown("---")
st.header("Step 3: AI-Matched Candidates")

candidates = [
    {
        "Name": "Rahul Sharma",
        "Experience": "2 years",
        "Location": "Bangalore",
        "Skills": ["Bike", "Area Knowledge", "Customer Service"],
        "Match": 92
    },
    {
        "Name": "Arjun Mehta",
        "Experience": "1.5 years",
        "Location": "Bangalore",
        "Skills": ["Bike", "Delivery"],
        "Match": 85
    },
    {
        "Name": "Sameer Rao",
        "Experience": "3 years",
        "Location": "Mysore",
        "Skills": ["Logistics", "Driving"],
        "Match": 73
    }
]

for c in candidates:
    with st.expander(f"{c['Name']} – {c['Match']}% Match"):
        st.markdown(f"""
        - 📍 **Location:** {c['Location']}
        - 🧑‍💼 **Experience:** {c['Experience']}
        - 🛠️ **Skills:** {', '.join(c['Skills'])}
        """)
        if c["Match"] >= 85:
            st.success(f"✔️ Strong match: {c['Name']} has relevant experience and meets all key criteria.")
        else:
            st.warning(f"⚠️ {c['Name']} may not fully match: Some experience or skill gaps found.")

st.markdown("---")
st.header("Step 4: WhatsApp Engagement Preview")

engaged_candidates = [
    {
        "Name": "Rahul Sharma",
        "Chat": [
            ("AI", "Hi Rahul, a delivery job is available near you. Interested?"),
            ("Rahul", "Yes! I have a bike and can start tomorrow."),
            ("AI", "Great! Can you confirm if you know local areas?"),
            ("Rahul", "Yes, I know the area well.")
        ],
        "Screening": {
            "Own Bike": "✅",
            "Can Join in 2 Days": "✅",
            "Knows Area": "✅"
        }
    },
    {
        "Name": "Arjun Mehta",
        "Chat": [
            ("AI", "Hi Arjun, there’s a delivery job near you. Interested?"),
            ("Arjun", "What's the salary?"),
            ("AI", "Rs. 15,000/month. Can you join this week?"),
            ("Arjun", "Yes, possible.")
        ],
        "Screening": {
            "Own Bike": "✅",
            "Can Join in 2 Days": "✅",
            "Knows Area": "Somewhat"
        }
    }
]

for c in engaged_candidates:
    st.subheader(f"📲 Chat with {c['Name']}")
    for speaker, msg in c["Chat"]:
        if speaker == "AI":
            st.markdown(f"**🟢 AI:** _{msg}_")
        else:
            st.markdown(f"**🔵 {speaker}:** _{msg}_")

    st.markdown("🧾 **Pre-Screening Summary:**")
    for k, v in c["Screening"].items():
        st.markdown(f"- {k}: {v}")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button(f"✅ Shortlist {c['Name']}"):
            st.success(f"{c['Name']} has been shortlisted.")
    with col2:
        if st.button(f"❌ Reject {c['Name']}"):
            st.warning(f"{c['Name']} has been rejected.")
    with col3:
        if st.button(f"💬 Chat with {c['Name']}"):
            st.info(f"Chat started with {c['Name']} (simulated).")

    st.markdown("🗓️ **Schedule Interview:**")
    selected_slot = st.selectbox(
        f"Select time for interview with {c['Name']}",
        ["Today 3 PM", "Today 5 PM", "Tomorrow 10 AM", "Tomorrow 2 PM"],
        key=f"slot_{c['Name']}"
    )
    if st.button(f"📩 Confirm Interview with {c['Name']}", key=f"confirm_{c['Name']}"):
        st.success(f"Interview with {c['Name']} scheduled at {selected_slot}. Candidate notified via WhatsApp.")

    st.markdown("---")
