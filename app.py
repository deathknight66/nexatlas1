import streamlit as st
import pandas as pd
import time

# --- BRANDING & UI SETUP (ELITE SYSTEM STYLING) ---
st.set_page_config(
    page_title="NexAtlas AI | Decision Intelligence Platform",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Corporate CSS Architecture (Palantir Matte Dark Interface)
st.markdown("""
    <style>
    .main { background-color: #0B0E14; }
    header { background-color: rgba(0,0,0,0) !important; }
    
    h1, h2, h3, h4, h5 { color: #58A6FF !important; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica; font-weight: 600; }
    p, span, label, li { color: #C9D1D9 !important; }
    
    .hero-portal { background: linear-gradient(135deg, #161B22 0%, #0D1117 100%); padding: 35px; border-radius: 12px; border: 1px solid #30363D; margin-bottom: 30px; box-shadow: 0 4px 20px rgba(0,0,0,0.3); text-align: center; }
    .verdict-box { background-color: #1A1F2C; padding: 30px; border-radius: 12px; border: 1px solid #388BFD; margin-bottom: 25px; }
    .timeline-node { background-color: #161B22; padding: 15px; border-radius: 8px; border-left: 4px solid #D4BB6C; margin-bottom: 10px; }
    .agent-bubble-premium { background-color: #161B22; padding: 20px; border-radius: 8px; border: 1px solid #30363D; margin-bottom: 15px; }
    
    /* Grid Card Systems */
    .profile-card { background-color: #161B22; padding: 20px; border-radius: 8px; border: 1px solid #30363D; height: 100%; }
    .framework-group { background-color: #11151C; padding: 15px; border-radius: 6px; border: 1px solid #21262D; margin-bottom: 10px; }
    .framework-badge { display: inline-block; background-color: #21262D; color: #58A6FF; padding: 4px 10px; border-radius: 4px; border: 1px solid #30363D; font-size: 11px; font-weight: bold; margin: 2px; }
    .evidence-badge { background-color: #21262D; color: #8B949E; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-family: monospace; }
    
    /* Deliverable & Capability Cards */
    .output-card { background-color: #161B22; padding: 15px; border-radius: 8px; border: 1px solid #21262D; text-align: left; height: 100%; }
    .milestone-card { background-color: #161B22; padding: 25px; border-radius: 10px; border: 1px solid #21262D; height: 100%; }
    .status-pill { display: inline-block; padding: 4px 10px; border-radius: 50px; font-size: 10px; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase; margin-bottom: 12px; }
    
    .badge-done { background-color: rgba(46, 160, 67, 0.15); color: #3fb950; border: 1px solid rgba(46, 160, 67, 0.3); }
    .badge-process { background-color: rgba(212, 187, 108, 0.15); color: #d4bb6c; border: 1px solid rgba(212, 187, 108, 0.3); }
    .badge-pending { background-color: rgba(139, 148, 158, 0.15); color: #8b949e; border: 1px solid rgba(139, 148, 158, 0.3); }
    
    .chat-agent-name { font-size: 15px; font-weight: bold; color: #58A6FF; margin-bottom: 2px; }
    .conflict-tag { color: #FF7B72; font-size: 12px; font-weight: bold; margin-bottom: 8px; }
    </style>
""", unsafe_allow_html=True)

if "simulation_active" not in st.session_state:
    st.session_state.simulation_active = False

# Header Terstandarisasi
st.title("🏛️ NexAtlas AI")
st.markdown("<p style='font-size: 16px; color: #8B949E !important;'>Your AI-powered Executive Committee for strategy, technology, and data transformation.</p>", unsafe_allow_html=True)
st.divider()

# --- SIDEBAR: REBRANDED CONSULTING KNOBS ---
st.sidebar.header("⚙️ Simulation Settings")
uploaded_file = st.sidebar.file_uploader("Upload Diagnostic Dataset (PDF, CSV, TXT)", type=["pdf", "csv", "txt", "json"])

st.sidebar.subheader("Configure Simulation Engine")
# Mengubah istilah kaku kodingan menjadi parameter konsultasi eksekutif
disc_rounds = st.sidebar.slider("Simulation Depth (Discussion Rounds)", min_value=5, max_value=50, value=34)
risk_tolerance = st.sidebar.select_slider("Risk Appetite Profile", options=["Conservative", "Balanced", "Aggressive"], value="Balanced")
decision_horizon = st.sidebar.selectbox("Decision Timeline Horizon", ["3 Months", "6 Months", "12 Months", "24 Months"], index=2)
confidence_threshold = st.sidebar.slider("AI Precision Guardrail (%)", min_value=70, max_value=98, value=90)

initiate_sim = st.sidebar.button("📊 Run Multi-Agent Simulation", use_container_width=True)

if initiate_sim:
    st.session_state.simulation_active = True

# --- DYNAMIC INITIAL DATA EVALUATOR ---
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
    
    # --- POINT 1 & 8: REBRANDED HIGH-END HERO LANDING PANEL ---
    st.markdown("""
    <div class="hero-portal">
        <h2 style='margin-top:0; font-size:26px;'>🏛️ NexAtlas AI</h2>
        <p style='font-size: 16px; color: #58A6FF !important; font-weight: bold; margin-bottom: 15px;'>Enterprise Decision Intelligence Platform</p>
        <p style='font-size: 15px; letter-spacing: 2px; color: #8B949E !important;'>ANALYZE. SIMULATE. DECIDE.</p>
        <div style="background-color: #0D1117; padding: 18px 25px; border-radius: 8px; border-left: 4px solid #D4BB6C; margin: 20px auto; max-width: 900px;">
            <i style='color:#C9D1D9; font-size: 14px;'>\"Traditional dashboards explain what happened. NexAtlas simulates why it happened, evaluates risks, and recommends strategic actions based on AI executive deliberation.\"</i>
        </div>
        <p style='font-size:13px; color:#8B949E !important;'>
            💡 <b>Strategic Action:</b> Silakan lakukan pengunggahan berkas data di panel kiri atau klik tombol <b>"Run Multi-Agent Simulation"</b> untuk memulai analisis.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Core Capabilities Quick Matrix
    col_c1, col_c2, col_c3, col_c4 = st.columns(4)
    with col_c1: st.markdown('<div class="output-card" style="text-align:center; border-top:2px solid #58A6FF;"><b>✓ Business Strategy</b></div>', unsafe_allow_html=True)
    with col_c2: st.markdown('<div class="output-card" style="text-align:center; border-top:2px solid #56D364;"><b>✓ Data Governance</b></div>', unsafe_allow_html=True)
    with col_c3: st.markdown('<div class="output-card" style="text-align:center; border-top:2px solid #A371F7;"><b>✓ IT Transformation</b></div>', unsafe_allow_html=True)
    with col_c4: st.markdown('<div class="output-card" style="text-align:center; border-top:2px solid #FF7B72;"><b>✓ Risk Intelligence</b></div>', unsafe_allow_html=True)

    st.write(" ")
    st.write(" ")

    col_left, col_right = st.columns(2)
    with col_left:
        # PROFILE CONTEXT CARD
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

        # POINT 3: ADAPTIVE FRAMEWORK ENGINE GROUPING
        st.markdown("### 🧠 Adaptive Framework Engine")
        st.write("Sistem AI secara otomatis memetakan kluster metodologi berdasarkan dokumen masalah:")
        
        st.markdown("""
        <div class="framework-group">
            <p style="font-size:13px; font-weight:bold; color:#58A6FF; margin:0 0 5px 0;">Business Strategy & Operations</p>
            <span class="framework-badge">SWOT Analysis</span><br><span class="framework-badge">Porter's Five Forces</span><br><span class="framework-badge">McKinsey 7S</span>
        </div>
        <div class="framework-group">
            <p style="font-size:13px; font-weight:bold; color:#56D364; margin:0 0 5px 0;">Data & Corporate Governance</p>
            <span class="framework-badge">DAMA-DMBOK Framework</span><br><span class="framework-badge">COBIT 2019 Standard</span>
        </div>
        <div class="framework-group">
            <p style="font-size:13px; font-weight:bold; color:#A371F7; margin:0 0 5px 0;">Technology Transformation</p>
            <span class="framework-badge">TOGAF Architecture</span><br><span class="framework-badge">ITIL 4 Operations</span>
        </div>
        """, unsafe_allow_html=True)

    with col_right:
        # POINT 2 & 6: VIBRANT EXECUTIVE COMMITTEE ARCHITECTURE WITH ARCHITECT AGENT
        st.markdown("### 👥 Executive Committee Architecture")
        st.write("Struktur komite pengambil keputusan virtual yang ditugaskan dalam kluster simulasi:")
        st.markdown("""
        <div class="profile-card" style="padding:15px;">
            <p style="margin:6px 0;">👔 <b>CEO Agent:</b> Strategic Growth & Market Positioning</p>
            <hr style="border:0; border-top:1px solid #21262D; margin:6px 0;">
            <p style="margin:6px 0;">💰 <b>CFO Agent:</b> Financial Risk & Investment Optimization</p>
            <hr style="border:0; border-top:1px solid #21262D; margin:6px 0;">
            <p style="margin:6px 0;">📊 <b>CDO Agent:</b> Information Management & Data Strategy</p>
            <hr style="border:0; border-top:1px solid #21262D; margin:6px 0;">
            <p style="margin:6px 0;">🏛️ <b>Chief Data Architect Agent:</b> Data Mesh, Medallion Pipeline & Modeling Audit</p>
            <hr style="border:0; border-top:1px solid #21262D; margin:6px 0;">
            <p style="margin:6px 0;">🖥️ <b>CIO Agent:</b> Enterprise Technology Modernization</p>
            <hr style="border:0; border-top:1px solid #21262D; margin:6px 0;">
            <p style="margin:6px 0;">🔐 <b>IT Auditor Agent:</b> Governance, Risk & COBIT Compliance</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()
    
    # POINT 5: VISUAL OUTPUT MATRIX CARDS
    st.markdown("### 📋 Expected Advisory Deliverables Matrix")
    col_v1, col_v2, col_v3, col_v4, col_v5 = st.columns(5)
    with col_v1: st.markdown('<div class="output-card">📄 <b>Executive Summary</b><br><span style="font-size:11px;color:#8B949E;">30-second strategic consensus.</span></div>', unsafe_allow_html=True)
    with col_v2: st.markdown('<div class="output-card">🔬 <b>Root Cause Analysis</b><br><span style="font-size:11px;color:#8B949E;">Framework-driven isolation.</span></div>', unsafe_allow_html=True)
    with col_v3: st.markdown('<div class="output-card">⚠ <b>Risk Heatmap</b><br><span style="font-size:11px;color:#8B949E;">COBIT severity thresholds.</span></div>', unsafe_allow_html=True)
    with col_v4: st.markdown('<div class="output-card">🗺 <b>Transformation Roadmap</b><br><span style="font-size:11px;color:#8B949E;">30-60-90 Day action mapping.</span></div>', unsafe_allow_html=True)
    with col_v5: st.markdown('<div class="output-card">📈 <b>ROI Projection</b><br><span style="font-size:11px;color:#8B949E;">Financial leak calculations.</span></div>', unsafe_allow_html=True)

    # FOOTER ACKNOWLEDGEMENT
    st.write(" ")
    st.markdown("""
    <div class="ack-card">
        <p style="font-size:12px; color:#8B949E; line-height:1.5; margin:0;">
            NexAtlas AI is built upon the open-source <b>MiroFish framework</b> developed by the MiroFish Team and supported by Shanda Group. 
            We sincerely appreciate the contributions of the MiroFish Team and the CAMEL-AI team for advancing multi-agent technology.
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
                <li style="margin-bottom:8px;">Beban <i>inventory holding cost</i> gudang regional membengkak akibat peramalan produksi yang menderita kebutaan dari realitas pasar.</li>
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

        # POINT 4: ENTERPRISE DIGITAL MATURITY SCORECARD
        st.markdown("### 📊 Enterprise Digital Maturity Scorecard")
        col_s1, col_s2, col_s3, col_s4, col_s5 = st.columns(5)
        with col_s1: st.metric(label="Business Strategy Score", value="78 / 100", delta="Level 3 - Defined")
        with col_s2: st.metric(label="Data Capability Score", value="62 / 100", delta="Level 2 - Managed", delta_color="inverse")
        with col_s3: st.metric(label="Technology Architecture", value="55 / 100", delta="Level 2 - Deficit", delta_color="inverse")
        with col_s4: st.metric(label="Corporate Governance", value="71 / 100", delta="Level 3 - Defined")
        with col_s5: st.metric(label="OVERALL MATURITY MATRIX", value="68 / 100", delta="Action Plan Required")

        st.divider()

        # 2. STRATEGIC RISK MATRIX
        st.markdown("### 🛡️ Strategic Risk Assessment Matrix")
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
            st.markdown("<div class='timeline-node'><b>Round 16</b><br><span style='font-size:12px;color:#8B949E;'>Data Architect flags pipeline schema corruption.</span></div>", unsafe_allow_html=True)
        with col_t4:
            st.markdown("<div class='timeline-node'><b>Round 24</b><br><span style='font-size:12px;color:#8B949E;'>CIO isolates SQL replication engine bottleneck.</span></div>", unsafe_allow_html=True)
        with col_t5:
            st.markdown("<div class='timeline-node' style='border-left:4px solid #56D364;'><b>Round 30</b><br><span style='font-size:12px;color:#56D364;'>Consensus reached: Real-time data modernization.</span></div>", unsafe_allow_html=True)

        st.divider()

        st.markdown("### 💬 Virtual Executive Deliberation Auditing")
        st.write("Bongkar transkrip perdebatan taktis untuk mengaudit dasar logika keputusan AI:")

        with st.expander("▼ View Executive Discussion Transcripts (34 Rounds of Deliberation)", expanded=True):
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

            # POINT 6: THE INTEGRATION OF CHIEF DATA ARCHITECT IN DIALOGUE TRANSCRIPT
            st.markdown("""<div class='agent-bubble-premium'>
                <div class='chat-agent-name'>Chief Data Architect Agent (Enterprise Architecture Fellow)</div>
                <div class='conflict-tag'>🛑 Data Architect intervened CDO & CFO Proposals (Reason: Kimball model pipeline cannot scale transactional anomalies)</div>
                <div style='margin-bottom:8px;'><span class='evidence-badge'>Confidence: 93%</span> | <span class='evidence-badge'>Source: DAMA-DMBOK Chapter 4; Medallion Integration Map</span></div>
                <p>Menyambung poin CDO, membalik rumus visualisasi tidak akan menyelesaikan problem integritas jika data di level hulu kotor. Arsitektur data kita saat ini gagal menerapkan prinsip <b>Data Mesh</b>. Replikasi data transaksional dari koridor logistik Lampung patah di level Silver Layer pada Medallion pipeline kita. Solusinya, tata kelola siklus data (Data Lifecycle) wajib dikunci otomatis di hulu.</p>
            </div>""", unsafe_allow_html=True)
            
            st.markdown("""<div class='agent-bubble-premium'>
                <div class='chat-agent-name'>CIO Agent (Technology Transformation Fellow)</div>
                <div class='conflict-tag'>🛑 CIO aligned with Data Architect (Reason: Transactional batch engine creates systemic data latency)</div>
                <div style='margin-bottom:8px;'><span class='evidence-badge'>Confidence: 95%</span> | <span class='evidence-badge'>Source: TOGAF Architecture Mapping; SQL Log Replication Lag</span></div>
                <p>Saya sepakat dengan Data Architect! Masalah fundamental hulu kita adalah pemrosesan batch kuno database SQL yang memicu delay 14 hari. Kita wajib membangun pipa <b>Streaming berbasis Apache Kafka</b> menuju arsitektur Cloud Hybrid. Hanya dengan memangkas delay ke di bawah 5 detik, kita bisa menyuplai data bersih ter-streaming untuk mengaktifkan model prediksi <b>Hybrid LSTM</b>!</p>
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

# --- GLOBAL EXPANDER FOOTER ---
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
