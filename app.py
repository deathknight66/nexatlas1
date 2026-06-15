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

# Custom Corporate CSS Architecture (Clean Matte Dark Theme)
st.markdown("""
    <style>
    .main { background-color: #0B0E14; }
    header { background-color: rgba(0,0,0,0) !important; }
    
    h1, h2, h3, h4, h5 { color: #58A6FF !important; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica; font-weight: 600; }
    p, span, label, li { color: #C9D1D9 !important; }
    
    .hero-portal { background: linear-gradient(135deg, #161B22 0%, #0D1117 100%); padding: 40px; border-radius: 12px; border: 1px solid #30363D; margin-bottom: 30px; box-shadow: 0 4px 20px rgba(0,0,0,0.3); }
    .verdict-box { background-color: #1A1F2C; padding: 30px; border-radius: 12px; border: 1px solid #388BFD; margin-bottom: 25px; }
    .timeline-node { background-color: #161B22; padding: 15px; border-radius: 8px; border-left: 4px solid #D4BB6C; margin-bottom: 10px; }
    .agent-bubble-premium { background-color: #161B22; padding: 20px; border-radius: 8px; border: 1px solid #30363D; margin-bottom: 15px; }
    
    .profile-card { background-color: #161B22; padding: 20px; border-radius: 8px; border: 1px solid #30363D; height: 100%; }
    .framework-badge { display: inline-block; background-color: #21262D; color: #58A6FF; padding: 4px 10px; border-radius: 4px; border: 1px solid #30363D; font-size: 12px; font-weight: bold; margin: 3px; }
    .evidence-badge { background-color: #21262D; color: #8B949E; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-family: monospace; }
    
    /* Executive Phase Milestones Modern Premium Styling */
    .milestone-card { background-color: #161B22; padding: 25px; border-radius: 10px; border: 1px solid #21262D; height: 100%; box-shadow: 0 4px 12px rgba(0,0,0,0.15); }
    .status-pill { display: inline-block; padding: 4px 10px; border-radius: 50px; font-size: 10px; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase; margin-bottom: 12px; }
    
    .badge-done { background-color: rgba(46, 160, 67, 0.15); color: #3fb950; border: 1px solid rgba(46, 160, 67, 0.3); }
    .badge-process { background-color: rgba(212, 187, 108, 0.15); color: #d4bb6c; border: 1px solid rgba(212, 187, 108, 0.3); }
    .badge-pending { background-color: rgba(139, 148, 158, 0.15); color: #8b949e; border: 1px solid rgba(139, 148, 158, 0.3); }
    
    /* System State Ingestion Badges */
    .state-badge-demo { background-color: rgba(212, 187, 108, 0.1); color: #d4bb6c; border: 1px solid #7E6C38; padding: 3px 8px; border-radius: 4px; font-size: 11px; font-weight: bold; }
    .state-badge-live { background-color: rgba(88, 166, 255, 0.1); color: #58A6FF; border: 1px solid #388BFD; padding: 3px 8px; border-radius: 4px; font-size: 11px; font-weight: bold; }
    
    /* Elegant Acknowledgement Footer Box */
    .ack-card { background-color: #11151C; padding: 25px; border-radius: 8px; border: 1px solid #21262D; border-left: 4px solid #8B949E; margin-top: 20px; }
    
    .chat-agent-name { font-size: 15px; font-weight: bold; color: #58A6FF; margin-bottom: 2px; }
    .conflict-tag { color: #FF7B72; font-size: 12px; font-weight: bold; margin-bottom: 8px; }
    .chat-agent-name { font-size: 15px; font-weight: bold; color: #58A6FF; margin-bottom: 5px; }
    </style>
""", unsafe_allow_html=True)

if "simulation_active" not in st.session_state:
    st.session_state.simulation_active = False

st.title("🏛️ NexAtlas AI")
st.markdown("<p style='font-size: 16px; color: #8B949E !important;'>Enterprise Digital Twin & Decision Intelligence Ecosystem</p>", unsafe_allow_html=True)
st.divider()

# --- SIDEBAR EXECUTIVE CONTROL CENTER ---
st.sidebar.header("⚙️ Simulation Settings")

# INPUT 1: DATA LOADING
st.sidebar.subheader("STEP 1: Upload Documents")
uploaded_file = st.sidebar.file_uploader("Upload Diagnostic Dataset (PDF, CSV, TXT)", type=["pdf", "csv", "txt", "json"])

# INPUT 2: OBJECTIVE SCENARIO NARRATIVE
st.sidebar.subheader("STEP 2: Define Strategic Agenda")
default_scenario = "Analyze why PT Maju Bersama Indonesia revenue declined 15% and simulate an executive boardroom session covering strategic positioning."
scenario = st.sidebar.text_area("Core Objective Narrative:", value=default_scenario)

st.sidebar.subheader("Configure Engine")
disc_rounds = st.sidebar.slider("Number of Discussion Rounds", min_value=5, max_value=50, value=34)
risk_tolerance = st.sidebar.select_slider("Risk Tolerance Threshold", options=["Conservative", "Medium", "Aggressive"], value="Medium")
decision_horizon = st.sidebar.selectbox("Decision Horizon", ["3 Months", "6 Months", "12 Months", "24 Months"], index=2)
confidence_threshold = st.sidebar.slider("AI Confidence Guardrail (%)", min_value=70, max_value=98, value=90)

initiate_sim = st.sidebar.button("📊 Run Multi-Agent Simulation", use_container_width=True)

if initiate_sim:
    st.session_state.simulation_active = True

# --- DYNAMIC INGESTION EVALUATOR ---
if uploaded_file is not None:
    state_badge = '<span class="state-badge-live">🟢 CUSTOM ASSET GROUNDED</span>'
    company_name = "Custom Enterprise Node"
    industry_sector = "Extracted from Ingested Schema"
    revenue_baseline = "Analyzing Ledger Boundaries..."
    workforce = "Calculating Operational Nodes..."
    crisis_vector = f"Processing context from file: {uploaded_file.name}"
    strategic_priority = "Executing user-defined simulation metrics"
else:
    state_badge = '<span class="state-badge-demo">🔹 SANDBOX DEMO PREVIEW</span>'
    company_name = "PT Maju Bersama Indonesia"
    industry_sector = "Agriculture & Supply Chain Network"
    revenue_baseline = "Rp 2.4 Trillion"
    workforce = "5,200 Employees (Field & HQ)"
    crisis_vector = "Revenue declined 15% in last 3 quarters"
    strategic_priority = "Cost optimization & data modernization"

# --- SCREEN CONTROLLER: PRE-FLIGHT VS EXECUTIVE WORKSPACE ---
if not st.session_state.simulation_active:
    
    # --- ENTERPRISE HERO PORTAL WITH DYNAMIC OVERVIEW INTEGRATION ---
    st.markdown("""
    <div class="hero-portal">
        <h2 style='margin-top:0;'>🏛️ NexAtlas Virtual Strategy Room</h2>
        <p style='font-size:15px; color:#C9D1D9 !important; line-height:1.6;'>
            NexAtlas AI is an AI-powered enterprise digital twin and advisory platform built upon the MiroFish architecture. 
            It transforms a general-purpose social simulation engine into a corporate intelligence ecosystem where autonomous 
            AI agents collaborate to analyze business strategies, data capabilities, IT governance, and digital transformation scenarios.
        </p>
        <div class="slogan-banner">
            <b style='color:#D4BB6C;'>The Decision Intelligence Core:</b><br>
            <i style='color:#A3A3A3;'>\"Traditional dashboards explain what happened. NexAtlas simulates why it happened, evaluates risks, and recommends strategic actions based on AI executive deliberation.\"</i>
        </div>
        <p style='font-size:14px; margin-bottom:0; color:#58A6FF !important;'>
            💡 <b>Action Required:</b> Silakan lakukan pengunggahan berkas strategis di panel kiri atau tentukan agenda draf objektif Anda, lalu klik tombol <b>"Run Multi-Agent Simulation"</b>.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col_left, col_right = st.columns(2)
    with col_left:
        # 1. PROFILE CONTEXT CARD
        st.markdown(f"### 🏢 Digital Twin Profile Context &nbsp;&nbsp; {state_badge}", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="profile-card">
            <table style="width:100%; border-collapse: collapse;">
                <tr><td style="color:#8B949E; padding:8px 0;"><b>Enterprise Entity:</b></td><td style="font-weight:bold; color:#58A6FF;">{company_name}</td></tr>
                <tr><td style="color:#8B949E; padding:8px 0;"><b>Industry Sector:</b></td><td>{industry_sector}</td></tr>
                <tr><td style="color:#8B949E; padding:8px 0;"><b>Annual Revenue Baseline:</b></td><td>{revenue_baseline}</td></tr>
                <tr><td style="color:#8B949E; padding:8px 0;"><b>Active Workforce:</b></td><td>{workforce}</td></tr>
                <tr><td style="color:#8B949E; padding:8px 0;"><b>Current Crisis Vector:</b></td><td style="color:#FF7B72;">{crisis_vector}</td></tr>
                <tr><td style="color:#8B949E; padding:8px 0;"><b>Strategic Directive:</b></td><td style="color:#56D364;">{strategic_priority}</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

        # 2. CORE ADVISORY DOMAINS & FRAMEWORKS
        st.markdown("### 🚀 Core Advisory Domains & Frameworks")
        st.markdown("""
        <ul style="color:#C9D1D9; margin-left:15px; margin-bottom:15px; font-size:14px;">
            <li><b>Business Strategy & Operations</b></li>
            <li><b>Data Analytics & Business Intelligence</b></li>
            <li><b>IT Governance, Risk & Compliance</b></li>
            <li><b>Digital Transformation & Technology Strategy</b></li>
        </ul>
        """, unsafe_allow_html=True)
        
        frameworks = ["SWOT Analysis", "Porter's Five Forces", "McKinsey 7S", "COBIT 2019", "DAMA-DMBOK", "ITIL 4", "TOGAF Architecture", "Digital Maturity Model"]
        for fw in frameworks:
            st.markdown(f'<span class="framework-badge">✓ {fw}</span>', unsafe_allow_html=True)

    with col_right:
        # 3. EXECUTIVE COMMITTEE ARCHITECTURE
        st.markdown("### 👥 Executive Committee Architecture")
        st.markdown("""
        <div class="agent-card-standby" style="border-top:3px solid #58A6FF; padding:12px; margin-bottom:10px;"><b>👔 CEO Agent (Corporate Strategy Partner)</b></div>
        <div class="agent-card-standby" style="border-top:3px solid #D4BB6C; padding:12px; margin-bottom:10px;"><b>💰 CFO Agent (Veteran Risk & Financial Allocator)</b></div>
        <div class="agent-card-standby" style="border-top:3px solid #56D364; padding:12px; margin-bottom:10px;"><b>📊 CDO Agent (Chief Data Officer Partner)</b></div>
        <div class="agent-card-standby" style="border-top:3px solid #A371F7; padding:12px; margin-bottom:10px;"><b>🖥️ CIO Agent (Technology Transformation Fellow)</b></div>
        <div class="agent-card-standby" style="border-top:3px solid #FF7B72; padding:12px; margin-bottom:10px;"><b>🔐 IT Auditor Agent (Governance & Compliance Inspector)</b></div>
        """, unsafe_allow_html=True)

    st.divider()
    
    # 4. TARGET DELIVERABLES & OFFICIAL ACKNOWLEDGEMENTS
    st.markdown("### 📋 Target Deliverables Matrix")
    st.write("Output Generated: Summary Verdict, Root Cause Analysis, Risk Matrix, Maturity Scorecard, Tech Gap, 90-Day Roadmap, ROI Calculation.")

    # INTEGRASI HALAMAN DEPAN: OFFICIAL ACKNOWLEDGEMENTS CARD
    st.markdown("""
    <div class="ack-card">
        <h4 style="color: #8B949E !important; margin-top:0; font-size:15px; font-weight:600;">🤝 Acknowledgements & Open-Source Foundations</h4>
        <p style="font-size:13px; color:#8B949E; line-height:1.5; margin-bottom:0;">
            NexAtlas AI is proudly built upon the open-source <b>MiroFish framework</b> developed by the <b>MiroFish Team</b> and supported by <b>Shanda Group</b>. 
            We sincerely appreciate the contributions of the MiroFish Team and the <b>CAMEL-AI team</b> for advancing open-source multi-agent simulation technology 
            and enabling the next generation of enterprise digital twin solutions.
        </p>
    </div>
    """, unsafe_allow_html=True)

else:
    # --- ACTIVE WORKSPACE: MULTI-MODE ADVISORY LAYOUT ---
    view_mode = st.radio(
        "Select Boardroom View Perspective:",
        ["🏢 Executive Mode (C-Level Verdict)", "🔬 Analyst Mode (Evidence & Reasoning Chain)"],
        horizontal=True
    )
    st.divider()

    # ==========================================
    # 🏢 OPTION 1: EXECUTIVE MODE (CEO VIEW)
    # ==========================================
    if "Executive Mode" in view_mode:
        
        st.markdown("""
        <div class="verdict-box">
            <h3 style="color: #58A6FF !important; margin-top:0; font-size:22px; font-weight:600;">🧠 NexAtlas Executive Verdict</h3>
            <p style="margin-top:15px; color:#C9D1D9;"><b>Strategic Diagnosis:</b><br>
            Penurunan pendapatan 15% pada PT Maju Bersama Indonesia didorong oleh tiga kegagalan struktural yang saling bertumpu:</p>
            <ul style="color:#C9D1D9; margin-left:20px; padding-left:5px;">
                <li style="margin-bottom:8px;">Metodologi pengukuran KPI visualisasi yang menyesatkan, menyembunyikan <b>31% data asimetris</b> di lapangan.</li>
                <li style="margin-bottom:8px;">Latensi sinkronisasi data operasional hulu-hilir sebesar <b>14 hari</b> (<i>Batch Processing</i> usang).</li>
                <li style="margin-bottom:8px;">Beban <i>inventory holding cost</i> gudang regional membengkak akibat peramalan produksi yang buta dari realitas pasar.</li>
            </ul>
            <p style="color:#C9D1D9; margin-top:20px;"><b>Recommended Actions:</b></p>
            <ol style="color:#C9D1D9; margin-left:20px; padding-left:5px;">
                <li style="margin-bottom:8px;"><b>Koreksi Metrik Dasar:</b> Ganti metrik proyeksi rencana lahan menjadi kalkulasi murni berbasis <b>Total Actual Ground Coverage</b>.</li>
                <li style="margin-bottom:8px;"><b>Modernisasi Arsitektur:</b> Migrasikan jalur data logistik menuju pipa <i>streaming architecture</i> (Kafka) secara instan.</li>
                <li style="margin-bottom:8px;"><b>Deploy Forecasting Model:</b> Integrasikan analitik prediktif berbasis pemodelan <b>Hybrid LSTM</b> untuk mengunci efisiensi gudang.</li>
            </ol>
            <p style="margin-top:20px; margin-bottom:0; color:#C9D1D9; border-top: 1px solid #30363D; padding-top:15px;">
                <b>Expected Impact & Return:</b><br>
                🎯 <span style="color:#56D364;"><b>+35%</b> Data Ground Accuracy</span> | ⚡ <span style="color:#58A6FF;"><b>-90%</b> Decision Latency</span> | 💰 <span style="color:#D4BB6C;"><b>Estimated ROI:</b> 18 Months</span>
            </p>
        </div>
        """, unsafe_allow_html=True)

        # 2. STRATEGIC RISK MATRIX
        st.markdown("### 🛡️ Strategic Risk Assessment")
        col_r1, col_r2, col_r3 = st.columns(3)
        with col_r1:
            st.markdown('<div style="background-color:#2D191E; padding:20px; border-radius:8px; border-left:4px solid #FF7B72; color:#FF7B72; height:100%;"><b>🔴 High Risk:</b> Data synchronization lag > 7 days (Memicu kegagalan pasokan komoditas makro)</div>', unsafe_allow_html=True)
        with col_r2:
            st.markdown('<div style="background-color:#2D2619; padding:20px; border-radius:8px; border-left:4px solid #D4BB6C; color:#D4BB6C; height:100%;"><b>🟡 Medium Risk:</b> Incomplete coverage patterns for secondary crops (Ubi Kayu at 69%)</div>', unsafe_allow_html=True)
        with col_r3:
            st.markdown('<div style="background-color:#192D20; padding:20px; border-radius:8px; border-left:4px solid #56D364; color:#56D364; height:100%;"><b>🟢 Low Risk:</b> Infrastructure availability and legacy SQL database uptime (Maintained at 99.8%)</div>', unsafe_allow_html=True)

        st.divider()

        # 3. 30-60-90 DAYS TRANSFORMATION ROADMAP
        st.markdown("### 🚀 90-Day Transformation Roadmap")
        col_rd1, col_rd2, col_rd3 = st.columns(3)
        with col_rd1:
            st.markdown("""
            <div class="milestone-card">
                <div><span class="status-pill badge-done">COMPLETED</span></div>
                <h4 style="margin: 0 0 10px 0; font-size:16px;">Month 1: Data Alignment</h4>
                <p style="font-size:13px; margin:5px 0; color:#C9D1D9;">✓ Koreksi aturan visualisasi murni berbasis <b>Actual Coverage</b> lapangan.</p>
                <p style="font-size:13px; margin:5px 0; color:#C9D1D9;">✓ Standardisasi template input enumerator lapangan.</p>
            </div>
            """, unsafe_allow_html=True)
        with col_rd2:
            st.markdown("""
            <div class="milestone-card">
                <div><span class="status-pill badge-process">IN PROGRESS</span></div>
                <h4 style="margin: 0 0 10px 0; font-size:16px;">Month 2: Infrastructure</h4>
                <p style="font-size:13px; margin:5px 0; color:#C9D1D9;">• Migrasi repository data logistik menuju Cloud Hybrid Storage.</p>
                <p style="font-size:13px; margin:5px 0; color:#C9D1D9;">• Konstruksi automated executive reporting architecture.</p>
            </div>
            """, unsafe_allow_html=True)
        with col_rd3:
            st.markdown("""
            <div class="milestone-card">
                <div><span class="status-pill badge-pending">SCHEDULED</span></div>
                <h4 style="margin: 0 0 10px 0; font-size:16px;">Month 3: Intelligent AI</h4>
                <p style="font-size:13px; margin:5px 0; color:#C9D1D9;">• Deploy pipeline streaming real-time via Apache Kafka.</p>
                <p style="font-size:13px; margin:5px 0; color:#C9D1D9;">• Aktivasi time-series forecasting engine via <b>Hybrid LSTM</b>.</p>
            </div>
            """, unsafe_allow_html=True)

        st.divider()

        # 4. INTERACTIVE WHAT-IF SIMULATION
        st.markdown("### 🔮 Decision Simulation Engine")
        selected_option = st.radio("Pilih intervensi kebijakan korporasi:", ["Scenario Alpha: Restructure field audit workforce", "Scenario Beta: Deploy Kafka Streaming + Hybrid LSTM Predictive Stack"])
        if st.button("Run Simulation"):
            if "Scenario Beta" in selected_option:
                st.success("🔮 **Simulation Projection:** Latensi data hancur hingga < 5 detik, mengamankan margin modal kerja Rp 950 Juta/tahun.")
            else:
                st.info("🔮 **Simulation Projection:** Jangkauan data naik ke 95% dalam 6 bulan, namun biaya overhead SDM membengkak 12%.")

    # ==========================================
    # 🔬 OPTION 2: ANALYST MODE (AUDITOR/DATA VIEW)
    # ==========================================
    else:
        st.markdown("### 📉 Multi-Agent Consensus Evolution Timeline")
        st.write("Visualisasi pergeseran argumen dewan pakar AI dari perdebatan buntu menuju konsensus strategis:")
        
        col_t1, col_t2, col_t3, col_t4, col_t5 = st.columns(5)
        with col_t1:
            st.markdown("<div class='timeline-node'><b>Round 1</b><br><span style='font-size:12px;color:#8B949E;'>CFO blames financial inefficiency in regional hubs.</span></div>", unsafe_allow_html=True)
        with col_t2:
            st.markdown("<div class='timeline-node'><b>Round 8</b><br><span style='font-size:12px;color:#8B949E;'>CDO isolates metric bias in target vs actual coverage.</span></div>", unsafe_allow_html=True)
        with col_t3:
            st.markdown("<div class='timeline-node'><b>Round 16</b><br><span style='font-size:12px;color:#8B949E;'>CIO flags 14-day SQL database replication lag.</span></div>", unsafe_allow_html=True)
        with col_t4:
            st.markdown("<div class='timeline-node'><b>Round 24</b><br><span style='font-size:12px;color:#8B949E;'>Auditor validates compliance gap via COBIT 2019.</span></div>", unsafe_allow_html=True)
        with col_t5:
            st.markdown("<div class='timeline-node' style='border-left:4px solid #56D364;'><b>Round 30</b><br><span style='font-size:12px;color:#56D364;'>Consensus reached: Real-time data modernization.</span></div>", unsafe_allow_html=True)

        st.divider()

        st.markdown("### 💬 Virtual Executive Deliberation Auditing")
        st.write("Bongkar transkrip perdebatan taktis untuk mengaudit dasar logika keputusan AI:")

        with st.expander("▼ View Executive Discussion Transcripts (30 Rounds of Deliberation)", expanded=True):
            st.markdown("""<div class='agent-bubble-premium'>
                <div class='chat-agent-name'>CEO Agent (Senior Corporate Advisor)</div>
                <div style='margin-bottom:8px;'><span class='evidence-badge'>Confidence: 88%</span> | <span class='evidence-badge'>Source: Corporate KPI Brief Q3</span></div>
                <p>Penurunan pendapatan 15% ini adalah indikator hulu bahwa manajemen menderita kelumpuhan keputusan akibat birokrasi pelaporan kuantitatif yang lamban.</p>
            </div>""", unsafe_allow_html=True)
            
            st.markdown("""<div class='agent-bubble-premium'>
                <div class='chat-agent-name'>CFO Agent (Veteran Risk & Financial Allocator)</div>
                <div style='margin-bottom:8px;'><span class='evidence-badge'>Confidence: 94%</span> | <span class='evidence-badge'>Source: Ledger Inefficiency Audit; Inventory Turnover Log</span></div>
                <p>Bocor Rp 1.2 Miliar/tahun terjadi karena operational drag di gudang regional. Kita mengunci modal kerja memproduksi komoditas berdasarkan Rencana Target, bukan serapan pasar riil.</p>
            </div>""", unsafe_allow_html=True)
            
            st.markdown("""<div class='agent-bubble-premium'>
                <div class='chat-agent-name'>CDO Agent (Chief Data Officer Partner)</div>
                <div class='conflict-tag'>🛑 CDO countered CFO Strategy (Reason: KPI calculation methodology is deeply biased)</div>
                <div style='margin-bottom:8px;'><span class='evidence-badge'>Confidence: 91%</span> | <span class='evidence-badge'>Source: DAMA-DMBOK Quality Registry; Field actual telemetry</span></div>
                <p>Jangan menyalahkan proyeksi gudang sebelum mengoreksi rumus dasarnya! Dashboard lama menghitung performa dari Rencana Target Lahan (data kertas). Faktanya, Total Actual Ground Coverage kita drop hingga 69%! Formula wajib dibalik total.</p>
            </div>""", unsafe_allow_html=True)
            
            st.markdown("""<div class='agent-bubble-premium'>
                <div class='chat-agent-name'>CIO Agent (Technology Transformation Fellow)</div>
                <div class='conflict-tag'>🛑 CIO countered CDO & CFO Proposals (Reason: Infrastructure stack cannot support real-time math)</div>
                <div style='margin-bottom:8px;'><span class='evidence-badge'>Confidence: 95%</span> | <span class='evidence-badge'>Source: TOGAF Architecture Mapping; SQL Log Replication Lag</span></div>
                <p>Anda berdua menuntut pembalikan rumus, tapi mengabaikan latensi sinkronisasi database kita yang delay 14 hari karena pemrosesan batch kuno. Pipa arsitektur wajib dimigrasikan ke Cloud Hybrid menggunakan Event Broker Apache Kafka untuk memotong delay menjadi < 5 detik sebelum mendeploy model peramalan Hybrid LSTM!</p>
            </div>""", unsafe_allow_html=True)

        st.divider()

        # 3. DATA & IT ASSESSMENT MATRIX
        st.markdown("### 📊 Data & IT Capability Assessment")
        col_g1, col_g2 = st.columns(2)
        with col_g1:
            st.markdown("##### **DAMA-DMBOK Capability Profile**")
            st.code("Data Quality: 85% | Data Integration: 72% | Governance: 65%", language="text")
        with col_g2:
            st.markdown("##### **COBIT 2019 Compliance Audit**")
            st.markdown("**Governance Maturity:** `Level 3 - Defined` | Standards applied across corporate data tiers.")

    # --- EXIT SIMULATION CTA ---
    st.divider()
    if st.button("↩ Exit Strategy Room & Reconfigure Settings"):
        st.session_state.simulation_active = False
        st.rerun()

# --- GLOBAL EXPANDER FOOTER (SINKRON DI KEDUA MODE) ---
st.write(" ")
st.write(" ")
with st.expander("ℹ️ About NexAtlas AI & Strategic Methodology"):
    st.markdown("""
    NexAtlas AI is an AI-powered enterprise digital twin and advisory platform built upon the MiroFish architecture. 
    It transforms a general-purpose social simulation engine into a corporate intelligence ecosystem where autonomous 
    AI agents collaborate to analyze complex organizational environments.
    
    **Core Advisory Domains Covered:**
    * Business Strategy & Operations
    * Data Analytics & Business Intelligence
    * IT Governance, Risk & Compliance
    * Digital Transformation & Technology Strategy
    
    **Acknowledgements:**
    NexAtlas AI is built upon the open-source MiroFish framework developed by the **MiroFish Team** and supported by **Shanda Group**. 
    We sincerely appreciate the contributions of the MiroFish Team and the **CAMEL-AI team** for advancing open-source multi-agent simulation technology.
    """)
