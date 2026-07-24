import streamlit as st

# ==========================================
# ⚙️ 1. PAGE SETUP & COMPACT ENTERPRISE STYLING
# ==========================================
st.set_page_config(page_title="Akamai Marketplace | Control Center", layout="wide", initial_sidebar_state="expanded")

AKAMAI_CSS = """
<style>
    /* 1. Ultra-Tight Padding to pull everything up into one view */
    .block-container { padding: 1.5rem 2rem 1rem 2rem !important; max-width: 100% !important; }
    header { display: none !important; }
    
    /* 2. Global Typography & Background */
    .stApp { 
        background-color: #F4F6F9; 
        font-family: 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; 
        color: #1E2228;
    }
    
    /* 3. Topbar */
    .akamai-topbar {
        background-color: #1E2228; color: #FFFFFF; padding: 12px 24px; 
        margin-top: -1.5rem; margin-left: -2rem; margin-right: -2rem; margin-bottom: 20px;
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
    
    /* 4. Base Cards */
    .akamai-card { background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 6px; padding: 20px 24px; margin-bottom: 12px; box-shadow: 0 1px 4px rgba(0,0,0,0.04); }
    .akamai-card-title { font-size: 18px; font-weight: 700; color: #1E2228; margin-bottom: 16px; }
    
    /* 5. Three-Pillar Status Cards */
    .pillar-card { background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 16px; display: flex; flex-direction: column; height: 100%; }
    .pillar-header { font-size: 14px; font-weight: 700; color: #1E2228; text-transform: uppercase; border-bottom: 1px solid #E2E8F0; padding-bottom: 10px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center; }
    
    /* Buttons - Corporate Theme */
    .mini-enable-btn { background-color: #FFFFFF; color: #0072CE; border: 1px solid #0072CE; border-radius: 4px; padding: 8px 12px; font-size: 12px; font-weight: 600; cursor: pointer; text-transform: none; margin-top: 10px; width: 100%; transition: background-color 0.2s ease; }
    .mini-enable-btn:hover { background-color: #F0F7FF; }
    
    .mini-buy-btn { background-color: #0072CE; color: #FFFFFF; border: none; border-radius: 4px; padding: 8px 12px; font-size: 12px; font-weight: 600; cursor: pointer; text-transform: none; margin-top: 10px; width: 100%; transition: background-color 0.2s ease; }
    .mini-buy-btn:hover { background-color: #005A9E; }
    
    .section-label { font-size: 11px; font-weight: 800; text-transform: uppercase; margin-bottom: 6px; letter-spacing: 0.5px; }
    
    /* Info Boxes inside Cards - Cleaned up to Corporate palette */
    .info-box { border-radius: 6px; padding: 14px; margin-bottom: 16px; border: 1px solid transparent; flex-grow: 1; display: flex; flex-direction: column;}
    .info-box.free { background-color: #F8FAFC; border-color: #E2E8F0; } /* Soft corporate gray/blue instead of bright green */
    .info-box.addon { background-color: #FFFFFF; border-color: #E2E8F0; box-shadow: 0 1px 2px rgba(0,0,0,0.02); }
    
    .info-title { font-size: 14px; font-weight: 700; color: #1E2228; margin-bottom: 6px; }
    .info-issue { font-size: 12px; font-weight: 600; margin-bottom: 6px; line-height: 1.5; color: #1E2228;}
    .info-desc { font-size: 12px; line-height: 1.5; margin-bottom: 10px; color: #475569; }

    .free-list { margin: 0; padding-left: 20px; font-size: 12px; color: #1E2228; font-weight: 500; margin-bottom: 10px; line-height: 1.6;}
    .free-list li { margin-bottom: 4px; }

    /* Tags for Compliance - Corporate Blue Style */
    .tag-container { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 10px; }
    .tag-badge { font-size: 10px; font-weight: 700; padding: 4px 8px; border-radius: 4px; line-height: 1.2; }
    .tag-compliance { background-color: #F0F7FF; color: #0072CE; border: 1px solid #CCE3FD; }

    /* Track 2 specific UI (Industry Dashboard) */
    .metric-box { background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 6px; padding: 16px; text-align: center; }
    .metric-val { font-size: 24px; font-weight: 800; color: #1E2228; margin-bottom: 4px; }
    .metric-label { font-size: 11px; color: #64748B; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;}
    
    .visual-bar-container { background-color: #E2E8F0; border-radius: 6px; height: 20px; width: 100%; display: flex; overflow: hidden; margin-top: 16px; margin-bottom: 10px;}
    .visual-segment { height: 100%; display: flex; align-items: center; justify-content: center; font-size: 11px; color: white; font-weight: 700; }
    .visual-legend { display: flex; gap: 16px; font-size: 12px; color: #475569; font-weight: 600; justify-content: center; }
    .legend-dot { display: inline-block; width: 10px; height: 10px; border-radius: 50%; margin-right: 6px; }

    .rec-card { background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 16px; height: 100%; border-top: 3px solid #0072CE; box-shadow: 0 1px 3px rgba(0,0,0,0.02); }
    .rec-card h4 { margin: 0 0 8px 0; font-size: 14px; color: #1E2228; }
    .rec-card p { margin: 0; font-size: 12px; color: #475569; line-height: 1.5; }

    /* Streamlit overrides for inputs */
    div[data-testid="stVerticalBlock"] > div { padding-bottom: 0.2rem !important; }
    .stTextArea textarea { font-size: 13px !important; padding: 10px !important; }
    .stSelectbox div { font-size: 13px !important; }
    .stRadio label { font-size: 13px !important; color: #1E2228 !important; }
    .stButton > button { padding: 6px 16px !important; font-weight: 600 !important; font-size: 13px !important; border-radius: 4px !important; transition: all 0.2s ease;}
</style>
"""
st.markdown(AKAMAI_CSS, unsafe_allow_html=True)

# SVG Icons
SVG_HELP = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>'
SVG_BELL = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg>'
SVG_ALERT = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>'

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
                "free_compliance": "PCI-DSS 4.0 Req 6.4",
                "addon_name": "Malware Protection (Add-on)",
                "addon_issue": "Vulnerability to malicious file uploads detected at the edge.",
                "addon_desc": "Malware Protection seamlessly integrates with AAP to intercept and block malicious files from reaching your backend.",
                "addon_compliance": "SOC 2 Type II"
            },
            "Reliability": {
                "icon": "⚙️", "color": "#0072CE",
                "free_issue": "Config Scan: No Site Failover or Site Shield origin cloaking configured for the primary backend.",
                "free_enh": "Activating these AAP modules cloaks your origin from direct internet attacks and gracefully handles timeout spikes.",
                "free_unused": ["Site Failover", "SureRoute for Failover", "Site Shield"],
                "free_compliance": "ISO 27001 Availability",
                "addon_name": "DataStream (Add-on)",
                "addon_issue": "Lack of real-time operational visibility into Edge events during critical outages.",
                "addon_desc": "DataStream provides near real-time log delivery to your SIEM/analytics endpoints for rapid reliability incident response.",
                "addon_compliance": "SIEM Audit Readiness"
            },
            "Performance": {
                "icon": "🚀", "color": "#0072CE",
                "free_issue": "Config Scan: Edge caching and SureRoute optimizations are severely underutilized.",
                "free_enh": "Applying these included features actively bypasses internet congestion and maximizes origin offload.",
                "free_unused": ["Caching", "SureRoute for Performance", "TCP Optimization"],
                "free_compliance": "Core Web Vitals Pass",
                "addon_name": "API Acceleration (Add-on)",
                "addon_issue": "Heavy dynamic API payloads are experiencing severe delivery latency.",
                "addon_desc": "API Acceleration specifically optimizes routing and delivery for non-cacheable, heavy API traffic.",
                "addon_compliance": "Global SLA Benchmark"
            }
        }
        return {"track": "Track 1", "pillars": pillars}

    # ----------------------------------------
    # TRACK 2: INDUSTRY BENCHMARK (MACRO-TELEMETRY)
    # ----------------------------------------
    elif track_internal == "Track 2":
        if industry == "Financial Services":
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
                "fact": f"In {region}, Financial platforms face hyper-targeted scraper bots and complex DDoS attacks designed to mask unauthorized transactions.",
                "recs": [
                    {"title": "Bot Manager Premier & API Security", "desc": "Intercepts credential stuffing and discovers shadow APIs.", "icon": "🤖", "compliance": "PCI-DSS 4.0"},
                    {"title": "Global Traffic Management (GTM)", "desc": "Ensures continuous availability through global DNS-level failover routing.", "icon": "⚙️", "compliance": "FSI Regulatory SLA"},
                    {"title": "API Acceleration", "desc": "Offloads origin compute and drastically improves heavy dynamic API latency.", "icon": "🚀", "compliance": "Open Banking Standard"}
                ]
            }
        else:
            ind_data = {
                "metrics": [
                    {"label": "Scraper Bot Traffic", "val": "42%", "color": "#1E2228"},
                    {"label": "Avg. Page Load Goal", "val": "< 2.0s", "color": "#0072CE"},
                    {"label": "Peer Edge Adoption", "val": "78%", "color": "#1E2228"}
                ],
                "visual": [
                    {"label": "Scraping & ATO", "pct": 45, "color": "#D93025"},
                    {"label": "Web Exploits (SQLi/XSS)", "pct": 35, "color": "#F59E0B"},
                    {"label": "DDoS", "pct": 20, "color": "#0072CE"}
                ],
                "fact": f"For {industry} in {region}, competitive scraping degrades inventory systems, while heavy media payloads impact conversion rates.",
                "recs": [
                    {"title": "Bot Manager Premier", "desc": "Stops inventory hoarding and pricing scrapers without degrading shopper experience.", "icon": "🤖", "compliance": "SOC 2 Type II"},
                    {"title": "App & API Protector", "desc": "Consolidates Layer-7 WAF protections and API governance to thwart exploits.", "icon": "🛡️", "compliance": "PCI-DSS 4.0"},
                    {"title": "Image & Video Manager", "desc": "Automatically converts media to next-gen formats at the edge to reduce payloads.", "icon": "🖼️", "compliance": "SEO & Core Web Vitals"}
                ]
            }
        return {"track": "Track 2", "industry_data": ind_data}

    # ----------------------------------------
    # TRACK 3: CUSTOM BUSINESS CONTEXT
    # ----------------------------------------
    else:
        c_lower = context.lower()
        
        # Scenario 1: Covered by existing AAP Contract (Needs PS)
        if any(k in c_lower for k in ["api", "data breach", "shadow", "sql", "xss"]):
            rec_title = "App & API Protector (Already on Contract)"
            rec_desc = "Our AI analysis indicates your current AAP contract already includes robust API discovery and WAF capabilities to address this challenge. However, they may not be fully optimized. To ensure you are utilizing 100% of these product capabilities, we recommend engaging Akamai Professional Services."
            rec_comp = "PCI-DSS 4.0 API Mandate"
            is_existing = True
            
        # Scenario 2: Upsell Required (Bot Manager)
        elif any(k in c_lower for k in ["bot", "scraper", "credential", "stuffing"]):
            rec_title = "Bot Manager Premier (New Solution)"
            rec_desc = "Your requirement specifically targets credential stuffing. Bot Manager Premier integrates seamlessly with your existing edge deployment, utilizing behavioral telemetry and advanced cryptographics to identify and drop malicious login attempts without CAPTCHAs."
            rec_comp = "Account Takeover Protection"
            is_existing = False
            
        # Scenario 3: Upsell Required (Malware)
        elif any(k in c_lower for k in ["file", "upload", "malware", "virus"]):
            rec_title = "Malware Protection (Add-on)"
            rec_desc = "Based on your requirement regarding file uploads, Malware Protection seamlessly integrates with AAP to intercept and block malicious files from reaching your backend."
            rec_comp = "SOC 2 & HIPAA Compliant"
            is_existing = False
            
        # Default Scenario: Covered by existing AAP Contract (Needs PS tuning)
        else:
            rec_title = "Adaptive Security Engine Optimization (Already on Contract)"
            rec_desc = "Based on your description, your existing AAP Adaptive Security Engine (ASE) has the capability to mitigate this risk. We recommend engaging Akamai Professional Services to review your active ruleset and fine-tune ASE into automatic mode to maximize your current investment."
            rec_comp = "ISO 27001 Security Standard"
            is_existing = True
            
        return {"track": "Track 3", "custom_insight": {"title": rec_title, "desc": rec_desc, "comp": rec_comp, "is_existing": is_existing}}


# ==========================================
# 4. MAIN UI LAYOUT
# ==========================================
st.markdown("<h2 style='margin-top:-10px; margin-bottom: 12px; font-weight: 800; color:#1E2228;'>Akamai EI - EdgeIntelligence Marketplace</h2>", unsafe_allow_html=True)

# Compact LA Banner
banner_html = (
    "<div style='background-color: #E6F4EA; border-left: 4px solid #137333; padding: 10px 16px; margin-bottom: 20px; border-radius: 4px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 1px 2px rgba(0,0,0,0.05);'>"
    "<span style='font-size: 13px; color: #137333; font-weight: 700;'>✨ New Solutions Available:</span>"
    "<span style='font-size: 13px; color: #2B313A; margin-left: 12px; flex-grow: 1;'>Explore our latest AI-era defenses including <b>Brand Guardian</b>, <b>AI Brand Presence</b>, and <b>Guardicore Segmentation</b>.</span>"
    "<a href='#' style='font-size: 13px; font-weight: 700; color: #137333; text-decoration: none; white-space: nowrap;'>View Catalog →</a>"
    "</div>"
)
st.markdown(banner_html, unsafe_allow_html=True)

# Adjusting column ratios to give the right side much more breathing room
col1, col2 = st.columns([0.8, 2.5], gap="large")

# --- LEFT PANE ---
with col1:
    st.markdown('<div class="akamai-card" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<div class="akamai-card-title">1. Analysis Approach</div>', unsafe_allow_html=True)
    
    st.markdown("<p style='font-size: 13px; color: #475569; margin-bottom: 12px; font-weight: 600;'>Select how you want us to evaluate your needs:</p>", unsafe_allow_html=True)
    track_choice = st.radio("Privacy Track", [
        "Scan My Configurations (Deep Analysis)", 
        "Use Industry Benchmarks (No Scan Required)",
        "Describe a Specific Challenge (Custom Input)"
    ], label_visibility="collapsed")
    
    st.markdown("<hr style='margin: 16px 0; border: none; border-top: 1px solid #E2E8F0;'>", unsafe_allow_html=True)

    del_env, sec_env, industry_input, region_input, issue_input = None, None, None, None, ""

    if track_choice == "Scan My Configurations (Deep Analysis)":
        track_internal = "Track 1"
        header_str = "Config Scan"
        st.markdown("<p style='font-size: 13px; color: #0072CE; font-weight: 500; margin-bottom: 10px;'>Select active AAP configs for deep analysis.</p>", unsafe_allow_html=True)
        del_env = st.selectbox("Delivery Config:", DELIVERY_CATALOG)
        st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
        sec_env = st.selectbox("Security Config:", SECURITY_CATALOG)
    elif track_choice == "Use Industry Benchmarks (No Scan Required)":
        track_internal = "Track 2"
        header_str = "Industry Benchmark"
        st.markdown("<p style='font-size: 13px; color: #0072CE; font-weight: 500; margin-bottom: 10px;'>Deep scanning disabled. Using macro-telemetry.</p>", unsafe_allow_html=True)
        industry_input = st.selectbox("Industry Sector:", ["Financial Services", "Retail & E-Commerce", "Media & Entertainment", "Public Sector"])
        st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
        region_input = st.selectbox("Primary Region:", ["North America", "EMEA", "Asia Pacific", "LATAM"])
    else:
        track_internal = "Track 3"
        header_str = "Custom Context"
        st.markdown("<p style='font-size: 13px; color: #0072CE; font-weight: 500; margin-bottom: 10px;'>Describe your specific business context or challenge below.</p>", unsafe_allow_html=True)
        issue_input = st.text_area("Business Context:", placeholder="e.g., We need to stop automated credential stuffing...", height=120, label_visibility="collapsed")
    
    st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)
    run_scan = st.button("Analyze Requirements", type="primary", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- RIGHT PANE ---
with col2:
    if run_scan:
        result = analyze_infrastructure(track_internal, del_env, sec_env, industry_input, region_input, issue_input)
        
        st.markdown('<div class="akamai-card" style="background-color: #FAFAFA; padding: 24px;">', unsafe_allow_html=True)
        
        # ----------------------------------------
        # UI RENDER FOR TRACK 1 (Config Scan)
        # ----------------------------------------
        if result["track"] == "Track 1":
            st.markdown(f'<div class="akamai-card-title" style="margin-bottom: 16px;">Configuration Gap Analysis ({header_str})</div>', unsafe_allow_html=True)
            
            p_cols = st.columns(3, gap="medium")
            for idx, (pillar_name, data) in enumerate(result["pillars"].items()):
                with p_cols[idx]:
                    free_items_html = "".join([f"<li>{item}</li>" for item in data['free_unused']])
                    card_html = (
                        f"<div class='pillar-card' style='border-top: 4px solid {data['color']};'>"
                        f"<div class='pillar-header'><span>{data['icon']} {pillar_name}</span></div>"
                        
                        f"<div class='section-label' style='color:#0072CE;'>✅ Available on Contract</div>"
                        f"<div class='info-box free'>"
                        f"<div style='flex-grow: 1;'>"
                        f"<div class='tag-container'>"
                        f"<span class='tag-badge tag-compliance'>🔒 {data['free_compliance']}</span>"
                        f"</div>"
                        f"<div class='info-issue'>{data['free_issue']}</div>"
                        f"<div class='info-desc'><b>Enhancement:</b> {data['free_enh']}</div>"
                        f"<ul class='free-list'>{free_items_html}</ul>"
                        f"</div>"
                        f"<button class='mini-enable-btn' title='View documentation on how to enable these contracted features.'>Learn How to Enable</button>"
                        f"</div>"
                        
                        f"<div class='section-label' style='color:#D93025; margin-top: 4px;'>🚀 Recommended Add-on</div>"
                        f"<div class='info-box addon'>"
                        f"<div style='flex-grow: 1;'>"
                        f"<div class='tag-container'>"
                        f"<span class='tag-badge tag-compliance'>🔒 {data['addon_compliance']}</span>"
                        f"</div>"
                        f"<div class='info-title'>{data['addon_name']}</div>"
                        f"<div class='info-issue' style='color:#D93025;'>Issue: {data['addon_issue']}</div>"
                        f"<div class='info-desc'>{data['addon_desc']}</div>"
                        f"</div>"
                        f"<button class='mini-buy-btn' title='Try: Adds a $0 line item for 30-60 days. Buy: Routes to your sales rep.'>Try / Buy Add-on</button>"
                        f"</div>"
                        f"</div>"
                    )
                    st.markdown(card_html, unsafe_allow_html=True)

        # ----------------------------------------
        # UI RENDER FOR TRACK 2 (Industry Dashboard)
        # ----------------------------------------
        elif result["track"] == "Track 2":
            ind_data = result["industry_data"]
            st.markdown(f'<div class="akamai-card-title" style="margin-bottom: 16px;">Industry Threat Landscape ({industry_input} - {region_input})</div>', unsafe_allow_html=True)
            
            # Top Metrics Row
            m_cols = st.columns(3, gap="medium")
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
            <div style='background-color: #FFFFFF; border: 1px solid #E2E8F0; padding: 20px; border-radius: 8px; margin-top: 16px; margin-bottom: 24px; box-shadow: 0 1px 3px rgba(0,0,0,0.02);'>
                <div style='font-size: 13px; color: #1E2228; font-weight: 600; line-height: 1.5;'>{ind_data["fact"]}</div>
                <div class='visual-bar-container'>{v_bars}</div>
                <div class='visual-legend'>{v_legend}</div>
            </div>
            <div class="akamai-card-title" style="margin-bottom: 12px; font-size: 16px;">Strategic Solution Recommendations</div>
            """, unsafe_allow_html=True)
            
            # Bottom Recommendations Row
            r_cols = st.columns(len(ind_data["recs"]), gap="medium")
            for i, rec in enumerate(ind_data["recs"]):
                with r_cols[i]:
                    st.markdown(f"""
                    <div class='rec-card' style='display: flex; flex-direction: column; padding-bottom: 12px; min-height: 130px;'>
                        <div style='flex-grow: 1;'>
                            <div class='tag-container'>
                                <span class='tag-badge tag-compliance'>🔒 {rec['compliance']}</span>
                            </div>
                            <h4 style='font-size: 14px; margin-bottom: 6px;'>{rec['icon']} {rec['title']}</h4>
                            <p style='font-size: 12px;'>{rec['desc']}</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
            # UNIFIED ACTION ROW FOR ALL TRACK 2 RECOMMENDATIONS
            st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
            b_spacer1, b_btn1, b_btn2, b_spacer2 = st.columns([1, 1.5, 1.5, 1])
            with b_btn1:
                st.button("Try / Buy Solutions", type="primary", use_container_width=True, key="t2_buy")
            with b_btn2:
                # Custom secondary button styling via markdown for alignment
                st.markdown("""
                <style>.btn-outline { width: 100%; text-align: center; display: inline-block; padding: 6px 16px; font-weight: 600; font-size: 13px; border: 1px solid #0072CE; color: #0072CE; border-radius: 4px; background-color: #FFFFFF; text-decoration: none; transition: 0.2s ease; cursor: pointer;}</style>
                <button class="btn-outline">Ask IAT for Assistance</button>
                """, unsafe_allow_html=True)
            
        # ----------------------------------------
        # UI RENDER FOR TRACK 3 (Custom Context)
        # ----------------------------------------
        else:
            custom_insight = result["custom_insight"]
            st.markdown(f'<div class="akamai-card-title" style="margin-bottom: 16px;">🎯 Tailored Solution Architecture</div>', unsafe_allow_html=True)
            
            # Dynamic styling based on whether product is existing (Needs PS) or new (Needs Upsell)
            if custom_insight.get("is_existing"):
                primary_btn = "Engage Akamai PS"
                secondary_btn = "View Documentation"
                tag_color = "#10B981" # Green for Existing/Optimization
            else:
                primary_btn = "Try / Buy Solution"
                secondary_btn = "Contact Sales Rep"
                tag_color = "#0072CE" # Blue for New Upsell
            
            insight_html = (
                f"<div style='background-color: #FFFFFF; border: 1px solid #E2E8F0; padding: 24px; border-radius: 8px; border-top: 4px solid {tag_color}; box-shadow: 0 1px 3px rgba(0,0,0,0.04);'>"
                "<div class='tag-container' style='margin-bottom: 12px;'>"
                f"<span class='tag-badge tag-compliance' style='font-size:12px; padding: 6px 10px;'>🔒 {custom_insight['comp']}</span>"
                "</div>"
                f"<h4 style='margin: 0 0 12px 0; color: #1E2228; font-size: 18px;'>Recommended Fit: <span style='color:{tag_color};'>{custom_insight['title']}</span></h4>"
                f"<p style='margin: 0 0 20px 0; font-size: 14px; color: #475569; line-height: 1.6;'>{custom_insight['desc']}</p>"
                "<div style='display: flex; gap: 16px;'>"
                f"<button style='background-color: {tag_color}; color: white; border: none; border-radius: 4px; padding: 10px 20px; font-weight: 600; font-size: 13px; cursor: pointer; transition: 0.2s ease;'>{primary_btn}</button>"
                f"<button style='background-color: white; color: {tag_color}; border: 1px solid {tag_color}; border-radius: 4px; padding: 10px 20px; font-weight: 600; font-size: 13px; cursor: pointer; transition: 0.2s ease;'>{secondary_btn}</button>"
                "</div>"
                "</div>"
            )
            st.markdown(insight_html, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)
            
    else:
        empty_state_html = (
            "<div class='akamai-card' style='height: 100%; display: flex; align-items: center; justify-content: center; background-color: #FAFAFA; min-height: 400px;'>"
            "<div style='text-align: center; padding: 60px 20px; max-width: 400px;'>"
            "<h4 style='color: #1E2228; margin-bottom: 12px; font-size: 18px;'>Awaiting Analysis Parameters</h4>"
            "<p style='font-size: 13px; color: #64748B; line-height: 1.6;'>Select your evaluation method on the left and run the scan to identify unused contract features, view industry benchmarks, or receive custom solutions.</p>"
            "</div>"
            "</div>"
        )
        st.markdown(empty_state_html, unsafe_allow_html=True)
