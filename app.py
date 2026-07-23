import streamlit as st
import json

# ==========================================
# ⚙️ 1. PAGE SETUP & SPACIOUS AKAMAI STYLING
# ==========================================
st.set_page_config(page_title="Akamai Marketplace | Control Center", layout="wide", initial_sidebar_state="expanded")

AKAMAI_CSS = """
<style>
    /* 1. Normal, spacious padding on the main block */
    .block-container { padding-top: 2rem !important; padding-left: 2rem !important; padding-right: 2rem !important; }
    header { display: none !important; }
    
    .stApp { background-color: #F4F6F9; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
    
    /* 2. Topbar with comfortable vertical padding */
    .akamai-topbar {
        background-color: #1E2228; color: #FFFFFF; padding: 12px 24px; 
        margin-top: -60px; margin-left: -60px; margin-right: -60px; margin-bottom: 25px;
        display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #2B313A;
    }
    .akamai-brand { font-weight: 800; font-size: 20px; letter-spacing: 0.5px; color: #0072CE; }
    .akamai-search-box { background-color: #2B313A; border: 1px solid #3A424D; border-radius: 4px; padding: 6px 16px; color: #C0C7D0; width: 380px; font-size: 13px; }
    .akamai-top-right { display: flex; align-items: center; gap: 20px; font-size: 12px; color: #E2E8F0; }
    .create-btn { background-color: #0072CE; color: white; padding: 6px 16px; border-radius: 4px; font-weight: 600; font-size: 13px; }
    
    .icon-container { position: relative; display: flex; align-items: center; justify-content: center; }
    .notification-badge { 
        position: absolute; top: -6px; right: -8px; background-color: #D93025; color: white; 
        font-size: 9px; font-weight: 700; padding: 2px 5px; border-radius: 10px; border: 2px solid #1E2228;
    }
    
    /* 3. Spacious Cards */
    .akamai-card { background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 4px; padding: 24px; margin-bottom: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.03); }
    .akamai-card-title { font-size: 18px; font-weight: 700; color: #1E2228; margin-bottom: 16px; }
    
    .empty-state-box { background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 4px; padding: 60px 20px; text-align: center; margin-top: 10px; }
    .empty-state-title { font-size: 16px; font-weight: 700; color: #2B313A; margin-bottom: 8px; }
    .empty-state-sub { font-size: 13px; color: #64748B; }
    
    .stButton > button { background-color: #0072CE !important; color: #FFFFFF !important; font-weight: 600 !important; border-radius: 4px !important; border: none !important; padding: 8px 18px !important; font-size: 14px !important; }
    
    /* 4. Three-Pillar Azure-Style Status Cards */
    .azure-card {
        background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 6px; padding: 16px; text-align: left;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02); height: 100%;
    }
    .azure-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px; }
    .azure-title { font-size: 14px; font-weight: 700; color: #1E2228; text-transform: uppercase; letter-spacing: 0.5px; }
    .azure-count { font-size: 18px; font-weight: 800; }
    .azure-sub { font-size: 11px; color: #64748B; margin-bottom: 12px; font-weight: 600;}
    .azure-hr { border: none; border-top: 1px solid #E2E8F0; margin: 10px 0; }
    .azure-section { font-size: 12px; color: #2B313A; margin-bottom: 8px; line-height: 1.4; }
    .azure-section b { color: #1E2228; font-weight: 700; display: block; margin-bottom: 2px;}

    .section-header { font-size: 15px; font-weight: 700; color: #1E2228; margin-top: 10px; margin-bottom: 15px; border-bottom: 1px solid #E2E8F0; padding-bottom: 8px;}
    p { font-size: 14px; margin-bottom: 10px; }
</style>
"""
st.markdown(AKAMAI_CSS, unsafe_allow_html=True)

# SVG Icons (Pure White)
SVG_HELP = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>'
SVG_CART = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg>'
SVG_BELL = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg>'
SVG_ALERT = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>'

st.markdown(f"""
<div class="akamai-topbar">
    <div class="akamai-brand">akamai</div>
    <div class="akamai-search-box">🔍 Search services, accounts, and more &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; All ⌄</div>
    <div class="akamai-top-right">
        <div class="create-btn">+ Create</div>
        <div class="icon-container">{SVG_HELP}</div>
        <div class="icon-container">{SVG_CART}</div>
        <div class="icon-container">{SVG_BELL}<span class="notification-badge">11</span></div>
        <div class="icon-container">{SVG_ALERT}<span class="notification-badge">17</span></div>
        <div style="text-align: right; margin-left: 10px;"><strong>Nikhil Goyal</strong><br><span style="font-size: 10px; color: #9DA7B3;">AKAMAI TECHNOLOGIES - ASSETS ⌄</span></div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==========================================
# 2. MOCK DATABASES
# ==========================================
MOCK_DELIVERY = {
    "Select Configuration...": "",
    "authentication.akamai.com (Auth & Identity)": """{
  "propertyName": "authentication.akamai.com",
  "propertyId": "prp_753664",
  "rules": {
    "behaviors": [
      { "name": "origin", "options": { "hostname": "www.example.com" } },
      { "name": "caching", "options": { "behavior": "NO_STORE" } }
    ],
    "options": { "is_secure": false }
  }
}""",
    "api.retailstore.com (E-Commerce API)": """{
  "propertyName": "api.retailstore.com",
  "propertyId": "prp_992100",
  "rules": {
    "behaviors": [
      { "name": "origin", "options": { "hostname": "origin-api.retailstore.com" } },
      { "name": "caching", "options": { "behavior": "NO_STORE" } },
      { "name": "sureRoute", "options": { "enabled": true } }
    ],
    "options": { "is_secure": true }
  }
}"""
}

MOCK_SECURITY = {
    "Select Configuration...": "",
    "No Security Configured (Empty)": """{
  "configId": 0,
  "securityPolicies": []
}""",
    "WAF Enabled (No Bot Protection)": """{
  "configId": 12345,
  "securityPolicies": [
    {
      "name": "Standard_WAF",
      "webApplicationFirewall": { "enabled": true },
      "botManagement": { "enabled": false }
    }
  ]
}"""
}

# ==========================================
# 3. DIAGNOSTIC ENGINE & LOGIC
# ==========================================
def generate_pitch_and_code(issue_lower, target_host, prop_name):
    # Determine dynamic 3-Pillar Data & Enhancements based on user context
    pillars = {
        "Security": {"color": "#0072CE", "count": 1, "beh": "Enforce strict rate limits", "setup": "Enable active threat intelligence feeds", "prod": "App & API Protector"},
        "Reliability": {"color": "#0072CE", "count": 1, "beh": "Configure Origin Health Checks", "setup": "Automate DNS failover routing", "prod": "Global Traffic Management"},
        "Performance": {"color": "#0072CE", "count": 1, "beh": "Enable dynamic content caching", "setup": "Optimize edge cache keys", "prod": "Akamai Ion"}
    }

    if any(keyword in issue_lower for keyword in ["lateral", "segmentation", "ransomware", "internal server", "hybrid cloud"]):
        product = "Akamai Guardicore Segmentation"
        pitch = "Guardicore is an AI-powered segmentation platform that understands asset exposure and automatically enforces containment, keeping your internal servers safe from lateral movement and ransomware across hybrid environments."
        enhancement = "Maps your hybrid environment down to the process level and overlays identity-based microsegmentation policies without requiring any underlying network changes."
        results = "Achieve up to a **99% reduction in lateral movement risk**, ensure compliance with Zero-Trust mandates, and instantly contain ransomware spread within seconds."
        pillars["Security"] = {"color": "#D93025", "count": 3, "beh": "Block unauthorized lateral traffic", "setup": "Deploy software-based microsegmentation agents", "prod": "Akamai Guardicore"}
        tf_code = f"""resource "akamai_guardicore_policy" "ei_trial_segmentation" {{
  policy_name = "Block_Lateral_Movement"
  status      = "MONITOR_ONLY"
  rules       = ["isolate_critical_databases"]
}}"""

    elif any(keyword in issue_lower for keyword in ["ddos", "attack", "security", "waf", "hack"]):
        product = "Akamai App & API Protector (AAP)"
        pitch = "AAP provides industry-leading Web Application Firewall and DDoS protection, instantly absorbing volumetric attacks and blocking malicious requests at the edge before they can overwhelm your origin servers."
        enhancement = "Automatically tunes WAF rules using Akamai's machine learning engine, analyzing edge traffic anomalies to drop malicious payloads before they reach your data center."
        results = "Expect a **100% volumetric DDoS mitigation SLA**, roughly an **85% reduction in false positives**, and sub-second automated threat response times."
        pillars["Security"] = {"color": "#D93025", "count": 2, "beh": "Enable volumetric attack scrubbing", "setup": "Deploy Layer 7 WAF rulesets", "prod": "App & API Protector (AAP)"}
        tf_code = f"""resource "akamai_appsec_security_policy" "ei_trial_ddos_shield" {{
  config_id           = "auto_detected_config"
  security_policy_name = "EI DDoS and WAF Shield"
  create_from_security_policy = "sp_default"
}}"""

    elif any(keyword in issue_lower for keyword in ["bot", "scraper", "stuffing"]) or "auth" in prop_name.lower():
        product = "Akamai App & API Protector (AAP) + Bot Manager"
        pitch = "This bundles Web Application Firewall and Bot Management into a unified edge deployment, consolidating security controls while mitigating credential stuffing and scraping."
        enhancement = "Injects behavior-based telemetry analysis and invisible cryptographic challenges to identify and intercept sophisticated botnets without impacting real human users."
        results = "Experience a **>95% drop in credential stuffing success rates**, immediate bandwidth savings from discarded scrapers, and significantly lower origin server load."
        pillars["Security"] = {"color": "#D93025", "count": 3, "beh": "Analyze behavioral telemetry for bots", "setup": "Implement credential stuffing defense", "prod": "Bot Manager"}
        tf_code = f"""resource "akamai_botman_bot_management_settings" "ei_trial_shield" {{
  config_id          = "auto_detected_config"
  target_hostname    = "{target_host}"
  execution_mode     = "EXECUTION_MODE_MONITOR"
}}"""

    elif any(keyword in issue_lower for keyword in ["image", "video", "media", "picture", "format", "visual"]):
        product = "Akamai Image & Video Manager (IVM)"
        pitch = "Image & Video Manager automatically optimizes and resizes visual content at the edge, drastically reducing payload sizes and improving perceived load times across all devices without sacrificing quality."
        enhancement = "Dynamically evaluates client device types and network conditions to serve next-generation formats (like WebP/AVIF) and optimal resolutions on the fly."
        results = "Typically delivers a **30-60% reduction in media payload size**, drastically improving Core Web Vitals (LCP) and driving higher e-commerce conversion rates."
        pillars["Performance"] = {"color": "#F59E0B", "count": 2, "beh": "Auto-convert next-gen image formats", "setup": "Set perceptual quality thresholds", "prod": "Image & Video Manager (IVM)"}
        tf_code = f"""resource "akamai_property_image_video_manager" "ei_ivm_trial" {{
  config_id  = "auto_detected_config"
  policy_set = "staging_evaluation"
}}"""

    elif any(keyword in issue_lower for keyword in ["cache", "speed", "delivery", "accelerate", "load time"]):
        product = "Akamai Ion"
        pitch = "Akamai Ion provides intelligent performance optimizations, advanced caching, and SureRoute to dynamically accelerate your web and API delivery while offloading your origin infrastructure."
        enhancement = "Applies predictive prefetching, advanced caching rules, and intelligent route optimization (SureRoute) to actively bypass internet congestion."
        results = "Deliver up to **3x faster page loads**, achieve **90%+ origin infrastructure offload**, and maintain highly consistent performance across global geographies."
        pillars["Performance"] = {"color": "#F59E0B", "count": 2, "beh": "Enable SureRoute & Brotli Compression", "setup": "Expand static asset TTLs", "prod": "Akamai Ion"}
        tf_code = f"""resource "akamai_property_activation" "ei_ion_trial" {{
  property_id = "auto_detected_config"
  network     = "STAGING"
}}"""

    else:
        product = "Akamai EdgeWorkers"
        pitch = "EdgeWorkers intercepts requests and executes custom operational logic directly at the edge proxy, drastically reducing origin dependency and latency."
        enhancement = "Moves custom computing logic (like dynamic redirects, token validation, or A/B testing) out of the core data center and executes it on the edge nodes closest to the user."
        results = "Experience **near-zero execution latency**, reduced origin compute costs, and infinite scalability without needing to provision a single server."
        pillars["Performance"] = {"color": "#10B981", "count": 1, "beh": "Offload dynamic routing to edge", "setup": "Deploy edge compute scripts", "prod": "Akamai EdgeWorkers"}
        tf_code = f"""resource "akamai_edgeworkers" "ei_trial_compute" {{
  name            = "edge_logic_accelerator"
  resource_tier   = "200"
  activation_mode = "STAGING_ONLY"
}}"""
        
    return product, pitch, enhancement, results, tf_code, pillars


def run_track_1_analysis(raw_delivery, raw_security, business_issue):
    try:
        delivery_data = json.loads(raw_delivery) if raw_delivery and raw_delivery.strip() else {}
    except Exception:
        pass
    
    origin_host = "Unknown Origin"
    prop_name = delivery_data.get("propertyName", "Custom Configuration") if isinstance(delivery_data, dict) else "Custom Configuration"
    
    def traverse_delivery(node):
        nonlocal origin_host
        if isinstance(node, dict):
            if "behaviors" in node and isinstance(node["behaviors"], list):
                for b in node["behaviors"]:
                    if "name" in b and b["name"] == "origin" and "options" in b:
                        origin_host = b["options"].get("hostname", origin_host)
            if "children" in node:
                for c in node["children"]: traverse_delivery(c)
            if "rules" in node: traverse_delivery(node["rules"])
            
    if delivery_data:
        traverse_delivery(delivery_data)

    issue_lower = business_issue.lower()
    product, pitch, enhancement, results, tf_code, pillars = generate_pitch_and_code(issue_lower, origin_host, prop_name)
    return product, pitch, enhancement, results, tf_code, pillars


def run_track_2_analysis(industry, region, business_issue):
    issue_lower = business_issue.lower()
    target_host = f"api.{industry.lower().replace(' ', '')}.internal"
    product, pitch, enhancement, results, tf_code, pillars = generate_pitch_and_code(issue_lower, target_host, "Enterprise API")
    return product, pitch, enhancement, results, tf_code, pillars


# ==========================================
# 4. MAIN UI LAYOUT
# ==========================================
st.title("Marketplace")
st.markdown("<p style='font-size: 14px; margin-top: -20px; margin-bottom: 20px; color: #64748B;'>Akamai EI - Akamai EdgeIntelligence Marketplace</p>", unsafe_allow_html=True)

# 🔥 LIMITED AVAILABILITY ANNOUNCEMENT BANNER
st.markdown("""
<div style="background-color: #E6F4EA; border-left: 4px solid #137333; padding: 15px; margin-bottom: 25px; border-radius: 4px;">
    <h4 style="margin-top: 0; margin-bottom: 10px; color: #137333; font-size: 16px;">✨ Early Access: Explore Akamai's Latest Innovations</h4>
    <p style="font-size: 13px; color: #2B313A; margin-bottom: 10px;">Discover our newest LA (Limited Availability) products designed to protect and optimize your environment in the AI era.</p>
    <ul style="font-size: 13px; color: #2B313A; padding-left: 20px; margin-bottom: 0;">
        <li style="margin-bottom: 8px;"><b>AI Brand Presence:</b> Ensures a brand's content is accurately represented across AI-driven experiences and agentic workflows. <a href="#">Read or initiate try here!</a></li>
        <li style="margin-bottom: 8px;"><b>Akamai Guardicore Segmentation:</b> The first AI-powered segmentation platform with built-in Exposure Analysis & Response capabilities. <a href="#">Read or initiate try here!</a></li>
        <li style="margin-bottom: 8px;"><b>API Security:</b> Protect APIs throughout their entire lifecycle to reduce the risk of data breaches. <a href="#">Read or initiate try here!</a></li>
        <li style="margin-bottom: 0;"><b>Brand Guardian:</b> AI-powered solution for continuously detecting and taking down modern, AI-driven brand abuse across the digital ecosystem. <a href="#">Read or initiate try here!</a></li>
    </ul>
</div>
""", unsafe_allow_html=True)

# GATEWAY QUESTION
gateway_choice = st.radio(
    "**How can we help you today?**",
    ["I know which Akamai product I want to buy or trial.", "I want Akamai EI to analyze my environment and recommend solutions."],
    index=1
)

st.markdown("<hr style='margin: 10px 0; border: none; border-top: 1px solid #E2E8F0;'>", unsafe_allow_html=True)

if gateway_choice == "I know which Akamai product I want to buy or trial.":
    st.markdown('<div class="akamai-card" style="text-align: center; padding: 40px;">', unsafe_allow_html=True)
    st.markdown("### Browse the Standard Marketplace")
    st.write("Explore our catalog of delivery, security, and edge compute products.")
    st.button("Go to Standard Marketplace", type="primary")
    st.markdown('</div>', unsafe_allow_html=True)

else:
    col1, col2 = st.columns([1, 1.25], gap="large")

    with col1:
        st.markdown('<div class="akamai-card">', unsafe_allow_html=True)
        st.markdown('<div class="akamai-card-title">1. Scope the Environment</div>', unsafe_allow_html=True)
        
        st.markdown("<span style='font-size: 14px; font-weight: 600; color: #1E2228;'>Data Privacy & Analysis Track:</span>", unsafe_allow_html=True)
        
        track_choice = st.radio("Privacy Track", [
            "Track 1: Deep-Insight Mode (Automated Config Scan)", 
            "Track 2: Contextual-Match Mode (Industry Benchmarks Only)"
        ], 
        captions=[
            "AI securely parses your active configurations to provide personalized recommendations.",
            "No config scan. AI suggests products based on external global industry benchmarks."
        ],
        help="Choose Track 1 for personalized insights based on your configuration, or Track 2 to maintain strict data privacy while utilizing global benchmarks.",
        label_visibility="collapsed")
        
        st.markdown("<hr style='margin: 10px 0; border: none; border-top: 1px solid #E2E8F0;'>", unsafe_allow_html=True)
        
        if "Track 1" in track_choice:
            st.info("Provide Delivery and/or Security configurations for analysis.")
            input_method = st.radio("Configuration Source:", ["Select from Catalog", "Paste Custom JSON (PAPI/AppSec)"], horizontal=True, label_visibility="collapsed")
            
            if input_method == "Select from Catalog":
                st.markdown("**Delivery Property Configuration:**")
                del_env = st.selectbox("Select Delivery Property:", list(MOCK_DELIVERY.keys()), label_visibility="collapsed")
                final_del_payload = MOCK_DELIVERY[del_env]
                
                st.markdown("**Security Policy Configuration (AppSec):**")
                sec_env = st.selectbox("Select Security Policy:", list(MOCK_SECURITY.keys()), label_visibility="collapsed")
                final_sec_payload = MOCK_SECURITY[sec_env]
                
            else:
                final_del_payload = st.text_area("Paste Delivery JSON (Property Manager):", height=150)
                final_sec_payload = st.text_area("Paste Security JSON (AppSec):", height=150)
        else:
            st.info("Deep-Insight Scanning Disabled. Analysis will be performed using Akamai Global Intelligence benchmarks.")
            col_ind, col_reg = st.columns(2)
            with col_ind: industry_input = st.selectbox("Industry Sector:", ["Financial Services", "Retail & E-Commerce", "Media & Entertainment", "Public Sector"])
            with col_reg: region_input = st.selectbox("Primary Region:", ["North America", "EMEA", "Asia Pacific", "LATAM"])
            final_del_payload = None
            final_sec_payload = None

        st.markdown('<div class="akamai-card-title" style="margin-top:20px;">2. Business Context (Copilot)</div>', unsafe_allow_html=True)
        issue_input = st.text_area("Describe what you are looking to enhance or any issues you are currently facing:", placeholder="e.g., We are migrating our inventory databases to a hybrid cloud and need to ensure our internal servers are safe from lateral attacks.", height=80)
        
        run_scan = st.button("Scan my configs", type="primary")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        if run_scan and issue_input:
            
            if "Track 1" in track_choice and (final_del_payload or final_sec_payload):
                product, pitch, enhancement, results, tf_code, pillars = run_track_1_analysis(final_del_payload, final_sec_payload, issue_input)
            elif "Track 2" in track_choice:
                product, pitch, enhancement, results, tf_code, pillars = run_track_2_analysis(industry_input, region_input, issue_input)
            else:
                st.error("Please provide at least one configuration dataset (Delivery or Security).")
                st.stop()
            
            st.markdown('<div class="akamai-card" style="padding-bottom: 10px;">', unsafe_allow_html=True)
            st.markdown('<div class="akamai-card-title">Diagnostic Product Recommendations</div>', unsafe_allow_html=True)
            
            # 🔥 THREE-PILLAR STATUS CARDS (Security, Reliability, Performance)
            p_col1, p_col2, p_col3 = st.columns(3)
            
            # 1. SECURITY PILLAR
            with p_col1:
                st.markdown(f"""
                <div class="azure-card" style="border-top: 4px solid {pillars['Security']['color']};">
                    <div class="azure-header">
                        <span class="azure-title">🛡️ Security</span>
                    </div>
                    <div class="azure-sub">Impact & Mitigation</div>
                    <hr class="azure-hr">
                    <div class="azure-section"><b>Behaviors:</b> {pillars['Security']['beh']}</div>
                    <div class="azure-section"><b>Setup:</b> {pillars['Security']['setup']}</div>
                    <div class="azure-section"><b>Recommended Product:</b> {pillars['Security']['prod']}</div>
                </div>
                """, unsafe_allow_html=True)
                
            # 2. RELIABILITY PILLAR
            with p_col2:
                st.markdown(f"""
                <div class="azure-card" style="border-top: 4px solid {pillars['Reliability']['color']};">
                    <div class="azure-header">
                        <span class="azure-title">⚙️ Reliability</span>
                    </div>
                    <div class="azure-sub">Availability & Failover</div>
                    <hr class="azure-hr">
                    <div class="azure-section"><b>Behaviors:</b> {pillars['Reliability']['beh']}</div>
                    <div class="azure-section"><b>Setup:</b> {pillars['Reliability']['setup']}</div>
                    <div class="azure-section"><b>Recommended Product:</b> {pillars['Reliability']['prod']}</div>
                </div>
                """, unsafe_allow_html=True)
                
            # 3. PERFORMANCE PILLAR
            with p_col3:
                st.markdown(f"""
                <div class="azure-card" style="border-top: 4px solid {pillars['Performance']['color']};">
                    <div class="azure-header">
                        <span class="azure-title">🚀 Performance</span>
                    </div>
                    <div class="azure-sub">Speed & Optimization</div>
                    <hr class="azure-hr">
                    <div class="azure-section"><b>Behaviors:</b> {pillars['Performance']['beh']}</div>
                    <div class="azure-section"><b>Setup:</b> {pillars['Performance']['setup']}</div>
                    <div class="azure-section"><b>Recommended Product:</b> {pillars['Performance']['prod']}</div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="akamai-card">', unsafe_allow_html=True)
                
            # 2. SOLUTION, FACTS & TRIAL BLUEPRINT
            if product != "N/A":
                st.markdown('<div class="section-header" style="margin-top: 5px;">Primary Solution Provisioning</div>', unsafe_allow_html=True)
                st.success(f"**{product}**")
                st.write(pitch)
                
                # 🔥 NEW: ENHANCEMENT & RESULTS FACTS BOX
                st.markdown(f"""
                <div style="background-color: #F8FAFC; border-left: 4px solid #0072CE; padding: 16px; margin-top: 15px; margin-bottom: 20px; border-radius: 4px;">
                    <p style="margin: 0 0 10px 0; font-size: 14px; color: #1E2228;"><strong>🛠️ Configuration Enhancement:</strong><br><span style="color: #475569;">{enhancement}</span></p>
                    <p style="margin: 0; font-size: 14px; color: #1E2228;"><strong>📈 Expected Results:</strong><br><span style="color: #475569;">{results}</span></p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("**Auto-Generated 90% Pre-Configured Trial Blueprint (HCL):**")
                st.code(tf_code, language="hcl")
                
                st.markdown("<br>", unsafe_allow_html=True)
                b1, b2, b3 = st.columns(3)
                with b1:
                    st.button("Activate Trial (Shadow Mode)", type="primary", use_container_width=True)
                with b2:
                    st.button("Initiate 1-Click Trial", use_container_width=True)
                with b3:
                    st.button("Reach out to your IAT", use_container_width=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
                
        else:
            st.markdown("""
            <div class="empty-state-box">
                <div class="empty-state-title">Your Marketplace is empty.</div>
                <br>
                <p style="font-size: 13px; color: #64748B; margin-top: 10px;">👈 After you provide all the details, the recommendations will be shown here.</p>
            </div>
            """, unsafe_allow_html=True)
