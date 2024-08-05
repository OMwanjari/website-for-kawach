import streamlit as st

# Set page config at the very beginning
st.set_page_config(page_title="Kawach - Women's Self Defense", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
            background-color: #333333;
            color: #FFFFFF;
        }
        .stApp {
            padding-top: 20px;
        }
        .page-title {
            color: #FFFFFF;
            text-align: center;
            padding: 20px 0;
        }
        .video-container, .weapon-container {
            background-color: #444444;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .video-title, .weapon-title {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .resources-header {
            color: #FFFFFF;
            padding-top: 20px;
            font-size: 24px;
            font-weight: bold;
        }
        .resources-text {
            color: #AAAAAA;
        }
        .footer {
            text-align: center;
            color: #AAAAAA;
            padding-top: 20px;
        }
        /* Responsive iframe */
        .video-container iframe {
            width: 100%;
            height: auto;
            aspect-ratio: 16/9;
        }
        @media (max-width: 768px) {
            .video-title, .weapon-title {
                font-size: 16px;
            }
            .resources-header {
                font-size: 20px;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Function to display the self defence techniques page
def self_defence_techniques():
    st.markdown("<h1 class='page-title'>Kawach</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='page-title' style='text-align: left;'>Self Defence Techniques</h2>", unsafe_allow_html=True)

    videos = [
        {"link": "https://www.youtube.com/embed/KVpxP3ZZtAc", "title": "5 Self-Defense Techniques for Women"},
        {"link": "https://www.youtube.com/embed/T7aNSRoDCmg", "title": "7 Essential Self-Defense Moves Every Woman Should Know"},
        {"link": "https://www.youtube.com/embed/Gx3_x6RH1J4", "title": "27 SELF-DEFENSE TRICKS FOR WOMEN"},
        {"link": "https://www.youtube.com/embed/k9Jn0eP-ZVg", "title": "SELF DEFENSE MOVES EVERY WOMAN SHOULD KNOW"},
        {"link": "https://www.youtube.com/embed/CH7DvnTNLuI", "title": "SELF-DEFENCE TECHNIQUES FOR WOMEN II 5-Minute Recovery Tips..."},
        {"link": "https://www.youtube.com/embed/0UqK3tfuu8Q", "title": "5 Self Defense Techniques Every Women Should Know I BeerBiceps..."},
    ]

    for video in videos:
        with st.container():
            st.markdown(f'<div class="video-container">', unsafe_allow_html=True)
            st.markdown(f'<p class="video-title">{video["title"]}</p>', unsafe_allow_html=True)
            st.markdown(f'<iframe src="{video["link"]}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="resources-header">Additional Resources</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="resources-text">
        Here are some additional resources for women's safety:
        <ul>
            <li>Local self-defense classes</li>
            <li>Women's safety apps</li>
            <li>Emergency contact information</li>
            <li>Community support groups</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer">
        ---
        Created with ❤️ using Streamlit | © 2024 Women's Safety Initiative
    </div>
    """, unsafe_allow_html=True)

# Function to display the self defence weapons page
def self_defence_weapons():
    st.markdown("<h1 class='page-title'>Kawach</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='page-title' style='text-align: left;'>Self Defence Weapons</h2>", unsafe_allow_html=True)

    weapons = [
        {"name": "Pepper Spray", "description": "A small canister of pepper spray can be used to deter attackers."},
        {"name": "Stun Gun", "description": "A stun gun delivers a high-voltage shock to incapacitate an attacker."},
        {"name": "Personal Alarm", "description": "A small device that emits a loud noise to attract attention."},
        {"name": "Tactical Pen", "description": "A sturdy pen that can be used for self-defense and writing."},
        {"name": "Keychain Weapon", "description": "A small, discreet weapon that can be attached to your keychain."},
        {"name": "Self-Defense Keychain", "description": "A keychain designed with a sharp point for self-defense."},
    ]

    for weapon in weapons:
        with st.container():
            st.markdown(f'<div class="weapon-container">', unsafe_allow_html=True)
            st.markdown(f'<p class="weapon-title">{weapon["name"]}</p>', unsafe_allow_html=True)
            st.markdown(f'<p>{weapon["description"]}</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="resources-header">Additional Resources</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="resources-text">
        Here are some additional resources for women's safety:
        <ul>
            <li>Local self-defense classes</li>
            <li>Women's safety apps</li>
            <li>Emergency contact information</li>
            <li>Community support groups</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer">
        ---
        Created with ❤️ using Streamlit | © 2024 Women's Safety Initiative
    </div>
    """, unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Self Defence Techniques", "Self Defence Weapons"])

# Check URL parameters for default page
query_params = st.query_params
url_page = query_params.get("page", ["Self Defence Techniques"])[0]

# Debugging
st.write(f"URL Parameter: {url_page}")
st.write(f"Sidebar Selection: {page}")

# Determine which page to show
if url_page == "Self Defence Techniques":
    self_defence_techniques()
elif url_page == "Self Defence Weapons":
    self_defence_weapons()
else:
    if page == "Self Defence Techniques":
        self_defence_techniques()
    elif page == "Self Defence Weapons":
        self_defence_weapons()
    else:
        st.write("Page not found. Use ?page=Self%20Defence%20Techniques or ?page=Self%20Defence%20Weapons in the URL.")
