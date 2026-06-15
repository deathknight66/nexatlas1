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
            time.sleep(1.5)
            query_lower = user_query.lower()
            
            # --- CONTEXT DETECTION (PT MAJU BERSAMA / REVENUE CRISIS) ---
            is_maju_bersama_context = "maju" in query_lower or "revenue" in query_lower or "decline" in query_lower or "turun" in query_lower or "dasar" in query_lower or "strategi" in query_lower or ("maju bersama" in scenario.lower())
            
            if is_maju_bersama_context:
                
                # JIKA USER MENANYAKAN "DASARNYA APA?" / "KENAPA?"
                if "dasar" in query_lower or "kenapa" in query_lower or "why" in query_lower or "alasan" in query_lower:
                    st.session_state.chat_history.append({
                        "role": "assistant", "avatar": "📊", "name": "📊 Senior Data Analyst (Principal Decision Intelligence)",
                        "content": """Dasar empirisnya sangat kokoh: audit internal Digital Twin kami menemukan adanya **diskrepansi fatal sebesar 31%** pada sektor komoditas sekunder. Laporan Power BI bulanan manajemen mencatat efisiensi 100% karena dihitung dari *Rencana Target Lahan* (data di atas kertas). 

Namun, jangkauan riil (*Actual Coverage*) di lapangan hanya menyentuh **69%**. Selisih 31% data gaib inilah yang membuat estimasi suplai kita buta dan memicu penumpukan *overhead* gudang yang memakan pendapatan."""
                    })
                    st.session_state.chat_history.append({
                        "role": "assistant", "avatar": "🏗", "name": "🏗️ CTO & Pipeline Architect (Enterprise Tech Fellow)",
                        "content": """Menambahkan dari kacamata arsitektur teknis, dasarnya adalah **data stagnation**. Delay 14 hari dalam sinkronisasi SQL database berarti keputusan taktis manajemen hari ini didasarkan pada kondisi logistik dua minggu lalu. Berjalan di pasar volatil dengan data kedaluwarsa adalah alasan utama mengapa kebocoran Rp 1.2 Miliar ini terjadi tanpa terdeteksi sistem pemantauan lama Anda."""
                    })
                
                # JIKA USER MENANYAKAN "STRATEGI AWALNYA APA?" / "SOLUSI?"
                elif "strategi" in query_lower or "solusi" in query_lower or "langkah" in query_lower or "awal" in query_lower:
                    st.session_state.chat_history.append({
                        "role": "assistant", "avatar": "👔", "name": "👔 CEO Agent (Senior Corporate Advisor)",
                        "content": """Strategi awal PT Maju Bersama terlalu berfokus pada **agresivitas ekspansi hilir** tanpa memperkuat fundamen *Data Supply Chain* di hulu. Manajemen memacu tim penjualan untuk mengejar omset, namun rantai input data kuantitatif dari enumerator lapangan dibiarkan manual dan lamban. Strategi awal yang buta koordinasi inilah yang menciptakan *blind spot* operasional."""
                    })
                    st.session_state.chat_history.append({
                        "role": "assistant", "avatar": "💰", "name": "💰 CFO Agent (Veteran Risk & Financial Allocator)",
                        "content": """Benar, strategi spekulatif itu harus segera kita akhiri. Langkah pemulihan instan kita adalah mematikan sistem pelaporan *batch* kuno dan mengalihkan anggaran modal kerja untuk menerapkan **Skenario B (Kafka Pipeline + Hybrid LSTM)**. Mitigasi risiko ini diproyeksikan langsung menyelamatkan margin laba sebesar **Rp 950 Juta pada kuartal depan**."""
                    })
                
                # RESPONS DEFAULT MULTI-AGENT JIKA PERTANYAAN PERTAMA KALI ATAU UMUM
                else:
                    st.session_state.chat_history.append({
                        "role": "assistant", "avatar": "👔", "name": "👔 CEO Agent (Senior Corporate Advisor)",
                        "content": """Penurunan pendapatan **15% pada PT Maju Bersama Indonesia** adalah krisis eksekusi struktural. Kita terlalu lambat merespons anomali pasar karena tata kelola informasi kita menderita kelumpuhan keputusan akibat data birokrasi pelaporan yang usang."""
                    })
                    st.session_state.chat_history.append({
                        "role": "assistant", "avatar": "💰", "name": "💰 CFO Agent (Veteran Risk & Financial Allocator)",
                        "content": """Kebocoran ini setara dengan **kerugian finansial Rp 1.2 Miliar/tahun**. Kita memproduksi barang berdasarkan target rencana, padahal permintaan pasar meleset jauh. Ini inefisiensi modal kerja yang sangat fatal."""
                    })
                    st.session_state.chat_history.append({
                        "role": "assistant", "avatar": "📊", "name": "📊 Senior Data Analyst (Principal Decision Intelligence)",
                        "content": """Biang keroknya ada pada bias rumus visualisasi dashboard lama Anda yang menghitung performa dari *Rencana Target Lahan*. Lapangan mencatat jangkauan aktual (*Actual Coverage*) komoditas drop ke **69%**. Balik rumus kalkulasinya ke basis jangkauan riil sekarang juga!"""
                    })
                    st.session_state.chat_history.append({
                        "role": "assistant", "avatar": "🏗", "name": "🏗️ CTO & Pipeline Architect (Enterprise Tech Fellow)",
                        "content": """Latensi sinkronisasi data 14 hari adalah pemicunya. Solusi mutlak: ganti pipa data lama dengan **Event Broker berbasis Apache Kafka** terintegrasi arsitektur **Cloud Hybrid** untuk menyuplai model forecasting **Hybrid LSTM** secara real-time (< 5 detik)."""
                    })
                    st.session_state.chat_history.append({
                        "role": "assistant", "avatar": "🎯", "name": "🎯 NexAtlas Strategic Consensus Verdict",
                        "content": """
### 🏛️ Executive Transformation Blueprint (Big 4 Advisory Standard)

| Pilar Strategis | Rekomendasi Taktis Intervensi Senior | Indikator Dampak Finansial | Target Ketat |
| :--- | :--- | :--- | :--- |
| **Metrik Analytics** | Koreksi total kalkulasi visualisasi; wajib berbasis **Total Actual Coverage**. | Menghilangkan bias prediksi manajemen | Minggu 1-2 |
| **Data Engine** | Deploy arsitektur Cloud Hybrid & Event Broker (Kafka Pipeline). | Memangkas latensi data dari 14 hari ke < 5 detik | Bulan 1 |
| **Decision AI** | Aktivasi pemodelan prediktif berbasis arsitektur **Hybrid LSTM / CNN-LSTM**. | Memitigasi operational loss & optimasi gudang | Bulan 2-3 |
""", "divider": True
                    })
            else:
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "🏛️", "name": "NexAtlas Consensus", 
                    "content": f"Pertanyaan mengenai '{user_query}' telah diproses. Seluruh jajaran direksi menyarankan untuk mengunci parameter kalkulasi operasional berdasarkan kondisi data aktual lapangan."
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
