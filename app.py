import streamlit as st

# ==========================================
# ⚙️ 1. PAGE SETUP & COMPACT ENTERPRISE STYLING
# ==========================================
st.set_page_config(page_title="Akamai Marketplace | Control Center", layout="wide", initial_sidebar_state="expanded")

AKAMAI_CSS = """
<style>
    /* 1. Precise Padding & Fluid Container */
    .block-container { padding: 3rem 2rem 1rem 2rem !important; max-width: 100% !important; }
    header { display: none !important; }
    
    .stApp { background-color: #F4F6F9; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
    
    /* 2. Topbar (Fixed margins to prevent squeezing) */
    .akamai-topbar {
        background-color: #1E2228; color: #FFFFFF; padding: 12px 24px; 
        margin-top: -3rem; margin-left: -2rem; margin-right: -2rem; margin-bottom: 20px;
        display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #2B313A;
    }
    .akamai-brand { font-weight: 800; font-size: 18px; letter-spacing: 0.5px; color: #0072CE; white-space: nowrap; }
    .akamai-search-box { background-color: #2B313A; border: 1px solid #3A424D; border-radius: 4px; padding: 6px 16px; color: #C0C7D0; width: 30vw; min-width: 250px; max-width: 400px; font-size: 12px; }
    .akamai-top-right { display: flex; align-items: center; gap: 20px; font-size: 12px; color: #E2E8F0; white-space: nowrap; }
    
    .icon-container { position: relative; display: flex; align-items: center; justify-content: center; cursor: pointer; }
    .notification-badge { 
        position: absolute; top: -5px; right: -6px; background-color: #D93025; color: white; 
        font-size: 8px; font-weight: 700; padding: 2px 4px; border-radius: 10px; border: 2px solid #1E2228;
    }
    
    /* 3. Base Cards */
    .akamai-card { background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 4px; padding: 16px 20px; margin-bottom: 15px; box-shadow: 0 1px 3px rgba(0,0,0,0.03); }
    .akamai-card-title { font-size: 16px; font-weight: 700; color: #1E2228; margin-bottom: 12px; }
    
    /* 4. Three-Pillar Status Cards (Fixed Heights) */
    .pillar-card { background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 6px; padding: 16px; height: 100%; min-height: 480px; display: flex; flex-direction: column; }
    .pillar-header { font-size: 14px; font-weight: 700; color: #1E2228; text-transform: uppercase; border-bottom: 2px solid #E2E8F0; padding-bottom: 8px; margin-bottom: 12px; }
    
    .section-label { font-size: 11px; font-weight: 800; color: #0072CE; text-transform: uppercase; margin-bottom: 6px; letter-spacing: 0.5px; }
    
    /* Info Boxes inside Cards */
    .info-box { border-radius: 4px; padding: 10px; margin-bottom: 12px; border: 1px solid transparent; flex-grow: 1; }
    .info-box.free { background-color: #F0FDF4; border-color: #BBF7D0; }
    .info-box.addon { background-color: #F8FAFC; border-color: #E2E8F0; }
    
    .info-title { font-size: 13px; font-weight: 700; color: #1E2228; margin-bottom: 4px; }
    .info-issue { font-size: 11px; font-weight: 600; margin-bottom: 4px; }
    .info-issue.free-text { color: #166534; }
    .info-issue.addon-text { color: #D93025; }
    .info-desc { font-size: 11px; line-height: 1.4; margin-bottom: 8px; }
    .info-desc.free-text { color: #15803D; }
    .info-desc.addon-text { color: #475569; }

    .free-list { margin: 0; padding-left: 18px; font-size: 11px; color: #166534; font-weight: 600; }
    .free-list li { margin-bottom: 3px; }
    
    /* 5. Bundled Product Box */
    .bundle-box { background-color: #F0F7FF; border: 1px solid #CCE3FD; border-radius: 4px; padding: 12px 16px; margin-top: 5px; display: flex; align-items: center; justify-content: space-between; }
    .bundle-text h4 { margin: 0 0 4px 0; color: #0072CE; font-size: 14px; }
    .bundle-text p { margin: 0; font-size: 12px; color: #2B313A; }

    /* 6. Context Insight Box */
    .context-box { background-color: #F4F6F8; border-left: 4px solid #10B981; padding: 12px 16px; margin-top: 15px; border-radius: 4px; }
    .context-box h4 { margin: 0 0 4px 0; color: #10B981; font-size: 13px; }
    .context-box p { margin: 0; font-size: 12px; color: #2B313A; }

    /* Streamlit overrides for tighter buttons */
    .stButton > button { font-size: 12px !important; padding: 6px 12px !important; min-height: 0 !important; font-weight: 600 !important; border-radius: 4px !important; width: 100% !important;}
    .btn-primary > button { background-color: #0072CE !important; color: white !important; border: none !important; }
    .btn-secondary > button { background-color: white !important; color: #0072CE !important; border: 1px solid #0072CE !important; }
    
    div[data-testid="stVerticalBlock"] > div { padding-bottom: 0.1rem !important; }
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
    "<div style='text-align: right; margin-left: 10px;'><strong>Nikhil Goyal</strong><br><span style='font-size: 10px; color: #9DA7B3;'>AKAMAI TECHNOLOGIES - ASSETS ⌄</span></div>"
    "</div>"
    "</div>"
)
st.markdown(topbar_html, unsafe_allow_html=True)

# ==========================================
# 2. MOCK CATALOG DATA
# ==========================================
DELIVERY_CATALOG = [
    "api.retailstore.com (E-Commerce API)",
    "www.globalbank.com (Main Site)",
    "media.streaming.net (Video Assets)"
]

SECURITY_CATALOG = [
    "WAF Enabled (No Bot Protection)",
    "Standard Security Base (Legacy)",
    "No Security Configured (Empty)"
]

# ==========================================
# 3. DIAGNOSTIC ENGINE LOGIC
# ==========================================
def analyze_infrastructure(track, del_env, sec_env, industry, region, context):
    """Simulates a background scan identifying used vs unused modules based on Track."""
    
    # Text changes dynamically if Track 2 is selected (no config scan)
    if track == "Track 1":
        sec_issue = "Config Scan: Basic rate limits are inactive on your selected policy, leaving endpoints exposed."
        rel_issue = "Config Scan: No active health checks configured for the primary origin in your property."
        perf_issue = "Config Scan: Static assets in your delivery property lack edge compression."
    else:
        sec_issue = f"Industry Benchmark: 72% of {industry} in {region} face Layer-7 exposure without rate limits."
        rel_issue = f"Industry Benchmark: Failover latency for {industry} requires advanced health checks."
        perf_issue = f"Industry Benchmark: {region} mobile users experience high LCP without edge compression."

    pillars = {
        "Security": {
            "icon": "🛡️", "color": "#0072CE",
            "free_issue": sec_issue,
            "free_enh": "Enabling these contracted modules instantly sheds junk traffic and reduces unnecessary origin compute costs.",
            "free_unused": ["Rate Controls", "Slow POST Protection", "IP Geo-Blocking"],
            "addon_name": "Bot Manager Premier",
            "addon_issue": "High volume of automated credential stuffing detected bypassing standard WAF.",
            "addon_desc": "Upgrading adds behavioral anomaly detection to intercept sophisticated scrapers and botnets."
        },
        "Reliability": {
            "icon": "⚙️", "color": "#10B981",
            "free_issue": rel_issue,
            "free_enh": "Activating these modules prevents dropped connections by gracefully handling timeout spikes.",
            "free_unused": ["Origin Health Checks", "Advanced Retry Logic", "Stale-While-Revalidate"],
            "addon_name": "Global Traffic Management (GTM)",
            "addon_issue": "Single point of failure identified at primary origin data center.",
            "addon_desc": "GTM provides DNS-level load balancing to automatically failover traffic during regional outages."
        },
        "Performance": {
            "icon": "🚀", "color": "#F59E0B",
            "free_issue": perf_issue,
            "free_enh": "Enabling these configurations will actively bypass internet congestion and reduce overall delivery time.",
            "free_unused": ["Brotli Compression", "SureRoute Advanced", "Predictive Prefetching"],
            "addon_name": "Image & Video Manager (IVM)",
            "addon_issue": "Heavy unoptimized visual payloads are severely impacting Core Web Vitals (LCP).",
            "addon_desc": "IVM automatically converts and scales media to next-gen formats (WebP/AVIF) at the edge."
        }
    }

    bundle = {
        "name": "Akamai App & API Protector Advanced (AAP)",
        "desc": "Consolidate your security posture. This bundle upgrades your legacy WAF, includes Bot Manager natively, and activates premium API discovery tools in a single contract."
    }

    context_insight = None
    if context.strip():
        c_lower = context.lower()
        if any(k in c_lower for k in ["segment", "lateral", "internal", "ransomware", "hybrid"]):
            context_insight = ("Guardicore Microsegmentation", "Based on your context regarding internal hybrid protection, Guardicore will map asset exposure and enforce Zero-Trust containment to prevent lateral threat movement without network changes.")
        elif any(k in c_lower for k in ["api", "data breach", "shadow"]):
            context_insight = ("API Security", "To address your API concerns, Akamai API Security will continuously discover shadow APIs and analyze behavior to protect them throughout their lifecycle.")
        elif any(k in c_lower for k in ["compute", "latency", "logic", "custom"]):
            context_insight = ("Akamai EdgeWorkers", "To resolve origin latency, EdgeWorkers allows you to offload your custom routing and validation logic directly to the edge proxy.")
        else:
            context_insight = ("Architect AI Recommendation", "Based on your specific use case, our AI recommends reviewing your caching hierarchies and enabling Zero-Trust application access to secure your evolving architecture.")

    return pillars, bundle, context_insight


# ==========================================
# 4. MAIN UI LAYOUT
# ==========================================
st.markdown("<h2 style='margin-top:-20px; margin-bottom: 10px; color:#1E2228;'>Akamai EI - EdgeIntelligence Marketplace</h2>", unsafe_allow_html=True)

# Compact LA Banner
banner_html = (
    "<div style='background-color: #E6F4EA; border-left: 3px solid #137333; padding: 8px 12px; margin-bottom: 15px; border-radius: 4px; display: flex; justify-content: space-between; align-items: center;'>"
    "<span style='font-size: 12px; color: #137333; font-weight: 600;'>✨ New Solutions Available:</span>"
    "<span style='font-size: 12px; color: #2B313A; margin-left: 10px; flex-grow: 1;'>Explore our latest AI-era defenses including <b>Brand Guardian</b>, <b>AI Brand Presence</b>, and <b>Guardicore Segmentation</b>.</span>"
    "<a href='#' style='font-size: 12px; font-weight: 600; color: #137333; text-decoration: none; white-space: nowrap;'>View Catalog →</a>"
    "</div>"
)
st.markdown(banner_html, unsafe_allow_html=True)

col1, col2 = st.columns([1, 2.2], gap="medium")

# --- LEFT PANE: SCOPE & INPUT ---
with col1:
    st.markdown('<div class="akamai-card" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<div class="akamai-card-title">1. Target Infrastructure</div>', unsafe_allow_html=True)
    
    st.markdown("<p style='font-size: 12px; color: #475569; margin-bottom: 10px; font-weight: 600;'>Select Privacy & Analysis Track:</p>", unsafe_allow_html=True)
    
    # 🔥 RE-ADDED THE DUAL TRACK RADIO BUTTON
    track_choice = st.radio("Privacy Track", [
        "Track 1: Deep-Insight Mode (Config Scan)", 
        "Track 2: Contextual-Match Mode (Industry Benchmark)"
    ], label_visibility="collapsed")
    
    st.markdown("<hr style='margin: 10px 0; border: none; border-top: 1px solid #E2E8F0;'>", unsafe_allow_html=True)

    del_env = None
    sec_env = None
    industry_input = None
    region_input = None

    if "Track 1" in track_choice:
        st.markdown("<p style='font-size: 12px; color: #0072CE; margin-bottom: 10px;'>Select active configurations from your catalog for deep analysis.</p>", unsafe_allow_html=True)
        del_env = st.selectbox("Delivery Property:", DELIVERY_CATALOG)
        sec_env = st.selectbox("Security Policy (AppSec):", SECURITY_CATALOG)
    else:
        st.markdown("<p style='font-size: 12px; color: #0072CE; margin-bottom: 10px;'>Deep scanning disabled. Analysis will use macro-industry telemetry.</p>", unsafe_allow_html=True)
        industry_input = st.selectbox("Industry Sector:", ["Financial Services", "Retail & E-Commerce", "Media & Entertainment", "Public Sector"])
        region_input = st.selectbox("Primary Region:", ["North America", "EMEA", "Asia Pacific", "LATAM"])
    
    st.markdown('<div class="akamai-card-title" style="margin-top:20px;">2. Business Context <span style="font-size:12px; color:#64748B; font-weight:normal;">(Optional)</span></div>', unsafe_allow_html=True)
    issue_input = st.text_area("Describe specific issues or use cases:", placeholder="e.g., We need to stop automated credential stuffing on our login endpoints...", height=80, label_visibility="collapsed")
    
    st.markdown("<br>", unsafe_allow_html=True)
    run_scan = st.button("Analyze Infrastructure", type="primary", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- RIGHT PANE: DIAGNOSTICS & STATUS CARDS ---
with col2:
    if run_scan:
        track_str = "Track 1" if "Track 1" in track_choice else "Track 2"
        pillars, bundle, context_insight = analyze_infrastructure(track_str, del_env, sec_env, industry_input, region_input, issue_input)
        
        st.markdown('<div class="akamai-card" style="background-color: #FAFAFA;">', unsafe_allow_html=True)
        st.markdown(f'<div class="akamai-card-title">Infrastructure Gap Analysis ({track_str})</div>', unsafe_allow_html=True)
        
        # 1. THREE-PILLAR STATUS CARDS
        p_cols = st.columns(3)
        for idx, (pillar_name, data) in enumerate(pillars.items()):
            with p_cols[idx]:
                free_items_html = "".join([f"<li>{item}</li>" for item in data['free_unused']])
                
                # Construct entire card as one flat string
                card_html = (
                    f"<div class='pillar-card' style='border-top: 4px solid {data['color']};'>"
                    f"<div class='pillar-header'>{data['icon']} {pillar_name}</div>"
                    
                    # Contracted / Free Section
                    f"<div class='section-label' style='color:#166534;'>✅ Contracted (Enable for Free)</div>"
                    f"<div class='info-box free'>"
                    f"<div class='info-issue free-text'>Result: {data['free_issue']}</div>"
                    f"<div class='info-desc free-text'>Enhancement: {data['free_enh']}</div>"
                    f"<ul class='free-list'>{free_items_html}</ul>"
                    f"</div>"
                    
                    # Recommended Add-on Section
                    f"<div class='section-label' style='color:#D93025; margin-top: 5px;'>🚀 Recommended Add-on</div>"
                    f"<div class='info-box addon'>"
                    f"<div class='info-title'>{data['addon_name']}</div>"
                    f"<div class='info-issue addon-text'>Issue: {data['addon_issue']}</div>"
                    f"<div class='info-desc addon-text'>{data['addon_desc']}</div>"
                    f"</div>"
                    
                    f"</div>"
                )
                st.markdown(card_html, unsafe_allow_html=True)
                
        # 2. SINGLE ROW OF ACTION BUTTONS
        st.markdown("<br>", unsafe_allow_html=True)
        btn_col1, btn_col2, btn_col3 = st.columns([1.5, 1.5, 2.5])
        with btn_col1:
            st.markdown('<div class="btn-primary">', unsafe_allow_html=True)
            st.button("1-Click Try/Buy", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        with btn_col2:
            st.markdown('<div class="btn-secondary">', unsafe_allow_html=True)
            st.button("Ask IAT", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # 3. BUNDLED UPGRADE RECOMMENDATION
        bundle_html = (
            "<div class='bundle-box'>"
            "<div class='bundle-text'>"
            f"<h4>📦 Recommended Architecture Upgrade: {bundle['name']}</h4>"
            f"<p>{bundle['desc']}</p>"
            "</div>"
            "<div>"
            "<button style='background-color: #0072CE; color: white; border: none; border-radius: 4px; padding: 6px 12px; font-weight: 600; font-size: 12px; cursor: pointer; white-space: nowrap;'>Upgrade Contract</button>"
            "</div>"
            "</div>"
        )
        st.markdown(bundle_html, unsafe_allow_html=True)

        # 4. OPTIONAL BUSINESS CONTEXT INSIGHT
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
            "<p style='font-size: 13px; color: #64748B;'>Select your tracking mode on the left and run the scan to identify unused contract features and recommended add-ons.</p>"
            "</div>"
            "</div>"
        )
        st.markdown(empty_state_html, unsafe_allow_html=True)
