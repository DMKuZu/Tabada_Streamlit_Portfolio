import streamlit as st

# Must be the first Streamlit command
st.set_page_config(page_title="Tabada Portfolio", layout="wide", page_icon="💻")

# --- CUSTOM CSS ---
# Injecting FontAwesome for icons and custom styles for tags and layout spacing
custom_css = """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
    /* Tech Stack Tags */
    .tech-tag {
        display: inline-block;
        border: 1px solid #E0E0E0;
        border-radius: 15px;
        padding: 4px 12px;
        margin-right: 8px;
        margin-bottom: 10px;
        font-size: 14px;
        font-weight: 500;
        background-color: transparent;
        transition: 0.3s ease;
    }
    .tech-tag:hover {
        border-color: #B22222; /* Red accent on hover */
        color: #B22222;
    }
    /* Social Links */
    .social-link {
        text-decoration: none;
        color: #E0E0E0;
        font-size: 16px;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        transition: 0.2s ease;
    }
    .social-link:hover {
        color: #B22222;
    }
    .social-icon {
        width: 30px;
        font-size: 20px;
        color: #5555ff; /* Matches the blueish tint in your wireframe icons */
    }
    .email-icon { color: #8a8a8a; }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- TOP SECTION: PROFILE ---
col1, col2 = st.columns([1, 3])

with col1:
    # Replace with your actual image path
    st.image("resources/face.jpeg", width=250)

with col2:
    st.title("John Winston Tabada")
    st.write("""
    I'm a 3rd year Computer Science student of Cebu Institute of Technology - University. 
    Not a lot to showcase just yet but eager enough to put more in. Other than vibe coding, 
    I enjoy exploring the great outdoors.
    """)

st.markdown("---")

# --- MIDDLE SECTION: PROJECTS ---
st.header("Projects")

p_col1, p_col2 = st.columns([1.5, 2])

with p_col1:
    # Native Streamlit Image Carousel Workaround using Session State
    if 'img_index' not in st.session_state:
        st.session_state.img_index = 0
        
    # Placeholder images for your CSVParser project
    project_images = [
        "https://via.placeholder.com/600x400.png?text=CSVParser+Image+1",
        "https://via.placeholder.com/600x400.png?text=CSVParser+Image+2",
        "https://via.placeholder.com/600x400.png?text=CSVParser+Image+3"
    ]
    
    st.image(project_images[st.session_state.img_index], use_container_width=True)
    
    # Carousel controls
    btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 1])
    with btn_col1:
        if st.button("◀ Prev"):
            st.session_state.img_index = (st.session_state.img_index - 1) % len(project_images)
            st.rerun()
    with btn_col2:
        st.write(f"<div style='text-align: center; color: #888;'>{st.session_state.img_index + 1} / {len(project_images)}</div>", unsafe_allow_html=True)
    with btn_col3:
        if st.button("Next ▶"):
            st.session_state.img_index = (st.session_state.img_index + 1) % len(project_images)
            st.rerun()

with p_col2:
    # Tech Stack Tags
    st.markdown("""
        <div>
            <span class="tech-tag">Java</span>
            <span class="tech-tag">HTML</span>
        </div>
    """, unsafe_allow_html=True)
    
    st.subheader("CSVParser")
    st.write("""
    A simple JavaFX desktop application that generates printable PDF vouchers from CSV data. 
    It reads voucher codes from CSV files and combines them with customizable parameters to produce 
    formatted, multi-card PDF documents.
    """)
    
    st.write("**In Collaboration with:**")
    # GitHub link to collaborator
    st.markdown("[Kintoyyy](https://github.com/Kintoyyy) *(GitHub Profile)*")

st.markdown("---")

# --- BOTTOM SECTION: CONTACT INFO ---
st.header("Contact Information")

c_col1, c_col2 = st.columns([1, 1])

with c_col1:
    st.write("Let's get in touch! Feel free to contact me through my social links.")

with c_col2:
    # Social Links using FontAwesome icons mapping to your wireframe
    st.markdown("""
        <a href="https://github.com/DMKuZu" target="_blank" class="social-link">
            <i class="fa-brands fa-github social-icon" style="color: #E1306C;"></i> Follow on GitHub
        </a>
        <a href="https://linkedin.com/in/jwtabada" target="_blank" class="social-link">
            <i class="fa-brands fa-linkedin social-icon" style="color: #0077b5;"></i> Follow on Linkedin
        </a>
        <br>
        <a href="mailto:john.winston.tabada@gmail.com" class="social-link">
            <i class="fa-solid fa-envelope social-icon email-icon"></i> john.winston.tabada@gmail.com
        </a>
    """, unsafe_allow_html=True)