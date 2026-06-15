import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import time

# --- BRANDING & UI SETUP ---
st.set_page_config(
    page_title="NexAtlas AI | Executive Boardroom",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Tema Gelap / Profesional
st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    h1, h2, h3 { color: #4A90E2; }
    .stAlert { background-color: #1E2530; border: 1px solid #4A90E2; color: white; }
    </style>
""", unsafe_allow_html=True)

st.title("🏛️ NexAtlas AI")
st.subheader("Enterprise Digital Twin & Strategic Advisory System")
st.divider()

# --- SIDEBAR: SCENARIO INJECTION ---
st.sidebar.header("⚙️ Scenario Injection")
scenario = st.sidebar.text_area("Input Strategic Scenario:", 
    "Evaluasi kesiapan AI untuk memonitor produksi komoditas pangan di Lampung.")

if st.sidebar.button("Initiate Scenario"):
    with st.spinner("Waking up AI Boardroom Agents (Data Analyst, Engineer, BI)..."):
        time.sleep(2) # Simulasi waktu eksekusi
    
    st.success("Simulation Complete! Boardroom Consensus Reached.")

    # --- KECERDASAN LOKAL & LOGIKA BISNIS ---
    st.markdown("### 📊 Data Intelligence Assessment Result")
    
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Data Maturity Score", value="78 / 100", delta="+5.4%")
    col2.metric(label="Actual Data Coverage", value="89.2%", delta="Real-time")
    col3.metric(label="Infrastructure Readiness", value="Moderate", delta="Needs Cloud Migration", delta_color="off")

    st.divider()

    # --- FRONTEND VISUALIZATION (PLOTLY) ---
    st.markdown("### Commodity Actual Coverage Flow")
    
    # Urutan Data (Red Flipped Style)
    categories = ['Padi', 'Jagung', 'Kedelai', 'Ubi Kayu']
    values = [210, 186, 179, 145] 

    fig = go.Figure(go.Funnel(
        y=categories,
        x=values,
        textposition="inside",
        textinfo="value+percent initial",
        marker={"color": ["#08306b", "#2171b5", "#6baed6", "#deebf7"]} # Biru Gradasi
    ))

    fig.update_layout(
        height=600, 
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="white", size=14),
        margin=dict(l=20, r=20, t=40, b=20)
    )

    st.plotly_chart(fig, use_container_width=True)

    # --- OUTPUT SUMMARY ---
    st.markdown("### 📋 Boardroom Transcript (Executive Summary)")
    st.info("""
    **Senior Data Analyst:** "Model prediksi sudah siap. Pengukuran dilakukan berdasarkan **Total Aktual Coverage**, bukan rencana target. Akurasi data di Lampung saat ini berada di angka 89.2%."
    
    **Lead Data Engineer:** "Infrastruktur siap untuk Hybrid LSTM. Disarankan migrasi ke arsitektur cloud untuk skalabilitas nasional."
    """)

else:
    st.info("Silakan klik 'Initiate Scenario' untuk memulai simulasi Boardroom.")
