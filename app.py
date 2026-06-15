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

# Rombak total CSS menggunakan warna matte dark korporat & kartu modern (Anti-Dashed-Border-Jelek)
st.markdown("""
    <style>
    /* Mengubah warna dasar workspace */
    .main { background-color: #0B0E14; }
    header { background-color: rgba(0,0,0,0) !important; }
    
    /* Font & Typography */
    h1, h2, h3, h4 { color: #58A6FF !important; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica; font-weight: 600; }
    p, span, label { color: #C9D1D9 !important; }
    
    /* Container Premium (Glassmorphism & Matte Gray) */
    .hero-portal { background: linear-gradient(135deg, #161B22 0%, #0D1117 100%); padding: 40px; border-radius: 12px; border: 1px solid #30363D; margin-bottom: 30px; box-shadow: 0 4px 20px rgba(0,0,0,0.3); }
    .verdict-box { background-color: #161B22; padding: 30px; border-radius: 12px; border: 1px solid #388BFD; margin-bottom: 25px; }
    .consensus-box { background-color: #1F241F; padding: 20px; border-radius: 8px; border-left: 5px solid #238636; margin-top: 15px; }
    
    /* Grid Kartu Agen Standby */
    .agent-card-standby { background-color: #161B22; padding: 20px; border-radius: 8px; border: 1px solid #21262D; border-top: 3px solid #8B949E; text-align: left; margin-bottom: 15px; }
    .agent-status-dot { height: 8px; width: 8px; background-color: #56D364; border-radius: 50%; display: inline-block; margin-right: 6px; }
    
    /* Slogan Banner */
    .slogan-banner { background-color: #0D1117; padding: 15px 25px; border-radius: 8px; border-left: 4px solid #D4BB6C; margin: 20px 0; }
    </style>
""", unsafe_allow_html=True)

# Inisialisasi Chat History awal
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "avatar": "🏛️", "name": "NexAtlas Engine", "content": "Executive Boardroom initialized. Drop your corporate diagnostic document or enter your strategic crisis scenario."}
    ]

# Header Utama (Sleek and Clean)
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
# Jalankan dashboard aktif hanya jika tombol ditekan, file dimasukkan, atau chat sudah berjalan
if initiate_sim or uploaded_file is not None or len(st.session_state.chat_history) > 1:
    
    # Top Tier Financial & Operation Status Metrics
    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        st.metric(label="Strategic Health Score", value="68 / 100", delta="-14% Crisis Mode")
    with col_m2:
        st.metric(label="Enterprise Risk Index", value="🔴 CRITICAL", delta="Revenue Leakage Detected")
    with col_m3:
        st.metric(label="Decision Latency", value="14 Days Lag", delta="Action Required", delta_color="inverse")

    st.divider()

    # --- CHATROOM BOARDROOM DISCUSSION ---
    st.markdown("### 💬 Live Multi-Agent Boardroom Debate & Simulation")
    st.write("Jajaran penasihat AI mandiri mendiagnosis data Anda. Ketik pertanyaan di bawah untuk menantang analisis mereka.")

    # Render Chat History
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"], avatar=msg["avatar"]):
            st.markdown(f"### {msg['name']}")
            st.write(msg["content"])
            if "divider" in msg:
                st.divider()

    # Chat Input Logic
    if user_query := st.chat_input("Tanyakan sesuatu pada dewan direksi AI..."):
        st.session_state.chat_history.append({"role": "user", "avatar": "👤", "name": "Executive (You)", "content": user_query})
        
        with st.spinner("Board members are debating the strategic impact..."):
            time.sleep(1.8)
            query_lower = user_query.lower()
            
            if "maju bersama" in query_lower or "revenue" in query_lower or "decline" in query_lower or "turun" in query_lower:
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "👔", "name": "👔 CEO Agent (Strategic Alignment)",
                    "content": """Penurunan pendapatan **15% pada PT Maju Bersama Indonesia** bukan sekadar masalah fluktuasi pasar, melainkan **krisis eksekusi taktis**. Digital Twin kami mendeteksi adanya kebutaan arah (*blind spot*) dalam rantai pasok distribusi komoditas pangan kita. Kita terlalu lambat merespons anomali lapangan karena data yang sampai ke meja saya sudah kedaluwarsa."""
                })
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "💰", "name": "💰 CFO Agent (Financial Impact Estimation)",
                    "content": """Saya sudah membedah angka kebocoran tersebut. Penurunan 15% ini setara dengan **kerugian finansial Rp 1.2 Miliar/tahun**. Kebocoran ini terjadi karena penumpukan *inventory overhead* di gudang regional regional. Kita memproduksi barang berdasarkan *Rencana Target*, padahal permintaan riil di pasar meleset jauh. Ini adalah inefisiensi modal kerja yang fatal!"""
                })
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "📊", "name": "📊 Senior Data Analyst (Decision Intelligence)",
                    "content": """Menyambung poin CFO, biang keroknya ada pada bias visualisasi. Selama ini manajemen disidang menggunakan metrik Power BI konvensional yang mengukur persentase performa terhadap *Rencana Target Lahan*. Ini pembodohan! Analisis kami menunjukkan jangkauan aktual komoditas sekunder seperti Ubi Kayu drop ke **69%**. Kita wajib membalik kalkulasi formula: **Ukur performa murni dari Total Aktual Coverage di lapangan!**"""
                })
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "🏗", "name": "🏗️ CTO & Data Engineer Agent (Technical Infrastructure)",
                    "content": """Secara infrastruktur, alasan data kita hancur adalah karena **latensi sinkronisasi data mencapai 14 hari**. Sistem database SQL saat ini menggunakan pemrosesan *batch* kuno. Solusi teknisnya: Kita harus mendepak arsitektur lama dan membangun **Pipeline Streaming berbasis Apache Kafka** yang terintegrasi dengan model **Hybrid LSTM**. Ini memotong delay data dari 14 hari menjadi **di bawah 5 detik**, menyuplai data prediksi secara *real-time*."""
                })
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "🔐", "name": "🔐 IT Auditor Agent (Governance & Risk Matrix)",
                    "content": """Dari kacamata tata kelola, kita berada di Zona Risiko Tinggi. Tanpa adanya *Single Source of Truth* yang terpusat, kepatuhan integrasi data kita berada di angka **65% (Level 3 - Defined)**. Risiko manipulasi atau *human error* saat enumerator menginput data komoditas sangat tinggi. Tata kelola data baru wajib disahkan bulan ini."""
                })
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "🎯", "name": "🎯 NexAtlas Strategic Consensus Verdict",
                    "content": """
### 📋 90-Day Transformation Roadmap & Verdict

| Pilar Fokus | Intervensi Taktis (Rekomendasi AI) | Estimasi Dampak Bisnis | Timeline |
| :--- | :--- | :--- | :--- |
| **Data Governance** | Ubah total rumus persentase komoditas berbasis *Actual Coverage* lapangan. | Menghilangkan bias prediksi manajemen | Minggu 1-2 |
| **Infrastruktur** | Migrasi arsitektur SQL Batch ke Cloud Hybrid + Streaming Event Broker (Kafka). | Memotong latensi data sebesar 80% | Bulan 1 |
| **AI Deployment** | Implementasikan pemodelan *Time-Series Forecasting* berbasis **Hybrid LSTM**. | Efisiensi biaya logistik & mitigasi rugi | Bulan 2-3 |

**🔮 What-If Simulation Projection:**
Jika dewan direksi menyetujui investasi **Skenario B (Implementasi IoT + Real-time Pipeline)**, Digital Twin memproyeksikan pemulihan pendapatan sebesar **Rp 950 Juta pada kuartal berikutnya** dan mempercepat pembuatan laporan keputusan sebesar **35%**.""",
                    "divider": True
                })
            else:
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "🏛️", "name": "NexAtlas Consensus", 
                    "content": f"Pertanyaan Anda mengenai '{user_query}' telah diproses oleh Digital Twin. Seluruh jajaran direksi menyarankan untuk mengunci parameter kalkulasi operasional berdasarkan kondisi data aktual lapangan."
                })
        st.rerun()

else:
    # --- NEW LANDING PAGE DESIGN: HIGH END ENTERPRISE PORTAL ---
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
    
    # Membuat tampilan grid Agen Standby agar halaman tidak terlihat kosong melompong
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
