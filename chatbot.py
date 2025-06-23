import streamlit as st
import requests

# ============CSS BACKGROUND COLOR============
def set_background_color():
    st.markdown("""
    <style>
    .stApp {
        background-color: #1e3d59;
        background: linear-gradient(45deg, #1e3d59, #f5f7fa);
    }
    
    /* Sidebar background */
    .css-1d391kg {
        background-color: #2c3e50;
    }
    
    /* Chat messages styling */
    .stChatMessage {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# ============SIDEBAR CONFIGURATION============
st.sidebar.title("⚙️ Konfigurasi")

# Input nama pengguna
user_name = st.sidebar.text_input(
    "Nama Anda:", 
    value="", 
    placeholder="Masukkan nama Anda"
)

# Input API Key
user_api_key = st.sidebar.text_input(
    "OpenRouter API Key:", 
    value="", 
    type="password",
    placeholder="sk-or-v1-..."
)

# Model selection
MODEL = st.sidebar.selectbox(
    "Pilih Model:",
    [
        "meta-llama/llama-3.3-8b-instruct:free",
        "meta-llama/llama-3.1-8b-instruct:free",
        "google/gemma-2-9b-it:free",
        "mistralai/mistral-7b-instruct:free"
    ]
)

# Default API key (fallback)
DEFAULT_API_KEY = "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"

# Gunakan API key dari user atau default
OPENROUTER_API_KEY = user_api_key if user_api_key else DEFAULT_API_KEY

# Info di sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### 📋 Informasi")
if user_name:
    st.sidebar.markdown(f"**Pengguna:** {user_name}")
else:
    st.sidebar.markdown("**Pengguna:** Guest")

if user_api_key:
    st.sidebar.markdown("**API Key:** ✅ Tersedia")
else:
    st.sidebar.markdown("**API Key:** ⚠️ Menggunakan default")

st.sidebar.markdown(f"**Model:** {MODEL}")

# Tombol reset chat
if st.sidebar.button("🗑️ Reset Chat"):
    st.session_state.chat_history = []
    st.rerun()

# ============API CONFIGURATION============
HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "HTTP-Referer": "https://psychic-capybara-5g9vp55r4v6r376jw-8501.app.github.dev",
    "Content-Type": "application/json",
    "X-Title": "AI Chatbot Streamlit"
}

API_URL = "https://openrouter.ai/api/v1/chat/completions"
# =====================================

# Main title dengan nama pengguna
if user_name:
    st.title(f"🧠 AI Chatbot - Halo, {user_name}!")
else:
    st.title("🧠 AI Chatbot Bubble Style")

st.markdown("Chatbot sederhana dengan menggunakan OpenRouterAPI made by Rico :>")

# Peringatan jika tidak ada API key
if not user_api_key:
    st.warning("⚠️ Anda menggunakan API key default. Masukkan API key Anda sendiri di sidebar untuk penggunaan personal.")

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

# Input dari pengguna
user_input = st.chat_input("Ketik pesan Anda di sini...")

if user_input:
    # Validasi API key
    if not OPENROUTER_API_KEY or OPENROUTER_API_KEY == "":
        st.error("❌ API Key tidak valid! Silakan masukkan API key yang benar di sidebar.")
        st.stop()
    
    # Add user message to chat
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    # Mengirim permintaan ke OpenRouter API
    with st.spinner("Mengolah prompt-mu..."):
        # System message yang dapat disesuaikan dengan nama
        system_message = "You are a helpful assistant."
        if user_name:
            system_message += f" The user's name is {user_name}, you can address them by name if appropriate."
        
        payload = {
            "model": MODEL,
            "messages": [
                {"role": "system", "content": system_message}
            ] + st.session_state.chat_history
        }
        
        try:
            response = requests.post(API_URL, headers=HEADERS, json=payload)
            
            if response.status_code == 200:
                bot_reply = response.json()['choices'][0]['message']['content']
            else:
                bot_reply = f"⚠️ Error {response.status_code}: {response.text}"
                
        except Exception as e:
            bot_reply = f"⚠️ Connection error: {str(e)}"
        
        # Display bot response
        st.chat_message("assistant").markdown(bot_reply)
        st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})
        
        st.rerun()