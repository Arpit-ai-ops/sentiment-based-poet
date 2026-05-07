import streamlit as st
from textblob import TextBlob
from generator import generate_poetry

# --- UI Configuration ---
st.set_page_config(page_title="Sentiment based poet", layout="centered", page_icon="✒️")


def inject_custom_design(sentiment_score):
    """Professional UI with Human-Centric Design."""

    if sentiment_score > 0.3:
        grad_1, grad_2 = "#FFD200", "#F7971E"
        emoji, label = "✨", "Radiant"
    elif sentiment_score < -0.3:
        grad_1, grad_2 = "#0f2027", "#2c5364"
        emoji, label = "🌙", "Melancholy"
    else:
        grad_1, grad_2 = "#eef2f3", "#8e9eab"
        emoji, label = "🌿", "Serene"

    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(135deg, {grad_1} 0%, {grad_2} 100%);
            background-attachment: fixed;
            transition: all 2s ease-in-out;
        }}

        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,700&family=Montserrat:wght@300;400;600;800&display=swap');

        /* Sidebar Styling */
        [data-testid="stSidebar"] {{
            background-color: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(15px);
            border-right: 1px solid rgba(255, 255, 255, 0.1);
        }}

        /* Sidebar Info Box (From Screenshot Style) */
        .info-box {{
            background-color: rgba(255, 255, 255, 0.6);
            padding: 20px;
            border-radius: 10px;
            color: #1f3b64;
            font-family: 'Montserrat', sans-serif;
            font-size: 0.9rem;
            line-height: 1.4;
            border: 1px solid rgba(255, 255, 255, 0.2);
            margin-bottom: 20px;
        }}

        .dev-badge {{
            background-color: rgba(220, 245, 230, 0.8);
            padding: 15px;
            border-radius: 10px;
            color: #2e7d32;
            font-weight: 600;
            text-align: center;
            margin-top: 20px;
        }}

        .main-card {{
            background: rgba(255, 255, 255, 0.07);
            backdrop-filter: blur(40px);
            border-radius: 40px;
            border: 1px solid rgba(255, 255, 255, 0.15);
            padding: 60px 40px;
            box-shadow: 0 30px 60px rgba(0,0,0,0.3);
            text-align: center;
            margin-top: 20px;
            animation: fadeIn 1.5s ease-in-out;
        }}

        .poem-text {{
            font-family: 'Playfair Display', serif;
            font-size: 2.3rem;
            line-height: 1.5;
            color: #FFFFFF;
            text-shadow: 0 0 20px rgba(255,255,255,0.4);
            font-style: italic;
            font-weight: 700;
        }}

        .main-title {{
            font-family: 'Montserrat', sans-serif;
            font-weight: 800;
            color: #FFFFFF;
            text-transform: uppercase;
            letter-spacing: 10px;
            text-align: center;
            margin-bottom: 5px;
        }}

        .mood-badge {{
            display: inline-block;
            padding: 12px 35px;
            border-radius: 100px;
            background: rgba(255, 255, 255, 0.15);
            color: #FFFFFF;
            backdrop-filter: blur(10px);
            font-family: 'Montserrat', sans-serif;
            font-size: 0.7rem;
            font-weight: 600;
            letter-spacing: 3px;
            margin-bottom: 40px;
            border: 1px solid rgba(255, 255, 255, 0.3);
        }}

        .stTextInput > div > div > input {{
            background: rgba(0, 0, 0, 0.2) !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
            border-radius: 20px !important;
            padding: 25px !important;
            color: #FFFFFF !important;
            font-family: 'Montserrat', sans-serif;
            text-align: center;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        #MainMenu, footer, header {{visibility: hidden;}}
        </style>
    """, unsafe_allow_html=True)
    return emoji, label


# Initialize Session State for History
if "history" not in st.session_state:
    st.session_state.history = []

# --- UI Setup ---
current_emoji, mood_label = inject_custom_design(0)

# Sidebar: Control Center
with st.sidebar:
    # 1. Top Icon (Laptop Illustration style)
    st.image("https://cdn-icons-png.flaticon.com/512/4233/4233925.png", width=120)

    # 2. About Section (Styled like your screenshot)
    st.markdown("## About Poet")
    st.markdown("""
    <div class="info-box">
        <b>Sentiment based poet</b> is an advanced NLP-driven utility that leverages 
        machine learning to weave your current emotions into artistic poetry.
        <br><br>
        Our primary objective is to harmonize human sentiment with generative 
        artificial intelligence for real-time creative expression.
    </div>
    """, unsafe_allow_html=True)

    # 3. Model Details
    st.markdown("**Model:** Generative Transformer")
    st.markdown("**NLP Engine:** TextBlob / GPT")
    st.divider()

    # 4. Your existing controls
    st.markdown("### 🎨 Creative Mode")
    poetry_style = st.selectbox("Select Poetic Voice",
                                ["Classical Sonnet", "Modern Free Verse", "Haiku", "Dark Romanticism"])

    st.markdown("### 📜 Reflection Log")
    if not st.session_state.history:
        st.caption("Recent emotional reflections will appear here.")
    else:
        for item in reversed(st.session_state.history[-5:]):
            st.markdown(f"**{item['mood']}**: *{item['input'][:30]}...*")

    st.divider()

    # 5. Developer Badge (Styled like your screenshot)
    st.markdown('<div class="dev-badge">Developer: Arpit Thakur , Hansika bhati , Shambhavi</div>', unsafe_allow_html=True)

    if st.button("Clear Creative History"):
        st.session_state.history = []
        st.rerun()

# --- Main Interface ---
st.markdown("<h1 class='main-title'>Sentiment based Poet</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; color: white; opacity: 0.8; font-family: Montserrat; letter-spacing: 2px; font-size: 0.8rem;'>A Mirror to Your Inner World</p>",
    unsafe_allow_html=True)

user_input = st.text_input("", placeholder="Whisper your soul into the model...")

if user_input:
    score = TextBlob(user_input).sentiment.polarity
    current_emoji, mood_label = inject_custom_design(score)
    st.session_state.history.append({"input": user_input, "mood": mood_label})

    with st.spinner(f"Aligning with your {mood_label} energy..."):
        poem = generate_poetry(user_input, f"{mood_label} in the style of {poetry_style}")

    st.markdown(f"""
        <div class="main-card">
            <div class="mood-badge">{current_emoji} &nbsp; {mood_label.upper()} RESONANCE</div>
            <div class="poem-text">{poem.replace('\n', '<br>')}</div>
        </div>
    """, unsafe_allow_html=True)

    resonance_percent = int((score + 1) * 50)
    st.markdown(
        f"<p style='text-align: center; color: white; opacity: 0.7; margin-top: 30px; font-family: Montserrat; font-size: 0.7rem; letter-spacing: 2px;'>AURA DEPTH: {resonance_percent}%</p>",
        unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style="position: fixed; bottom: 20px; left: 0; width: 100%; text-align: center; color: white; opacity: 0.4; font-family: Montserrat; font-size: 0.6rem; letter-spacing: 4px;">
        POWERED BY MACHINE LEARNING &bull; 2026
    </div>
""", unsafe_allow_html=True)
