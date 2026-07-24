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
    
    /* 4. Three-Pillar Status Cards (Removed min-height to hug content tightly) */
    .pillar-card { background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 6px; padding: 12px; display: flex; flex-direction: column; height: 100%; }
    .pillar-header { font-size: 13px; font-weight: 700; color: #1E2228; text-transform: uppercase; border-bottom: 2px solid #E2E8F0; padding-bottom: 6px; margin-bottom: 8px; }
    
    .section-label { font-size: 10px; font-weight: 800; color: #0072CE; text-transform: uppercase; margin-bottom: 4px; letter-spacing: 0.5px; }
    
    /* Info Boxes inside Cards (Tighter padding) */
    .info-box { border-radius: 4px; padding: 8px; margin-bottom: 8px; border: 1px solid transparent; flex-grow: 1; }
    .info-box.free { background-color: #F0FDF4; border-color: #BBF7D0; }
    .info-box.addon { background-color: #F8FAFC; border-color: #E2E8F0; }
    
    .info-title { font-size: 12px; font-weight: 700; color: #1E2228; margin-bottom: 3px; }
    .info-issue { font-size: 10.5px; font-weight: 600; margin-bottom: 3px; line-height: 1.3;}
    .info-issue.free-text { color: #166534; }
    .info-issue.addon-text { color: #D93025; }
    .info-desc { font-size: 10.5px; line-height: 1.3; margin-bottom: 6px; }
    .info-desc.free-text { color: #15803D; }
    .info-desc.addon-text { color: #475569; }

    .free-list { margin: 0; padding-left: 16px; font-size: 10.5px; color: #166534; font-weight: 600; }
    .free-list li { margin-bottom: 2px; }
    
    /* 5. Bundled Product Box (Tighter) */
    .bundle-box { background-color: #F0F7FF; border: 1px solid #CCE3FD; border-radius: 4px; padding: 8px 12px; margin-bottom: 5px; display: flex; align-items: center; justify-content: space-between; }
    .bundle-text h4 { margin: 0 0 2px 0; color: #0072CE; font-size: 13px; }
    .bundle-text p { margin: 0; font-size: 11px; color: #2B313A; }

    /* 6. Context Insight Box (Tighter) */
    .context-box { background-color: #F4F6F8; border-left: 4px solid #10B981; padding: 8px 12px; margin-bottom: 5px; border-radius: 4px; }
    .context-box h4 { margin: 0 0 2px 0; color: #10B981; font-size: 12px; }
    .context-box p { margin: 0; font-size: 11px; color: #2B313A; }

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
# 3. AAP-SPECIFIC DIAGNOSTIC ENGINE LOGIC
# ==========================================
def analyze_infrastructure(track, del_env, sec_env, industry, region, context):
    if track == "Track 1":
        sec_issue = "Config Scan: Essential Adaptive Rate Controls and Bot Visibility are inactive on this policy."
        rel_issue = "Config Scan: No Site Failover or Site Shield origin cloaking configured for the primary backend."
        perf_issue = "Config Scan: Edge caching and SureRoute optimizations are severely underutilized."
    else:
        sec_issue = f"Industry Benchmark: 72% of {industry} in {region} suffer without Adaptive Rate Controls and Bot Visibility."
        rel_issue = f"Industry Benchmark: Failover latency for {industry} requires advanced Site Failover topologies."
        perf_issue = f"Industry Benchmark: {region} users experience high latency without SureRoute and optimal caching."

    pillars = {
        "Security": {
            "icon": "🛡️", "color": "#0072CE",
            "free_issue": sec_issue,
            "free_enh": "Enabling these contracted AAP features will instantly map bot traffic and mitigate volumetric spikes.",
            "free_unused": ["Adaptive Rate Controls", "Bot Visibility and Mitigation", "IP Deny"],
            "addon_name": "Malware Protection (Add-on)",
            "addon_issue": "Vulnerability to malicious file uploads detected at the edge.",
            "addon_desc": "Malware Protection seamlessly integrates with AAP to intercept and block malicious files from reaching your backend."
        },
        "Reliability": {
            "icon": "⚙️", "color": "#10B981",
            "free_issue": rel_issue,
            "free_enh": "Activating these AAP modules cloaks your origin from direct internet attacks and gracefully handles timeout spikes.",
            "free_unused": ["Site Failover", "SureRoute for Failover", "Site Shield"],
            "addon_name": "DataStream (Add-on)",
            "addon_issue": "Lack of real-time operational visibility into Edge events during critical outages.",
            "addon_desc": "DataStream provides near real-time log delivery to your SIEM/analytics endpoints for rapid reliability incident response."
        },
        "Performance": {
            "icon": "🚀", "color": "#F59E0B",
            "free_issue": perf_issue,
            "free_enh": "Applying these included features actively bypasses internet congestion and maximizes origin offload.",
            "free_unused": ["Caching", "SureRoute for Performance", "TCP Optimization"],
            "addon_name": "API Acceleration (Add-on)",
            "addon_issue": "Heavy dynamic API payloads are experiencing severe delivery latency.",
            "addon_desc": "API Acceleration specifically optimizes routing and delivery for non-cacheable, heavy API traffic."
        }
    }

    bundle = {
        "name": "AAP Ultimate Extension Bundle",
        "desc": "Maximize your App & API Protector deployment. This bundle unlocks API Acceleration, DataStream visibility, and Malware Protection in a single unified contract extension."
    }

    context_insight = None
    if context.strip():
        c_lower = context.lower()
        if any(k in c_lower for k in ["file", "upload", "malware", "virus"]):
            context_insight = ("Malware Protection Add-on", "Based on your context regarding file uploads, Malware Protection will scan all inbound user-generated content at the edge before it reaches your servers.")
        elif any(k in c_lower for k in ["api", "data breach", "shadow"]):
            context_insight = ("API Protections - Basic", "To address your API concerns, ensure the 'API Protections - Basic' module (included in your current AAP contract) is fully configured for endpoint enforcement.")
        elif any(k in c_lower for k in ["bot", "scraper", "credential"]):
            context_insight = ("Bot Visibility and Mitigation", "Your current AAP contract includes 'Bot Visibility'. Enabling this will immediately provide actionable intelligence on the credential stuffing you are facing.")
        else:
            context_insight = ("Architect AI Recommendation", "Based on your specific use case, our AI recommends reviewing your active AAP ruleset and ensuring Adaptive Security Engine (ASE) is in automatic mode.")

    return pillars, bundle, context_insight

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
    st.markdown('<div class="akamai-card-title">1. Target Infrastructure</div>', unsafe_allow_html=True)
    
    st.markdown("<p style='font-size: 11px; color: #475569; margin-bottom: 6px; font-weight: 600;'>Select Privacy & Analysis Track:</p>", unsafe_allow_html=True)
    track_choice = st.radio("Privacy Track", ["Track 1: Deep-Insight Mode (Config Scan)", "Track 2: Contextual-Match Mode (Industry Benchmark)"], label_visibility="collapsed")
    
    st.markdown("<hr style='margin: 8px 0; border: none; border-top: 1px solid #E2E8F0;'>", unsafe_allow_html=True)

    del_env, sec_env, industry_input, region_input = None, None, None, None

    if "Track 1" in track_choice:
        st.markdown("<p style='font-size: 11.5px; color: #0072CE; margin-bottom: 6px;'>Select active AAP configs for deep analysis.</p>", unsafe_allow_html=True)
        del_env = st.selectbox("Delivery Property:", DELIVERY_CATALOG)
        sec_env = st.selectbox("Security Policy (AppSec):", SECURITY_CATALOG)
    else:
        st.markdown("<p style='font-size: 11.5px; color: #0072CE; margin-bottom: 6px;'>Deep scanning disabled. Using macro-telemetry.</p>", unsafe_allow_html=True)
        industry_input = st.selectbox("Industry Sector:", ["Financial Services", "Retail & E-Commerce", "Media & Entertainment", "Public Sector"])
        region_input = st.selectbox("Primary Region:", ["North America", "EMEA", "Asia Pacific", "LATAM"])
    
    st.markdown('<div class="akamai-card-title" style="margin-top:12px; margin-bottom: 6px;">2. Business Context <span style="font-size:11px; color:#64748B; font-weight:normal;">(Optional)</span></div>', unsafe_allow_html=True)
    issue_input = st.text_area("Describe specific issues:", placeholder="e.g., We need to stop automated credential stuffing...", height=65, label_visibility="collapsed")
    
    run_scan = st.button("Analyze Infrastructure", type="primary", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- RIGHT PANE ---
with col2:
    if run_scan:
        track_str = "Track 1" if "Track 1" in track_choice else "Track 2"
        pillars, bundle, context_insight = analyze_infrastructure(track_str, del_env, sec_env, industry_input, region_input, issue_input)
        
        st.markdown('<div class="akamai-card" style="background-color: #FAFAFA; padding: 12px 16px;">', unsafe_allow_html=True)
        st.markdown(f'<div class="akamai-card-title" style="margin-bottom: 8px;">Infrastructure Gap Analysis ({track_str})</div>', unsafe_allow_html=True)
        
        # 1. THREE-PILLAR CARDS
        p_cols = st.columns(3)
        for idx, (pillar_name, data) in enumerate(pillars.items()):
            with p_cols[idx]:
                free_items_html = "".join([f"<li>{item}</li>" for item in data['free_unused']])
                card_html = (
                    f"<div class='pillar-card' style='border-top: 3px solid {data['color']};'>"
                    f"<div class='pillar-header'>{data['icon']} {pillar_name}</div>"
                    f"<div class='section-label' style='color:#166534;'>✅ Contracted (Enable for Free)</div>"
                    f"<div class='info-box free'>"
                    f"<div class='info-issue free-text'>{data['free_issue']}</div>"
                    f"<div class='info-desc free-text'><b>Enhancement:</b> {data['free_enh']}</div>"
                    f"<ul class='free-list'>{free_items_html}</ul>"
                    f"</div>"
                    f"<div class='section-label' style='color:#D93025; margin-top: 2px;'>🚀 Recommended Add-on</div>"
                    f"<div class='info-box addon'>"
                    f"<div class='info-title'>{data['addon_name']}</div>"
                    f"<div class='info-issue addon-text'>Issue: {data['addon_issue']}</div>"
                    f"<div class='info-desc addon-text'>{data['addon_desc']}</div>"
                    f"</div>"
                    f"</div>"
                )
                st.markdown(card_html, unsafe_allow_html=True)
                
        # 2. ACTION BUTTONS 
        btn_col1, btn_col2, btn_col3 = st.columns([1.5, 1.5, 2.5])
        with btn_col1:
            st.markdown('<div class="btn-primary">', unsafe_allow_html=True)
            st.button("1-Click Try/Buy Recommended Add-ons", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        with btn_col2:
            st.markdown('<div class="btn-secondary">', unsafe_allow_html=True)
            st.button("Ask IAT for Assistance", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # 3. BUNDLE
        bundle_html = (
            "<div class='bundle-box'>"
            "<div class='bundle-text'>"
            f"<h4>📦 Contract Consolidation: {bundle['name']}</h4>"
            f"<p>{bundle['desc']}</p>"
            "</div>"
            "<div>"
            "<button style='background-color: #0072CE; color: white; border: none; border-radius: 4px; padding: 5px 10px; font-weight: 600; font-size: 11px; cursor: pointer; white-space: nowrap;'>Upgrade Contract</button>"
            "</div>"
            "</div>"
        )
        st.markdown(bundle_html, unsafe_allow_html=True)

        # 4. CONTEXT
        if context_insight:
            insight_html = (
                "<div class='context-box'>"
                f"<h4>🧠 Copilot Insight: {context_insight[0]}</h4>"
                f"<p>{context_insight[1]}</p>"
                "</div>"
            )
            st.markdown(insight_html, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)
            
    else:
        empty_state_html = (
            "<div class='akamai-card' style='height: 100%; display: flex; align-items: center; justify-content: center; background-color: #FAFAFA;'>"
            "<div style='text-align: center; padding: 60px 20px;'>"
            "<h4 style='color: #1E2228; margin-bottom: 8px;'>Awaiting Configuration Selection</h4>"
            "<p style='font-size: 12px; color: #64748B;'>Select your tracking mode on the left and run the scan to identify unused contract features and recommended add-ons.</p>"
            "</div>"
            "</div>"
        )
        st.markdown(empty_state_html, unsafe_allow_html=True)
