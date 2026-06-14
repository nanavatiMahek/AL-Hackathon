import streamlit as st
from agent import chat_with_agent

st.set_page_config(
    page_title="Verity",
    page_icon="⚖️",
    layout="centered"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:wght@600&display=swap');

    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        font-family: 'Inter', sans-serif;
    }

    .block-container {
        padding-top: 0.8rem !important;
        padding-bottom: 0.5rem !important;
    }

    .main-header {
        text-align: center;
        padding: 0.6rem 0 0.5rem 0;
    }
    .main-header h1 {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        color: #FFD700;
        margin: 0;
        text-shadow: 0 0 40px rgba(255,215,0,0.6), 0 0 80px rgba(255,215,0,0.2);
        line-height: 1.2;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 12px;
        letter-spacing: 2px;
    }
    .main-header p {
        color: rgba(255,255,255,0.65);
        font-size: 0.88rem;
        margin-top: 0.4rem;
        margin-bottom: 1.4rem;
    }

    .info-cards {
        display: flex;
        gap: 10px;
        margin: 0rem 0 1.6rem 0;
        flex-wrap: wrap;
    }
    .info-card {
        background: rgba(255,255,255,0.07);
        border: 1px solid rgba(255,215,0,0.18);
        border-radius: 14px;
        padding: 10px 12px;
        flex: 1;
        min-width: 130px;
        text-align: center;
        transition: transform 0.2s ease, background 0.2s ease;
    }
    .info-card:hover {
        background: rgba(255,215,0,0.1);
        transform: translateY(-2px);
    }
    .info-card .icon {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 6px;
    }
    .info-card .category {
        color: rgba(255,255,255,0.5);
        font-size: 0.65rem;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 3px;
    }
    .info-card .title {
        color: #FFD700;
        font-size: 0.82rem;
        font-weight: 600;
        margin-bottom: 5px;
    }

    .chat-wrapper {
        display: flex;
        flex-direction: column;
        gap: 8px;
        margin: 0.5rem 0;
        padding: 0 4px;
    }

    .bubble-row-ai {
        display: flex;
        align-items: flex-end;
        gap: 8px;
        justify-content: flex-start;
    }
    .bubble-avatar {
        font-size: 1.5rem;
        flex-shrink: 0;
        line-height: 1;
        margin-bottom: 2px;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 32px;
        height: 32px;
        background: rgba(255,215,0,0.12);
        border: 1px solid rgba(255,215,0,0.25);
        border-radius: 50%;
    }
    .bubble-ai {
        background: rgba(255,255,255,0.10);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 0px 16px 16px 16px;
        padding: 10px 14px;
        max-width: 78%;
        color: rgba(255,255,255,0.92);
        font-size: 0.88rem;
        line-height: 1.6;
        word-wrap: break-word;
    }

    .bubble-row-user {
        display: flex;
        align-items: flex-end;
        gap: 8px;
        justify-content: flex-end;
    }
    .bubble-user {
        background: linear-gradient(135deg, #2d6a4f, #1b4332);
        border: 1px solid rgba(45,106,79,0.5);
        border-radius: 16px 0px 16px 16px;
        padding: 10px 14px;
        max-width: 78%;
        color: rgba(255,255,255,0.95);
        font-size: 0.88rem;
        line-height: 1.6;
        word-wrap: break-word;
    }

    .suggestion-label {
        color: rgba(255,215,0,0.7);
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.6px;
        margin: 40px 0 6px 44px;
    }
    .suggestion-chips {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin: 0 0 10px 44px;
    }
    .chip {
        background: rgba(255,215,0,0.08);
        border: 1px solid rgba(255,215,0,0.35);
        border-radius: 20px;
        padding: 6px 13px;
        color: #FFD700 !important;
        font-size: 0.78rem;
        cursor: pointer;
        transition: background 0.2s;
        white-space: nowrap;
        display: flex;
        align-items: center;
        gap: 6px;
        text-decoration: none !important;
    }
    .chip svg { flex-shrink: 0; }
    .chip:hover { background: rgba(255,215,0,0.18); }

    .stChatInput textarea,
    .stChatInput input {
        background: rgba(255,255,255,0.08) !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        border-radius: 12px !important;
        color: white !important;
        font-family: 'Inter', sans-serif !important;
        padding-left: 16px !important;
        text-indent: 6px !important;
    }
    .stChatInput textarea::placeholder,
    .stChatInput input::placeholder {
        color: rgba(255,255,255,0.4) !important;
    }

    .stChatMessage { display: none !important; }

    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }

    ::-webkit-scrollbar { width: 4px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: rgba(255,215,0,0.3); border-radius: 2px; }
</style>
""", unsafe_allow_html=True)

# ── SVG Icons ──
ICON_SHIELD = """<svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#FFD700" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/></svg>"""
ICON_LOCK = """<svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#FFD700" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>"""
ICON_BALANCE = """<svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#FFD700" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" x2="12" y1="3" y2="21"/><path d="M5 21h14"/><path d="M3 6l9-3 9 3"/><path d="m3 6 4 8c.83 1.67 2.67 1.67 3.5 0L14 6"/><path d="m14 6 3.5 7c.83 1.67 2.67 1.67 3.5 0L17 6"/></svg>"""
ICON_GIFT = """<svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#FFD700" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="8" width="18" height="4" rx="1"/><path d="M12 8v13"/><path d="M19 12v7a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2v-7"/><path d="M7.5 8a2.5 2.5 0 0 1 0-5A4.8 8 0 0 1 12 8a4.8 8 0 0 1 4.5-5 2.5 2.5 0 0 1 0 5"/></svg>"""
ICON_FILE_TEXT = """<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#FFD700" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/></svg>"""
ICON_SHOPPING_CART = """<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#FFD700" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="8" cy="21" r="1"/><circle cx="19" cy="21" r="1"/><path d="M2.05 2.05h2l2.66 12.42a2 2 0 0 0 2 1.58h9.78a2 2 0 0 0 1.95-1.57l1.65-7.43H5.12"/></svg>"""
ICON_CLOCK = """<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#FFD700" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>"""
ICON_ALERT = """<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#FFD700" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/></svg>"""
ICON_HOME = """<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#FFD700" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>"""
ICON_USERS = """<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#FFD700" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>"""
ICON_CREDIT = """<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#FFD700" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="14" x="2" y="5" rx="2"/><line x1="2" x2="22" y1="10" y2="10"/></svg>"""
ICON_BOT = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#FFD700" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/></svg>"""
ICON_USER = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.8)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="5"/><path d="M20 21a8 8 0 1 0-16 0"/></svg>"""
ICON_SCALE_HEADER = """<svg xmlns="http://www.w3.org/2000/svg" width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="#FFD700" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 10px rgba(255,215,0,0.7));"><line x1="12" x2="12" y1="3" y2="21"/><path d="M5 21h14"/><path d="M3 6l9-3 9 3"/><path d="m3 6 4 8c.83 1.67 2.67 1.67 3.5 0L14 6"/><path d="m14 6 3.5 7c.83 1.67 2.67 1.67 3.5 0L17 6"/></svg>"""

# ── Header ──
st.markdown(f"""
<div class="main-header">
    <h1>{ICON_SCALE_HEADER} Verity</h1>
    <p>Know Your Rights. File Your Complaint. Get Justice.</p>
</div>
""", unsafe_allow_html=True)

# ── Info Cards ──
st.markdown(f"""
<div class="info-cards">
    <div class="info-card">
        <div class="icon">{ICON_SHIELD}</div>
        <div class="category">Legally Accurate</div>
        <div class="title">RTI Act 2005</div>
    </div>
    <div class="info-card">
        <div class="icon">{ICON_LOCK}</div>
        <div class="category">Privacy</div>
        <div class="title">No Data Stored</div>
    </div>
    <div class="info-card">
        <div class="icon">{ICON_BALANCE}</div>
        <div class="category">Consumer Law</div>
        <div class="title">CP Act 2019</div>
    </div>
    <div class="info-card">
        <div class="icon">{ICON_GIFT}</div>
        <div class="category">Cost</div>
        <div class="title">Completely Free</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Session state ──
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Namaste 🙏\nFile RTI requests and consumer complaints hustle free.\nTell me your problem in simple words — have you been wronged by a company, government office or something else?"
    })
if "suggestions_used" not in st.session_state:
    st.session_state.suggestions_used = False

# ── Handle chip query param ──
CHIP_MAP = {
    "0": "I want to file an RTI request against a government office",
    "1": "I have a consumer complaint against a company for defective product or poor service",
    "2": "My government application or service has been delayed or ignored",
    "3": "I have been cheated or scammed online",
    "4": "I have a property or real estate dispute with a builder under RERA",
    "5": "I am facing sexual harassment or misconduct at my workplace",
    "6": "My bank or UPI transaction has failed or I have been defrauded",
}

params = st.query_params
if "chip" in params:
    chip_text = CHIP_MAP.get(params["chip"])
    if chip_text:
        st.query_params.clear()
        st.session_state.suggestions_used = True
        st.session_state.messages.append({"role": "user", "content": chip_text})
        with st.spinner("Analyzing your case..."):
            reply = chat_with_agent(st.session_state.messages)
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.rerun()

# ── Render chat bubbles ──
chat_html = '<div class="chat-wrapper">'
for i, msg in enumerate(st.session_state.messages):
    content = (msg["content"]
               .replace("&", "&amp;")
               .replace("<", "&lt;")
               .replace(">", "&gt;")
               .replace("\n", "<br>"))
    if msg["role"] == "assistant":
        chat_html += f'''
        <div class="bubble-row-ai">
            <div class="bubble-avatar">{ICON_BOT}</div>
            <div class="bubble-ai">{content}</div>
        </div>'''
        if i == 0 and not st.session_state.suggestions_used:
            chat_html += f'''
            <div class="suggestion-label">Quick Issues — tap to ask</div>
            <div class="suggestion-chips">
                <a class="chip" href="?chip=0">{ICON_FILE_TEXT} File RTI Request</a>
                <a class="chip" href="?chip=1">{ICON_SHOPPING_CART} Consumer Complaint</a>
                <a class="chip" href="?chip=2">{ICON_CLOCK} Govt. Delay / No Reply</a>
                <a class="chip" href="?chip=3">{ICON_ALERT} Online Fraud / Scam</a>
                <a class="chip" href="?chip=4">{ICON_HOME} Property / RERA</a>
                <a class="chip" href="?chip=5">{ICON_USERS} Workplace / POSH</a>
                <a class="chip" href="?chip=6">{ICON_CREDIT} Banking / UPI Fraud</a>
            </div>'''
    else:
        chat_html += f'''
        <div class="bubble-row-user">
            <div class="bubble-user">{content}</div>
            <div class="bubble-avatar" style="background:rgba(45,106,79,0.3);border-color:rgba(45,106,79,0.5);">{ICON_USER}</div>
        </div>'''
chat_html += '</div>'
st.markdown(chat_html, unsafe_allow_html=True)

# ── Chat input ──
if user_input := st.chat_input("Describe your problem here..."):
    st.session_state.suggestions_used = True
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("Analyzing your case..."):
        reply = chat_with_agent(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()