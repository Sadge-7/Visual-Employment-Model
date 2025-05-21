import streamlit as st
from job_visualizations import show_trends, show_interest_fit, show_salaries, show_3d_match, grab_sample_data

st.set_page_config(page_title="Career Buddy", layout="centered")
st.title("🎉 Welcome to Your Career Buddy!")
st.markdown("""
Hey there! This little AI buddy is here to help you figure out what jobs fit your vibe and skills.  
Choose your interests on the left, and let's explore what the market looks like for you!
""")

# Sidebar for input from the user
st.sidebar.header("🎯 Pick Your Interests & Level")
choices = ["AI", "Finance", "Education", "Healthcare", "Manufacturing"]
user_picks = st.sidebar.multiselect("What are you into?", choices, default=["AI", "Finance"])

interest_levels = []
for area in user_picks:
    level = st.sidebar.slider(f"How much do you like {area}?", 0.0, 1.0, 0.7, 0.05)
    interest_levels.append(level)

if st.sidebar.button("Show Me My Matches!"):
    st.subheader("📈 Industry Demand over the Years")
    data = grab_sample_data()
    show_trends(data)

    st.subheader("💡 How Your Interests Stack Up")
    show_interest_fit(user_picks, interest_levels)

    st.subheader("💰 Jobs & What They Pay")
    sample_jobs = ["Data Analyst", "Financial Planner", "AI Engineer"][:len(user_picks)]
    sample_salaries = [15000, 13000, 17000][:len(user_picks)]
    show_salaries(sample_jobs, sample_salaries)

    st.subheader("🚀 3D Overview of Your Career Fit")
    skill_levels = [min(1.0, lvl + 0.1) for lvl in interest_levels]
    demand_estimates = [1.0 - abs(lvl - 0.75) for lvl in interest_levels]
    show_3d_match(interest_levels, skill_levels, demand_estimates)

else:
    st.info("Select your interests and hit the button to get some career magic!")
