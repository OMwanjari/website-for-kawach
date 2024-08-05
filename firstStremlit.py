import streamlit as st

# Custom CSS for a responsive and beautiful mobile-friendly look
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    
    body {
        font-family: 'Roboto', sans-serif;
        background-color: #1E1E1E;
        color: #FFFFFF;
    }
    .stApp {
        max-width: 100%;
        padding: 10px;
    }
    h1 {
        color: #FF69B4;
        text-align: center;
        padding: 20px 0;
        font-size: 36px;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    h2 {
        color: #AAAAAA;
        text-align: left;
        padding: 15px 0;
        font-size: 24px;
        font-weight: 400;
    }
    .video-container {
        background: linear-gradient(145deg, #2a2a2a, #333333);
        border-radius: 15px;
        padding: 15px;
        margin: 20px 0;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }
    .video-title {
        font-size: 18px;
        font-weight: 500;
        margin-bottom: 15px;
        color: #FF69B4;
    }
    .resources-header {
        color: #FF69B4;
        padding: 25px 0 15px;
        font-size: 24px;
        font-weight: 700;
    }
    .resources-text {
        color: #CCCCCC;
        padding: 0 10px;
        font-size: 16px;
        line-height: 1.6;
    }
    .resources-text ul {
        padding-left: 20px;
    }
    .footer {
        text-align: center;
        color: #888888;
        padding: 30px 15px;
        font-size: 14px;
    }
    .video-container iframe {
        width: 100%;
        height: auto;
        aspect-ratio: 16/9;
        border-radius: 10px;
    }
    @media (max-width: 768px) {
        h1 { font-size: 28px; }
        h2 { font-size: 20px; }
        .video-title { font-size: 16px; }
        .resources-header { font-size: 22px; }
        .resources-text { font-size: 14px; }
    }
</style>
""", unsafe_allow_html=True)

# Main heading
st.markdown("<h1>Kawach: Women's Self-Defense</h1>", unsafe_allow_html=True)

# Subheading
st.markdown("<h2>Essential Self-Defense Techniques</h2>", unsafe_allow_html=True)

# List of YouTube video links and titles
videos = [
    {"link": "https://www.youtube.com/embed/KVpxP3ZZtAc", "title": "5 Self-Defense Techniques for Women"},
    {"link": "https://www.youtube.com/embed/T7aNSRoDCmg", "title": "7 Essential Self-Defense Moves Every Woman Should Know"},
    {"link": "https://www.youtube.com/embed/Gx3_x6RH1J4", "title": "27 SELF-DEFENSE TRICKS FOR WOMEN"},
    {"link": "https://www.youtube.com/embed/k9Jn0eP-ZVg", "title": "SELF DEFENSE MOVES EVERY WOMAN SHOULD KNOW"},
    {"link": "https://www.youtube.com/embed/CH7DvnTNLuI", "title": "SELF-DEFENCE TECHNIQUES FOR WOMEN II 5-Minute Recovery Tips"},
    {"link": "https://www.youtube.com/embed/0UqK3tfuu8Q", "title": "5 Self Defense Techniques Every Women Should Know"},
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
    Empower yourself with these additional women's safety resources:
    <ul>
        <li>Find local self-defense classes near you</li>
        <li>Download women's safety apps for instant help</li>
        <li>Save emergency contact information on speed dial</li>
        <li>Join community support groups for women's safety</li>
        <li>Learn about personal safety devices and alarms</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Add a footer
st.markdown("""
<div class="footer">
    Stay safe, stay strong! 💪<br>
    Created with ❤️ using Streamlit | © 2024 Kawach Women's Safety Initiative
</div>
""", unsafe_allow_html=True)