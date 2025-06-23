import streamlit as st

# App setup
st.set_page_config(page_title="EasyHire AI", layout="centered")
st.title("🧠 EasyHire AI – SMB Hiring Assistant")
st.markdown("Hire in minutes. Just say what you need.")

# User input
user_input = st.text_input("Type your hiring need:", placeholder="e.g., Need a delivery boy with bike in Bangalore")

if user_input:
    # Step 2 – AI Parsing Simulation
    st.header("Step 2: AI Parsed Job Intent")
    parsed_output = {
        "Role Title": "Delivery Executive",
        "Location": "Bangalore",
        "Requirements": ["Owns bike", "Local knowledge"],
        "Language": "Any",
        "Experience": "0–2 years"
    }
    st.json(parsed_output)

    # Step 3 – Candidate Matching
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

    # Render candidate cards
    for c in candidates:
        with st.container():
            st.markdown(f"""
            #### {c['Name']} — {c['Match']}% Match
            - 📍 **Location:** {c['Location']}
            - 🧑‍💼 **Experience:** {c['Experience']}
            - 🛠️ **Skills:** {', '.join(c['Skills'])}
            """)
            st.markdown("---")

    # Step 4 – Auto-Engagement + WhatsApp Replies
    st.header("Step 4: WhatsApp Auto-Engagement & Replies")

    engaged_candidates = [
        {
            "Name": "Rahul Sharma",
            "Reply": "Hi, I’m interested. I have a bike and live in Koramangala.",
            "Screening": {
                "Has Bike?": "Yes",
                "Can Join Within 2 Days?": "Yes",
                "Knows Local Area?": "Yes"
            }
        },
        {
            "Name": "Arjun Mehta",
            "Reply": "Can I know the salary first?",
            "Screening": {
                "Has Bike?": "Yes",
                "Can Join Within 2 Days?": "No",
                "Knows Local Area?": "Somewhat"
            }
        }
    ]

   for c in engaged_candidates:
    with st.container():
        # ... your previous code ...
        
        st.subheader(f"📲 {c['Name']}")
        st.markdown(f"💬 **Reply:** _{c['Reply']}_")

        # Pre-screen answers
        st.markdown("🧾 **Pre-Screening Summary:**")
        for question, answer in c["Screening"].items():
            st.markdown(f"- **{question}**: {answer}")

        # Buttons for Shortlist / Reject / Chat
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button(f"✅ Shortlist {c['Name']}", key=f"shortlist_{c['Name']}"):
                st.success(f"{c['Name']} has been shortlisted.")
        with col2:
            if st.button(f"❌ Reject {c['Name']}", key=f"reject_{c['Name']}"):
                st.warning(f"{c['Name']} has been rejected.")
        with col3:
            if st.button(f"💬 Chat with {c['Name']}", key=f"chat_{c['Name']}"):
                st.info(f"Chat started with {c['Name']} (simulated).")

        # Interview Scheduling
        st.markdown("🗓️ **Schedule Interview:**")
        selected_slot = st.selectbox(
            f"Select time for interview with {c['Name']}",
            ["Today 3 PM", "Today 5 PM", "Tomorrow 10 AM", "Tomorrow 2 PM"],
            key=f"slot_{c['Name']}"
        )
        if st.button(f"📩 Confirm Interview with {c['Name']}", key=f"confirm_{c['Name']}"):
            st.success(f"Interview with {c['Name']} scheduled at {selected_slot}. Candidate notified via WhatsApp.")

        # 🏁 Hiring Confirmation
        if "hired_candidates" not in st.session_state:
            st.session_state["hired_candidates"] = []

        if st.button(f"🎉 Mark {c['Name']} as Hired", key=f"hired_{c['Name']}"):
            st.success(f"🎉 {c['Name']} marked as hired!")
            st.session_state["hired_candidates"].append(c['Name'])

            feedback = st.text_area(
                f"Optional: Share feedback on {c['Name']}’s interview or hiring experience",
                key=f"feedback_{c['Name']}"
            )
            if feedback:
                st.info("✅ Feedback recorded. Thank you!")

        st.markdown("---")  # separator between candidates


# Final Summary (after the for-loop)
if "hired_candidates" in st.session_state and st.session_state["hired_candidates"]:
    st.header("📊 Final Hiring Summary")
    st.markdown(f"- 👤 {len(st.session_state['hired_candidates'])} candidate(s) hired:")
    for name in st.session_state["hired_candidates"]:
        st.markdown(f"  - ✅ {name}")
    st.markdown("- 🕐 Avg time-to-hire: ~1.2 days (simulated)")



