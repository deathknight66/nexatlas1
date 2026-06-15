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
            
            # --- DETEKSI SKENARIO SENTIMEN / VIRAL / JALAN RUSAK / DATA SOSIAL ---
            is_sentiment_query = "sentimen" in query_lower or "viral" in query_lower or "sosial" in query_lower or "jalan" in query_lower or "komplain" in query_lower or "masyarakat" in query_lower
            is_maju_bersama_context = "maju" in query_lower or "revenue" in query_lower or "decline" in query_lower or "turun" in query_lower or "dasar" in query_lower or "strategi" in query_lower
            
            if is_sentiment_query:
                # CEO Agent
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "👔", "name": "👔 CEO Agent (Senior Corporate Advisor)",
                    "content": """Sentimen publik yang Anda unggah dalam file CSV tersebut adalah **leading indicator atas risiko operasional makro**. Di era digitalisasi ini, jika narasi viral mengenai isu sosial, pembangunan macet, atau infrastruktur jalan rusak di daerah operasional (seperti koridor Lampung) menyentuh angka sentimen negatif di atas 70%, itu bukan sekadar riak kecil di media sosial.

Itu adalah alarm keras bahwa legitimasi operasional kita terancam. Ketika persepsi publik hancur, koordinasi regulasi dengan birokrasi lokal akan otomatis mengeras dan biayanya sangat mahal."""
                })
                
                # CFO Agent
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "💰", "name": "💰 CFO Agent (Veteran Risk & Financial Allocator)",
                    "content": """Saya melihat korelasi finansial langsung dari grafik sentimen negatif ini. Ambil contoh isu konkret: keluhan masif tentang infrastruktur jalan rusak. Keluhan publik ini bertransformasi menjadi **real financial drag** pada neraca kas kita. 

Kendaraan logistik kita mengalami depresiasi aset 20% lebih cepat, konsumsi bahan bakar membengkak, dan *delivery time variance* naik tak terkendali. Sentimen negatif adalah cerminan langsung dari inefisiensi biaya operasional riil yang belum tercatat di sistem akuntansi internal Anda."""
                })
                
                # Senior Data Analyst
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "📊", "name": "📊 Senior Data Analyst (Principal Decision Intelligence)",
                    "content": """Analisis teks (*Text Analytics*) pada dataset `combine (1).csv` mengonfirmasi adanya polarisasi kluster keluhan yang sangat pekat. Masalahnya, sistem monitoring Anda saat ini buta terhadap data tidak terstruktur (*unstructured data*) seperti ini. 

Jika laporan performa internal mengklaim target infrastruktur beres 90%, sementara *public sentiment registry* mencatat keluhan 80% negatif, artinya terjadi **validasi asimetris**. Metrik internal Anda tidak membumi. Kita wajib mengintegrasikan indeks kepuasan riil ini ke dalam penentuan prioritas alokasi coverage lahan."""
                })
                
                # CTO & Pipeline Engineer
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "🏗", "name": "🏗️ CTO & Pipeline Architect (Enterprise Tech Fellow)",
                    "content": """Untuk menangkap pergerakan sentimen yang dinamis ini, mengandalkan unggahan file CSV manual seperti ini sangat tidak efisien. Kita butuh solusi automasi di level hulu.

Rekomendasi arsitektur saya: Kita harus mendeploy sebuah **NLP Ingestion Pipeline** menggunakan model bahasa lokal yang dituning (seperti IndoBERT/RoBERTa) untuk mem-parsing dialek dan slang lokal secara akurat. Pipeline ini harus dikaitkan langsung ke **Kafka Event Broker** yang sudah kita bahas, sehingga setiap ada lonjakan komplain viral di lapangan, sistem kecerdasan **Hybrid LSTM** kita bisa langsung menyesuaikan prediksi risiko distribusi logistik secara *near real-time* (< 5 detik)."""
                })
                
                # Consensus Summary
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "🎯", "name": "🎯 NexAtlas Strategic Consensus Verdict",
                    "content": """
### 📋 Public Sentiment Crisis Mitigation Matrix

| Parameter Krisis | Analisis Akar Masalah (AI Core) | Solusi Arsitektur | Target Pemulihan |
| :--- | :--- | :--- | :--- |
| **Volatilitas Isu Sosial** | Sentimen negatif bertindak sebagai penanda disrupsi distribusi fisik lapangan. | Integrasi *Public Sentiment Index* ke Decision Dashboard. | Minggu 1 |
| **Infrastruktur Defisit** | Keluhan jalan rusak berkolerasi dengan lonjakan biaya perawatan armada logistik. | Audit rute alternatif menggunakan *geo-spatial tracking*. | Minggu 2-3 |
| **Automasi Data** | Pemrosesan file data keluhan masih bersifat manual (*batch CSV*). | Implementasi *Streaming NLP Telemetry Pipeline* berbasis Kafka. | Bulan 1 |
""", "divider": True
                })

            # --- CONTEXT DETEKSI MAJU BERSAMA ---
            elif is_maju_bersama_context:
                if "dasar" in query_lower or "kenapa" in query_lower or "why" in query_lower or "alasan" in query_lower:
                    st.session_state.chat_history.append({
                        "role": "assistant", "avatar": "📊", "name": "📊 Senior Data Analyst (Principal Decision Intelligence)",
                        "content": """Dasar empirisnya sangat kokoh: audit internal Digital Twin kami menemukan adanya **diskrepansi fatal sebesar 31%** pada sektor komoditas sekunder. Jangkauan riil (*Actual Coverage*) di lapangan hanya menyentuh **69%**, sementara target di atas kertas diklaim sempurna. Selisih data gaib inilah pemicunya."""
                    })
                elif "strategi" in query_lower or "solusi" in query_lower or "langkah" in query_lower or "awal" in query_lower:
                    st.session_state.chat_history.append({
                        "role": "assistant", "avatar": "👔", "name": "👔 CEO Agent (Senior Corporate Advisor)",
                        "content": """Strategi awal PT Maju Bersama terlalu berfokus pada agresivitas ekspansi hilir tanpa memperkuat fundamen *Data Supply Chain* di hulu. Langkah pemulihan instan kita adalah mengalihkan anggaran modal kerja untuk menerapkan **Skenario B (Kafka Pipeline + Hybrid LSTM)** guna menyelamatkan margin laba sebesar **Rp 950 Juta**."""
                    })
                else:
                    st.session_state.chat_history.append({
                        "role": "assistant", "avatar": "👔", "name": "👔 CEO Agent (Senior Corporate Advisor)",
                        "content": """Penurunan pendapatan **15% pada PT Maju Bersama Indonesia** adalah krisis eksekusi struktural akibat data birokrasi pelaporan yang usang."""
                    })
            
            # --- DEFAULT FALLBACK ---
            else:
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "🏛️", "name": "NexAtlas Consensus", 
                    "content": f"Pertanyaan mengenai '{user_query}' telah dievaluasi oleh dewan penasihat senior. Prinsip dasar kami: Jangan selesaikan masalah struktural dengan perbaikan kosmetik di hilir. Perbaiki tata kelola validasi data aktualnya terlebih dahulu."
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
