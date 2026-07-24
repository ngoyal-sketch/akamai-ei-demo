import streamlit as st

# ==========================================
# ⚙️ 1. PAGE SETUP & COMPACT ENTERPRISE STYLING
# ==========================================
st.set_page_config(page_title="Akamai Marketplace | Control Center", layout="wide", initial_sidebar_state="expanded")

AKAMAI_CSS = """
<style>
    /* 1. Ultra-Tight Padding to pull everything up into one view */
    .block-container { padding: 1.5rem 2rem 0.5rem 2rem !important; max-width: 100% !important; }
    header { display: none !important; }
    
    .stApp { background-color: #F4F6F9; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
    
    /* 2. Topbar */
    .akamai-topbar {
        background-color: #1E2228; color: #FFFFFF; padding: 10px 24px; 
        margin-top: -1.5rem; margin-left: -2rem; margin-right: -2rem; margin-bottom: 12px;
        display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #2B313A;
    }
    .akamai-brand { font-weight: 800; font-size: 17px; letter-spacing: 0.5px; color: #0072CE; white-space: nowrap; }
    .akamai-search-box { background-color: #2B313A; border: 1px solid #3A424D; border-radius: 4px; padding: 5px 12px; color: #C0C7D0; width: 30vw; min-width: 250px; max-width: 400px; font-size: 11px; }
    .akamai-top-right { display: flex; align-items: center; gap: 16px; font-size: 11px; color: #E2E8F0; white-space: nowrap; }
    
    .icon-container { position: relative; display: flex; align-items: center; justify-content: center; cursor: pointer; }
    .notification-badge { 
        position: absolute; top: -5px; right: -6px; background-color: #D93025; color: white; 
        font-size: 8px; font-weight: 700; padding: 2px 4px; border-radius: 10px; border: 2px solid #1E2228;
    }
    
    /* 3. Base Cards */
    .akamai-card { background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 4px; padding: 12px 16px; margin-bottom: 10px; box-shadow: 0 1px 3px rgba(0,0,0,0.03); }
    .akamai-card-title { font-size: 15px; font-weight: 700; color: #1E2228; margin-bottom: 10px; }
    
    /* 4. Three-Pillar Status Cards */
    .pillar-card { background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 6px; padding: 12px; display: flex; flex-direction: column; height: 100%; }
    .pillar-header { font-size: 13px; font-weight: 700; color: #1E2228; text-transform: uppercase; border-bottom: 2px solid #E2E8F0; padding-bottom: 6px; margin-bottom: 8px; display: flex; justify-content: space-between; align-items: center; }
    
    .mini-enable-btn { background-color: #10B981; color: #FFFFFF; border: none; border-radius: 3px; padding: 3px 8px; font-size: 9px; font-weight: 700; cursor: pointer; text-transform: none; letter-spacing: 0; }
    .mini-enable-btn:hover { background-color: #059669; }
    
    .mini-buy-btn { background-color: #0072CE; color: #FFFFFF; border: none; border-radius: 3px; padding: 4px 10px; font-size: 10px; font-weight: 700; cursor: pointer; text-transform: none; margin-top: 6px; width: 100%; }
    .mini-buy-btn:hover { background-color: #005A9E; }
    
    .section-label { font-size: 10px; font-weight: 800; color: #0072CE; text-transform: uppercase; margin-bottom: 4px; letter-spacing: 0.5px; }
    
    /* Info Boxes inside Cards */
    .info-box { border-radius: 4px; padding: 8px; margin-bottom: 8px; border: 1px solid transparent; flex-grow: 1; display: flex; flex-direction: column;}
    .info-box.free { background-color: #F0FDF4; border-color: #BBF7D0; }
    .info-box.addon { background-color: #F8FAFC; border-color: #E2E8F0; }
    .info-box.peer { background-color: #F0F7FF; border-color: #CCE3FD; }
    
    .info-title { font-size: 12px; font-weight: 700; color: #1E2228; margin-bottom: 3px; }
    .info-issue { font-size: 10.5px; font-weight: 600; margin-bottom: 3px; line-height: 1.3;}
    .info-issue.free-text { color: #166534; }
    .info-issue.addon-text { color: #D93025; }
    .info-desc { font-size: 10.5px; line-height: 1.3; margin-bottom: 6px; }
    .info-desc.free-text { color: #15803D; }
    .info-desc.addon-text { color: #475569; }
    .info-desc.peer-text { color: #0072CE; }

    .free-list { margin: 0; padding-left: 16px; font-size: 10.5px; color: #166534; font-weight: 600; }
    .free-list li { margin-bottom: 2px; }

    /* Track 2 specific UI (Industry Dashboard) */
    .metric-box { background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 4px; padding: 12px; text-align: center; }
    .metric-val { font-size: 20px; font-weight: 800; color: #1E2228; margin-bottom: 2px; }
    .metric-label { font-size: 10.5px; color: #64748B; font-weight: 700; text-transform: uppercase; }
    
    .visual-bar-container { background-color: #E2E8F0; border-radius: 4px; height: 16px; width: 100%; display: flex; overflow: hidden; margin-top: 10px; margin-bottom: 6px;}
    .visual-segment { height: 100%; display: flex; align-items: center; justify-content: center; font-size: 9px; color: white; font-weight: 700; }
    .visual-legend { display: flex; gap: 12px; font-size: 10.5px; color: #475569; font-weight: 600; justify-content: center; }
    .legend-dot { display: inline-block; width: 8px; height: 8px; border-radius: 50%; margin-right: 4px; }

    .rec-card { background-color: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 12px; height: 100%; border-top: 3px solid #0072CE; }
    .rec-card h4 { margin: 0 0 6px 0; font-size: 13px; color: #1E2228; }
    .rec-card p { margin: 0; font-size: 11px; color: #475569; line-height: 1.4; }

    /* Streamlit overrides for tighter buttons & inputs */
    .stButton > button { font-size: 11.5px !important; padding: 4px 10px !important; min-height: 0 !important; font-weight: 600 !important; border-radius: 4px !important; width: 100% !important;}
    .btn-primary > button { background-color: #0072CE !important; color: white !important; border: none !important; }
    .btn-secondary > button { background-color: white !important; color: #0072CE !important; border: 1px solid #0072CE !important; }
    
    div[data-testid="stVerticalBlock"] > div { padding-bottom: 0.1rem !important; }
    .stTextArea textarea { font-size: 12px !important; }
    .stSelectbox div { font-size: 12px !important; }
</style>
"""
st.markdown(AKAMAI_CSS, unsafe_allow_html=True)

# SVG Icons
SVG_HELP = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>'
SVG_BELL = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg>'
SVG_ALERT = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>'

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
    "<div style='text-align: right; margin-left: 10px;'><strong>Nikhil Goyal</strong><br><span style='font-size: 9px; color: #9DA7B3;'>AKAMAI TECHNOLOGIES - ASSETS ⌄</span></div>"
    "</div>"
    "</div>"
)
st.markdown(topbar_html, unsafe_allow_html=True)

# ==========================================
# 2. MOCK CATALOG DATA
# ==========================================
DELIVERY_CATALOG = ["api.retailstore.com (E-Commerce API)", "www.globalbank.com (Main Site)", "media.streaming.net (Video Assets)"]
SECURITY_CATALOG = ["AAP Baseline Security", "App & API Protector (No Bot Protection)", "Legacy WAF Ruleset"]

# ==========================================
# 3. DIAGNOSTIC ENGINE LOGIC
# ==========================================
def analyze_infrastructure(track_internal, del_env, sec_env, industry, region, context):
    
    # ----------------------------------------
    # TRACK 1: DEEP CONFIG SCAN
    # ----------------------------------------
    if track_internal == "Track 1":
        pillars = {
            "Security": {
                "icon": "🛡️", "color": "#0072CE",
                "free_issue": "Config Scan: Essential Adaptive Rate Controls and Bot Visibility are inactive on this policy.",
                "free_enh": "Enabling these contracted AAP features will instantly map bot traffic and mitigate volumetric spikes.",
                "free_unused": ["Adaptive Rate Controls", "Bot Visibility and Mitigation", "IP Deny"],
                "addon_name": "Malware Protection (Add-on)",
                "addon_issue": "Vulnerability to malicious file uploads detected at the edge.",
                "addon_desc": "Malware Protection seamlessly integrates with AAP to intercept and block malicious files from reaching your backend."
            },
            "Reliability": {
                "icon": "⚙️", "color": "#10B981",
                "free_issue": "Config Scan: No Site Failover or Site Shield origin cloaking configured for the primary backend.",
                "free_enh": "Activating these AAP modules cloaks your origin from direct internet attacks and gracefully handles timeout spikes.",
                "free_unused": ["Site Failover", "SureRoute for Failover", "Site Shield"],
                "addon_name": "DataStream (Add-on)",
                "addon_issue": "Lack of real-time operational visibility into Edge events during critical outages.",
                "addon_desc": "DataStream provides near real-time log delivery to your SIEM/analytics endpoints for rapid reliability incident response."
            },
            "Performance": {
                "icon": "🚀", "color": "#F59E0B",
                "free_issue": "Config Scan: Edge caching and SureRoute optimizations are severely underutilized.",
                "free_enh": "Applying these included features actively bypasses internet congestion and maximizes origin offload.",
                "free_unused": ["Caching", "SureRoute for Performance", "TCP Optimization"],
                "addon_name": "API Acceleration (Add-on)",
                "addon_issue": "Heavy dynamic API payloads are experiencing severe delivery latency.",
                "addon_desc": "API Acceleration specifically optimizes routing and delivery for non-cacheable, heavy API traffic."
            }
        }
        bundle = {
            "name": "AAP Ultimate Extension Bundle",
            "desc": "Based on the scan, upgrade to unlock all premium add-on features in a single, unified contract."
        }
        return {"track": "Track 1", "pillars": pillars, "bundle": bundle}

    # ----------------------------------------
    # TRACK 2: INDUSTRY BENCHMARK (MACRO-TELEMETRY)
    # ----------------------------------------
    elif track_internal == "Track 2":
        if industry == "Financial Services":
            ind_data = {
                "metrics": [
                    {"label": "YoY Attack Volume", "val": "+257%", "color": "#D93025"},
                    {"label": "Primary Vector", "val": "API Abuse", "color": "#F59E0B"},
                    {"label": "Peer Zero-Trust Adoption", "val": "83%", "color": "#10B981"}
                ],
                "visual": [
                    {"label": "Credential Stuffing", "pct": 55, "color": "#D93025"},
                    {"label": "Volumetric DDoS", "pct": 25, "color": "#F59E0B"},
                    {"label": "Web Exploits", "pct": 20, "color": "#0072CE"}
                ],
                "fact": f"In {region}, Financial platforms face hyper-targeted scraper bots and complex DDoS attacks designed to mask unauthorized transactions.",
                "recs": [
                    {"title": "Bot Manager Premier & API Security", "desc": "Intercepts sophisticated credential stuffing and discovers shadow APIs.", "icon": "🤖"},
                    {"title": "Global Traffic Management (GTM)", "desc": "Ensures continuous availability through global DNS-level failover routing.", "icon": "⚙️"},
                    {"title": "API Acceleration", "desc": "Offloads origin compute and drastically improves heavy dynamic API latency.", "icon": "🚀"}
                ]
            }
        else:
            ind_data = {
                "metrics": [
                    {"label": "Scraper Bot Traffic", "val": "42%", "color": "#D93025"},
                    {"label": "Avg. Page Load Goal", "val": "< 2.0s", "color": "#10B981"},
                    {"label": "Peer Edge Adoption", "val": "78%", "color": "#0072CE"}
                ],
                "visual": [
                    {"label": "Scraping & ATO", "pct": 45, "color": "#D93025"},
                    {"label": "Web Exploits (SQLi/XSS)", "pct": 35, "color": "#F59E0B"},
                    {"label": "DDoS", "pct": 20, "color": "#0072CE"}
                ],
                "fact": f"For {industry} in {region}, competitive scraping degrades inventory systems, while heavy media payloads impact conversion rates.",
                "recs": [
                    {"title": "Bot Manager Premier", "desc": "Stops inventory hoarding and pricing scrapers without degrading the shopper experience.", "icon": "🤖"},
                    {"title": "App & API Protector", "desc": "Consolidates Layer-7 WAF protections and API governance to thwart exploits.", "icon": "🛡️"},
                    {"title": "Image & Video Manager", "desc": "Automatically converts media to next-gen formats at the edge to reduce payloads.", "icon": "🖼️"}
                ]
            }
        return {"track": "Track 2", "industry_data": ind_data}

    # ----------------------------------------
    # TRACK 3: CUSTOM BUSINESS CONTEXT
    # ----------------------------------------
    else:
        c_lower = context.lower()
        if any(k in c_lower for k in ["file", "upload", "malware", "virus"]):
            rec_title = "Malware Protection (Add-on)"
            rec_desc = "Based on your requirement regarding file uploads, Malware Protection seamlessly integrates with AAP to intercept and block malicious files from reaching your backend."
        elif any(k in c_lower for k in ["api", "data breach", "shadow"]):
            rec_title = "API Protections - Basic (Included)"
            rec_desc = "To address your API concerns, ensure the 'API Protections - Basic' module (included in your current AAP contract) is fully configured for endpoint enforcement."
        elif any(k in c_lower for k in ["bot", "scraper", "credential", "stuffing"]):
            rec_title = "Bot Manager Premier"
            rec_desc = "Your requirement specifically targets credential stuffing. Bot Manager Premier utilizes behavioral telemetry and advanced cryptographics to identify and drop malicious login attempts without CAPTCHAs."
        else:
            rec_title = "Adaptive Security Engine (ASE)"
            rec_desc = "Based on your use case, our AI recommends reviewing your active AAP ruleset and ensuring Adaptive Security Engine (ASE) is operating in automatic mode to optimize your posture."
        return {"track": "Track 3", "custom_insight": {"title": rec_title, "desc": rec_desc}}


# ==========================================
# 4. MAIN UI LAYOUT
# ==========================================
st.markdown("<h2 style='margin-top:-15px; margin-bottom: 8px; color:#1E2228;'>Akamai EI - EdgeIntelligence Marketplace</h2>", unsafe_allow_html=True)

# Compact LA Banner
banner_html = (
    "<div style='background-color: #E6F4EA; border-left: 3px solid #137333; padding: 6px 10px; margin-bottom: 12px; border-radius: 4px; display: flex; justify-content: space-between; align-items: center;'>"
    "<span style='font-size: 11px; color: #137333; font-weight: 700;'>✨ New Solutions Available:</span>"
    "<span style='font-size: 11px; color: #2B313A; margin-left: 8px; flex-grow: 1;'>Explore our latest AI-era defenses including <b>Brand Guardian</b>, <b>AI Brand Presence</b>, and <b>Guardicore Segmentation</b>.</span>"
    "<a href='#' style='font-size: 11px; font-weight: 700; color: #137333; text-decoration: none; white-space: nowrap;'>View Catalog →</a>"
    "</div>"
)
st.markdown(banner_html, unsafe_allow_html=True)

col1, col2 = st.columns([1, 2.3], gap="medium")

# --- LEFT PANE ---
with col1:
    st.markdown('<div class="akamai-card" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<div class="akamai-card-title">1. Analysis Approach</div>', unsafe_allow_html=True)
    
    st.markdown("<p style='font-size: 11px; color: #475569; margin-bottom: 6px; font-weight: 600;'>Select how you want us to evaluate your needs:</p>", unsafe_allow_html=True)
    track_choice = st.radio("Privacy Track", [
        "Scan My Configurations (Deep Analysis)", 
        "Use Industry Benchmarks (No Scan Required)",
        "Describe a Specific Challenge (Custom Input)"
    ], label_visibility="collapsed")
    
    st.markdown("<hr style='margin: 8px 0; border: none; border-top: 1px solid #E2E8F0;'>", unsafe_allow_html=True)

    del_env, sec_env, industry_input, region_input, issue_input = None, None, None, None, ""

    if track_choice == "Scan My Configurations (Deep Analysis)":
        track_internal = "Track 1"
        header_str = "Config Scan"
        st.markdown("<p style='font-size: 11.5px; color: #0072CE; margin-bottom: 6px;'>Select active AAP configs for deep analysis.</p>", unsafe_allow_html=True)
        del_env = st.selectbox("Delivery Config:", DELIVERY_CATALOG)
        sec_env = st.selectbox("Security Config:", SECURITY_CATALOG)
    elif track_choice == "Use Industry Benchmarks (No Scan Required)":
        track_internal = "Track 2"
        header_str = "Industry Benchmark"
        st.markdown("<p style='font-size: 11.5px; color: #0072CE; margin-bottom: 6px;'>Deep scanning disabled. Using macro-telemetry.</p>", unsafe_allow_html=True)
        industry_input = st.selectbox("Industry Sector:", ["Financial Services", "Retail & E-Commerce", "Media & Entertainment", "Public Sector"])
        region_input = st.selectbox("Primary Region:", ["North America", "EMEA", "Asia Pacific", "LATAM"])
    else:
        track_internal = "Track 3"
        header_str = "Custom Context"
        st.markdown("<p style='font-size: 11.5px; color: #0072CE; margin-bottom: 6px;'>Describe your specific business context, issue, or requirement below.</p>", unsafe_allow_html=True)
        issue_input = st.text_area("Business Context:", placeholder="e.g., We need to stop automated credential stuffing...", height=100, label_visibility="collapsed")
    
    st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
    run_scan = st.button("Analyze Requirements", type="primary", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- RIGHT PANE ---
with col2:
    if run_scan:
        result = analyze_infrastructure(track_internal, del_env, sec_env, industry_input, region_input, issue_input)
        
        st.markdown('<div class="akamai-card" style="background-color: #FAFAFA; padding: 12px 16px;">', unsafe_allow_html=True)
        
        # ----------------------------------------
        # UI RENDER FOR TRACK 1 (Config Scan)
        # ----------------------------------------
        if result["track"] == "Track 1":
            st.markdown(f'<div class="akamai-card-title" style="margin-bottom: 8px;">Configuration Gap Analysis (Config Scan)</div>', unsafe_allow_html=True)
            
            p_cols = st.columns(3)
            for idx, (pillar_name, data) in enumerate(result["pillars"].items()):
                with p_cols[idx]:
                    free_items_html = "".join([f"<li>{item}</li>" for item in data['free_unused']])
                    card_html = (
                        f"<div class='pillar-card' style='border-top: 3px solid {data['color']};'>"
                        f"<div class='pillar-header'><span>{data['icon']} {pillar_name}</span></div>"
                        
                        f"<div class='section-label' style='color:#166534;'>✅ Contracted (Free)</div>"
                        f"<div class='info-box free' style='display: flex; flex-direction: column;'>"
                        f"<div style='flex-grow: 1;'>"
                        f"<div class='info-issue free-text'>{data['free_issue']}</div>"
                        f"<div class='info-desc free-text'><b>Enhancement:</b> {data['free_enh']}</div>"
                        f"<ul class='free-list'>{free_items_html}</ul>"
                        f"</div>"
                        f"<button class='mini-enable-btn' title='View documentation on how to enable these contracted features.'>Enable Features</button>"
                        f"</div>"
                        
                        f"<div class='section-label' style='color:#D93025; margin-top: 2px;'>🚀 Recommended Add-on</div>"
                        f"<div class='info-box addon' style='display: flex; flex-direction: column;'>"
                        f"<div style='flex-grow: 1;'>"
                        f"<div class='info-title'>{data['addon_name']}</div>"
                        f"<div class='info-issue addon-text'>Issue: {data['addon_issue']}</div>"
                        f"<div class='info-desc addon-text'>{data['addon_desc']}</div>"
                        f"</div>"
                        f"<button class='mini-buy-btn' title='Try: Adds a $0 line item for 30-60 days. Buy: Routes to your sales rep.'>Try / Buy</button>"
                        f"</div>"
                        f"</div>"
                    )
                    st.markdown(card_html, unsafe_allow_html=True)
                    
            bundle = result["bundle"]
            bundle_html = (
                "<div style='background-color: #F0F7FF; border: 1px solid #CCE3FD; border-radius: 4px; padding: 10px 14px; margin-top: 12px; display: flex; align-items: center; justify-content: space-between;'>"
                "<div>"
                f"<div style='font-size: 13px; font-weight: 700; color: #0072CE; margin-bottom: 2px;'>💡 Contract Consolidation: {bundle['name']}</div>"
                f"<div style='font-size: 11px; color: #475569;'>{bundle['desc']}</div>"
                "</div>"
                "<div style='display: flex; gap: 8px;'>"
                "<button title='Try: Adds a $0 line item for 30-60 days. Buy: Routes to your sales rep.' style='background-color: #0072CE; color: white; border: none; border-radius: 4px; padding: 6px 12px; font-weight: 600; font-size: 11px; cursor: pointer; white-space: nowrap;'>Try/Buy Bundle</button>"
                "<button style='background-color: white; color: #0072CE; border: 1px solid #0072CE; border-radius: 4px; padding: 6px 12px; font-weight: 600; font-size: 11px; cursor: pointer; white-space: nowrap;'>Ask IAT</button>"
                "</div>"
                "</div>"
            )
            st.markdown(bundle_html, unsafe_allow_html=True)

        # ----------------------------------------
        # UI RENDER FOR TRACK 2 (Industry Dashboard)
        # ----------------------------------------
        elif result["track"] == "Track 2":
            ind_data = result["industry_data"]
            st.markdown(f'<div class="akamai-card-title" style="margin-bottom: 8px;">Industry Threat Landscape ({industry_input} - {region_input})</div>', unsafe_allow_html=True)
            
            # Top Metrics Row
            m_cols = st.columns(3)
            for i, metric in enumerate(ind_data["metrics"]):
                with m_cols[i]:
                    st.markdown(f"""
                    <div class='metric-box'>
                        <div class='metric-val' style='color: {metric["color"]};'>{metric["val"]}</div>
                        <div class='metric-label'>{metric["label"]}</div>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Middle Visual Row (Traffic / Attack Graph)
            v_bars = "".join([f"<div class='visual-segment' style='width: {v['pct']}%; background-color: {v['color']};'>{v['pct']}%</div>" for v in ind_data["visual"]])
            v_legend = "".join([f"<div><span class='legend-dot' style='background-color: {v['color']};'></span>{v['label']}</div>" for v in ind_data["visual"]])
            
            st.markdown(f"""
            <div style='background-color: #FFFFFF; border: 1px solid #E2E8F0; padding: 12px; border-radius: 6px; margin-top: 10px; margin-bottom: 12px;'>
                <div style='font-size: 11.5px; color: #2B313A; font-weight: 600;'>{ind_data["fact"]}</div>
                <div class='visual-bar-container'>{v_bars}</div>
                <div class='visual-legend'>{v_legend}</div>
            </div>
            <div class="akamai-card-title" style="margin-bottom: 8px; font-size: 14px;">Strategic Solution Recommendations</div>
            """, unsafe_allow_html=True)
            
            # Bottom Recommendations Row (NO BUTTONS INSIDE CARDS)
            r_cols = st.columns(len(ind_data["recs"]))
            for i, rec in enumerate(ind_data["recs"]):
                with r_cols[i]:
                    st.markdown(f"""
                    <div class='rec-card' style='display: flex; flex-direction: column; padding-bottom: 8px; min-height: 110px;'>
                        <div style='flex-grow: 1;'>
                            <h4 style='font-size: 12.5px; margin-bottom: 4px;'>{rec['icon']} {rec['title']}</h4>
                            <p style='font-size: 11px;'>{rec['desc']}</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
            # UNIFIED ACTION ROW FOR ALL TRACK 2 RECOMMENDATIONS
            st.markdown("<div style='margin-top: 12px;'></div>", unsafe_allow_html=True)
            b_spacer1, b_btn1, b_btn2, b_spacer2 = st.columns([1, 1.5, 1.5, 1])
            with b_btn1:
                st.button("Try / Buy Solutions", type="primary", use_container_width=True, key="t2_buy")
            with b_btn2:
                st.button("Ask IAT for Assistance", use_container_width=True, key="t2_iat")
            
        # ----------------------------------------
        # UI RENDER FOR TRACK 3 (Custom Context)
        # ----------------------------------------
        else:
            custom_insight = result["custom_insight"]
            st.markdown(f'<div class="akamai-card-title" style="margin-bottom: 8px;">🎯 Tailored Solution Architecture</div>', unsafe_allow_html=True)
            insight_html = (
                "<div style='background-color: #FFFFFF; border: 1px solid #E2E8F0; padding: 20px; border-radius: 6px; border-top: 4px solid #10B981;'>"
                f"<h4 style='margin: 0 0 8px 0; color: #1E2228; font-size: 16px;'>Recommended Fit: <span style='color:#10B981;'>{custom_insight['title']}</span></h4>"
                f"<p style='margin: 0 0 16px 0; font-size: 13px; color: #475569; line-height: 1.5;'>{custom_insight['desc']}</p>"
                "<div style='display: flex; gap: 10px;'>"
                "<button title='Try: Adds a $0 line item for 30-60 days. Buy: Routes to your sales rep.' style='background-color: #0072CE; color: white; border: none; border-radius: 4px; padding: 8px 16px; font-weight: 600; font-size: 12px; cursor: pointer;'>Try / Buy Solution</button>"
                "<button style='background-color: white; color: #0072CE; border: 1px solid #0072CE; border-radius: 4px; padding: 8px 16px; font-weight: 600; font-size: 12px; cursor: pointer;'>Contact IAT</button>"
                "</div>"
                "</div>"
            )
            st.markdown(insight_html, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)
            
    else:
        empty_state_html = (
            "<div class='akamai-card' style='height: 100%; display: flex; align-items: center; justify-content: center; background-color: #FAFAFA;'>"
            "<div style='text-align: center; padding: 60px 20px;'>"
            "<h4 style='color: #1E2228; margin-bottom: 8px;'>Awaiting Analysis Parameters</h4>"
            "<p style='font-size: 12px; color: #64748B;'>Select your evaluation method on the left and run the scan to identify unused contract features, view industry benchmarks, or receive custom solutions.</p>"
            "</div>"
            "</div>"
        )
        st.markdown(empty_state_html, unsafe_allow_html=True)
