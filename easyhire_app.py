import streamlit as st
import random
import time
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key securely
openai.api_key = os.getenv("OPENAI_API_KEY")

# Dummy candidate pool
CANDIDATES = [
    {"name": "Ravi Kumar", "location": "Bangalore", "skills": ["delivery", "bike", "local knowledge"], "experience": "1 year"},
    {"name": "Pooja Reddy", "location": "Hyderabad", "skills": ["bike", "communication", "delivery"], "experience": "2 years"},
    {"name": "Amit Sharma", "location": "Delhi", "skills": ["sales", "cold calling", "CRM"], "experience": "3 years"},
    {"name": "Neha Verma", "location": "Mumbai", "skills": ["telecalling", "data entry", "MS Excel"], "experience": "1.5 years"},
    {"name": "Rajesh Iyer", "location": "Chennai", "skills": ["delivery", "local knowledge"], "experience": "1 year"},
    {"name": "Sneha Das", "location": "Bangalore", "skills": ["retail", "POS", "customer handling"], "experience": "2.5 years"},
    {"name": "Ankit Patel", "location": "Ahmedabad", "skills": ["bike", "delivery", "maps"], "experience": "6 months"},
    {"name": "Shreya Nair", "location": "Mumbai", "skills": ["calling", "coordination"], "experience": "2 years"},
    {"name": "Deepak Choudhary", "location": "Bangalore", "skills": ["delivery", "bike", "local knowledge", "communication"], "experience": "1.5 years"},
    {"name": "Meera Joshi", "location": "Pune", "skills": ["data entry", "back office", "Excel"], "experience": "1 year"},
]

# Function to simulate AI parsing of job intent
from openai import OpenAI

client = OpenAI()

def parse_job_intent(requirement_text):
    prompt = f"""
Extract structured hiring intent from the following requirement:

Input: \"\"\"{requirement_text}\"\"\"

Format:
{{
    "Role Title": <string>,
    "Location": <string>,
    "Requirements": [<list of required skills or attributes>],
    "Language": <string>,
    "Experience": <string>
}}
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert recruiter assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=300
    )
    parsed = response.choices[0].message.content.strip()
    return eval(parsed)

# Function to match candidates
def match_candidates(job):
    matches = []
    for candidate in CANDIDATES:
        score = 0
        if candidate["location"].lower() == job["Location"].lower():
            score += 1
        skill_overlap = set(candidate["skills"]).intersection(set(job["Requirements"]))
        score += len(skill_overlap)
        if score >= 2:
            matches.append((candidate, score))
    matches.sort(key=lambda x: x[1], reverse=True)
    return [m[0] for m in matches[:3]]

# Function to generate explanation
def generate_explanation(candidate, job):
    overlap = set(candidate["skills"]).intersection(set(job["Requirements"]))
    return f"{candidate['name']} is a good fit because they have {', '.join(overlap)} and are based in {candidate['location']}."

# Sample conversation
def get_sample_conversation(candidate, job):
    return [
        f"AI: Hi {candidate['name']}, we found a job opportunity as a {job['Role Title']} in {job['Location']} that matches your profile.",
        "AI: Would you like to learn more or proceed with the application?",
        f"{candidate['name']}: Yes, I'm interested!",
        "AI: Great! Can you confirm your availability for an interview tomorrow at 3 PM?",
        f"{candidate['name']}: That works for me.",
        "AI: Interview confirmed. You'll receive details shortly."
    ]

# Streamlit App
st.title("SMBHire AI Recruiter")

# Step 1: Input
requirement_text = st.text_area("Step 1: Enter your hiring requirement")

if st.button("Submit Requirement"):
    with st.spinner("Parsing job intent using AI..."):
        job = parse_job_intent(requirement_text)
        st.success("AI Parsed Job Intent")
        st.json(job)

    if st.button("Find Top Matched Candidates"):
        with st.spinner("Matching candidates..."):
            candidates = match_candidates(job)
            st.subheader("Top Matched Candidates")
            for candidate in candidates:
                explanation = generate_explanation(candidate, job)
                st.markdown(f"**{candidate['name']}** ({candidate['experience']} experience)")
                st.markdown(f"Location: {candidate['location']}")
                st.markdown(f"Skills: {', '.join(candidate['skills'])}")
                st.info(explanation)

                if st.button(f"Initiate Conversation with {candidate['name']}", key=candidate['name']):
                    conversation = get_sample_conversation(candidate, job)
                    for line in conversation:
                        st.write(line)

                    if st.button(f"Reschedule Interview with {candidate['name']}", key=f"resched_{candidate['name']}"):
                        st.write(f"AI: Okay, please suggest a new time.")
                        st.write(f"{candidate['name']}: Tomorrow at 5 PM works for me.")
                        st.write("AI: Noted. Rescheduled. You will receive an updated calendar invite.")
