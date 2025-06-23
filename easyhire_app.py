import streamlit as st

st.set_page_config(page_title="EasyHire AI", layout="centered")
st.title("🧠 EasyHire AI – SMB Hiring Assistant")
st.markdown("Hire in minutes. Just say what you need.")

user_input = st.text_input("Type your hiring need:", placeholder="e.g., Need a delivery boy with bike in Bangalore")

if user_input:
    st.header("Step 2: AI Parsed Job Intent")

    parsed_output = {
        "Role Title": "Delivery Executive",
        "Location": "Bangalore",
        "Requirements": ["Owns bike", "Local knowledge"],
        "Language": "Any",
        "Experience": "0–2 years"
    }
    st.json(parsed_output)

    st.header("Step 3: AI-Matched Candidates")

    candidates = [
        {
            "Name": "Rahul Sharma",
            "Experience": "2 years",
            "Location": "Bangalore",
            "Skills": ["Bike", "Area Knowledge", "Customer Service"],
            "Match %": 92
        },
        {
            "Name": "Arjun Mehta",
            "Experience": "1.5 years",
            "Location": "Bangalore",
            "Skills": ["Bike", "Delivery"],
            "Match %": 85
        },
        {
            "Name": "Sameer Rao",
            "Experience": "3 years",
            "Location": "Mysore",
            "Skills": ["Logistics", "Driving"],
            "Match %": 73
        }
    ]

    for c in candidates:
        st.markdown(f"""
        #### {c['Name']} ({c['Match %']}% Match)
        - 📍 Location: {c['Location']}
        - 🧑‍💼 Experience: {c['Experience']}
        - 🛠️ Skills: {', '.join(c['Skills'])}
        """)
