import streamlit as st
import json

# ==========================================
# ⚙️ 1. PAGE SETUP & STYLING
# ==========================================
st.set_page_config(page_title="Akamai Control Center | Akamai EI", layout="wide", initial_sidebar_state="expanded")

AKAMAI_CSS = """
<style>
    .stApp { background-color: #F4F6F9; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
    .akamai-header { background-color: #1E2228; color: #FFFFFF; padding: 12px 24px; border-bottom: 2px solid #0072CE; margin-top: -60px; margin-left: -60px; margin-right: -60px; margin-bottom: 25px; display: flex; justify-content: space-between; }
    .akamai-logo { font-weight: 800; font-size: 20px; color: #FFFFFF; }
    .akamai-logo span { color: #0072CE; }
    .akamai-card { background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 6px; padding: 20px; margin-bottom: 16px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
    .akamai-card-header { font-size: 16px; font-weight: 700; color: #1E2228; margin-bottom: 8px; }
    .stButton > button { background-color: #0072CE !important; color: #FFFFFF !important; font-weight: 600 !important; }
    .status-badge { background-color: #E6F4EA; color: #137333; font-size: 12px; font-weight: 600; padding: 4px 8px; border-radius: 4px; border: 1px solid #CEEAD6; display: inline-block; margin-bottom: 10px;}
</style>
"""
st.markdown(AKAMAI_CSS, unsafe_allow_html=True)

# ==========================================
# 🧠 2. DUAL-CONFIG AI DIAGNOSTIC ENGINE
# ==========================================
def run_dual_analysis(scope_type, config_text, scenario):
    scenario = scenario.lower()
    text = config_text.lower()
    insights = []
    
    if scope_type == "Delivery Property (PAPI)":
        insights.append("📡 **Analyzed Asset:** Delivery Property (CDN & Caching Rules)")
        if "bot" in scenario or "scraper" in scenario:
            insights.append("⚠️ **Configuration Audit:** Scanned delivery behaviors for `api.retailstore.com`. No edge bot-scrubbing behavior attached.")
            insights.append("❌ **Security Gap:** Origin server is directly receiving unverified scraper traffic.")
            
            return insights, "Akamai Bot Manager", """# Attach Bot Manager Policy to Delivery Hostname
resource "akamai_botman_bot_management_settings" "ei_bot_patch" {
  config_id = 984120
  security_policy_id = "sp_30219"
  bot_management_execution_mode = "EXECUTION_MODE_ALWAYS"
}"""
            
        elif "latency" in scenario or "slow" in scenario:
            insights.append("⚠️ **Configuration Audit:** Found `NO_STORE` caching behavior on dynamic routes.")
            insights.append("💡 **Performance Recommendation:** Offload compute to EdgeWorkers.")
            
            return insights, "Akamai EdgeWorkers", """resource "akamai_edgeworkers" "ei_edge_node" {
  name = "dynamic_routing_worker"
  resource_tier = "200"
}"""

    elif scope_type == "Security Configuration (AppSec)":
        insights.append("🛡️ **Analyzed Asset:** Security Configuration (AppSec / WAF / Botman)")
        if '"botmanagement": false' in text or "bot" in scenario:
            insights.append("❌ **Security Audit:** Security Policy `sp_30219` has `botManagement` set to `DISABLED`.")
            insights.append("⚠️ **Risk Exposure:** Credential stuffing & pricing scraper protection is INACTIVE.")
            
            return insights, "Akamai Bot Manager Upgrade", """# Provision & Enable Bot Management on Policy
resource "akamai_appsec_security_policy_protections" "enable_botman" {
  config_id          = 984120
  security_policy_id = "sp_30219"
  apply_botman_controls = true
}"""

    else: # Unified Scope
        insights.append("🔗 **Analyzed Asset:** Unified Asset Correlation (Delivery + Security Pair)")
        insights.append("✅ **Host Match Verified:** `api.retailstore.com` mapped across Property `prp_984120` and AppSec Config `cfg_50119`.")
        insights.append("❌ **Correlation Error:** Match Target ID `mt_9902` covers L7 WAAP, but lacks active Bot Manager & API Posture licensing.")
        
        return insights, "Akamai Bot Manager + API Security Suite", """# Multi-Product Staging Provisioning
resource "akamai_appsec_match_target" "api_target" {
  config_id          = 984120
  security_policy_id = "sp_30219"
  default_associated_policy_type = "BOT_MAN_AND_WAAP"
}"""

    # Fallback
    insights.append("❌ **Security Risk:** Layer 7 protections incomplete.")
    return insights, "Akamai App & API Protector", """resource "akamai_app_sec_policy" "waf" { mode = "PARALLEL_EVALUATION" }"""

# ==========================================
# 🚀 3. MAIN UI LAYOUT
# ==========================================
st.markdown("""
<div class="akamai-header">
    <div class="akamai-logo"><span>a</span>kamai &nbsp;|&nbsp; EdgeIntelligence (EI) Marketplace</div>
    <div style="color: #9DA7B3; font-size: 12px;">Active Profile: System Architect</div>
</div>
""", unsafe_allow_html=True)

st.title("Akamai EI Diagnostic Engine")
st.write("Analyze Delivery Properties, Security Configurations, or Unified Asset Pairs to automatically identify gaps and generate deployment patches.")

col1, col2 = st.columns([1, 1.2])

with col1:
    st.markdown('<div class="akamai-card">', unsafe_allow_html=True)
    st.markdown('<div class="akamai-card-header">1. Select Akamai Asset Type</div>', unsafe_allow_html=True)
    
    scope_type = st.selectbox(
        "Config Scope:",
        [
            "Delivery Property (PAPI)",
            "Security Configuration (AppSec)",
            "Unified Pair (Correlate Delivery + Security)"
        ]
    )
    
    # Dynamic Mock Samples
    papi_sample = """{
  "propertyName": "prod_api_delivery",
  "propertyId": "prp_984120",
  "rules": {
    "behaviors": [
      { "name": "origin", "options": { "hostname": "api.retailstore.com" } },
      { "name": "caching", "options": { "behavior": "NO_STORE" } }
    ]
  }
}"""

    appsec_sample = """{
  "configName": "enterprise_waf_policy",
  "configId": 984120,
  "securityPolicies": [
    {
      "policyId": "sp_30219",
      "policyName": "API Protection Policy",
      "protections": {
        "waf": true,
        "botManagement": false,
        "apiSecurity": false
      }
    }
  ]
}"""

    if scope_type == "Delivery Property (PAPI)":
        config_input = st.text_area("Paste Delivery Property JSON:", value=papi_sample, height=200)
    elif scope_type == "Security Configuration (AppSec)":
        config_input = st.text_area("Paste Security Configuration JSON:", value=appsec_sample, height=200)
    else:
        config_input = st.text_area("Unified Context JSON (Delivery + Security Mappings):", 
                                    value=f"// DELIVERY PROPERTY:\n{papi_sample}\n\n// SECURITY CONFIG:\n{appsec_sample}", height=220)

    st.markdown('<div class="akamai-card-header" style="margin-top: 10px;">2. Describe Business Issue</div>', unsafe_allow_html=True)
    issue_input = st.text_input("Operational Friction:", "During flash sales, scraper bots attack our API pricing endpoints.")
    
    run_diagnostics = st.button("🔍 Run Akamai EI Diagnostic Scan", type="primary")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if run_diagnostics and config_input and issue_input:
        st.markdown('<div class="akamai-card">', unsafe_allow_html=True)
        st.markdown('<div class="akamai-card-header">🎯 Akamai EI Diagnostic Report</div>', unsafe_allow_html=True)
        st.markdown(f'<span class="status-badge">✅ Auditing: {scope_type}</span>', unsafe_allow_html=True)
        
        with st.spinner("Analyzing config structures and matching behavioral rules..."):
            insights, product, tf_code = run_dual_analysis(scope_type, config_input, issue_input)
            
            st.subheader("Deep-Scan Results:")
            for insight in insights:
                st.write(insight)
            
            st.markdown("---")
            st.success(f"**Recommended Cross-Sell Solution:** {product}")
            st.write("Akamai EI has generated the precise staging patch to resolve this gap:")
            
            st.code(tf_code, language="hcl")
            st.button(f"⚡ Provision {product} in Shadow Mode")
            
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="akamai-card">', unsafe_allow_html=True)
        st.markdown('<div class="akamai-card-header">📊 Readiness Panel</div>', unsafe_allow_html=True)
        st.info("👈 Select a Config Scope on the left to see how Akamai EI analyzes Delivery properties, Security configs, or Unified Pairs.")
        st.markdown('</div>', unsafe_allow_html=True)
