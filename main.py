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

# Project data structure
projects = [
    {
        "name": "CSVParser",
        "tech": ["Java", "HTML"],
        "description": "A JavaFX desktop application that generates printable PDF vouchers from CSV data. It reads voucher codes from CSV files and combines them with customizable parameters to produce formatted, multi-card PDF documents.",
        "images": [
            "resources/CSVParser1.png",
            "resources/CSVParser2.png"
        ],
        "github": "https://github.com/DMKuZu/CSVParser",
        "collaborators": [{"name": "Kintoyyy", "github": "https://github.com/Kintoyyy"}]
    },
    {
        "name": "PPPoE Management System",
        "tech": ["Java", "MikroTik"],
        "description": "A JavaFX application that enables administrators to manage PPPoE user accounts, monitor connections, and assign IP addresses over a shared Ethernet network. Integrates with MikroTik routers to handle authentication and connection management.",
        "images": [
            "resources/PPPoE1.png",
            "resources/PPPoE2.png",
            "resources/PPPoE3.png",
        ],
        "github": "Private repo",
        "collaborators": [{"name": "Kintoyyy", "github": "https://github.com/Kintoyyy"},{"name": "jojseph", "github": "https://github.com/jojseph"}, {"name": "Naweeeeeh", "github": "https://github.com/Naweeeeeeh"}, {"name": "IgnisFrostBurn", "github": "https://github.com/IgnisFrostBurn"}]
    },
    {
        "name": "Dunzo",
        "tech": ["Django", "React", "TailwindCSS"],
        "description": "A task manager web application similar to monday.com featuring project management, calendar functionality, and user management. Built with a Django REST backend and a React frontend using Tailwind CSS.",
        "images": [
            "resources/dunzo1.png",
        ],
        "github": "Private repo",
        "collaborators": [{"name": "jojseph", "github": "https://github.com/jojseph"},{"name": "Joryuoo", "github": "https://github.com/Joryuoo"},{"name": "Fay-V", "github": "https://github.com/Fay-V"},{"name": "Libron-ChristianNeil", "github": "https://github.com/Libron-ChristianNeil"}]
    },
    {
        "name": "NavCit",
        "tech": ["SpringBoot", "Java", "React"],
        "description": "An interactive map application for the Cebu Institute of Technology - University campus. Navigate buildings, view locations, and explore campus facilities with an intuitive web interface.",
        "images": [
            "resources/navcit1.png",
            "resources/navcit2.png",
            "resources/navcit3.png"
        ],
        "github": "Private repo",
        "collaborators": [{"name": "jojseph", "github": "https://github.com/jojseph"},{"name": "Joryuoo", "github": "https://github.com/Joryuoo"},{"name": "Beansman", "github": "https://github.com/Beansman"},{"name": "Pallu", "github": "https://github.com/Pallu"}]
    },
    {
        "name": "AgarthaTech",
        "tech": ["Next.js", "Solidity"],
        "description": " A trustless, decentralized legal escrow service binding Philippine digital agreements with blockchain-enforced payments. Web3 dApp built with Next.js/React and Solidity smart contracts deployed on Polkadot EVM Testnet.",
        "images": [
            "resources/agarthatech1.png",
            "resources/agarthatech2.png",
            "resources/agarthatech3.png",
            "resources/agarthatech4.png",
            "resources/agarthatech5.png",
        ],
        "github": "https://github.com/DMKuZu/Agartha-Polkadot",
        "collaborators": [{"name": "Beansman", "github": "https://github.com/Beansman"},{"name": "IgnisFrostBurn", "github": "https://github.com/IgnisFrostBurn"}]
    }
]

# Render projects as expandable sections
for project in projects:
    with st.expander(f"📌 **{project['name']}**", expanded=False):
        # Tech Stack Tags
        tech_tags = ''.join([f'<span class="tech-tag">{tech}</span>' for tech in project['tech']])
        st.markdown(f"<div>{tech_tags}</div>", unsafe_allow_html=True)

        # Description
        st.write(project['description'])

        # Images with carousel
        if project['images']:
            carousel_key = f"carousel_{project['name']}"
            if carousel_key not in st.session_state:
                st.session_state[carousel_key] = 0

            # Display current image
            st.image(project['images'][st.session_state[carousel_key]], use_container_width=True)

            # Carousel controls
            if len(project['images']) > 1:
                btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 1])
                with btn_col1:
                    if st.button("◀ Prev", key=f"prev_{project['name']}"):
                        st.session_state[carousel_key] = (st.session_state[carousel_key] - 1) % len(project['images'])
                        st.rerun()
                with btn_col2:
                    st.write(f"<div style='text-align: center; color: #888;'>{st.session_state[carousel_key] + 1} / {len(project['images'])}</div>", unsafe_allow_html=True)
                with btn_col3:
                    if st.button("Next ▶", key=f"next_{project['name']}"):
                        st.session_state[carousel_key] = (st.session_state[carousel_key] + 1) % len(project['images'])
                        st.rerun()

        # GitHub Link
        st.markdown(f"🔗 [View on GitHub]({project['github']})")

        # Collaborators
        if project['collaborators']:
            st.write("**In Collaboration with:**")
            for collab in project['collaborators']:
                st.markdown(f"[{collab['name']}]({collab['github']})")

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
            <i class="fa-brands fa-github social-icon"></i> Follow on GitHub
        </a>
        <a href="https://linkedin.com/in/jwtabada" target="_blank" class="social-link">
            <i class="fa-brands fa-linkedin social-icon"></i> Follow on Linkedin
        </a>
        <br>
        <a href="mailto:john.winston.tabada@gmail.com" class="social-link">
            <i class="fa-solid fa-envelope social-icon email-icon"></i> john.winston.tabada@gmail.com
        </a>
    """, unsafe_allow_html=True)