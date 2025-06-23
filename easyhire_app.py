
import streamlit as st

# Simulated response from Step 2: AI Parsed Job Intent
parsed_intent = {
    "Role Title": "Delivery Executive",
    "Location": "Bangalore",
    "Requirements": ["Owns bike", "Local knowledge"],
    "Language": "Any",
    "Experience": "0–2 years"
}

# Simulated engaged candidates (Step 4 result)
engaged_candidates = [
    {
        "Name": "Ravi Kumar",
        "Reply": "Yes, I’m interested and have my own bike.",
        "Screening": {
            "Has bike": "Yes",
            "Knows local area": "Yes",
            "Available for full-time": "Yes"
        }
    },
    {
        "Name": "Anil Verma",
        "Reply": "Can join immediately. I live in Koramangala.",
        "Screening": {
            "Has bike": "Yes",
            "Knows local area": "Partial",
            "Available for full-time": "Yes"
        }
    }
]

st.title("🧠 EasyHire AI – SMB Hiring Assistant")

st.header("Step 2: AI Parsed Job Intent")
st.json(parsed_intent)

st.header("Step 4: Auto-Engaged Candidates")

if "hired_candidates" not in st.session_state:
    st.session_state["hired_candidates"] = []

for c in engaged_candidates:
    with st.container():
        st.subheader(f"📲 {c['Name']}")
        st.markdown(f"💬 **Reply:** _{c['Reply']}_")

        st.markdown("🧾 **Pre-Screening Summary:**")
        for question, answer in c["Screening"].items():
            st.markdown(f"- **{question}**: {answer}")

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

        st.markdown("🗓️ **Schedule Interview:**")
        selected_slot = st.selectbox(
            f"Select time for interview with {c['Name']}",
            ["Today 3 PM", "Today 5 PM", "Tomorrow 10 AM", "Tomorrow 2 PM"],
            key=f"slot_{c['Name']}"
        )
        if st.button(f"📩 Confirm Interview with {c['Name']}", key=f"confirm_{c['Name']}"):
            st.success(f"Interview with {c['Name']} scheduled at {selected_slot}. Candidate notified via WhatsApp.")

        if st.button(f"🎉 Mark {c['Name']} as Hired", key=f"hired_{c['Name']}"):
            st.success(f"🎉 {c['Name']} marked as hired!")
            st.session_state["hired_candidates"].append(c['Name'])

            feedback = st.text_area(
                f"Optional: Share feedback on {c['Name']}’s interview or hiring experience",
                key=f"feedback_{c['Name']}"
            )
            if feedback:
                st.info("✅ Feedback recorded. Thank you!")

        st.markdown("---")

if st.session_state["hired_candidates"]:
    st.header("📊 Final Hiring Summary")
    st.markdown(f"- 👤 {len(st.session_state['hired_candidates'])} candidate(s) hired:")
    for name in st.session_state["hired_candidates"]:
        st.markdown(f"  - ✅ {name}")
    st.markdown("- 🕐 Avg time-to-hire: ~1.2 days (simulated)")
