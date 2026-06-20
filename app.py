import streamlit as st

# Mengatur tema tampilan gelap ala profesional
st.set_page_config(
    page_title="Terminal Trading Utama",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- MENU SAMPING (SIDEBAR) ---
with st.sidebar:
    st.markdown("### 🖥️ Menu Utama")
    st.button("🌐 Live Terminal", use_container_width=True)
    st.button("💼 Manajer Aset", use_container_width=True)
    st.button("⚙️ Pengaturan Global", use_container_width=True)
    st.button("📜 Log Aktivitas", use_container_width=True)
    st.markdown("---")
    st.error("⚠️ Peringatan Risiko")

# --- AREA UTAMA (MAIN DASHBOARD) ---
st.title("📊 Terminal Trading Utama")
st.caption("Status Algoritma: 🟢 SIAGA")

# Membuat 4 kotak metrik data di bagian atas
kolom1, kolom2, kolom3, kolom4 = st.columns(4)

with kolom1:
    st.metric(label="Saldo / Ekuitas", value="$1,193.78")
with kolom2:
    st.metric(label="Profit Total", value="$594.10", delta="+$24.00")
with kolom3:
    st.metric(label="Max Drawdown", value="-$22.00")
with kolom4:
    st.metric(label="Aset Aktif", value="BTCUSD")

st.markdown("---")

# Area grafik pertumbuhan dan posisi aktif
kolom_grafik, kolom_posisi = st.columns([2, 1])

with kolom_grafik:
    st.subheader("📈 Grafik Pertumbuhan Profit ($)")
    # Data simulasi grafik naik ke atas
    data_grafik = [100, 150, 130, 200, 280, 350, 410, 480, 520, 594]
    st.line_chart(data_grafik)

with kolom_posisi:
    st.subheader("📌 Posisi Trading Aktif")
    st.info("Tidak ada posisi trading yang terbuka saat ini.")
  
