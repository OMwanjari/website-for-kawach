import streamlit as st

# Custom CSS for a responsive and minimalistic look
st.markdown("""
<style>
    .stApp {
        color: #FFFFFF;
    }
    h1 {
        color: #FFFFFF;
        text-align: center;
        padding: 10px 0;
        font-size: 36px;
    }
    h2 {
        color: #AAAAAA;
        text-align: left;
        padding: 5px 0;
        font-size: 24px;
    }
    .video-container {
        background-color: #333333;
        border-radius: 5px;
        padding: 5px;
        margin-bottom: 5px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        max-width: 100%;
    }
    .video-title {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 10px;
        color: #FFFFFF;
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
        .video-title {
            font-size: 16px;
        }
        .resources-header {
            font-size: 20px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Main heading
st.markdown("<h1>Kawach</h1>", unsafe_allow_html=True)
# Subheading
st.markdown("<h2>Self Defence Techniques</h2>", unsafe_allow_html=True)

# List of YouTube video links and titles
videos = [
    {"link": "https://www.youtube.com/embed/KVpxP3ZZtAc", "title": "5 Self-Defense Techniques for Women"},
    {"link": "https://www.youtube.com/embed/T7aNSRoDCmg", "title": "7 Essential Self-Defense Moves Every Woman Should Know"},
    {"link": "https://www.youtube.com/embed/Gx3_x6RH1J4", "title": "27 SELF-DEFENSE TRICKS FOR WOMEN"},
    {"link": "https://www.youtube.com/embed/k9Jn0eP-ZVg", "title": "SELF DEFENSE MOVES EVERY WOMAN SHOULD KNOW"},
    {"link": "https://www.youtube.com/embed/CH7DvnTNLuI", "title": "SELF-DEFENCE TECHNIQUES FOR WOMEN II 5-Minute Recovery Tips..."},
    {"link": "https://www.youtube.com/embed/0UqK3tfuu8Q", "title": "5 Self Defense Techniques Every Women Should Know I BeerBiceps..."},
]

# Display videos
for video in videos:
    with st.container():
        st.markdown(f'<div class="video-container">', unsafe_allow_html=True)
        st.markdown(f'<p class="video-title">{video["title"]}</p>', unsafe_allow_html=True)
        st.markdown(f'<iframe src="{video["link"]}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Add a section for additional resources
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

# Add a footer
st.markdown("""
<div class="footer">
    | © 2024 Kawach Women Safety App
</div>
""", unsafe_allow_html=True)
