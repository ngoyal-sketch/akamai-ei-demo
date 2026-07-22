import streamlit as st
import json

# ==========================================
# ⚙️ 1. PAGE SETUP & CORPORATE AKAMAI STYLING
# ==========================================
st.set_page_config(page_title="Akamai Marketplace | Control Center", layout="wide", initial_sidebar_state="expanded")

AKAMAI_CSS = """
<style>
    /* Clean up Streamlit's default padding to remove any blank white space at the top */
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
    
    /* Notification Badge Styling */
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
    
    /* Clean list styling for enterprise look */
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

# Top Bar
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
# 📂 2. MOCK CATALOG (For Dropdown)
# ==========================================
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
      { "name": "webApplicationFirewall", "options": { "enabled": true } }
    ],
    "options": { "is_secure": true }
  }
}"""
}

# ==========================================
# 🧠 3. ENTERPRISE AI DIAGNOSTIC ENGINE (No Emojis)
# ==========================================
def analyze_json_and_context(raw_json, business_issue):
    try:
        data = json.loads(raw_json)
    except Exception:
        return ["Invalid JSON format provided. Cannot parse rule tree."], ["Please ensure the pasted configuration is valid JSON."], "N/A", "N/A", ""

    prop_name = data.get("propertyName", "Custom PAPI Property")
    behaviors = []
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
                        behaviors.append(b["name"].lower())
                        if b["name"] == "origin" and "options" in b:
                            origin_host = b["options"].get("hostname", origin_host)
            if "children" in node:
                for c in node["children"]: traverse(c)
            if "rules" in node: traverse(node["rules"])

    traverse(data)
    issue_lower = business_issue.lower()
    
    observations = []
    observations.append(f"Analyzed configuration for **{prop_name}** routing to origin `{origin_host}`.")
    if not is_secure:
        observations.append("The `is_secure` flag is set to **false**, meaning edge traffic is currently permitted over unencrypted HTTP.")
    
    has_bot = "botmanagement" in behaviors
    has_waf = "webapplicationfirewall" in behaviors or "appsec" in behaviors
    
    if not has_waf and not has_bot:
        observations.append("There are **zero active Layer-7 security behaviors** (WAF, Bot Management) attached to this property rule tree.")
    elif has_waf and not has_bot:
        observations.append("A Web Application Firewall (WAF) is active, but specialized `botManagement` protections are missing.")
    
    recommendations = []
    if "bot" in issue_lower or "stuffing" in issue_lower or "scraper" in issue_lower or "auth" in prop_name.lower():
        recommendations.append("To mitigate automated attacks, behavior-based bot mitigation must be implemented at the edge proxy before traffic reaches the origin.")
    if "slow" in issue_lower or "crash" in issue_lower or "performance" in issue_lower or "enhance" in issue_lower or "offload" in issue_lower:
        recommendations.append("To reduce origin load and optimize performance, consider offloading dynamic routing logic or token validation to serverless edge compute.")
    if not is_secure:
        recommendations.append("Enforce strict TLS (HTTPS only) across all endpoints to secure data in transit.")
        
    if not recommendations:
        recommendations.append("Apply Layer-7 application security controls to filter malicious traffic and review caching rules to optimize edge delivery.")

    if not has_bot and ("bot" in issue_lower or "auth" in prop_name.lower() or "scraper" in issue_lower):
        product = "Akamai App & API Protector (AAP) + Bot Manager"
        pitch = "AAP bundles Web Application Firewall, Bot Manager, and API Security into a single edge deployment. This consolidates security controls, protects endpoints from credential stuffing and scraping, and enforces strict security compliance."
        tf_code = f"""resource "akamai_botman_bot_management_settings" "ei_shield" {{
  config_id          = 123456
  target_hostname    = "{origin_host}"
  execution_mode     = "EXECUTION_MODE_ALWAYS"
}}"""
    else:
        product = "Akamai EdgeWorkers + App & API Protector"
        pitch = "By deploying EdgeWorkers, you can intercept requests and execute custom operational logic at the edge, drastically reducing origin dependency. Pairing this with AAP secures the enhanced API flows."
        tf_code = f"""resource "akamai_edgeworkers" "edge_compute" {{
  name          = "edge_logic_router"
  resource_tier = "200"
}}"""

    return observations, recommendations, product, pitch, tf_code


# ==========================================
# 🚀 4. MAIN UI LAYOUT
# ==========================================
st.title("Marketplace")
st.caption("Akamai EI - Akamai EdgeIntelligence Marketplace")

col1, col2 = st.columns([1, 1.25])

with col1:
    st.markdown('<div class="akamai-card">', unsafe_allow_html=True)
    st.markdown('<div class="akamai-card-title">1. Scope the Environment</div>', unsafe_allow_html=True)
    
    input_method = st.radio("Configuration Source:", ["Select from Catalog", "Paste Custom JSON (PAPI)"], horizontal=True, label_visibility="collapsed")
    
    if input_method == "Select from Catalog":
        selected_env = st.selectbox("Select Affected Customer Property / Hostname:", list(MOCK_ENVIRONMENTS.keys()))
        final_json_payload = MOCK_ENVIRONMENTS[selected_env]
        with st.expander("View Underlying Property JSON Configuration", expanded=False):
            st.code(final_json_payload, language="json")
    else:
        final_json_payload = st.text_area("Paste your raw Akamai Property Manager JSON here:", height=200)
    
    st.markdown('<div class="akamai-card-title" style="margin-top:20px;">2. Business Context</div>', unsafe_allow_html=True)
    issue_input = st.text_area("Describe what you are looking to enhance or any issues you are currently facing:", placeholder="e.g., Credential stuffing attacks are locking out real users, or looking to reduce origin latency.", height=80)
    
    run_scan = st.button("Run Contextual Audit", type="primary")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if run_scan and final_json_payload and issue_input:
        observations, recommendations, product, pitch, tf_code = analyze_json_and_context(final_json_payload, issue_input)
        
        st.markdown('<div class="akamai-card">', unsafe_allow_html=True)
        st.markdown('<div class="akamai-card-title">Diagnostic Report</div>', unsafe_allow_html=True)
        
        # --- STEP 1: FACTUAL OBSERVATIONS ---
        st.markdown('<div class="section-header">1. Current State Observations</div>', unsafe_allow_html=True)
        st.info("Based only on the provided configuration file, I observed the following:")
        
        obs_html = "<ul>" + "".join([f"<li>{obs}</li>" for obs in observations]) + "</ul>"
        st.markdown(obs_html, unsafe_allow_html=True)
            
        # --- STEP 2: AGNOSTIC RECOMMENDATIONS ---
        st.markdown('<div class="section-header">2. Architectural Recommendations</div>', unsafe_allow_html=True)
        st.warning(f"To address the context: \"{issue_input}\"")
        
        rec_html = "<ul>" + "".join([f"<li>{rec}</li>" for rec in recommendations]) + "</ul>"
        st.markdown(rec_html, unsafe_allow_html=True)
            
        # --- STEP 3: AKAMAI PRODUCT PITCH ---
        if product != "N/A":
            st.markdown('<div class="section-header">3. Recommended Akamai Solution</div>', unsafe_allow_html=True)
            st.success(f"**{product}**")
            st.write(pitch)
            
            st.markdown("**Auto-Generated Staging Fix Blueprint (HCL):**")
            st.code(tf_code, language="hcl")
            
            st.button("Deploy Configuration to Staging", type="primary")
        
        st.markdown('</div>', unsafe_allow_html=True)
            
    else:
        st.markdown("""
        <div class="empty-state-box">
            <div class="empty-state-title">Your Marketplace is empty.</div>
            <br>
            <p style="font-size: 13px; color: #64748B; margin-top: 10px;">👈 After you provide all the details, the recommendations will be shown here.</p>
        </div>
        """, unsafe_allow_html=True)
