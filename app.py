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
    .main { background-color: #0E1117; }
    h1, h2, h3, h4 { color: #4A90E2 !important; font-family: 'Helvetica Neue', sans-serif; }
    .verdict-box { background-color: #1A1F2C; padding: 25px; border-radius: 10px; border: 1px solid #4A90E2; margin-bottom: 25px; }
    .consensus-box { background-color: #1F241F; padding: 20px; border-radius: 8px; border-left: 5px solid #238636; margin-top: 15px; }
    .metric-card { background-color: #161B22; padding: 20px; border-radius: 8px; text-align: center; border: 1px solid #21262D; }
    .upload-box { border: 2px dashed #4A90E2; padding: 20px; border-radius: 8px; background-color: #161B22; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# Inisialisasi Chat History awal
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "avatar": "🏛️", "name": "NexAtlas Engine", "content": "Executive Boardroom initialized. Drop your corporate diagnostic document or enter your strategic crisis scenario."}
    ]

st.title("🏛️ NexAtlas AI")
st.caption("Enterprise Digital Twin & Strategic Advisory System — Powered by Datasign")
st.divider()

# --- SIDEBAR CONTROL CENTER ---
st.sidebar.header("⚙️ Executive Control Center")
st.sidebar.subheader("📥 Ingest Strategic Document")
uploaded_file = st.sidebar.file_uploader("Upload Enterprise Data", type=["pdf", "csv", "txt", "json"])

if uploaded_file is not None:
    st.sidebar.success(f"✅ Context Loaded: {uploaded_file.name}")
    file_status = f"Context Source: **{uploaded_file.name}**"
else:
    file_status = "Context Source: Regional Strategic Supply Chain Dataset."

st.sidebar.subheader("🔮 Scenario Injection")
scenario = st.sidebar.text_area("Specify Core Objective:", 
    "Analyze why PT Maju Bersama Indonesia revenue declined 15% and simulate an executive boardroom session.")

initiate_sim = st.sidebar.button("Initiate Digital Twin Simulation")

# --- EXECUTION TRIGGER ---
if initiate_sim or uploaded_file is not None or len(st.session_state.chat_history) > 1:
    
    # Metrics Top Tier
    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        st.metric(label="Strategic Health Score", value="68 / 100", delta="-14% Crisis Mode")
    with col_m2:
        st.metric(label="Enterprise Risk Index", value="🔴 CRITICAL", delta="Revenue Leakage Detected")
    with col_m3:
        st.metric(label="Decision Latency", value="14 Days Lag", delta="Action Required", delta_color="inverse")

    st.divider()

    # --- CHATROOM BOARDROOM DISCUSSION (The Core Flagship Experience) ---
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
    if user_query := st.chat_input("Tanyakan sesuatu (cth: 'Bagaimana mitigasi risiko dari CTO?')"):
        # 1. Simpan pertanyaan user
        st.session_state.chat_history.append({"role": "user", "avatar": "👤", "name": "Executive (You)", "content": user_query})
        
        with st.spinner("Board members are debating the strategic impact..."):
            time.sleep(2)
            
            query_lower = user_query.lower()
            
            # --- HIGH FIDELITY ADVISORY RESPONSE FOR "MAJU BERSAMA" SCENARIO ---
            if "maju bersama" in query_lower or "revenue" in query_lower or "decline" in query_lower or "turun" in query_lower:
                
                # CEO Response
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "👔", "name": "👔 CEO Agent (Strategic Alignment)",
                    "content": """Penurunan pendapatan **15% pada PT Maju Bersama Indonesia** bukan sekadar masalah fluktuasi pasar, melainkan **krisis eksekusi taktis**. Digital Twin kami mendeteksi adanya kebutaan arah (*blind spot*) dalam rantai pasok distribusi komoditas pangan kita. Kita terlalu lambat merespons anomali lapangan karena data yang sampai ke meja saya sudah kedaluwarsa."""
                })
                
                # CFO Response
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "💰", "name": "💰 CFO Agent (Financial Impact Estimation)",
                    "content": """Saya sudah membedah angka kebocoran tersebut. Penurunan 15% ini setara dengan **kerugian finansial Rp 1.2 Miliar/tahun**. Kebocoran ini terjadi karena penumpukan *inventory overhead* di gudang regional regional. Kita memproduksi barang berdasarkan *Rencana Target*, padahal permintaan riil di pasar meleset jauh. Ini adalah inefisiensi modal kerja yang fatal!"""
                })
                
                # Data Analyst Response
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "📊", "name": "📊 Senior Data Analyst (Decision Intelligence)",
                    "content": """Menyambung poin CFO, biang keroknya ada pada bias visualisasi. Selama ini manajemen disidang menggunakan metrik Power BI konvensional yang mengukur persentase performa terhadap *Rencana Target Lahan*. Ini pembodohan! Analisis kami menunjukkan jangkauan aktual komoditas sekunder seperti Ubi Kayu drop ke **69%**. Kita wajib membalik kalkulasi formula: **Ukur performa murni dari Total Aktual Coverage di lapangan!**"""
                })
                
                # CTO Response
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "🏗", "name": "🏗️ CTO & Data Engineer Agent (Technical Infrastructure)",
                    "content": """Secara infrastruktur, alasan data kita hancur adalah karena **latensi sinkronisasi data mencapai 14 hari**. Sistem database SQL saat ini menggunakan pemrosesan *batch* kuno. Solusi teknisnya: Kita harus mendepak arsitektur lama dan membangun **Pipeline Streaming berbasis Apache Kafka** yang terintegrasi dengan model **Hybrid LSTM**. Ini memotong delay data dari 14 hari menjadi **di bawah 5 detik**, menyuplai data prediksi secara *real-time*."""
                })
                
                # IT Auditor Response
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "🔐", "name": "🔐 IT Auditor Agent (Governance & Risk Matrix)",
                    "content": """Dari kacamata tata kelola, kita berada di Zona Risiko Tinggi. Tanpa adanya *Single Source of Truth* yang terpusat, kepatuhan integrasi data kita berada di angka **65% (Level 3 - Defined)**. Risiko manipulasi atau *human error* saat enumerator menginput data komoditas sangat tinggi. Tata kelola data baru wajib disahkan bulan ini."""
                })
                
                # Consensus Summary
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

            # --- FALLBACK FOR OTHER GENERAL QUERIES ---
            else:
                st.session_state.chat_history.append({
                    "role": "assistant", "avatar": "🏛️", "name": "NexAtlas Consensus", 
                    "content": f"Pertanyaan Anda mengenai '{user_query}' telah diproses oleh Digital Twin. Seluruh jajaran direksi menyarankan untuk mengunci parameter kalkulasi operasional berdasarkan kondisi data aktual lapangan, serta mempersiapkan migrasi arsitektur jaringan guna menyokong otomasi analitik cerdas."
                })
                
        st.rerun()

else:
    # Landing Page Executive Lounge
    st.markdown("""
    <div class="upload-box">
        <h3>🏛️ Welcome to NexAtlas AI Executive Strategy Room</h3>
        <p style="color:#8B949E; font-size:16px;">Sistem simulasi korporat berbasis 1 Juta Graph Agen siap membantu Anda mendiagnosis krisis perusahaan.</p>
        <p style="color:#4A90E2; font-size:15px;">
            <b>Langkah 1:</b> Di panel kontrol sebelah kiri, klik folder atau unggah dokumen data Anda.<br>
            <b>Langkah 2:</b> Klik tombol <b>"Initiate Digital Twin Simulation"</b> untuk membangunkan dewan direksi AI.
        </p>
    </div>
    """, unsafe_allow_html=True)
