import streamlit as st
import requests
import time

# 1. UI Configuration
st.set_page_config(page_title="SĀVI-Shield Forensics", page_icon="🛡️", layout="wide")

# Custom CSS for Premium Dark Mode
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .stButton>button { 
        width: 100%; 
        background-color: #ff4b4b; 
        color: white; 
        border-radius: 10px;
        font-weight: bold;
        border: none;
        padding: 0.5rem;
    }
    .stButton>button:hover { background-color: #d43f3f; border: none; }
    [data-testid="stMetricValue"] { color: #f2a154; }
    </style>
    """, unsafe_allow_html=True)

# 2. Header & Lore
st.title("🛡️ SĀVI-Shield: Agentic AI Honeypot")
st.subheader("Real-time Cyber-Forensics Engine")

col_img, col_txt = st.columns([1, 3])
with col_img:
    try:
        st.image("savi-face.png", use_container_width=True)
        st.markdown("<p style='text-align: center; color: #888; font-size: 0.8rem;'>Sāvi: The Forensics Expert</p>", unsafe_allow_html=True)
    except:
        st.warning("Sāvi character art not found.")

with col_txt:
    st.write("""
    **Mission:** SĀVI-Shield analyzes the psychology 
    behind scam messages, extracting entities and predicting threat levels before they strike.
    
    *Powered by Sāvi Intelligence | Seconds Matter.*
    """)

# 3. Analysis Interface
st.divider()
scam_input = st.text_area("📥 Drop the suspicious message here:", placeholder="Paste the SMS, Email, or Link message...", height=150)

if st.button("🚀 RUN AGENTIC ANALYSIS"):
    if scam_input:
        with st.spinner("Sāvi is investigating the digital fingerprints..."):
            try:
                response = requests.post(
                    "https://saavi-shield.onrender.com/test-honeypot",
                    headers={"x-api-key": "winner_secret_2026"},
                    json={"message": scam_input},
                    timeout=20
                )
                
                if response.status_code == 200:
                    data = response.json()
                    intel = data['forensics']['threat_intel']
                    
                    st.success("Forensic Analysis Complete!")
                    
                    # 4. Results Visualization
                    c1, c2, c3 = st.columns(3)
                    level = intel['threat_level'].upper()
                    color = "🔴" if level == "HIGH" else "🟡" if level == "MEDIUM" else "🟢"
                    
                    c1.metric("Threat Level", f"{color} {level}")
                    c2.metric("Scam Type", intel['scam_type'])
                    c3.metric("Is Scam?", "YES" if intel['is_scam'] else "NO")
                    
                    st.divider()
                    tab1, tab2 = st.tabs(["🧠 Intelligence Report", "🔗 Extracted Entities"])
                    
                    with tab1:
                        st.json(intel)
                    with tab2:
                        st.write("**URL Links Found:**", intel.get('extracted_entities', {}).get('urls', []))
                        st.write("**Phone Numbers:**", intel.get('extracted_entities', {}).get('phones', []))
                
                elif response.status_code == 503:
                    st.error("Backend is currently warming up on Render. Please wait 30 seconds and try again!")
                else:
                    st.error(f"Error: {response.status_code}. Details: {response.text}")
                    
            except Exception as e:
                st.error("Connection Failed. Check if the SĀVI-Shield API is online.")
    else:
        st.warning("Please enter a message first!")

# 5. Footer
st.divider()
st.markdown("""
    <div style="background-color: #000; padding: 40px 20px; text-align: center; border-top: 1px solid rgba(255,255,255,0.1); border-radius: 10px;">
        <p style="color: #fff; font-weight: 800; letter-spacing: 3px; text-transform: uppercase; font-size: 0.9rem; margin: 10px 0;">
            SĀVI INTELLIGENCE
        </p>
        <div style="height: 2px; background: #f2a154; width: 40px; margin: 15px auto;"></div>
        <p style="color: #666; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px; font-weight: 600;">
            © 2026 All Rights Reserved | Seconds Matter
        </p>
    </div>
    """, unsafe_allow_html=True)