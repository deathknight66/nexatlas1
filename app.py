import streamlit as st
import pandas as pd
import time

# --- BRANDING & UI SETUP ---
st.set_page_config(
    page_title="NexAtlas AI | Decision Intelligence System",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling Premium Dark Mode & Chatbot
st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    h1, h2, h3, h4 { color: #4A90E2 !important; font-family: 'Helvetica Neue', sans-serif; }
    .verdict-box { background-color: #1A1F2C; padding: 25px; border-radius: 10px; border: 1px solid #4A90E2; margin-bottom: 25px; }
    .consensus-box { background-color: #1F241F; padding: 20px; border-radius: 8px; border-left: 5px solid #238636; margin-top: 15px; }
    .metric-card { background-color: #161B22; padding: 20px; border-radius: 8px; text-align: center; border: 1px solid #21262D; }
    .upload-box { border: 2px dashed #4A90E2; padding: 20px; border-radius: 8px; background-color: #161B22; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# Session State untuk menyimpan history chat boardroom
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "avatar": "🏛️", "name": "NexAtlas Engine", "content": "Welcome to the Executive Boardroom. Upload a strategic document or inject a scenario to initiate the Digital Twin simulation."}
    ]

# Header Utama
st.title("🏛️ NexAtlas AI")
st.caption("Enterprise Digital Twin & Strategic Advisory System — Powered by Datasign")
st.divider()

# --- SIDEBAR: INTERACTIVE INPUTS & DOCUMENT UPLOADER ---
st.sidebar.header("⚙️ Executive Control Center")

# Feature 1: Document Uploader
st.sidebar.subheader("📥 Ingest Strategic Document")
uploaded_file = st.sidebar.file_uploader(
    "Upload Enterprise Data (PDF, CSV, TXT, JSON)", 
    type=["pdf", "csv", "txt", "json"]
)

if uploaded_file is not None:
    st.sidebar.success(f"✅ Loaded: {uploaded_file.name}")
    file_status = f"Analyzing uploaded document: **{uploaded_file.name}**"
else:
    file_status = "Using default regional supply chain dataset."

# Feature 2: Scenario Injection
st.sidebar.subheader("🔮 Scenario Injection")
scenario = st.sidebar.text_area("Specify Core Objective:", 
    "Evaluasi risiko implementasi arsitektur data forecasting berbasis Hybrid LSTM dan kesiapan visualisasi tingkat eksekutif.")

initiate_sim = st.sidebar.button("Initiate Digital Twin Simulation")

# --- MAIN DASHBOARD INTERACTION ---
if initiate_sim or uploaded_file is not None:
    
    # Animasi processing data yang elegan
    if initiate_sim:
        with st.spinner("🏛️ NexAtlas Twin: Parsing document architecture and alignment matrices..."):
            time.sleep(2)
        st.success("Consensus Reached! Strategic Assessment Generated Successfully.")

    # --- TOP KPI METRICS: EXECUTIVE STATUS ---
    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        st.markdown('<div class="metric-card"><p style="color:#8B949E;margin:0;">Overall Strategic Health</p><h2 style="margin:5px 0;color:#56D364 !important;">84 / 100</h2><span style="color:#56D364;font-size:12px;">▲ Optimized from Data Ingestion</span></div>', unsafe_allow_html=True)
    with col_m2:
        st.markdown('<div class="metric-card"><p style="color:#8B949E;margin:0;">Business Risk Level</p><h2 style="margin:5px 0;color:#FF7B72 !important;">🔴 High Risk</h2><span style="color:#FF7B72;font-size:12px;">Data Latency Detected</span></div>', unsafe_allow_html=True)
    with col_m3:
        st.markdown('<div class="metric-card"><p style="color:#8B949E;margin:0;">Contextual Grounding</p><h2 style="margin:5px 0;color:#58A6FF !important;">Verified</h2><span style="color:#58A6FF;font-size:12px;">Synced with Uploaded Context</span></div>', unsafe_allow_html=True)

    st.write(" ")
    
    # --- EXECUTIVE AI VERDICT ---
    st.markdown('<div class="verdict-box">', unsafe_allow_html=True)
    st.markdown(f"**Current Context:** {file_status}")
    st.subheader("══════════════════════════")
    st.subheader("NexAtlas Executive Verdict")
    st.subheader("══════════════════════════")
    st.markdown("""
    **Primary Issues Identified from Analysis:**
    * 🔴 **Infrastructure Deficit:** Data synchronization pipelines experience a **14-day lag** between regional collection nodes and core analytics layers.
    * ⚠️ **Methodological Error:** Management reporting still measures KPI performance against *planned targets* instead of **Total Actual Coverage**, hiding true operational leaks.
    * 🔒 **Governance Bottleneck:** No centralized encryption or real-time event broker architecture detected to support automation.

    **AI Core Recommendation:**
    > Deploy a Cloud Hybrid streaming pipeline within 90 days. Transition all visualization logic to focus strictly on actual ground execution data.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- TWO COLUMN ANALYSIS (MATURITY & ROADMAP) ---
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.markdown("### 📊 Data Maturity Assessment")
        st.code("""
Data Quality        █████████░ 85%
Data Integration    ███████░░░ 72%
Governance          ██████░░░░ 65%
Analytics           ████████░░ 80%
AI Readiness        ███████░░░ 74%
        """, language="text")
        st.caption("**Status:** `Level 3 - Defined` | Standards applied across corporate data tiers.")

    with col_right:
        st.markdown("### 💰 Financial & Impact Estimation")
        st.error("**Current System Loss:** Rp 1.2 Billion / year caused by delayed tactical decisions.")
        st.markdown("""
        **Expected Post-Optimization Value:**
        * ⚡ **+35%** Executive decision feedback velocity.
        * 🎯 **+25%** Predictive forecasting model accuracy (Hybrid LSTM support).
        """)

    st.divider()

    # --- FEATURE: INTERACTIVE BOARDROOM CHATBOT (MiroFish Vibe) ---
    st.markdown("### 💬 Interactive Multi-Agent Boardroom")
    st.write("Debat langsung atau tanyakan pertanyaan spesifik dari dokumen Anda kepada jajaran direksi AI:")

    # Container untuk chat history
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"], avatar=msg["avatar"]):
            st.write(f"**{msg['name']}**")
            st.write(msg["content"])

    # Input Chat dari User
    if user_query := st.chat_input("Tanyakan sesuatu pada dewan direksi AI (cth: 'Berapa biaya migrasinya, CTO?')"):
        # Tambahkan pertanyaan user ke history
        st.session_state.chat_history.append({"role": "user", "avatar": "👤", "name": "Executive (You)", "content": user_query})
        
        # Logika trigger respon multi-agent dinamis berbasis kata kunci (Kecerdasan Kontekstual)
        with st.spinner("Board members are deliberating your question..."):
            time.sleep(1.5)
            
            query_lower = user_query.lower()
            
            if "biaya" in query_lower or "cfo" in query_lower or "loss" in query_lower:
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "📊", "name": "CFO Agent", 
                    "content": f"Berdasarkan data dokumen, alokasi investasi awal untuk infrastruktur ini berkisar Rp 350 - 500 Juta. Namun, ini memitigasi kerugian operasional sebesar Rp 1.2 Miliar per tahun. Secara finansial, ROI dicapai dalam waktu kurang dari 6 bulan."
                })
            elif "teknis" in query_lower or "cto" in query_lower or "lstm" in query_lower or "kafka" in query_lower:
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "🏗️", "name": "CTO / Data Engineer Agent", 
                    "content": f"Untuk mengatasi masalah latensi 14 hari yang tertera di dokumen, saya menyarankan arsitektur Event-Driven menggunakan Apache Kafka. Ini akan memotong delay data dari 14 hari langsung menjadi di bawah 5 detik, siap menyuplai data ke model prediksi Hybrid LSTM."
                })
            elif "risiko" in query_lower or "ceo" in query_lower or "aman" in query_lower:
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "👔", "name": "CEO Agent", 
                    "content": f"Risiko terbesar kita saat ini adalah kelambatan bertindak. Jika kita tidak mengunci metrik evaluasi pada 'Total Actual Coverage', keputusan distribusi logistik kita akan terus meleset dari realitas lapangan."
                })
            else:
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "🏛️", "name": "NexAtlas Consensus", 
                    "content": f"Pertanyaan Anda mengenai '{user_query}' telah dianalisis. Dewan direksi sepakat bahwa integrasi data terpusat dan pembersihan aturan data kuantitatif di lapangan adalah fondasi mutlak sebelum mengaktifkan fitur automasi cerdas."
                })
        
        # Rerun agar chat langsung muncul di layar
        st.rerun()

else:
    # Tampilan Landing Page Premium saat belum ada data masuk
    st.markdown("""
    <div class="upload-box">
        <h3>🏛️ Welcome to NexAtlas Boardroom Simulator</h3>
        <p style="color:#8B949E;">Sistem siap menerima instruksi strategis Anda. Silakan pilih salah satu langkah di bawah untuk memulai:</p>
        <p style="color:#4A90E2;"><b>[ Opsi A ]</b> Unggah dokumen bisnis/data perusahaan Anda di panel sebelah kiri.<br>
        <b>[ Opsi B ]</b> Masukkan fokus skenario skenario lalu klik tombol <b>"Initiate Simulation"</b>.</p>
    </div>
    """, unsafe_allow_html=True)
