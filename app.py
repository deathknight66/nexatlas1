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

st.markdown("""
    <style>
    .main { background-color: #0B0E14; }
    header { background-color: rgba(0,0,0,0) !important; }
    h1, h2, h3, h4 { color: #58A6FF !important; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica; font-weight: 600; }
    p, span, label { color: #C9D1D9 !important; }
    .hero-portal { background: linear-gradient(135deg, #161B22 0%, #0D1117 100%); padding: 40px; border-radius: 12px; border: 1px solid #30363D; margin-bottom: 30px; box-shadow: 0 4px 20px rgba(0,0,0,0.3); }
    .verdict-box { background-color: #161B22; padding: 30px; border-radius: 12px; border: 1px solid #388BFD; margin-bottom: 25px; }
    .consensus-box { background-color: #1F241F; padding: 20px; border-radius: 8px; border-left: 5px solid #238636; margin-top: 15px; }
    .agent-card-standby { background-color: #161B22; padding: 20px; border-radius: 8px; border: 1px solid #21262D; border-top: 3px solid #8B949E; text-align: left; margin-bottom: 15px; }
    .agent-status-dot { height: 8px; width: 8px; background-color: #56D364; border-radius: 50%; display: inline-block; margin-right: 6px; }
    .slogan-banner { background-color: #0D1117; padding: 15px 25px; border-radius: 8px; border-left: 4px solid #D4BB6C; margin: 20px 0; }
    </style>
""", unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "avatar": "🏛️", "name": "NexAtlas Engine", "content": "Executive Boardroom initialized with 30+ years institutional wisdom. Awaiting diagnostic data or high-stakes crisis scenarios."}
    ]

st.title("🏛️ NexAtlas AI")
st.markdown("<p style='font-size: 16px; color: #8B949E !important;'>Enterprise Digital Twin & Decision Intelligence Ecosystem</p>", unsafe_allow_html=True)
st.divider()

# --- SIDEBAR CONTROL CENTER ---
st.sidebar.header("⚙️ Control Center")
st.sidebar.subheader("📥 Ingest Data")
uploaded_file = st.sidebar.file_uploader("Upload Enterprise Data (PDF, CSV, TXT)", type=["pdf", "csv", "txt", "json"])

if uploaded_file is not None:
    st.sidebar.success(f"✅ Context Loaded: {uploaded_file.name}")
    file_status = f"Context Source: **{uploaded_file.name}**"
else:
    file_status = "Context Source: Regional Strategic Supply Chain Dataset."

st.sidebar.subheader("🔮 Scenario Injection")
scenario = st.sidebar.text_area("Specify Core Objective:", 
    "Analyze why PT Maju Bersama Indonesia revenue declined 15% and simulate an executive boardroom session.")

initiate_sim = st.sidebar.button("Initiate Digital Twin Simulation")

# --- MAIN WORKSPACE LOGIC ---
if initiate_sim or uploaded_file is not None or len(st.session_state.chat_history) > 1:
    
    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        st.metric(label="Strategic Health Score", value="68 / 100", delta="-14% Volatility Risk")
    with col_m2:
        st.metric(label="Enterprise Risk Index", value="🔴 CRITICAL ALERT", delta="Structural Leakage Detected")
    with col_m3:
        st.metric(label="Decision Latency Gap", value="14 Days Lag", delta="Action Required Instantly", delta_color="inverse")

    st.divider()

    st.markdown("### 💬 Live Multi-Agent Boardroom Debate & Simulation")
    st.write("Jajaran Advisor Utama (25+ Tahun Pengalaman Industri) sedang membedah anomali sistem Anda:")

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"], avatar=msg["avatar"]):
            st.markdown(f"### {msg['name']}")
            st.write(msg["content"])
            if "divider" in msg:
                st.divider()

    if user_query := st.chat_input("Tantang analisis dewan direksi senior di sini..."):
        st.session_state.chat_history.append({"role": "user", "avatar": "👤", "name": "Executive (You)", "content": user_query})
        
        with st.spinner("Jajaran Executive Partner sedang melakukan konvergensi strategi..."):
            time.sleep(2)
            query_lower = user_query.lower()
            
            if "maju bersama" in query_lower or "revenue" in query_lower or "decline" in query_lower or "turun" in query_lower:
                
                # CEO Agent - The Master Strategist
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "👔", "name": "👔 CEO Agent (Senior Corporate Advisor)",
                    "content": """Pernyataan bahwa pasar sedang lesu adalah alasan klasik manajemen untuk menutupi **kebutaan operasional**. Penurunan 15% pada PT Maju Bersama Indonesia adalah indikator hulu bahwa kita kehilangan kontrol atas rantai pasok wilayah. 

Selama 25 tahun saya memimpin transformasi, polanya selalu sama: eksekutif terlalu silau dengan laporan pertumbuhan makro di atas kertas, tapi menutup mata terhadap *data asymmetry* di tingkat akar rumput. Kita tidak sedang kekurangan data; kita sedang menderita **kelumpuhan keputusan** akibat birokrasi pelaporan kuantitatif yang lamban."""
                })
                
                # CFO Agent - The Ruthless Capital Allocator
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "💰", "name": "💰 CFO Agent (Veteran Risk & Financial Allocator)",
                    "content": """Mari kita bicara angka riil, bukan justifikasi naratif. Bocor **Rp 1.2 Miliar per tahun** itu adalah *bleeding* modal kerja yang sangat tidak bisa ditoleransi. Masalah fundamentalnya bukan di tim penjualan, melainkan pada **operational drag** di gudang regional logistik. 

Kita mengunci likuiditas perusahaan untuk memproduksi komoditas berdasarkan *Rencana Target Lahan*—sebuah metrik fiktif warisan birokrasi lama yang tidak mencerminkan daya serap pasar riil. Akibatnya? *Inventory holding cost* kita membengkak dan memakan margin laba bersih. Berhenti mendanai intuisi; setiap rupiah ekspansi harus dikunci oleh kepastian serapan data lapangan."""
                })
                
                # Senior Data Analyst - The Skeptical Methodologist
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "📊", "name": "📊 Senior Data Analyst (Principal Decision Intelligence)",
                    "content": """Saya harus bersikap sangat keras pada metode visualisasi yang Anda gunakan saat ini. Tim visualisasi Anda masih terjebak pada paradigma visual kosmetik Power BI: menyajikan grafik indah tapi menyesatkan. Dashboard Anda mengukur rasio performa komoditas dari *Rencana Target Coverage Lahan*. Itu adalah ilusi optik korporat! 

Kenyataan di lapangan menunjukkan jangkauan data aktual untuk Ubi Kayu drop hingga **69%**. Manajemen mengira mereka aman karena target di atas kertas terpenuhi, padahal kenyataannya rantai pasok kita sedang mengalami kekosongan pasokan secara riil. Mulai hari ini, **rumus perhitungan wajib dibalik secara radikal: ukur efisiensi murni dari Total Actual Coverage**, bukan dari rencana di atas kertas. Jika metrik dasarnya salah, model AI tercanggih pun hanya akan menghasilkan keputusan salah yang terotomatisasi."""
                })
                
                # CTO & Pipeline Engineer - The Deep-Tech Pragmatist
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "🏗", "name": "🏗️ CTO & Pipeline Architect (Enterprise Tech Fellow)",
                    "content": """Dari sisi infrastruktur, arsitektur data Anda saat ini adalah peninggalan dekade lalu yang dipaksakan hidup. **Latensi sinkronisasi data 14 hari** itu adalah bencana untuk bisnis modern. Anda tidak bisa membangun sistem deteksi anomali yang presisi jika database Anda masih mengandalkan sistem *SQL Batch Processing* tradisional yang kaku.

Rekomendasi teknis saya tidak bisa ditawar: bongkar *pipeline* lama, migrasikan ke arsitektur **Cloud Hybrid**, dan pasang **Event Broker berbasis Apache Kafka** untuk menangani *streaming data telemetry* langsung dari lapangan. Infrastruktur ini yang akan memotong *delay* dari 14 hari menjadi **di bawah 5 detik (Near Real-Time)**. Data dengan latensi super rendah inilah yang krusial untuk menyuplai algoritma **Hybrid LSTM** kita agar mampu memprediksi volatilitas harga dan volume panen secara akurat sebelum kerugian finansial terjadi."""
                })
                
                # IT Auditor Agent - The Governance Gatekeeper
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "🔐", "name": "🔐 IT Auditor Agent (Principal Risk & Governance)",
                    "content": """Teknologi hebat tanpa tata kelola adalah resep instan menuju kegagalan audit. Kepatuhan integrasi data kita berada di angka **65% (Level 3 - Defined)**, yang artinya standardisasi input data dari para enumerator di lapangan sangat rentan terhadap *human error* dan manipulasi data kuantitatif. 

Sebelum CTO menerapkan model prediksi canggihnya, kita wajib memberlakukan kerangka kerja *Data Governance* yang ketat bulan ini. Setiap data masuk harus melewati validasi aturan otomatis di tingkat hulu (*edge logging*) untuk menjamin *Single Source of Truth* yang bersih dan sah secara hukum korporasi."""
                })
                
                # Consensus Summary
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "🎯", "name": "🎯 NexAtlas Strategic Consensus Verdict",
                    "content": """
### 🏛️ Executive Transformation Blueprint (Big 4 Advisory Standard)

| Pilar Strategis | Rekomendasi Taktis Intervensi Senior | Indikator Dampak Finansial | Target Ketat |
| :--- | :--- | :--- | :--- |
| **Metrik Analytics** | Koreksi total kalkulasi visualisasi; wajib berbasis **Total Actual Coverage**. | Menghilangkan bias prediksi manajemen | Minggu 1-2 |
| **Data Engine** | Deploy arsitektur Cloud Hybrid & Event Broker (Kafka Pipeline). | Memangkas latensi data dari 14 hari ke < 5 detik | Bulan 1 |
| **Decision AI** | Aktivasi pemodelan prediktif berbasis arsitektur **Hybrid LSTM / CNN-LSTM**. | Memitigasi operational loss & optimasi gudang | Bulan 2-3 |

**🔮 Hasil Simulasi Prediktif (What-If Simulation):**
Jika dewan direksi memilih **Skenario B (Implementasi IoT + Real-time Streaming Pipeline)**, sistem memproyeksikan **pemulihan margin pendapatan sebesar Rp 950 Juta pada kuartal berikutnya** serta meningkatkan kecepatan respons kebijakan C-Level sebesar **35%**.""",
                    "divider": True
                })
            else:
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "🏛️", "name": "NexAtlas Consensus", 
                    "content": f"Pertanyaan Anda mengenai '{user_query}' telah dievaluasi oleh dewan penasihat senior. Prinsip dasar kami: Jangan selesaikan masalah struktural dengan perbaikan kosmetik di hilir. Perbaiki tata kelola validasi data aktualnya terlebih dahulu."
                })
        st.rerun()

else:
    # --- LANDING PAGE PORTAL ---
    st.markdown("""
    <div class="hero-portal">
        <h2 style='margin-top:0;'>🏛️ NexAtlas Virtual Strategy Room</h2>
        <p style='font-size:15px; color:#8B949E !important;'>
            Selamat datang di ekosistem Digital Twin korporat. Sistem ini mengorkestrasi <b>Multi-Agent Network (1M Graph Nodes)</b> 
            untuk menjalankan simulasi skenario taktis, pemetaan matriks risiko Big 4, serta pembongkaran bias metrik bisnis secara otonom.
        </p>
        <div class="slogan-banner">
            <b style='color:#D4BB6C;'>The Decision Intelligence Core:</b><br>
            <i style='color:#C9D1D9;'>\"Power BI tells you <b>what</b> happened. NexAtlas tells you <b>why</b> it happened, what the risks are, what needs to be done, and <b>what will happen</b> if decision A or B is taken.\"</i>
        </div>
        <p style='font-size:14px; margin-bottom:0; color:#58A6FF !important;'>
            💡 <b>Action Required:</b> Silakan unggah file rahasia perusahaan Anda di panel kiri atau langsung klik tombol <b>"Initiate Digital Twin Simulation"</b> untuk mengaktifkan ruang rapat dewan direksi.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 👥 Orchestration Nodes Status (Agents Standby)")
    st.write("Jajaran penasihat ahli AI yang saat ini terpasang di dalam kluster simulasi Anda:")
    
    col_a1, col_a2, col_a3, col_a4 = st.columns(4)
    with col_a1:
        st.markdown("""
        <div class="agent-card-standby">
            <span class="agent-status-dot"></span><b>CEO Agent</b><br>
            <span style='font-size:12px; color:#8B949E;'>Type: ENTJ (The Commander)</span><br>
            <p style='font-size:13px; margin-top:5px;'>Fokus pada penyelarasan strategi makro, mitigasi krisis, dan akselerasi pertumbuhan pendapatan.</p>
        </div>
        """, unsafe_allow_html=True)
    with col_a2:
        st.markdown("""
        <div class="agent-card-standby" style="border-top: 3px solid #D4BB6C;">
            <span class="agent-status-dot"></span><b>CFO Agent</b><br>
            <span style='font-size:12px; color:#8B949E;'>Type: ESTJ (The Executive)</span><br>
            <p style='font-size:13px; margin-top:5px;'>Bertanggung jawab menghitung kebocoran modal, estimasi ROI investasi sistem, dan efisiensi logistik.</p>
        </div>
        """, unsafe_allow_html=True)
    with col_a3:
        st.markdown("""
        <div class="agent-card-standby" style="border-top: 3px solid #58A6FF;">
            <span class="agent-status-dot"></span><b>Senior Data Analyst</b><br>
            <span style='font-size:12px; color:#8B949E;'>Type: INTJ (The Architect)</span><br>
            <p style='font-size:13px; margin-top:5px;'>Spesialis validasi kuantitatif. Berfokus membedah bias data dari jangkauan aktual lapangan.</p>
        </div>
        """, unsafe_allow_html=True)
    with col_a4:
        st.markdown("""
        <div class="agent-card-standby" style="border-top: 3px solid #A371F7;">
            <span class="agent-status-dot"></span><b>CTO & Pipeline Engineer</b><br>
            <span style='font-size:12px; color:#8B949E;'>Type: ISTJ (The Inspector)</span><br>
            <p style='font-size:13px; margin-top:5px;'>Arsitek pipa data. Menangani skalabilitas cloud, arsitektur Kafka, dan deployment model Hybrid LSTM.</p>
        </div>
        """, unsafe_allow_html=True)
