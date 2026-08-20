import streamlit as st
import time

# ==========================================
# ⚙️ 1. PAGE SETUP
# ==========================================
st.set_page_config(page_title="Akamai Marketplace | Control Center", layout="wide", initial_sidebar_state="expanded")

# ==========================================
# 🔒 2. LOGIN LOGIC (Case & Space Insensitive)
# ==========================================
def check_password():
    """Returns `True` if the user entered the correct password."""
    
    def password_entered():
        user_input = st.session_state["username"].strip().lower()
        pass_input = st.session_state["password"].strip().lower()
        
        if user_input == "admin" and pass_input == "akamai2024":
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.markdown("<br><br><h2 style='text-align: center; color: #0072CE;'>Akamai EI Marketplace</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #475569;'>Please log in to access the Control Center</p>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1.5, 1, 1.5])
        with col2:
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.button("Login", on_click=password_entered, type="primary", use_container_width=True)
        return False
    
    elif not st.session_state["password_correct"]:
        st.markdown("<br><br><h2 style='text-align: center; color: #0072CE;'>Akamai EI Marketplace</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #475569;'>Please log in to access the Control Center</p>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1.5, 1, 1.5])
        with col2:
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.button("Login", on_click=password_entered, type="primary", use_container_width=True)
            st.error("😕 Username or password incorrect")
        return False
    else:
        return True

if not check_password():
    st.stop()

# ==========================================
# 🎨 3. COMPACT ENTERPRISE STYLING
# ==========================================
AKAMAI_CSS = """
<style>
    .block-container { padding: 1.2rem 2rem 1rem 2rem !important; max-width: 100% !important; }
    header { display: none !important; }
    
    .stApp { 
        background-color: #F4F6F9; 
        font-family: 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; 
        color: #1E2228;
    }
    
    .akamai-topbar {
        background-color: #1E2228; color: #FFFFFF; padding: 12px 24px; 
        margin-top: -1.2rem; margin-left: -2rem; margin-right: -2rem; margin-bottom: 16px;
        display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #2B313A;
    }
    .akamai-brand { font-weight: 800; font-size: 18px; letter-spacing: 0.5px; color: #0072CE; white-space: nowrap; }
    .akamai-search-box { background-color: #2B313A; border: 1px solid #3A424D; border-radius: 4px; padding: 6px 16px; color: #C0C7D0; width: 35vw; min-width: 250px; max-width: 500px; font-size: 12px; }
    .akamai-top-right { display: flex; align-items: center; gap: 20px; font-size: 12px; color: #E2E8F0; white-space: nowrap; }
    
    .icon-container { position: relative; display: flex; align-items: center; justify-content: center; cursor: pointer; }
    .notification-badge { 
        position: absolute; top: -5px; right: -6px; background-color: #D93025; color: white; 
        font-size: 9px; font-weight: 700; padding: 2px 5px; border-radius: 10px; border: 2px solid #1E2228;
    }
    
    .akamai-card { background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 6px; padding: 20px 24px; margin-bottom: 12px; box-shadow: 0 1px 4px rgba(0,0,0,0.04); }
    .akamai-card-title { font-size: 18px; font-weight: 700; color: #1E2228; margin-bottom: 16px; }
    
    .pillar-card { background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 14px; display: flex; flex-direction: column; height: 100%; }
    .pillar-header { font-size: 13px; font-weight: 700; color: #1E2228; text-transform: uppercase; border-bottom: 1px solid #E2E8F0; padding-bottom: 8px; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center; }
    
    .mini-enable-btn { background-color: #FFFFFF; color: #0072CE; border: 1px solid #0072CE; border-radius: 4px; padding: 6px 10px; font-size: 11px; font-weight: 600; cursor: pointer; margin-top: 6px; width: 100%; }
    .mini-buy-btn { background-color: #0072CE; color: #FFFFFF; border: none; border-radius: 4px; padding: 6px 10px; font-size: 11px; font-weight: 600; cursor: pointer; margin-top: 6px; width: 100%; }
    .mini-stage-btn { background-color: #10B981; color: #FFFFFF; border: none; border-radius: 4px; padding: 6px 10px; font-size: 11px; font-weight: 600; cursor: pointer; margin-top: 6px; width: 100%; }
    
    .section-label { font-size: 10px; font-weight: 800; text-transform: uppercase; margin-bottom: 4px; letter-spacing: 0.5px; }
    
    .info-box { border-radius: 6px; padding: 10px; margin-bottom: 12px; border: 1px solid transparent; flex-grow: 1; display: flex; flex-direction: column;}
    .info-box.free { background-color: #F8FAFC; border-color: #E2E8F0; }
    .info-box.addon { background-color: #FFFFFF; border-color: #E2E8F0; box-shadow: 0 1px 2px rgba(0,0,0,0.02); }
    
    .info-title { font-size: 13px; font-weight: 700; color: #1E2228; margin-bottom: 4px; }
    .info-issue { font-size: 11px; font-weight: 600; margin-bottom: 4px; line-height: 1.4; color: #1E2228;}
    .info-desc { font-size: 11px; line-height: 1.4; margin-bottom: 8px; color: #475569; }

    .free-list { margin: 0; padding-left: 16px; font-size: 11px; color: #1E2228; font-weight: 500; margin-bottom: 8px; line-height: 1.5;}
    
    .tag-container { display: flex; flex-wrap: wrap; gap: 4px; margin-bottom: 8px; }
    .tag-badge { font-size: 9px; font-weight: 700; padding: 3px 6px; border-radius: 4px; line-height: 1.2; }
    .tag-compliance { background-color: #F0F7FF; color: #0072CE; border: 1px solid #CCE3FD; }
    .tag-value { background-color: #FEF3C7; color: #92400E; border: 1px solid #FDE68A; }

    /* V2 ROI Banner */
    .roi-banner { background-color: #1E2228; color: white; padding: 16px 20px; border-radius: 8px; margin-bottom: 20px; display: flex; align-items: center; justify-content: space-between; }
    .roi-score { font-size: 28px; font-weight: 800; color: #10B981; }
    .roi-wasted { font-size: 28px; font-weight: 800; color: #EF4444; }

    /* V2 Nudge Banner */
    .nudge-alert { background-color: #FEF2F2; border-left: 4px solid #EF4444; padding: 10px 16px; margin-bottom: 16px; border-radius: 4px; display: flex; align-items: center; justify-content: space-between; }

    .metric-box { background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 6px; padding: 14px; text-align: center; }
    .metric-val { font-size: 22px; font-weight: 800; color: #1E2228; margin-bottom: 4px; }
    .metric-label { font-size: 10px; color: #64748B; font-weight: 700; text-transform: uppercase; }
    
    .visual-bar-container { background-color: #E2E8F0; border-radius: 6px; height: 18px; width: 100%; display: flex; overflow: hidden; margin-top: 12px; margin-bottom: 8px;}
    .visual-segment { height: 100%; display: flex; align-items: center; justify-content: center; font-size: 10px; color: white; font-weight: 700; }
    .visual-legend { display: flex; gap: 12px; font-size: 11px; color: #475569; font-weight: 600; justify-content: center; }
    .legend-dot { display: inline-block; width: 8px; height: 8px; border-radius: 50%; margin-right: 4px; }

    .rec-card { background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 14px; height: 100%; border-top: 3px solid #0072CE; }

    div[data-testid="stVerticalBlock"] > div { padding-bottom: 0.2rem !important; }
</style>
"""
st.markdown(AKAMAI_CSS, unsafe_allow_html=True)

# Icons
SVG_HELP = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>'
SVG_BELL = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg>'
SVG_ALERT = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>'

# Topbar
topbar_html = (
    "<div class='akamai-topbar'>"
    "<div class='akamai-brand'>akamai</div>"
    "<div class='akamai-search-box'>🔍 Search services, accounts, and more &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; All ⌄</div>"
    "<div class='akamai-top-right'>"
    "<div style='cursor:pointer;'>+ Create</div>"
    f"<div class='icon-container'>{SVG_HELP}</div>"
    f"<div class='icon-container'>{SVG_BELL}<span class='notification-badge'>3</span></div>"
    f"<div class='icon-container'>{SVG_ALERT}<span class='notification-badge'>1</span></div>"
    "<div style='text-align: right; margin-left: 10px; line-height: 1.2;'><strong>Nikhil Goyal</strong><br><span style='font-size: 10px; color: #9DA7B3;'>AKAMAI TECHNOLOGIES - ASSETS ⌄</span></div>"
    "</div>"
    "</div>"
)
st.markdown(topbar_html, unsafe_allow_html=True)

# ==========================================
# 🎛️ 4. MODE & VERSION SELECTOR
# ==========================================
mode_col1, mode_col2 = st.columns([2, 1])
with mode_col1:
    st.markdown("<h2 style='margin-top:-5px; margin-bottom: 0px; font-weight: 800; color:#1E2228;'>Akamai EI - EdgeIntelligence Marketplace</h2>", unsafe_allow_html=True)
with mode_col2:
    app_version = st.selectbox("Marketplace Mode:", ["Standard GTM Engine (V1)", "Advanced Enterprise Engine (V2)"])

is_v2 = "V2" in app_version

# ==========================================
# 📣 5. BANNERS (V1 vs V2)
# ==========================================
if is_v2:
    # V2 Feature 5: Event-Driven Proactive Threat Nudge
    nudge_html = (
        "<div class='nudge-alert'>"
        "<div><span style='color:#EF4444; font-weight:800;'>⚠️ PROACTIVE THREAT ALERT:</span> "
        "<span style='font-size:12px; color:#1E2228;'>Akamai Telemetry detected a <b>340% surge in API Scraping</b> across Retail peers in APAC in the last 24 hrs. Your active AAP rules are unshielded.</span></div>"
        "<button style='background-color:#EF4444; color:white; border:none; padding:5px 12px; font-weight:700; border-radius:4px; font-size:11px; cursor:pointer;'>Auto-Apply $0 Trial Shield</button>"
        "</div>"
    )
    st.markdown(nudge_html, unsafe_allow_html=True)
else:
    banner_html = (
        "<div style='background-color: #E6F4EA; border-left: 4px solid #137333; padding: 10px 16px; margin-bottom: 16px; border-radius: 4px; display: flex; justify-content: space-between; align-items: center;'>"
        "<span style='font-size: 12px; color: #137333; font-weight: 700;'>✨ New Solutions Available:</span>"
        "<span style='font-size: 12px; color: #2B313A; margin-left: 12px; flex-grow: 1;'>Explore our latest AI-era defenses including <b>Brand Guardian</b> and <b>Guardicore Segmentation</b>.</span>"
        "<a href='#' style='font-size: 12px; font-weight: 700; color: #137333; text-decoration: none;'>View Catalog →</a>"
        "</div>"
    )
    st.markdown(banner_html, unsafe_allow_html=True)

# ==========================================
# 📊 6. CATALOG & DIAGNOSTIC LOGIC
# ==========================================
DELIVERY_CATALOG = ["api.retailstore.com (E-Commerce API)", "www.globalbank.com (Main Site)", "media.streaming.net (Video Assets)"]
SECURITY_CATALOG = ["AAP Baseline Security", "App & API Protector (No Bot Protection)", "Legacy WAF Ruleset"]

def analyze_infrastructure(track_internal, del_env, sec_env, industry, region, context, v2_active):
    if track_internal == "Track 1":
        pillars = {
            "Security": {
                "icon": "🛡️", "color": "#0072CE",
                "free_issue": "Config Scan: Essential Adaptive Rate Controls and Bot Visibility are inactive.",
                "free_enh": "Enabling these contracted features maps bot traffic and mitigates volumetric spikes.",
                "free_unused": ["Adaptive Rate Controls", "Bot Visibility", "IP Deny"],
                "free_compliance": "PCI-DSS 4.0 Req 6.4",
                "free_value": "$14,000 Included Value",
                "addon_name": "Malware Protection",
                "addon_issue": "Vulnerability to malicious file uploads detected at edge.",
                "addon_desc": "Intercepts and blocks malicious files from reaching backend.",
                "addon_compliance": "SOC 2 Type II"
            },
            "Reliability": {
                "icon": "⚙️", "color": "#0072CE",
                "free_issue": "Config Scan: No Site Failover or Site Shield origin cloaking configured.",
                "free_enh": "Cloaks origin from direct attacks and gracefully handles timeout spikes.",
                "free_unused": ["Site Failover", "SureRoute", "Site Shield"],
                "free_compliance": "ISO 27001 Availability",
                "free_value": "$18,000 Included Value",
                "addon_name": "DataStream 2",
                "addon_issue": "Lack of real-time operational log visibility during outages.",
                "addon_desc": "Delivers sub-second logs to SIEM for rapid incident response.",
                "addon_compliance": "SIEM Audit Readiness"
            },
            "Performance": {
                "icon": "🚀", "color": "#0072CE",
                "free_issue": "Config Scan: Edge caching and SureRoute optimizations underutilized.",
                "free_enh": "Bypasses internet congestion and maximizes origin offload.",
                "free_unused": ["Dynamic Caching", "TCP Optimization", "Edge Compression"],
                "free_compliance": "Core Web Vitals Pass",
                "free_value": "$10,000 Included Value",
                "addon_name": "API Acceleration",
                "addon_issue": "Dynamic API payloads experiencing latency bottleneck.",
                "addon_desc": "Optimizes routing for non-cacheable dynamic API traffic.",
                "addon_compliance": "Global SLA Benchmark"
            }
        }
        
        # V2 Feature 1: Add 4th Pillar (Cloud Compute)
        if v2_active:
            pillars["Cloud Compute"] = {
                "icon": "☁️", "color": "#10B981",
                "free_issue": "Config Scan: Heavy origin compute tasks executing on expensive AWS/GCP instances.",
                "free_enh": "Shift lightweight computing and header logic directly to Akamai EdgeWorkers.",
                "free_unused": ["EdgeWorkers Basic", "EdgeKV Storage", "JWT Edge Auth"],
                "free_compliance": "Origin Offload Standard",
                "free_value": "$8,500 Included Value",
                "addon_name": "Akamai Connected Cloud (Linode)",
                "addon_issue": "High egress fee costs on third-party cloud origin infrastructure.",
                "addon_desc": "Migrate core microservices to Akamai Cloud for 80% lower egress costs.",
                "addon_compliance": "Multi-Cloud FinOps"
            }
        return {"track": "Track 1", "pillars": pillars}

    elif track_internal == "Track 2":
        ind_data = {
            "metrics": [
                {"label": "YoY Attack Volume", "val": "+257%", "color": "#1E2228"},
                {"label": "Primary Vector", "val": "API Abuse", "color": "#0072CE"},
                {"label": "Peer Zero-Trust Adoption", "val": "83%", "color": "#1E2228"}
            ],
            "visual": [
                {"label": "Credential Stuffing", "pct": 55, "color": "#D93025"},
                {"label": "Volumetric DDoS", "pct": 25, "color": "#F59E0B"},
                {"label": "Web Exploits", "pct": 20, "color": "#0072CE"}
            ],
            "fact": f"In {region}, {industry} platforms face hyper-targeted scraper bots and complex API DDoS attacks.",
            "recs": [
                {"title": "Bot Manager Premier & API Security", "desc": "Intercepts credential stuffing and discovers shadow APIs.", "icon": "🤖", "compliance": "PCI-DSS 4.0"},
                {"title": "Global Traffic Management (GTM)", "desc": "Ensures continuous availability via DNS failover.", "icon": "⚙️", "compliance": "FSI Regulatory SLA"},
                {"title": "API Acceleration", "desc": "Offloads origin compute and improves heavy dynamic API latency.", "icon": "🚀", "compliance": "Open Banking"}
            ]
        }
        return {"track": "Track 2", "industry_data": ind_data}
    else:
        return {"track": "Track 3", "custom_insight": {
            "title": "Bot Manager Premier (New Solution)",
            "desc": "Your requirement targets credential stuffing. Bot Manager Premier integrates seamlessly with your edge deployment to drop malicious attempts without CAPTCHAs.",
            "comp": "Account Takeover Protection",
            "is_existing": False
        }}

# ==========================================
# 🖥️ 7. MAIN UI LAYOUT
# ==========================================
col1, col2 = st.columns([0.8, 2.5], gap="large")

with col1:
    st.markdown('<div class="akamai-card">', unsafe_allow_html=True)
    st.markdown('<div class="akamai-card-title">1. Analysis Approach</div>', unsafe_allow_html=True)
    
    track_choice = st.radio("Privacy Track", [
        "Scan My Configurations (Deep Analysis)", 
        "Use Industry Benchmarks (No Scan Required)",
        "Describe a Specific Challenge (Custom Input)"
    ], label_visibility="collapsed")
    
    st.markdown("<hr style='margin: 12px 0; border: none; border-top: 1px solid #E2E8F0;'>", unsafe_allow_html=True)

    del_env, sec_env, industry_input, region_input, issue_input = None, None, None, None, ""

    if track_choice == "Scan My Configurations (Deep Analysis)":
        track_internal = "Track 1"
        header_str = "Config Scan"
        st.markdown("<p style='font-size: 11px; color: #0072CE; font-weight: 600;'>Select active AAP configs for deep analysis.</p>", unsafe_allow_html=True)
        del_env = st.selectbox("Delivery Config:", DELIVERY_CATALOG)
        sec_env = st.selectbox("Security Config:", SECURITY_CATALOG)
    elif track_choice == "Use Industry Benchmarks (No Scan Required)":
        track_internal = "Track 2"
        header_str = "Industry Benchmark"
        industry_input = st.selectbox("Industry Sector:", ["Financial Services", "Retail & E-Commerce", "Media & Entertainment"])
        region_input = st.selectbox("Primary Region:", ["North America", "EMEA", "Asia Pacific"])
    else:
        track_internal = "Track 3"
        header_str = "Custom Context"
        issue_input = st.text_area("Business Context:", placeholder="e.g., We need to stop automated credential stuffing...", height=100)
    
    st.markdown("<br>", unsafe_allow_html=True)
    run_scan = st.button("Analyze Requirements", type="primary", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if run_scan:
        result = analyze_infrastructure(track_internal, del_env, sec_env, industry_input, region_input, issue_input, is_v2)
        
        st.markdown('<div class="akamai-card" style="background-color: #FAFAFA;">', unsafe_allow_html=True)
        
        # V2 Feature 2: Financial ROI & "Wasted Value" Calculator
        if is_v2 and result["track"] == "Track 1":
            st.markdown("""
            <div class='roi-banner'>
                <div>
                    <div style='font-size:11px; color:#9CA3AF; text-transform:uppercase; font-weight:700;'>Contract Utilization Score</div>
                    <div class='roi-score'>58% <span style='font-size:14px; color:#E5E7EB;'>(Underutilized)</span></div>
                </div>
                <div>
                    <div style='font-size:11px; color:#9CA3AF; text-transform:uppercase; font-weight:700;'>Unclaimed Contract Value</div>
                    <div class='roi-wasted'>$50,500 <span style='font-size:12px; color:#FCA5A5;'>/ year left on table</span></div>
                </div>
                <div>
                    <button style='background-color:#0072CE; color:white; border:none; padding:8px 14px; font-weight:700; border-radius:4px; font-size:11px; cursor:pointer;'>📄 Export CISO Board Report</button>
                </div>
            </div>
            """, unsafe_allow_html=True)

        if result["track"] == "Track 1":
            st.markdown(f'<div class="akamai-card-title">Configuration Gap Analysis ({header_str})</div>', unsafe_allow_html=True)
            
            p_count = len(result["pillars"])
            p_cols = st.columns(p_count, gap="small")
            
            for idx, (pillar_name, data) in enumerate(result["pillars"].items()):
                with p_cols[idx]:
                    free_items_html = "".join([f"<li>{item}</li>" for item in data['free_unused']])
                    
                    value_tag = f"<span class='tag-badge tag-value'>💰 {data['free_value']}</span>" if is_v2 else ""
                    
                    # V2 Feature 3: "Push to Staging" button alongside TechDocs/PS
                    stage_btn_html = "<button class='mini-stage-btn' title='Safely test config on Akamai Staging Network.'>🧪 Push to Staging</button>" if is_v2 else ""

                    card_html = (
                        f"<div class='pillar-card' style='border-top: 3px solid {data['color']};'>"
                        f"<div class='pillar-header'><span>{data['icon']} {pillar_name}</span></div>"
                        
                        f"<div class='section-label' style='color:#0072CE;'>✅ Available on Contract</div>"
                        f"<div class='info-box free'>"
                        f"<div style='flex-grow: 1;'>"
                        f"<div class='tag-container'>"
                        f"<span class='tag-badge tag-compliance'>🔒 {data['free_compliance']}</span>"
                        f"{value_tag}"
                        f"</div>"
                        f"<div class='info-issue'>{data['free_issue']}</div>"
                        f"<ul class='free-list'>{free_items_html}</ul>"
                        f"</div>"
                        f"<button class='mini-enable-btn'>Learn How to Enable</button>"
                        f"{stage_btn_html}"
                        f"</div>"
                        
                        f"<div class='section-label' style='color:#D93025;'>🚀 Recommended Add-on</div>"
                        f"<div class='info-box addon'>"
                        f"<div style='flex-grow: 1;'>"
                        f"<div class='tag-container'>"
                        f"<span class='tag-badge tag-compliance'>🔒 {data['addon_compliance']}</span>"
                        f"</div>"
                        f"<div class='info-title'>{data['addon_name']}</div>"
                        f"<div class='info-desc'>{data['addon_desc']}</div>"
                        f"</div>"
                        f"<button class='mini-buy-btn'>Try / Buy Add-on</button>"
                        f"</div>"
                        f"</div>"
                    )
                    st.markdown(card_html, unsafe_allow_html=True)

        elif result["track"] == "Track 2":
            ind_data = result["industry_data"]
            st.markdown(f'<div class="akamai-card-title">Industry Threat Landscape ({industry_input} - {region_input})</div>', unsafe_allow_html=True)
            
            m_cols = st.columns(3, gap="small")
            for i, metric in enumerate(ind_data["metrics"]):
                with m_cols[i]:
                    st.markdown(f"""
                    <div class='metric-box'>
                        <div class='metric-val' style='color: {metric["color"]};'>{metric["val"]}</div>
                        <div class='metric-label'>{metric["label"]}</div>
                    </div>
                    """, unsafe_allow_html=True)
            
            v_bars = "".join([f"<div class='visual-segment' style='width: {v['pct']}%; background-color: {v['color']};'>{v['pct']}%</div>" for v in ind_data["visual"]])
            v_legend = "".join([f"<div><span class='legend-dot' style='background-color: {v['color']};'></span>{v['label']}</div>" for v in ind_data["visual"]])
            
            st.markdown(f"""
            <div style='background-color: #FFFFFF; border: 1px solid #E2E8F0; padding: 14px; border-radius: 6px; margin-top: 12px; margin-bottom: 16px;'>
                <div style='font-size: 12px; color: #1E2228; font-weight: 600;'>{ind_data["fact"]}</div>
                <div class='visual-bar-container'>{v_bars}</div>
                <div class='visual-legend'>{v_legend}</div>
            </div>
            """, unsafe_allow_html=True)

        else:
            custom_insight = result["custom_insight"]
            st.markdown(f"""
            <div style='background-color: #FFFFFF; border: 1px solid #E2E8F0; padding: 20px; border-radius: 8px; border-top: 4px solid #0072CE;'>
                <div class='tag-badge tag-compliance' style='font-size:11px; display:inline-block;'>🔒 {custom_insight['comp']}</div>
                <h4 style='margin: 8px 0; color: #1E2228;'>Recommended Fit: {custom_insight['title']}</h4>
                <p style='font-size: 13px; color: #475569;'>{custom_insight['desc']}</p>
                <button style='background-color: #0072CE; color: white; border: none; padding: 8px 16px; font-weight: 600; border-radius: 4px; font-size: 12px;'>Try / Buy Solution</button>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class='akamai-card' style='text-align: center; padding: 60px 20px; background-color: #FAFAFA;'>
            <h4 style='color: #1E2228; margin-bottom: 8px;'>Awaiting Analysis Parameters</h4>
            <p style='font-size: 12px; color: #64748B;'>Select your evaluation method on the left and click "Analyze Requirements" to view configuration insights.</p>
        </div>
        """, unsafe_allow_html=True)
