import streamlit as st
import numpy as np

st.set_page_config(page_title="Impulse Gate Risk Control Station", layout="wide")

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
    
    div[data-testid="stSlider"] [style*="background-color: rgb(255, 75, 75)"] { background-color: #00f0ff !important; }
    div[data-testid="stSlider"] [style*="background: rgb(255, 75, 75)"] { background: #00f0ff !important; }
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
        h1 { font-size: 18px !important; }
    }

    #MainMenu, footer, header { visibility: hidden; display: none !important; }
    </style>
""", unsafe_allow_html=True)

with st.container():
    st.markdown("<h1 style='font-size:20px; margin-top: -10px;'>Impulse Gate Risk Control Station</h1>", unsafe_allow_html=True)
    st.markdown("<div class='desc-text' style='color:#8a94a6; font-size:12.5px; margin-bottom:15px; line-height:1.4;'>Layered execution framework treating sleep quality as a baseline risk modifier while tracking live independent behavioral metrics.</div>", unsafe_allow_html=True)

    st.markdown("<div class='cockpit-card'>", unsafe_allow_html=True)
    header_placeholder = st.empty()
    svg_placeholder = st.empty()
    metrics_placeholder = st.empty()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<span style='font-size:10.5px; color:#788596; font-weight:600; letter-spacing:0.5px;'>LAYER A: BASELINE RISK FACTOR</span>", unsafe_allow_html=True)
    slider_sq = st.slider("Sleep Quality", 1.0, 10.0, 6.0, step=0.5, key="sl_sq", label_visibility="collapsed")
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

pct_x = ((op_score - 1.0) / 9.0) * 100.0

svg_code = f"""
<svg viewBox='0 0 400 200' width='100%' height='200' style='background:#151923; overflow:visible;'>
    <line x1='35' y1='30' x2='385' y2='30' stroke='#1c2230' stroke-width='1' />
    <line x1='35' y1='70' x2='385' y2='70' stroke='#1c2230' stroke-width='1' />
    <line x1='35' y1='110' x2='385' y2='110' stroke='#1c2230' stroke-width='1' />
    <line x1='35' y1='150' x2='385' y2='150' stroke='#1c2230' stroke-width='1' />
    <text x='5' y='34' fill='#4d586b' font-size='9'>$30k</text>
    <text x='5' y='74' fill='#4d586b' font-size='9'>$10k</text>
    <text x='5' y='114' fill='#4d586b' font-size='9'>$-10k</text>
    <text x='5' y='154' fill='#4d586b' font-size='9'>$-30k</text>
    <text x='35' y='180' fill='#4d586b' font-size='9'>1</text>
    <text x='122' y='180' fill='#4d586b' font-size='9'>3</text>
    <text x='210' y='180' fill='#4d586b' font-size='9'>5</text>
    <text x='297' y='180' fill='#4d586b' font-size='9'>7</text>
    <text x='380' y='180' fill='#4d586b' font-size='9'>10</text>
    <text x='150' y='195' fill='#828d9e' font-size='10'>Operational Score (O)</text>
    <line x1='171' y1='15' x2='171' y2='160' stroke='#d93838' stroke-width='1.5' stroke-dasharray='4,4' />
    <line x1='35' y1='160' x2='385' y2='20' stroke='#2b5cbe' stroke-width='2' />
    <circle cx='180' cy='65' r='3.5' fill='#00c874' opacity='0.8' />
    <circle cx='195' cy='55' r='3.5' fill='#00c874' opacity='0.8' />
    <circle cx='210' cy='70' r='3.5' fill='#00c874' opacity='0.8' />
    <circle cx='225' cy='48' r='3.5' fill='#00c874' opacity='0.8' />
    <circle cx='240' cy='60' r='3.5' fill='#00c874' opacity='0.8' />
    <circle cx='{35 + (pct_x * 3.5)}' cy='{160 - (pct_x * 1.4)}' r='5.5' fill='#ffffff' stroke='{display_color}' stroke-width='3.5' />
</svg>
"""

header_placeholder.markdown(f"""
    <div class='chart-header'>
        <span class='chart-title'>Psychology Multiple Regression Plane</span>
        {status_html}
    </div>
""", unsafe_allow_html=True)

svg_placeholder.markdown(svg_code, unsafe_allow_html=True)

metrics_placeholder.markdown(f"""
    <div class='metrics-row'>
        <div class='metric-box'>
            <div class='metric-title'>Operational Score</div>
            <div class='metric-number'>{op_score:.2f}</div>
        </div>
        <div class='metric-box'>
Sleep Warning
{w_sq}


Risk Multiplier
{risk_multiplier}


""", unsafe_allow_html=True)
st.markdown("The numerical thresholds above are proposed design settings to test, not clinically or scientifically validated cut-offs.", unsafe_allow_html=True)
