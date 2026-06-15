import streamlit as st
import pandas as pd
import time

# --- BRANDING & UI SETUP (ELITE SYSTEM STYLING) ---
st.set_page_config(
    page_title="NexAtlas AI | Decision Intelligence System",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-End Theme Architecture (Glassmorphism & Crisp Typography)
st.markdown("""
    <style>
    .main { background-color: #0B0E14; }
    header { background-color: rgba(0,0,0,0) !important; }
    
    h1, h2, h3, h4, h5 { color: #58A6FF !important; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica; font-weight: 600; }
    p, span, label, li { color: #C9D1D9 !important; }
    
    .hero-portal { background: linear-gradient(135deg, #161B22 0%, #0D1117 100%); padding: 40px; border-radius: 12px; border: 1px solid #30363D; margin-bottom: 30px; box-shadow: 0 4px 20px rgba(0,0,0,0.3); }
    .verdict-box { background-color: #1A1F2C; padding: 30px; border-radius: 12px; border: 1px solid #388BFD; margin-bottom: 25px; }
    .consensus-box { background-color: #1F241F; padding: 20px; border-radius: 8px; border-left: 5px solid #238636; margin-top: 15px; }
    
    .profile-card { background-color: #161B22; padding: 20px; border-radius: 8px; border: 1px solid #30363D; height: 100%; }
    .framework-badge { display: inline-block; background-color: #21262D; color: #58A6FF; padding: 4px 10px; border-radius: 4px; border: 1px solid #30363D; font-size: 12px; font-weight: bold; margin: 3px; }
    
    .chat-agent-name { font-size: 15px; font-weight: bold; color: #58A6FF; margin-bottom: 5px; }
    .conflict-quote { border-left: 3px solid #FF7B72; padding-left: 10px; font-style: italic; color: #FF7B72; background-color: #25181C; padding: 10px; border-radius: 4px; margin: 10px 0; }
    </style>
""", unsafe_allow_html=True)

# Session State to lock simulation lifecycle
if "simulation_active" not in st.session_state:
    st.session_state.simulation_active = False

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Title Banner
st.title("🏛️ NexAtlas AI")
st.markdown("<p style='font-size: 16px; color: #8B949E !important;'>Enterprise Digital Twin & Decision Intelligence Ecosystem</p>", unsafe_allow_html=True)
st.divider()

# --- SIDEBAR EXECUTIVE CONTROL CENTER ---
st.sidebar.header("⚙️ Simulation Settings")

# Step 1: Document Upload
st.sidebar.subheader("STEP 1: Upload Documents")
uploaded_file = st.sidebar.file_uploader("Ingest Corporate Reports (PDF, CSV, TXT)", type=["pdf", "csv", "txt", "json"])

# Step 3: Engine Configuration (The MiroFish Knobs)
st.sidebar.subheader("STEP 3: Configure Engine")
disc_rounds = st.sidebar.slider("Number of Discussion Rounds", min_value=5, max_value=50, value=30)
risk_tolerance = st.sidebar.select_slider("Risk Tolerance Threshold", options=["Conservative", "Medium", "Aggressive"], value="Medium")
decision_horizon = st.sidebar.selectbox("Decision Horizon", ["3 Months", "6 Months", "12 Months", "24 Months"], index=2)
confidence_threshold = st.sidebar.slider("AI Confidence Guardrail (%)", min_value=70, max_value=98, value=90)

initiate_sim = st.sidebar.button("📊 Run Multi-Agent Simulation", use_container_width=True)

if initiate_sim:
    st.session_state.simulation_active = True

# --- SCREEN CONTROLLER: LANDING PAGE VS SIMULATION ROOM ---
if not st.session_state.simulation_active:
    
    # --- ENTERPRISE HERO INTERFACE ---
    st.markdown("""
    <div class="hero-portal">
        <h2 style='margin-top:0;'>🏛️ NexAtlas Virtual Strategy Room</h2>
        <div style="background-color: #0D1117; padding: 18px 25px; border-radius: 8px; border-left: 4px solid #D4BB6C; margin: 20px 0;">
            <i style='color:#C9D1D9; font-size: 15px;'>\"Traditional dashboards explain what happened. NexAtlas simulates why it happened, evaluates risks, and recommends strategic actions based on AI executive deliberation.\"</i>
        </div>
        <p style='font-size:14px; margin-bottom:0; color:#8B949E !important;'>
            Sistem orkestrasi dewan direksi virtual siap menganalisis dokumen strategis, menantang asumsi manajemen, dan memproyeksikan lintasan masa depan korporasi.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # --- TWO COLUMN PRE-FLIGHT SETUP ---
    col_left, col_right = st.columns(2)
    
    with col_left:
        # STEP 2: COMPANY DIGITAL TWIN PROFILE
        st.markdown("### 🏢 STEP 2: Digital Twin Profile Context")
        st.markdown("""
        <div class="profile-card">
            <table style="width:100%; border-collapse: collapse;">
                <tr><td style="color:#8B949E; padding:8px 0;"><b>Enterprise Entity:</b></td><td>PT Maju Bersama Indonesia</td></tr>
                <tr><td style="color:#8B949E; padding:8px 0;"><b>Industry Sector:</b></td><td>Agriculture & Supply Chain Network</td></tr>
                <tr><td style="color:#8B949E; padding:8px 0;"><b>Annual Revenue Baseline:</b></td><td>Rp 2.4 Trillion</td></tr>
                <tr><td style="color:#8B949E; padding:8px 0;"><b>Active Workforce:</b></td><td>5,200 Employees (Field & HQ)</td></tr>
                <tr><td style="color:#8B949E; padding:8px 0;"><b>Current Crisis Vector:</b></td><td style="color:#FF7B72;">Revenue declined 15% in last 3 quarters</td></tr>
                <tr><td style="color:#8B949E; padding:8px 0;"><b>Strategic Directive:</b></td><td style="color:#56D364;">Cost optimization & framework-driven modernization</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

        # STEP 4: GOVERNANCE & CONSULTING FRAMEWORKS
        st.markdown("### 📐 STEP 4: Applied Frameworks Layer")
        st.write("Metodologi tata kelola data dan konsultasi strategis Big 4 yang disuntikkan ke dalam agen:")
        frameworks = ["SWOT Analysis", "Porter's Five Forces", "McKinsey 7S", "COBIT 2019", "DAMA-DMBOK", "ITIL 4", "TOGAF Architecture", "Digital Maturity Model"]
        for fw in frameworks:
            st.markdown(f'<span class="framework-badge">✓ {fw}</span>', unsafe_allow_html=True)

    with col_right:
        # STEP 3: MANUSIAWI EXECUTIVE BOARD MEMBERS
        st.markdown("### 👥 Executive Committee Architecture")
        st.write("Struktur dewan pakar virtual yang akan memperdebatkan data Anda:")
        
        st.markdown("""
        <div class="agent-card-standby" style="border-top:3px solid #58A6FF; padding:12px; margin-bottom:10px;">
            <span class="agent-status-dot"></span><b>👔 CEO Agent (Corporate Strategy Partner)</b><br>
            <span style='font-size:12px; color:#8B949E;'>Focus: Macro alignment, market responsiveness, risk ownership.</span>
        </div>
        <div class="agent-card-standby" style="border-top:3px solid #D4BB6C; padding:12px; margin-bottom:10px;">
            <span class="agent-status-dot"></span><b>💰 CFO Agent (Veteran Risk & Financial Allocator)</b><br>
            <span style='font-size:12px; color:#8B949E;'>Focus: Working capital efficiency, inventory leakage mitigation, ROI boundaries.</span>
        </div>
        <div class="agent-card-standby" style="border-top:3px solid #56D364; padding:12px; margin-bottom:10px;">
            <span class="agent-status-dot"></span><b>📊 CDO Agent (Chief Data Officer Partner)</b><br>
            <span style='font-size:12px; color:#8B949E;'>Focus: DAMA-DMBOK standards, actual ground coverage metrics, algorithm auditing.</span>
        </div>
        <div class="agent-card-standby" style="border-top:3px solid #A371F7; padding:12px; margin-bottom:10px;">
            <span class="agent-status-dot"></span><b>🖥️ CIO Agent (Technology Transformation Fellow)</b><br>
            <span style='font-size:12px; color:#8B949E;'>Focus: Kafka pipeline streaming, hybrid data lakehouses, Hybrid LSTM architectures.</span>
        </div>
        <div class="agent-card-standby" style="border-top:3px solid #FF7B72; padding:12px; margin-bottom:10px;">
            <span class="agent-status-dot"></span><b>🔐 IT Auditor Agent (Governance & Compliance Inspector)</b><br>
            <span style='font-size:12px; color:#8B949E;'>Focus: COBIT 2019 compliance, data lineage validation, audit trail logs.</span>
        </div>
        """, unsafe_allow_html=True)

    st.divider()
    
    # STEP 5: EXPECTED ADVISORY DELIVERABLES
    st.markdown("### 📋 STEP 5: Target Deliverables Matrix")
    st.write("Dokumen keluaran strategis yang akan dikonstruksikan secara otonom oleh simulasi engine:")
    
    col_d1, col_d2, col_d3, col_d4 = st.columns(4)
    with col_d1:
        st.markdown("✔ Executive Summary Verdict<br>✔ Root Cause Analysis", unsafe_allow_html=True)
    with col_d2:
        st.markdown("✔ Risk Assessment Matrix<br>✔ Data Maturity Scorecard", unsafe_allow_html=True)
    with col_d3:
        st.markdown("✔ Technology Gap Mapping<br>✔ 30-60-90 Day Roadmap", unsafe_allow_html=True)
    with col_d4:
        st.markdown("✔ What-If Simulation Engine<br>✔ Financial Impact Optimization", unsafe_allow_html=True)

    st.info("💡 Konfigurasi komplit. Silakan sesuaikan parameter mesin di panel kontrol sebelah kiri, lalu tekan 'Run Multi-Agent Simulation' untuk memulai sidang otonom.")

else:
    # --- SIMULATION ACTIVE ROOM (THE FLAGSHIP PORTAL EXECUTED) ---
    with st.spinner("🏛️ Orchestrating Live AI Boardroom Simulation... Executing Multi-Agent Dialogue Nodes..."):
        time.sleep(1.5)
        
    # KPI Metrics Banner
    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        st.metric(label="Overall Strategic Health", value="68 / 100", delta="-14% Volatility Risk")
    with col_m2:
        st.metric(label="Business Risk Status", value="🔴 CRITICAL INTERNAL CRISIS", delta="Revenue Leakage Identified")
    with col_m3:
        st.metric(label="Simulation Guardrail Profile", value=f"Rounds: {disc_rounds} | Conf: {confidence_threshold}%", delta=f"Horizon: {decision_horizon}")

    st.divider()

    # --- 1. THE ADVANCED EXECUTIVE VERDICT ---
    st.markdown('<div class="verdict-box">', unsafe_allow_html=True)
    st.subheader("═════════════════════════════")
    st.subheader("NexAtlas Executive Verdict")
    st.subheader("═════════════════════════════")
    st.markdown(f"""
    **Context:** Active Digital Twin Framework deployed for **PT Maju Bersama Indonesia** against a 15% revenue drop.
    
    **Primary Issues Decoded via Applied Governance Frameworks:**
    * 🔴 **Methodological Error (DAMA-DMBOK Deficit):** Performance reporting still measures KPI execution against obsolete *planned targets*, hiding a **31% actual data gap** in regional supply chain coverage.
    * ⏳ **Infrastructure Deficit (TOGAF/ITIL Latency):** Core transaction layers suffer a **14-day synchronization lag**, leaving the CEO with stale intelligence.
    * ⚠️ **Financial Drain (SWOT Risk Vector):** Working capital is heavily trapped in inventory overhead due to speculative production forecasting unlinked to field reality.

    **AI Core Consensus Recommendation:**
    > Restructure all reporting to measure strictly against **Total Actual Ground Coverage**. Authorize immediate deployment of an Event-Driven Streaming Pipeline (Kafka) to feed real-time analytics to a **Hybrid LSTM Forecasting model** within 90 days.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 2. MULTI-AGENT DEBATE ROOM (THE FIERCE CONFLICT & RESOLUTION) ---
    st.markdown("### 🧠 Live Multi-Agent Boardroom Transcripts")
    st.write("Saksikan perdebatan tajam antar jajaran direksi virtual (Aksi Saling Sanggah Menuju Konsensus):")
    
    # Render the fierce boardroom debate where agents clash
    with st.chat_message("assistant", avatar="👔"):
        st.markdown("<div class='chat-agent-name'>CEO Agent (Corporate Strategy Partner)</div>", unsafe_allow_html=True)
        st.write("""Penurunan pendapatan 15% ini adalah bukti kegagalan eksekusi makro. Tim penjualan beralasan pasar bergejolak, tapi Digital Twin mendeteksi kita buta arah di level hulu rantai pasok. Saya butuh transparansi data sekarang juga.""")
        
    with st.chat_message("assistant", avatar="💰"):
        st.markdown("<div class='chat-agent-name'>CFO Agent (Veteran Risk & Financial Allocator)</div>", unsafe_allow_html=True)
        st.write("""Saya harus memotong intervensi CEO. Akar kebocorannya ada pada **financial drain sebesar Rp 1.2 Miliar per tahun** akibat pembengkakan *inventory cost* di gudang regional. Kita membuang modal kerja untuk memproduksi barang berdasarkan target imajiner rencana lahan birokrasi, bukan serapan pasar.""")
        
    with st.chat_message("assistant", avatar="📊"):
        st.markdown("<div class='chat-agent-name'>CDO Agent (Chief Data Officer Partner)</div>", unsafe_allow_html=True)
        st.markdown("""<div class='conflict-quote'><b>CDO Menyanggah CFO:</b> "Tunggu CFO, jangan menyalahkan proyeksi produksi sebelum Anda mengoreksi metodologi pengukuran dasarnya!"</div>""", unsafe_allow_html=True)
        st.write("""Berdasarkan audit standar **DAMA-DMBOK**, dashboard Power BI lama manajemen mengukur rasio performa dari rencana target lahan sehingga angkanya selalu tampak 100% aman. Faktanya, **Total Actual Ground Coverage kita drop hingga 69%**. Manajemen disidang menggunakan ilusi optik data! Rumus wajib kita balik total.""")

    with st.chat_message("assistant", avatar="🖥️"):
        st.markdown("<div class='chat-agent-name'>CIO Agent (Technology Transformation Fellow)</div>", unsafe_allow_html=True)
        st.markdown("""<div class='conflict-quote'><b>CIO Menyanggah CDO & CFO:</b> "Anda berdua menuntut pembalikan rumus, tapi mengabaikan fakta bahwa infrastruktur database SQL kita saat ini sedang sekarat!"</div>""", unsafe_allow_html=True)
        st.write("""Bagaimana CDO bisa mendapatkan data aktual jika kita menderita **latensi sinkronisasi data selama 14 hari**? Database kita memakai sistem *batch processing* kuno! Saya tidak akan mengizinkan tim data science mendeploy model peramalan **Hybrid LSTM** apa pun sebelum kita merombak pipa arsitektur ke **Cloud Hybrid** menggunakan **Streaming Event Broker berbasis Apache Kafka**. Kita harus memotong delay data dari 14 hari langsung ke di bawah 5 detik!""")

    with st.chat_message("assistant", avatar="🔐"):
        st.markdown("<div class='chat-agent-name'>IT Auditor Agent (Governance & Compliance Inspector)</div>", unsafe_allow_html=True)
        st.write("""Saya menengahi debat teknis ini. Berdasarkan kerangka **COBIT 2019**, kepatuhan integrasi data kita berada di ambang batas kritis: **65% (Level 3 - Defined)**. Usulan CIO untuk memigrasikan pipeline ke Kafka sangat krusial untuk menciptakan *Single Source of Truth* otomatis dan memitigasi risiko manipulasi entri manual di lapangan.""")

    with st.chat_message("assistant", avatar="🏛️"):
        st.markdown("<div class='chat-agent-name'>🎯 NexAtlas Core Consensus Verdict</div>", unsafe_allow_html=True)
        st.markdown("""Dewan direksi виртуал menyepakati resolusi terpadu: CFO mengunci anggaran Rp 450 Juta untuk restrukturisasi teknologi, CIO mengomandani migrasi Kafka Pipeline, CDO merombak formula visualisasi berbasis jangkauan aktual lapangan, untuk menyuplai data latensi rendah ke sistem prediksi otonom.""")

    st.divider()

    # --- 3. BIG 4 FRAMEWORK ASSESSMENT GRID ---
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.markdown("### 📊 Data Maturity Scorecard (DAMA-DMBOK Audit)")
        st.code("""
Data Quality        █████████░ 85%
Data Integration    ███████░░░ 72%
Governance          ██████░░░░ 65%
Analytics           ████████░░ 80%
AI Readiness        ███████░░░ 74%
        """, language="text")
        st.markdown("**Overall Maturity Rating:** `Level 3 - Defined` (Proses terstandardisasi seluruh organisasi).")
    
    with col_g2:
        st.markdown("### 🛡️ Risk Assessment Matrix (COBIT 2019 Mapping)")
        st.markdown('<div style="background-color:#2D191E; padding:12px; border-radius:6px; border-left:4px solid #FF7B72; color:#FF7B72; margin-bottom:10px;"><b>🔴 High Risk:</b> Data synchronization lag > 7 days (Triggers systemic warehouse errors)</div>', unsafe_allow_html=True)
        st.markdown('<div style="background-color:#2D2619; padding:12px; border-radius:6px; border-left:4px solid #D4BB6C; color:#D4BB6C; margin-bottom:10px;"><b>🟡 Medium Risk:</b> Incomplete coverage patterns for secondary agricultural crops (Ubi Kayu at 69%)</div>', unsafe_allow_html=True)

    st.divider()

    # --- 4. ROADMAP & WHAT-IF INTERACTIVE ENGINE ---
    st.markdown("### 🔮 Predictive What-If Interactive Engine")
    st.write("Simulasikan opsi intervensi kebijakan taktis Anda berdasarkan pemodelan dewan eksekutif virtual:")
    
    selected_option = st.radio(
        "Select Boardroom Intervention Scenario:",
        ("Scenario Alpha: Restructure field audit workforce (+20% operational alignment)", 
         "Scenario Beta: Approve CIO's Kafka Pipeline + Hybrid LSTM Core Architecture Integration")
)

    if st.button("Initiate Predictive Simulation Run"):
        with st.spinner("Re-calculating multi-agent graph future matrices..."):
            time.sleep(1.2)
        if "Scenario Alpha" in selected_option:
            st.info("""**🔮 Digital Twin Future Projection (Scenario Alpha):**
            * Field validation coverage reaches **95% within two quarters**.
            * Operational cost inflates by **12%** due to workforce expansion.
            * Strategic latency remains trapped at **7 days** due to lack of a real-time event broker architecture.""")
        else:
            st.success("""**🔮 Digital Twin Future Projection (Scenario Beta):**
            * Operational latency completely eliminated **(Data lag slashed from 14 days to < 5 seconds)**.
            * Automated integration mitigates human data reporting entry risks by **91%**.
            * **Financial Impact Potential:** Saves up to **Rp 950 Million / year** in warehouse overhead liquidation.""")

    st.divider()
    
    # Back to Config Boardroom CTA
    if st.button("↩ Exit Strategy Room & Reconfigure Boardroom Settings"):
        st.session_state.simulation_active = False
        st.session_state.chat_history = []
        st.rerun()
