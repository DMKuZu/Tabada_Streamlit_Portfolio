import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="My Portfolio", layout="wide", page_icon="🌐")

# Load animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Intro section
with st.container():
    left_col, right_col = st.columns([1, 3])

    with left_col:
        st.image("face.jpeg", caption="John Winston Tabada", width=300)
    
    with right_col:
        st.subheader("Hi, I'm John Winston W. Tabada👋")
        st.title("A 3rd Year Computer Science Student of CIT-U")
        st.write("I develop Programs and Web Applications mainly using Java and Python.")
        st.write("[Check out my GitHub >](https://github.com/DMKuZu)")

# Overvuiew section
with st.container():
    left_column, right_column = st.columns(2)

    with left_column:
        with st.container():
            st.header("About Me")
            st.write(
                """
                I enjoy playing Valorant and Genshin Impact during my free time.
                From time to time, I also like to read manga and light novels.
                Lately I've been studying about AI and Cloud Computing.
                Slowly Building up experience for the future.
                """
            )
            st.image("https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif", width=300)

    with right_column:
        with st.container():
            lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_jcikwtux.json")
            st_lottie(lottie_coding, width=300, key="coding")
            st.header("What I Do")
            st.write(
                """
                - Create Figma Prototypes  
                - Develop web applications using Java and Python  
                - Design mobile apps with Kotlin
                - Build Programs in C#
                """
            )

# Skills in Card View
st.header("My Skills")
skills = [
    {
        "title": "Python",
        "text": "50% proficiency",
        "image": "https://www.python.org/static/community_logos/python-logo.png"
    },
    {
        "title": "Java",
        "text": "70% proficiency",
        "image": "https://upload.wikimedia.org/wikipedia/en/3/30/Java_programming_language_logo.svg"
    },
    {
        "title": "Kotlin",
        "text": "30% proficiency",
        "image": "https://upload.wikimedia.org/wikipedia/commons/7/74/Kotlin_Icon.png"
    },
    {
        "title": "Figma",
        "text": "80% proficiency",
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/33/Figma-logo.svg"
    },
    {
        "title": "C++",
        "text": "30% proficiency",
        "image": "https://upload.wikimedia.org/wikipedia/commons/1/18/ISO_C%2B%2B_Logo.svg"
    },
    {
        "title": "C#",
        "text": "30% proficiency",
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/4f/Csharp_Logo.png"
    }
]
num_cols = 3
rows = [skills[i:i + num_cols] for i in range(0, len(skills), num_cols)]

for row in rows:
    cols = st.columns(num_cols)
    for col, skill in zip(cols, row):
        with col:
            st.markdown(f"""
            <div style="
                background-color: transparent;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                text-align: center;
                padding: 20px;
                margin: 10px;
                height: 300px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;">
                <img src="{skill['image']}" 
                     style="width:100%; height:160px; object-fit:contain; border-radius:8px;">
                <h4 style="margin:10px 0 0 0;">{skill['title']}</h4>
                <p style="color:#555; font-size:14px;">{skill['text']}</p>
            </div>
            """, unsafe_allow_html=True)

# Tabs for Projects
st.header("Projects Showcase")
tab1, tab2, tab3 = st.tabs(["Random Projects 📚", "Web Apps 🌐", "Mobile Apps 📱"])

with tab1:
    st.write("### CSV Parser in Java")
    st.write("A tool for parsing and analyzing CSV files built with Java.")

with tab2:
    st.write("### NavCit")
    st.write("A web app made in SpringBoot. It is an interactive map for CIT-U campus.")
    st.write("### Dunzo")
    st.write("A web app made in Django. It is a task management application.")

with tab3:
    st.write("### Vetality Shop")
    st.write("A mobile ecommerce app for agrivet products built with Kotlin.")
