import streamlit as st

st.set_page_config(page_title="AI Surveillance", layout="wide")

# --------- CUSTOM CSS (MAIN MAGIC) ----------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

/* Header */
.header {
    text-align: center;
    padding: 20px;
    border-radius: 15px;
    background: #1e293b;
    margin-bottom: 20px;
}
.title {
    font-size: 32px;
    font-weight: bold;
    color: #ff4b4b;
}
.subtitle {
    font-size: 16px;
    color: #cbd5e1;
}

/* Status badges */
.badge {
    display: inline-block;
    padding: 6px 12px;
    margin: 5px;
    border-radius: 20px;
    background: #334155;
    color: #22c55e;
    font-size: 14px;
}

/* Cards */
.card {
    background: #1e293b;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
}

/* Upload box */
.upload-box {
    border: 2px dashed #38bdf8;
    padding: 40px;
    text-align: center;
    border-radius: 12px;
    color: #94a3b8;
}

/* Buttons */
.main-btn button {
    width: 100%;
    background-color: #ef4444 !important;
    color: white !important;
    border-radius: 10px;
    padding: 12px;
    font-size: 16px;
}

.green-btn button {
    width: 100%;
    background-color: #22c55e !important;
    color: white !important;
    border-radius: 10px;
    padding: 12px;
    font-size: 16px;
}

/* Stats box */
.stat-box {
    background: #0f172a;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    margin-bottom: 10px;
}

/* Alerts */
.alert {
    background: #0f172a;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

# --------- HEADER ----------
st.markdown("""
<div class="header">
    <div class="title">🚨 AI Video Surveillance System</div>
    <div class="subtitle">Intelligent Real-time Abnormal Activity Detection</div>
    <div>
        <span class="badge">🟢 YOLO Detection</span>
        <span class="badge">📧 Email Alerts</span>
        <span class="badge">💻 System Online</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --------- MAIN BUTTON ----------
st.markdown('<div class="main-btn">', unsafe_allow_html=True)
st.button("🎥 Start Live Webcam Detection")
st.markdown('</div>', unsafe_allow_html=True)

# --------- LAYOUT ----------
left, right = st.columns([3,1])

# --------- LEFT SIDE ----------
with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown("### 📤 Upload Video for Analysis")

    st.markdown("""
    <div class="upload-box">
        📁 Drag & drop video file or click to browse<br>
        <small>Supported: MP4, AVI, MOV, MKV, WebM</small>
    </div>
    """, unsafe_allow_html=True)

    video = st.file_uploader("", type=["mp4","avi","mov","mkv","webm"])

    if video:
        st.video(video)

    st.markdown('<div class="green-btn">', unsafe_allow_html=True)
    st.button("🔍 Upload & Analyze")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# --------- RIGHT SIDE ----------
with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown("### 📊 Detection Stats (7 Days)")

    st.markdown('<div class="stat-box">Total Events<br><b>0</b></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-box">Violence<br><b>0</b></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-box">Loitering<br><b>0</b></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-box">Running<br><b>0</b></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown("### 🔔 Recent Alerts")

    st.markdown('<div class="alert">📍 Accident<br><small>2026-03-16 08:40</small></div>', unsafe_allow_html=True)
    st.markdown('<div class="alert">📍 Accident<br><small>2026-03-16 08:39</small></div>', unsafe_allow_html=True)
    st.markdown('<div class="alert">📍 Accident<br><small>2026-03-16 08:38</small></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)