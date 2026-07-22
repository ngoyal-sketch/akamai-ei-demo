import streamlit as st
import json

# ==========================================
# 1. PAGE SETUP & CORPORATE AKAMAI STYLING
# ==========================================
st.set_page_config(page_title="Akamai Marketplace | Control Center", layout="wide", initial_sidebar_state="expanded")

AKAMAI_CSS = """
<style>
    .block-container { padding-top: 2rem !important; }
    header { display: none !important; }
    
    .stApp { background-color: #F4F6F9; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
    .akamai-topbar {
        background-color: #1E2228; color: #FFFFFF; padding: 10px 24px; margin-top: -60px; margin-left: -60px; margin-right: -60px; margin-bottom: 25px;
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
    
    .akamai-card { background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 4px; padding: 24px; margin-bottom: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.03); }
    .akamai-card-title { font-size: 18px; font-weight: 700; color: #1E2228; margin-bottom: 16px; }
    .empty-state-box { background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 4px; padding: 60px 20px; text-align: center; margin-top: 10px; }
    .empty-state-title { font-size: 16px; font-weight: 700; color: #2B313A; margin-bottom: 8px; }
    .empty-state-sub { font-size: 13px; color: #64748B; }
    .stButton > button { background-color: #0072CE !important; color: #FFFFFF !important; font-weight: 600 !important; border-radius: 4px !important; border: none !important; padding: 8px 18px !important; }
    .section-header { font-size: 15px; font-weight: 700; color: #1E2228; margin-top: 20px; margin-bottom: 10px; border-bottom: 1px solid #E2E8F0; padding-bottom: 8px;}
    
    ul { margin-top: 10px; padding-left: 20px; color: #2B313A; font-size: 14px; }
    li { margin-bottom: 8px; }
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

MOCK_ENVIRONMENTS = {
    "authentication.akamai.com (Auth & Identity)": """{
  "propertyName": "authentication.akamai.com",
  "propertyId": "prp_753664",
  "rules": {
    "behaviors": [
      { "name": "origin", "options": { "hostname": "www.example.com", "verificationMode": "PLATFORM_SETTINGS" } },
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

# ==========================================
# 2. DIAGNOSTIC ENGINE & LOGIC
# ==========================================
def generate_pitch_and_code(issue_lower, target_host, prop_name):
    """Generates the Pillar C 90% Pre-Configured Artifact."""
    
    # 1. DDOS & WAF USE CASES 
    if any(keyword in issue_lower for keyword in ["ddos", "attack", "security", "waf", "hack"]):
        product = "Akamai App & API Protector (AAP)"
        pitch = "AAP provides industry-leading Web Application Firewall and DDoS protection, instantly absorbing volumetric attacks and blocking malicious requests at the edge before they can overwhelm your origin servers."
        tf_code = f"""# 90% Pre-Configured Trial Blueprint (Pillar C)
# Mode: Shadow / Monitor-Only (Zero Production Impact)
resource "akamai_appsec_security_policy" "ei_trial_ddos_shield" {{
  config_id           = "auto_detected_config"
  security_policy_name = "EI DDoS and WAF Shield"
  create_from_security_policy = "sp_default"
}}"""

    # 2. BOT & SCRAPER USE CASES
    elif any(keyword in issue_lower for keyword in ["bot", "scraper", "stuffing"]) or "auth" in prop_name.lower():
        product = "Akamai App & API Protector (AAP) + Bot Manager"
        pitch = "This bundles Web Application Firewall and Bot Management into a unified edge deployment, consolidating security controls while mitigating credential stuffing and scraping."
        tf_code = f"""# 90% Pre-Configured Trial Blueprint (Pillar C)
# Mode: Shadow / Monitor-Only (Zero Production Impact)
resource "akamai_botman_bot_management_settings" "ei_trial_shield" {{
  config_id          = "auto_detected_config"
  target_hostname    = "{target_host}"
  
  # Non-blocking activation for safe evaluation
  execution_mode     = "EXECUTION_MODE_MONITOR"
}}"""

    # 3. MEDIA & IMAGE USE CASES
    elif any(keyword in issue_lower for keyword in ["image", "video", "media", "picture", "format", "visual"]):
        product = "Akamai Image & Video Manager (IVM)"
        pitch = "Image & Video Manager automatically optimizes and resizes visual content at the edge, drastically reducing payload sizes and improving perceived load times across all devices without sacrificing quality."
        tf_code = f"""# 90% Pre-Configured Trial Blueprint (Pillar C)
# Mode: Shadow / Monitor-Only (Zero Production Impact)
resource "akamai_property_image_video_manager" "ei_ivm_trial" {{
  config_id  = "auto_detected_config"
  policy_set = "staging_evaluation"
}}"""

    # 4. DELIVERY & PERFORMANCE USE CASES
    elif any(keyword in issue_lower for keyword in ["cache", "speed", "delivery", "accelerate", "load time"]):
        product = "Akamai Ion"
        pitch = "Akamai Ion provides intelligent performance optimizations, advanced caching, and SureRoute to dynamically accelerate your web and API delivery while offloading your origin infrastructure."
        tf_code = f"""# 90% Pre-Configured Trial Blueprint (Pillar C)
# Mode: Shadow / Monitor-Only (Zero Production Impact)
resource "akamai_property_activation" "ei_ion_trial" {{
  property_id = "auto_detected_config"
  network     = "STAGING"
}}"""

    # 5. EDGE COMPUTE (Default for offload/custom logic)
    else:
        product = "Akamai EdgeWorkers"
        pitch = "EdgeWorkers intercepts requests and executes custom operational logic directly at the edge proxy, drastically reducing origin dependency and latency."
        tf_code = f"""# 90% Pre-Configured Trial Blueprint (Pillar C)
# Mode: Shadow / Monitor-Only (Zero Production Impact)
resource "akamai_edgeworkers" "ei_trial_compute" {{
  name            = "edge_logic_accelerator"
  resource_tier   = "200"
  activation_mode = "STAGING_ONLY"
}}"""
        
    return product, pitch, tf_code


def run_track_1_analysis(raw_json, business_issue):
    """Deep-Insight Mode: Scans the JSON Config for ALL Akamai Products."""
    try:
        data = json.loads(raw_json)
    except Exception:
        return ["Invalid JSON format provided."], ["Please ensure valid configuration data."], "N/A", "N/A", ""

    prop_name = data.get("propertyName", "Custom Property")
    behaviors_found = set()
    is_secure = True 
    origin_host = "Unknown Origin"
    
    def traverse(node):
        nonlocal is_secure, origin_host
        if isinstance(node, dict):
            if "options" in node and "is_secure" in node["options"]:
                is_secure = node["options"]["is_secure"]
            if "behaviors" in node and isinstance(node["behaviors"], list):
                for b in node["behaviors"]:
                    if "name" in b:
                        behaviors_found.add(b["name"].lower())
                        if b["name"] == "origin" and "options" in b:
                            origin_host = b["options"].get("hostname", origin_host)
            if "children" in node:
                for c in node["children"]: traverse(c)
            if "rules" in node: traverse(node["rules"])
            
    traverse(data)
    
    # Exhaustive Feature Mapping based on extensive Akamai behaviors
    FEATURE_MAP = {
        "Security": {
            "webapplicationfirewall": "Web Application Firewall (WAF)",
            "botmanager": "Bot Manager",
            "contentprotector": "Content Protector (CPR)",
            "apisecurity": "API Security",
            "clientreputation": "Client Reputation",
            "requestcontrol": "Request Control (Deny/Allow)",
            "enhancedtls": "Enhanced TLS (HSTS)",
            "ddosprotection": "DDoS Protection",
            "securityconnector": "Security Connector"
        },
        "Delivery & Performance": {
            "caching": "Advanced Caching",
            "origin": "Origin Definition",
            "sureroute": "SureRoute",
            "cpcode": "CP Codes",
            "prefetch": "Prefetching",
            "compression": "Compression",
            "modifyoutgoingrequestheader": "Request/Response Modifiers",
            "modifyincomingresponseheader": "Request/Response Modifiers",
            "redirect": "Edge Redirect",
            "forwardrewrite": "Forward Rewrite",
            "ratecontrol": "Rate Control",
            "accesscontrol": "Access Control",
            "tls": "TLS Enforcement",
            "origincharacteristics": "Origin Characteristics",
            "requestvalidation": "Request Validation",
            "setvariable": "Variable Management",
            "variableredirect": "Variable Management",
            "variablerewrite": "Variable Management",
            "variablemodifyheader": "Variable Management",
            "variablecachekey": "Variable Management",
            "variableorigin": "Variable Management",
            "variablecpcode": "Variable Management",
            "variableprefetch": "Variable Management",
            "variablecompression": "Variable Management",
            "variableratecontrol": "Variable Management",
            "variablecloudlet": "Variable Management",
            "variableimagemanager": "Variable Management",
            "variablevideomanager": "Variable Management",
            "setcookie": "Cookie Management",
            "removecookie": "Cookie Management",
            "variablesetcookie": "Cookie Management",
            "variableremovecookie": "Cookie Management"
        },
        "Edge Compute & Cloudlets": {
            "edgeworkers": "EdgeWorkers",
            "edgekv": "EdgeKV",
            "apigateway": "API Gateway",
            "cloudlets": "Cloudlets General",
            "phasedrelease": "Phased Release Cloudlet",
            "applicationloadbalancer": "ALB Cloudlet",
            "audiencesegmentation": "Audience Segmentation Cloudlet",
            "visitorprioritization": "Visitor Prioritization Cloudlet",
            "edgeredirector": "Edge Redirector Cloudlet"
        },
        "Media & Data": {
            "imagemanager": "Image Manager",
            "videomanager": "Video Manager",
            "netstorage": "NetStorage",
            "customlogging": "Custom Logging",
            "datastream": "DataStream",
            "logdeliveryservice": "Log Delivery Service"
        }
    }

    active_features = {"Security": [], "Delivery & Performance": [], "Edge Compute & Cloudlets": [], "Media & Data": []}
    for b in behaviors_found:
        for category, mappings in FEATURE_MAP.items():
            if b in mappings:
                if mappings[b] not in active_features[category]:
                    active_features[category].append(mappings[b])

    issue_lower = business_issue.lower()
    observations = [f"Analyzed configuration for {prop_name} routing to origin {origin_host}."]
    
    if not is_secure: 
        observations.append("CRITICAL: The is_secure flag is set to false, permitting unencrypted HTTP edge traffic.")
    
    active_summary = []
    for category, items in active_features.items():
        if items:
            active_summary.append(f"<b>{category}:</b> " + ", ".join(items))
    
    if active_summary:
        observations.append("<b>Active Akamai Capabilities Detected:</b><br>" + "<br>".join(active_summary))
    else:
        observations.append("WARNING: No advanced Security, Media, or Edge Compute features detected in this rule tree.")
        
    if "botmanager" not in behaviors_found: 
        observations.append("WARNING: There are zero active Layer-7 Bot Management behaviors attached to this rule tree.")
    
    recommendations = []
    if any(keyword in issue_lower for keyword in ["ddos", "attack", "security", "waf", "hack"]):
        recommendations.append("Deploy robust Layer-7 Web Application Firewall and volumetric DDoS mitigation to absorb attacks at the edge.")
    elif any(keyword in issue_lower for keyword in ["bot", "scraper", "stuffing"]) or "auth" in prop_name.lower():
        recommendations.append("Implement behavior-based bot mitigation at the edge proxy to filter automated threats before origin impact.")
    elif any(keyword in issue_lower for keyword in ["image", "video", "media", "picture", "format", "visual"]):
        recommendations.append("Implement automated edge-based media optimization to dynamically compress and format visual assets based on client device capabilities.")
    elif any(keyword in issue_lower for keyword in ["cache", "speed", "delivery", "accelerate", "load time"]):
        recommendations.append("Enhance edge caching policies and enable dynamic routing to accelerate delivery and offload origin infrastructure.")
    else:
        recommendations.append("Offload dynamic routing logic or custom configurations to serverless edge compute to reduce origin latency.")

    product, pitch, tf_code = generate_pitch_and_code(issue_lower, origin_host, prop_name)
    return observations, recommendations, product, pitch, tf_code


def run_track_2_analysis(industry, region, business_issue):
    """Contextual-Match Mode: Uses Industry Benchmarks (No Scan)."""
    issue_lower = business_issue.lower()
    
    observations = [
        f"Data Privacy Track 2 Active: Internal configurations were bypassed. Analysis is based on {industry} sector telemetry in {region}.",
        f"Akamai Global Intelligence indicates that 63% of operational friction in {industry} networks stems from automated API abuse and credential stuffing.",
        "Regional baseline data shows a high volume of distributed scraping attacks originating from unmitigated edge connections."
    ]
    
    recommendations = [
        "Adopt a Zero-Trust architecture by shifting API and login authentication validation to the CDN edge.",
        "Implement heuristic bot profiling to distinguish between legitimate customer traffic and advanced persistent bots."
    ]
    
    target_host = f"api.{industry.lower().replace(' ', '')}.internal"
    product, pitch, tf_code = generate_pitch_and_code(issue_lower, target_host, "Enterprise API")
    
    return observations, recommendations, product, pitch, tf_code


# ==========================================
# 3. MAIN UI LAYOUT
# ==========================================
st.title("Marketplace")
st.caption("Akamai EI - Akamai EdgeIntelligence Marketplace")

col1, col2 = st.columns([1, 1.25])

with col1:
    st.markdown('<div class="akamai-card">', unsafe_allow_html=True)
    st.markdown('<div class="akamai-card-title">1. Scope the Environment</div>', unsafe_allow_html=True)
    
    st.markdown("<span style='font-size: 14px; font-weight: 600; color: #1E2228;'>Data Privacy & Analysis Track:</span>", unsafe_allow_html=True)
    track_choice = st.radio("Privacy Track", [
        "Track 1: Deep-Insight Mode (Automated Config Scan)", 
        "Track 2: Contextual-Match Mode (Industry Benchmarks Only)"
    ], label_visibility="collapsed")
    
    st.markdown("<hr style='margin: 10px 0; border: none; border-top: 1px solid #E2E8F0;'>", unsafe_allow_html=True)
    
    if "Track 1" in track_choice:
        input_method = st.radio("Configuration Source:", ["Select from Catalog", "Paste Custom JSON (PAPI)"], horizontal=True, label_visibility="collapsed")
        if input_method == "Select from Catalog":
            selected_env = st.selectbox("Select Affected Customer Property / Hostname:", list(MOCK_ENVIRONMENTS.keys()))
            final_payload = MOCK_ENVIRONMENTS[selected_env]
            with st.expander("View Underlying Property JSON Configuration", expanded=False):
                st.code(final_payload, language="json")
        else:
            final_payload = st.text_area("Paste your raw Akamai Property Manager JSON here:", height=150)
    else:
        st.info("Deep-Insight Scanning Disabled. Analysis will be performed using Akamai Global Intelligence benchmarks.")
        col_ind, col_reg = st.columns(2)
        with col_ind: industry_input = st.selectbox("Industry Sector:", ["Financial Services", "Retail & E-Commerce", "Media & Entertainment", "Public Sector"])
        with col_reg: region_input = st.selectbox("Primary Region:", ["North America", "EMEA", "Asia Pacific", "LATAM"])
        final_payload = None

    st.markdown('<div class="akamai-card-title" style="margin-top:20px;">2. Business Context (Copilot)</div>', unsafe_allow_html=True)
    issue_input = st.text_area("Describe what you are looking to enhance or any issues you are currently facing:", placeholder="e.g., Credential stuffing attacks are locking out real users, or looking to reduce origin latency.", height=80)
    
    run_scan = st.button("Run Contextual Audit", type="primary")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if run_scan and issue_input:
        
        if "Track 1" in track_choice and final_payload:
            observations, recommendations, product, pitch, tf_code = run_track_1_analysis(final_payload, issue_input)
        elif "Track 2" in track_choice:
            observations, recommendations, product, pitch, tf_code = run_track_2_analysis(industry_input, region_input, issue_input)
        else:
            st.error("Please provide configuration data.")
            st.stop()
        
        st.markdown('<div class="akamai-card">', unsafe_allow_html=True)
        st.markdown('<div class="akamai-card-title">Diagnostic Report</div>', unsafe_allow_html=True)
        
        # --- 1: OBSERVATIONS ---
        st.markdown('<div class="section-header">1. Current State Observations</div>', unsafe_allow_html=True)
        if "Track 1" in track_choice: st.info("Based only on the provided configuration file, I observed the following:")
        
        obs_html = "<ul>" + "".join([f"<li>{obs}</li>" for obs in observations]) + "</ul>"
        st.markdown(obs_html, unsafe_allow_html=True)
            
        # --- 2: RECOMMENDATIONS ---
        st.markdown('<div class="section-header">2. Architectural Recommendations</div>', unsafe_allow_html=True)
        st.warning(f"To address the context: \"{issue_input}\"")
        
        rec_html = "<ul>" + "".join([f"<li>{rec}</li>" for rec in recommendations]) + "</ul>"
        st.markdown(rec_html, unsafe_allow_html=True)
            
        # --- 3: PRODUCT PITCH & PILLAR C TRIAL ---
        if product != "N/A":
            st.markdown('<div class="section-header">3. Recommended Akamai Solution</div>', unsafe_allow_html=True)
            st.success(f"**{product}**")
            st.write(pitch)
            
            st.markdown("**Auto-Generated 90% Pre-Configured Trial Blueprint (HCL):**")
            st.code(tf_code, language="hcl")
            
            st.button("Activate Pre-Configured Trial (Shadow Mode)", type="primary")
        
        st.markdown('</div>', unsafe_allow_html=True)
            
    else:
        st.markdown("""
        <div class="empty-state-box">
            <div class="empty-state-title">Your Marketplace is empty.</div>
            <br>
            <p style="font-size: 13px; color: #64748B; margin-top: 10px;">👈 After you provide all the details, the recommendations will be shown here.</p>
        </div>
        """, unsafe_allow_html=True)
