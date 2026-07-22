import streamlit as st
import json

# ==========================================
# ⚙️ 1. PAGE SETUP & CORPORATE AKAMAI STYLING
# ==========================================
st.set_page_config(page_title="Akamai Marketplace | Control Center", layout="wide", initial_sidebar_state="expanded")

AKAMAI_CSS = """
<style>
    .stApp { background-color: #F4F6F9; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
    .akamai-topbar {
        background-color: #1E2228; color: #FFFFFF; padding: 10px 24px; margin-top: -60px; margin-left: -60px; margin-right: -60px; margin-bottom: 20px;
        display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #2B313A;
    }
    .akamai-brand { font-weight: 800; font-size: 20px; letter-spacing: 0.5px; }
    .akamai-brand span { color: #0072CE; }
    .akamai-search-box { background-color: #2B313A; border: 1px solid #3A424D; border-radius: 4px; padding: 6px 16px; color: #C0C7D0; width: 380px; font-size: 13px; }
    .akamai-top-right { display: flex; align-items: center; gap: 16px; font-size: 12px; color: #E2E8F0; }
    .create-btn { background-color: #0072CE; color: white; padding: 6px 16px; border-radius: 4px; font-weight: 600; font-size: 13px; }
    .notification-badge { background-color: #D93025; color: white; font-size: 10px; font-weight: 700; padding: 2px 6px; border-radius: 10px; margin-left: -8px; }
    .akamai-card { background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 4px; padding: 24px; margin-bottom: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.03); }
    .akamai-card-title { font-size: 20px; font-weight: 700; color: #1E2228; margin-bottom: 16px; }
    .empty-state-box { background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 4px; padding: 60px 20px; text-align: center; margin-top: 10px; }
    .empty-state-title { font-size: 18px; font-weight: 700; color: #2B313A; margin-bottom: 8px; }
    .empty-state-sub { font-size: 13px; color: #64748B; }
    .stButton > button { background-color: #0072CE !important; color: #FFFFFF !important; font-weight: 600 !important; border-radius: 4px !important; border: none !important; padding: 8px 18px !important; }
    .section-header { font-size: 16px; font-weight: 700; color: #1E2228; margin-top: 15px; margin-bottom: 10px; border-bottom: 2px solid #E2E8F0; padding-bottom: 5px;}
</style>
"""
st.markdown(AKAMAI_CSS, unsafe_allow_html=True)

# Top Bar
st.markdown("""
<div class="akamai-topbar">
    <div class="akamai-brand"><div><span>a</span>kamai</div></div>
    <div class="akamai-search-box">🔍 Search services, accounts, and more &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; All ⌄</div>
    <div class="akamai-top-right">
        <div class="create-btn">+ Create</div>
        <div>❓</div><div>🛒</div>
        <div>🔔<span class="notification-badge">11</span></div>
        <div>⚠️<span class="notification-badge">17</span></div>
        <div style="text-align: right;"><strong>Nikhil Goyal</strong><br><span style="font-size: 10px; color: #9DA7B3;">AKAMAI TECHNOLOGIES - ASSETS ⌄</span></div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==========================================
# 📂 2. MOCK CUSTOMER ENVIRONMENTS (JSON)
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
# 🧠 3. THE 3-STEP DIAGNOSTIC AI ENGINE
# ==========================================
def run_diagnostic_engine(property_name, raw_json, business_issue):
    issue_lower = business_issue.lower()
    
    # 1. OBSERVATIONS (Factual JSON parsing)
    observations = []
    is_auth = "authentication" in property_name.lower()
    is_api = "api" in property_name.lower()
    
    if is_auth:
        observations.append("The property `is_secure` flag is set to **false**, meaning authentication traffic is currently allowed over unencrypted HTTP.")
        observations.append("The origin hostname is hardcoded to a placeholder (`www.example.com`).")
        observations.append("There are **zero active security behaviors** (no WAF, Bot Management, or Rate Control) attached to this rule tree.")
    elif is_api:
        observations.append("A basic Web Application Firewall (WAF) is active, but specialized `botManagement` behaviors are missing.")
        observations.append("Caching is strictly set to `NO_STORE`, forcing 100% of API requests to hit the origin server.")

    # 2. AGNOSTIC RECOMMENDATIONS (Architectural Advice)
    recommendations = []
    if "bot" in issue_lower or "stuffing" in issue_lower or "scraper" in issue_lower:
        recommendations.append("To stop automated attacks, behavior-based bot mitigation must be implemented at the edge proxy *before* traffic reaches your origin.")
        recommendations.append("Authentication and pricing API endpoints should have dedicated rate-limiting policies applied.")
    if "slow" in issue_lower or "crash" in issue_lower or "performance" in issue_lower:
        recommendations.append("To reduce origin load, consider offloading token validation or dynamic routing logic to serverless edge compute.")
    
    if not recommendations:
        recommendations.append("Enforce strict TLS (HTTPS only) across all endpoints and apply Layer 7 application security controls to filter malicious traffic.")

    # 3. AKAMAI PRODUCT PITCH (The Solution)
    if is_auth:
        product = "Akamai App & API Protector (AAP) + Bot Manager"
        pitch = "AAP bundles Web Application Firewall, Bot Manager, and API Security into a single edge deployment. This instantly protects your login flows from credential stuffing and enforces strict TLS compliance."
        tf_code = """resource "akamai_botman_bot_management_settings" "auth_shield" {
  config_id          = 753664
  target_hostname    = "www.example.com"
  protected_paths    = ["/login", "/oauth/token"]
  execution_mode     = "EXECUTION_MODE_ALWAYS"
}"""
    else:
        product = "Akamai EdgeWorkers + Bot Manager"
        pitch = "By deploying EdgeWorkers, you can intercept API calls and validate tokens at the edge, drastically reducing origin load. Pairing this with Bot Manager will scrub scraper traffic before it impacts performance."
        tf_code = """resource "akamai_edgeworkers" "api_edge_compute" {
  name          = "api_token_validator"
  resource_tier = "200"
}"""

    return observations, recommendations, product, pitch, tf_code


# ==========================================
# 🚀 4. MAIN MARKETPLACE UI LAYOUT
# ==========================================
st.title("Marketplace")
st.caption("Marketplace start / Akamai EdgeIntelligence (EI) Diagnostic Advisor")

col1, col2 = st.columns([1, 1.25])

with col1:
    st.markdown('<div class="akamai-card">', unsafe_allow_html=True)
    st.markdown('<div class="akamai-card-title">1. Scope the Environment</div>', unsafe_allow_html=True)
    
    # Target Selection
    selected_env = st.selectbox("Select Affected Customer Property / Hostname:", list(MOCK_ENVIRONMENTS.keys()))
    
    # Read-only JSON view to prove we are looking at real configs
    with st.expander("View Underlying Property JSON Configuration", expanded=False):
        config_input = st.text_area("PAPI JSON:", value=MOCK_ENVIRONMENTS[selected_env], height=200, disabled=True)
    
    st.markdown('<div class="akamai-card-title" style="margin-top:20px;">2. Business Context</div>', unsafe_allow_html=True)
    
    # Dynamic placeholder based on selection
    placeholder = "e.g., Credential stuffing attacks are locking out real users." if "Auth" in selected_env else "e.g., Flash sales cause our origin to crash due to scrapers."
    issue_input = st.text_area("Describe the operational friction or business issue:", placeholder=placeholder, height=100)
    
    run_scan = st.button("🔍 Run Contextual Audit", type="primary")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if run_scan and issue_input:
        observations, recommendations, product, pitch, tf_code = run_diagnostic_engine(selected_env, MOCK_ENVIRONMENTS[selected_env], issue_input)
        
        st.markdown('<div class="akamai-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="akamai-card-title">Diagnostic Report: <code>{selected_env.split(" ")[0]}</code></div>', unsafe_allow_html=True)
        
        # --- STEP 1: FACTUAL OBSERVATIONS ---
        st.markdown('<div class="section-header">🔍 1. Current State Observations</div>', unsafe_allow_html=True)
        st.info("Based *only* on the provided configuration file, I observed the following:")
        for obs in observations:
            st.write(f"• {obs}")
            
        # --- STEP 2: AGNOSTIC RECOMMENDATIONS ---
        st.markdown('<div class="section-header">🏗️ 2. Architectural Recommendations</div>', unsafe_allow_html=True)
        st.warning(f"To resolve the stated issue: *\"{issue_input}\"*")
        for rec in recommendations:
            st.write(f"• {rec}")
            
        # --- STEP 3: AKAMAI PRODUCT PITCH ---
        st.markdown('<div class="section-header">🚀 3. Recommended Akamai Solution</div>', unsafe_allow_html=True)
        st.success(f"**{product}**")
        st.write(pitch)
        
        st.markdown("**Auto-Generated Staging Fix Blueprint (HCL):**")
        st.code(tf_code, language="hcl")
        
        st.button(f"⚡ Deploy {product.split('+')[0].strip()} to Staging", type="primary")
        st.markdown('</div>', unsafe_allow_html=True)
            
    else:
        st.markdown("""
        <div class="empty-state-box">
            <div class="empty-state-title">Your Marketplace is empty.</div>
            <div class="empty-state-sub">Kindly check <a href="#">Marketplace Control Center (MPCC)</a> for managing your customer's trials/PoCs.</div>
            <br>
            <p style="font-size: 13px; color: #64748B; margin-top: 20px;">👈 Select a target property on the left, describe your business issue, and run the audit.</p>
        </div>
        """, unsafe_allow_html=True)
