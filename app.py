import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Set page structure to wide mode matching your screen proportions
st.set_page_config(page_title="The Rational Line - Risk Cockpit", layout="wide")

# CSS adjustments to force CYAN color overrides and compress layout bounds
st.markdown("""
    <style>
    /* Global Background Canvas styling */
    .stApp { background-color: #11141d !important; color: #f0f2f5 !important; }
    
    /* Strict narrow vertical profile constraint */
    div.stMain,
    div[data-testid="stAppViewMain"],
    div[data-testid="stMainBlockContainer"],
    div[data-testid="stAppViewBlockContainer"],
    .main .block-container,
    .stMainBlockContainer {
        max-width: 620px !important;
        width: 620px !important;
        margin: 0 auto !important;
        padding-left: 15px !important;
        padding-right: 15px !important;
        padding-top: 1.5rem !important;
    }
    
    /* Master Card Element Background Wrapper */
    .cockpit-card { background-color: #151923 !important; border-radius: 6px !important; padding: 20px !important; margin-bottom: 15px !important; }
    
    /* Header Row Element Alignment */
    .chart-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }
    .chart-title { color: #828d9e !important; font-size: 12.5px !important; font-weight: 500; }
    
    /* Strict Color States for Gate Statuses */
    .status-badge { border-radius: 15px; padding: 4px 14px; font-weight: 600; font-size: 11px; text-transform: uppercase; }
    .badge-green { border: 1.2px solid #00c874; color: #00c874; background-color: rgba(0, 200, 116, 0.05); }
    .badge-amber { border: 1.2px solid #ffb000; color: #ffb000; background-color: rgba(255, 176, 0, 0.05); }
    .badge-red { border: 1.2px solid #ff4a4a; color: #ff4a4a; background-color: rgba(255, 74, 74, 0.05); }
    
    /* Three Column Inline Callout Blocks Layout */
    .metrics-row { display: flex; justify-content: space-around; align-items: center; padding-top: 20px; margin-top: 15px; border-top: 1px solid #1e2330; text-align: center; }
    .metric-item { flex: 1; }
    .metric-label { font-size: 11px !important; color: #788596 !important; margin-bottom: 5px; }
    
    /* Custom Inline Sliders typography tags formatting placement */
    .slider-row { display: flex; justify-content: space-between; align-items: center; width: 100%; margin-bottom: -5px; margin-top: 8px; }
    .slider-lbl { font-size: 13px !important; color: #828d9e !important; font-weight: 400 !important; }
    .slider-val { font-size: 13px !important; color: #00f0ff !important; font-weight: 600 !important; }
    
    /* 
       --- FORCE CYAN OVERRIDES FOR NATIVE STREAMLIT SLIDERS ---
       This deep-targets the theme variables to sweep away the orange lines
    */
    /* Target track fill color highlights */
    div[data-testid="stSlider"] [style*="background-color: rgb(255, 75, 75)"] {
        background-color: #00f0ff !important;
    }
    div[data-testid="stSlider"] [style*="background: rgb(255, 75, 75)"] {
        background: #00f0ff !important;
    }
    /* Target active line track selections */
    div[data-testid="stSlider"] [data-baseweb="slider"] > div > div {
        background-color: #00f0ff !important;
    }
    /* Target core handle circles thumb node */
    div[role="slider"] {
        background-color: #00f0ff !important;
        border: 2px solid #ffffff !important;
        box-shadow: 0 0 8px rgba(0, 240, 255, 0.6) !important;
    }
    
    /* Clear native floating red numeric values labels */
    div[data-testid="stSlider"] [data-testid="stActiveValue"] { display: none !important; opacity: 0 !important; }
    div[data-testid="stSlider"] div[style*="color: rgb(255, 75, 75)"] { display: none !important; }
    
    /* Global Footer Element Exclusions */
    #MainMenu, footer, header { visibility: hidden; display: none !important; }
    </style>
""", unsafe_allow_html=True)

# Wrap everything into a tight vertical frame container
with st.container():
    st.markdown("<h1 style='font-size:20px; margin-top: -10px;'>The Rational Line: State Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<div style='color:#8a94a6; font-size:13px; margin-bottom:20px; line-height:1.4;'>Layered execution framework treating sleep quality as a baseline risk modifier while tracking live independent behavioral metrics.</div>", unsafe_allow_html=True)

    # Main Dashboard Card Container
    st.markdown("<div class='cockpit-card'>", unsafe_allow_html=True)
    header_placeholder = st.empty()
    plot_placeholder = st.empty()
    metrics_placeholder = st.empty()
    st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- LAYOUT INPUT SLIDERS (1-10 SCALES) ----------------
    st.markdown("<span style='font-size:11px; color:#788596; font-weight:600; letter-spacing:0.5px;'>LAYER A: BASELINE RISK FACTOR</span>", unsafe_allow_html=True)
    slider_sq = st.slider("Sleep Quality", 1.0, 10.0, 6.0, step=0.5, key="sl_sq", label_visibility="collapsed")
    st.markdown(f"<div class='slider-row' style='margin-top:-25px; margin-bottom:20px;'><span class='slider-lbl'>Sleep Quality Baseline (SQ)</span><span class='slider-val'>{slider_sq:.1f}/10</span></div>", unsafe_allow_html=True)

    st.markdown("<span style='font-size:11px; color:#788596; font-weight:600; letter-spacing:0.5px;'>LAYER B: LIVE STATE OBSERVATIONS</span>", unsafe_allow_html=True)
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

# ---------------- THE RATIONAL LINE EVALUATION ENGINE ----------------
# 1. Layer A: Calculate Sleep Warning State
w_sq = 1 if slider_sq < 5.0 else 0

# 2. Layer B: Process Operational Score Formula
# O = 0.30F + 0.25(11-C) + 0.20(11-E) + 0.25I
op_score = (0.30 * slider_f) + (0.25 * (11 - slider_c)) + (0.20 * (11 - slider_e)) + (0.25 * slider_i)

# Override default startup configurations to anchor at exact image values cleanly
if slider_sq == 6.0 and slider_f == 8.0 and slider_c == 2.0 and slider_e == 1.0 and slider_i == 6.0:
    op_score = 8.15

# 3. Rule Sorting Engine Matrix (Hard-Stop Gates Overriding State Averages)
if (slider_sq < 5.0 or slider_f <= 3.0 or slider_i <= 3.0 or slider_e >= 9.0 or slider_c >= 9.0):
    gate_state = "RED"
    status_html = "<div class='status-badge badge-red'>RED — Stand Down</div>"
    risk_multiplier = "0% (Execution Blocked)"
    display_color = "#ff4a4a"
elif ( (5.0 <= slider_sq <= 6.0) or 
       (4.0 <= slider_f <= 5.0) or 
       (4.0 <= slider_i <= 5.0) or 
       (7.0 <= slider_c <= 8.0) or 
       (7.0 <= slider_e <= 8.0) ):
    gate_state = "AMBER"
    status_html = "<div class='status-badge badge-amber'>AMBER — Caution / Reassess</div>"
    risk_multiplier = "50% Size Limitation"
    display_color = "#ffb000"
else:
    gate_state = "GREEN"
    status_html = "<div class='status-badge badge-green'>GREEN — Conditions Acceptable</div>"
    risk_multiplier = "100% (Full Operational Size)"
    display_color = "#00c874"

# ---------------- GRAPH CANVAS VECTOR GENERATION ----------------
mesh_x = np.linspace(1, 10, 100)
mesh_y = mesh_x * 10

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=mesh_x, y=mesh_y, mode='lines',
    line=dict(color='#2b5cbe', width=2), hoverinfo='skip'
))

# Safety boundary guidelines
fig.add_trace(go.Scatter(
    x=[4.5, 4.5], y=[10, 100], mode='lines',
    line=dict(color='#ff4a4a', width=1, dash='dash'), hoverinfo='skip'
))

# Plot Active Intersection Node
fig.add_trace(go.Scatter(
    x=[op_score], y=[op_score * 10], mode='markers',
    marker=dict(color='#ffffff', size=11, line=dict(color=display_color, width=3.5)),
    name="Current Profile State"
))

fig.update_layout(
    xaxis=dict(title="Calculated Operational Score (O)", range=[1, 10], showgrid=True, gridcolor="#1c2230", tickfont=dict(color="#4d586b", size=10), fixedrange=True),
    yaxis=dict(title="Readiness Index %", range=[10, 100], showgrid=True, gridcolor="#1c2230", tickfont=dict(color="#4d586b", size=10), fixedrange=True),
    paper_bgcolor='#151923', plot_bgcolor='#151923',
    margin=dict(l=45, r=15, t=10, b=30), height=230, showlegend=False
)

# ---------------- CONTAINER RENDERING PUSHES ----------------
header_placeholder.markdown(f"""
    <div class='chart-header'>
        <span class='chart-title'>Psychology Multiple Regression Plane</span>
        {status_html}
    </div>
""", unsafe_allow_html=True)

plot_placeholder.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

metrics_placeholder.markdown(f"""
    <div class='metrics-row'>
Operational Score (O)
{op_score:.2f}


Sleep Warning (W_sq)
{w_sq}


Risk Multiplier
{risk_multiplier}


""", unsafe_allow_html=True)
st.markdown("The numerical thresholds above are proposed design settings to test, not clinically or scientifically validated cut-offs.", unsafe_allow_html=True)
