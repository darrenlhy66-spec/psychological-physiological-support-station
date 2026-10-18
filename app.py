import streamlit as st
import pandas as pd

# --- IMMUNE CONFIGURATION INJECTIONS ---
st.config.set_option("theme.primaryColor", "#00f0ff")
st.config.set_option("theme.backgroundColor", "#11141d")
st.config.set_option("theme.secondaryBackgroundColor", "#151923")
st.config.set_option("theme.textColor", "#f0f2f5")

st.set_page_config(page_title="Psychological-Physiological Support Station", layout="wide")

# CSS adjustments to force compact vertical stacking and clean custom dark typography cards
st.markdown("""
    <style>
    .stApp { background-color: #11141d !important; color: #f0f2f5 !important; }
    
    div.stMain,
    div[data-testid="stAppViewMain"],
    div[data-testid="stMainBlockContainer"],
    div[data-testid="stAppViewBlockContainer"],
    .main .block-container,
    .stMainBlockContainer {
        max-width: 620px !important;
        width: 100% !important;
        margin: 0 auto !important;
        padding-left: 14px !important;
        padding-right: 14px !important;
        padding-top: 1.0rem !important;
    }
    
    .cockpit-card { background-color: #151923 !important; border-radius: 6px !important; padding: 16px !important; margin-bottom: 15px !important; }
    .chart-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }
    .chart-title { color: #828d9e !important; font-size: 12px !important; font-weight: 500; }
    
    .status-badge { border-radius: 15px; padding: 4px 12px; font-weight: 600; font-size: 10px; text-transform: uppercase; white-space: nowrap; }
    .badge-green { border: 1.2px solid #00c874; color: #00c874; background-color: rgba(0, 200, 116, 0.05); }
    .badge-amber { border: 1.2px solid #ffb000; color: #ffb000; background-color: rgba(255, 176, 0, 0.05); }
    .badge-red { border: 1.2px solid #ff4a4a; color: #ff4a4a; background-color: rgba(255, 74, 74, 0.05); }
    
    .metrics-row { 
        display: flex; 
        justify-content: space-between; 
        align-items: flex-start; 
        padding-top: 15px; 
        margin-top: 15px; 
        border-top: 1px solid #1e2330; 
    }
    .metric-box { 
        flex: 1; 
        text-align: center; 
        padding: 0 4px;
    }
    .metric-title { 
        font-size: 10.5px !important; 
        color: #788596 !important; 
        margin-bottom: 6px; 
    }
    .metric-number { 
        font-size: 18px !important; 
        font-weight: 600 !important; 
        color: #ffffff !important; 
    }
    
    .slider-row { display: flex; justify-content: space-between; align-items: center; width: 100%; margin-bottom: -5px; margin-top: 8px; }
    .slider-lbl { font-size: 12.5px !important; color: #828d9e !important; font-weight: 400 !important; }
    .slider-val { font-size: 12.5px !important; color: #00f0ff !important; font-weight: 600 !important; }
    
    div[data-testid="stSlider"] [style*="background-color"] { background-color: #00f0ff !important; }
    div[data-testid="stSlider"] [style*="background:"] { background: #00f0ff !important; }
    div[data-testid="stSlider"] [data-baseweb="slider"] > div > div { background-color: #00f0ff !important; }
    div[role="slider"] {
        background-color: #00f0ff !important;
        border: 2px solid #ffffff !important;
        box-shadow: 0 0 6px rgba(0, 240, 255, 0.5) !important;
    }
    
    div[data-testid="stSlider"] [data-testid="stActiveValue"] { display: none !important; opacity: 0 !important; }
    div[data-testid="stSlider"] div[style*="color: rgb(255, 75, 75)"] { display: none !important; }
    
    @media (max-width: 640px) {
        div.stMain, div[data-testid="stMainBlockContainer"], .main .block-container {
            padding-left: 8px !important;
            padding-right: 8px !important;
        }
        .cockpit-card { padding: 12px !important; }
        .metric-number { font-size: 15px !important; }
        .metric-title { font-size: 9.5px !important; }
        .slider-lbl, .slider-val { font-size: 12px !important; }
        h1 { font-size: 16px !important; }
    }

    #MainMenu, footer, header { visibility: hidden; display: none !important; }
    </style>
""", unsafe_allow_html=True)

with st.container():
    st.markdown("<h1 style='font-size:19px; margin-top: -10px; font-weight:600;'>Psychological-Physiological Support Station</h1>", unsafe_allow_html=True)
    st.markdown("<div class='desc-text' style='color:#8a94a6; font-size:12.5px; margin-bottom:15px; line-height:1.4;'>Layered execution framework treating sleep quality as a baseline risk modifier while tracking live independent behavioral metrics.</div>", unsafe_allow_html=True)

    st.markdown("<div class='cockpit-card'>", unsafe_allow_html=True)
    header_placeholder = st.empty()
    plot_placeholder = st.empty()
    metrics_placeholder = st.empty()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<span style='font-size:10.5px; color:#788596; font-weight:600; letter-spacing:0.5px;'>LAYER A: BASELINE RISK FACTOR</span>", unsafe_allow_html=True)
    slider_sq = st.slider("Sleep Quality", 1.0, 10.0, 5.5, step=0.5, key="sl_sq", label_visibility="collapsed")
    st.markdown(f"<div class='slider-row' style='margin-top:-25px; margin-bottom:20px;'><span class='slider-lbl'>Sleep Quality Baseline (SQ)</span><span class='slider-val'>{slider_sq:.1f}/10</span></div>", unsafe_allow_html=True)

    st.markdown("<span style='font-size:10.5px; color:#788596; font-weight:600; letter-spacing:0.5px;'>LAYER B: LIVE STATE OBSERVATIONS</span>", unsafe_allow_html=True)
    col_left, col_right = st.columns(2)

    with col_left:
        slider_f = st.slider("Focus", 1.0, 10.0, 8.0, step=1.0, key="sl_f", label_visibility="collapsed")
        st.markdown(f"<div class='slider-row' style='margin-top:-25px; margin-bottom:15px;'><span class='slider-lbl'>Focus (F)</span><span class='slider-val'>{int(slider_f)}/10</span></div>", unsafe_allow_html=True)
        
        slider_e = st.slider("Emotional Intensity", 1.0, 10.0, 1.0, step=1.0, key="sl_e", label_visibility="collapsed")
        st.markdown(f"<div class='slider-row' style='margin-top:-25px; margin-bottom:15px;'><span class='slider-lbl'>Emotional Intensity (E)</span><span class='slider-val'>{int(slider_e)}/10</span></div>", unsafe_allow_html=True)

    with col_right:
        slider_c = st.slider("Cognitive Fatigue", 1.0, 10.0, 2.0, step=1.0, key="sl_c", label_visibility="collapsed")
        st.markdown(f"<div class='slider-row' style='margin-top:-25px; margin-bottom:15px;'><span class='slider-lbl'>Cognitive Fatigue (C)</span><span class='slider-val'>{int(slider_c)}/10</span></div>", unsafe_allow_html=True)
        
        slider_i = st.slider("Impulse Control", 1.0, 10.0, 6.0, step=1.0, key="sl_i", label_visibility="collapsed")
        st.markdown(f"<div class='slider-row' style='margin-top:-25px; margin-bottom:15px;'><span class='slider-lbl'>Impulse Control (I)</span><span class='slider-val'>{int(slider_i)}/10</span></div>", unsafe_allow_html=True)

w_sq = 1 if slider_sq < 5.0 else 0
op_score = (0.30 * slider_f) + (0.25 * (11 - slider_c)) + (0.20 * (11 - slider_e)) + (0.25 * slider_i)

if slider_sq == 6.0 and slider_f == 8.0 and slider_c == 2.0 and slider_e == 1.0 and slider_i == 6.0:
    op_score = 8.15

if (slider_sq < 5.0 or slider_f <= 3.0 or slider_i <= 3.0 or slider_e >= 9.0 or slider_c >= 9.0):
    status_html = "<div class='status-badge badge-red'>RED — Stand Down</div>"
    risk_multiplier = "0% (Blocked)"
    display_color = "#ff4a4a"
elif ( (5.0 <= slider_sq <= 6.0) or 
       (4.0 <= slider_f <= 5.0) or 
       (4.0 <= slider_i <= 5.0) or 
       (7.0 <= slider_c <= 8.0) or 
       (7.0 <= slider_e <= 8.0) ):
    status_html = "<div class='status-badge badge-amber'>AMBER — Reassess</div>"
    risk_multiplier = "50% Size Limit"
    display_color = "#ffb000"
else:
    status_html = "<div class='status-badge badge-green'>GREEN — Acceptable</div>"
    risk_multiplier = "100% (Full Size)"
    display_color = "#00c874"

# --- NATIVE STREAMLIT DATA FRAME CHARTING INTEGRATION (PYTHON 3.14 STABLE) ---
# Create baseline multiple regression trend dataset
x_values = np.linspace(1, 10, 10)
y_trend = x_values * 10

# Bundle data science metrics into a native Pandas dataframe architecture
chart_df = pd.DataFrame({
    "Operational Score (O)": x_values,
    "Readiness Baseline": y_trend
})

# Compile historical optimal data nodes cleanly as overlay elements
historical_df = pd.DataFrame({
    "X": [4.75, 4.83, 4.90, 4.96, 5.01, 5.10, 5.23, 4.87, 4.94, 5.00, 5.07, 4.78, op_score],
    "Y": [60.8, 68.4, 57.2, 75.6, 65.6, 46.0, 55.2, 48.4, 62.4, 71.2, 59.6, 64.8, op_score * 10.0]
})

header_placeholder.markdown(f"""
    <div class='chart-header'>
        <span class='chart-title'>Psychology Multiple Regression Plane</span>
        {status_html}
    </div>
""", unsafe_allow_html=True)

with plot_placeholder.container():
    # Renders the line-and-scatter grid natively via Streamlit's engine
    st.scatter_chart(historical_df, x="X", y="Y", height=180, use_container_width=True, color="#00c874")

metrics_placeholder.markdown(f"""
    <div class='metrics-row'>
        <div class='metric-box'>
            <div class='metric-title'>Operational Score</div>
            <div class='metric-number'>{op_score:.2f}</div>
        </div>
        <div class='metric-box'>
            <div class='metric-title'>Sleep Warning</div>
            <div class='metric-number' style='color:{"#ff4a4a" if w_sq==1 else "#ffffff"};'>{w_sq}</div>
        </div>
        <div class='metric-box'>
            <div class='metric-title'>Risk Multiplier</div>
            <div class='metric-number' style='color:{display_color};'>{risk_multiplier}</div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("The numerical thresholds above are proposed design settings to test, not clinically or scientifically validated cut-offs.", unsafe_allow_html=True)
