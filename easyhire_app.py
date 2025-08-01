import streamlit as st
import openai
import random

# Set your OpenAI API key here or in your environment
openai.api_key = st.secrets["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"]

# ----- MOCK CANDIDATE POOL ----- #
candidate_pool = [
    {
        "name": "Amit Kumar",
        "location": "Bangalore",
        "experience": 1,
        "skills": ["bike ownership", "local knowledge", "delivery"],
        "language": "Hindi",
    },
    {
        "name": "Priya Sharma",
        "location": "Bangalore",
        "experience": 2,
        "skills": ["bike ownership", "Google Maps", "customer service"],
        "language": "English",
    },
    {
        "name": "Rahul Verma",
        "location": "Mumbai",
        "experience": 1,
        "skills": ["delivery", "punctuality", "bike ownership"],
        "language": "Marathi",
    },
    {
        "name": "Sneha Reddy",
        "location": "Hyderabad",
        "experience": 3,
        "skills": ["local knowledge", "customer support", "bike ownership"],
        "language": "Telugu",
    },
    {
        "name": "Mohit Singh",
        "location": "Bangalore",
        "experience": 0,
        "skills": ["bike ownership", "delivery"],
        "language": "Hindi",
    },
    # Add more profiles as needed...
]

# ----- FUNCTIONS ----- #
def parse_job_requirement(requirement_text):
    prompt = f"""You are a helpful recruiter assistant. Parse the following hiring requirement into structured fields:
Role Title, Location, Required Skills, Language, Experience

Input: \"\"\"{requirement_text}\"\"\"
"""

    Output as JSON.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return eval(response["choices"][0]["message"]["content"].strip())

def match_candidates(parsed):
    matches = []
    for candidate in candidate_pool:
        score = 0
        if candidate["location"].lower() == parsed["Location"].lower():
            score += 1
        if parsed["Experience"] >= candidate["experience"]:
            score += 1
        skill_match = len(set(candidate["skills"]).intersection(set(parsed["Requirements"])))
        score += skill_match
        matches.append({"candidate": candidate, "score": score})
    matches.sort(key=lambda x: x["score"], reverse=True)
    return matches[:3]

def simulate_ai_chat(candidate, job):
    return f"""
    🤖 AI: Hi {candidate['name']}, we found a job opportunity as a {job['Role Title']} in {job['Location']} that matches your profile.

    🧑‍💼 {candidate['name']}: Sounds good! What are the details?

    🤖 AI: It requires {', '.join(job['Requirements'])}. Are you interested in exploring it?

    🧑‍💼 {candidate['name']}: Yes, I am.

    🤖 AI: Great. Can you do a 15-min call tomorrow at 11 AM?

    🧑‍💼 {candidate['name']}: Sure!

    ✅ AI has scheduled the interview for tomorrow at 11 AM.
    """

# ----- STREAMLIT UI ----- #
st.title("🧠 SMBHire AI Recruiter")
st.markdown("Automating hiring for small businesses with AI")

# Step 1: Recruiter input
requirement = st.text_area("Enter your hiring requirement (e.g., 'Need a delivery boy in Bangalore who owns a bike and knows the city. Experience 1-2 years')")

if requirement and st.button("🚀 Run AI Recruiter"):
    with st.spinner("Parsing job requirement with AI..."):
        parsed = parse_job_requirement(requirement)

    st.subheader("Step 1: AI-Parsed Job Intent")
    st.json(parsed)

    if st.button("🔍 Find Top Candidates"):
        with st.spinner("Matching candidates..."):
            top_matches = match_candidates(parsed)

        st.subheader("Step 2: Top Matches")
        for m in top_matches:
            c = m["candidate"]
            st.markdown(f"**{c['name']}** — {c['location']} — {c['experience']} yrs exp")
            st.markdown(f"🧩 Skills match: {', '.join(c['skills'])}")
            st.markdown(f"🤝 Match Score: {m['score']}/5")

        if st.button("💬 Start AI Outreach"):
            st.subheader("Step 3: AI-to-Candidate Conversation")
            for m in top_matches:
                convo = simulate_ai_chat(m["candidate"], parsed)
                with st.expander(f"Conversation with {m['candidate']['name']}"):
                    st.markdown(convo)

            if st.button("📅 Confirm Interview or Suggest New Time"):
                time_choice = st.radio("Confirm or Reschedule?", ["Confirm 11 AM", "Suggest New Time"])
                if time_choice == "Confirm 11 AM":
                    st.success("✅ AI confirms the interview with all candidates at 11 AM.")
                else:
                    new_time = st.text_input("Enter new time (e.g., 3 PM tomorrow)")
                    if new_time:
                        st.success(f"✅ AI reschedules interview and confirms with all candidates for {new_time}.")
