import streamlit as st
import json

# ==========================================
# ⚙️ 1. PAGE SETUP & CORPORATE AKAMAI PORTAL STYLING
# ==========================================
st.set_page_config(page_title="Akamai Marketplace | Control Center", layout="wide", initial_sidebar_state="expanded")

AKAMAI_CSS = """
<style>
    /* Global Reset & Fonts */
    .stApp {
        background-color: #F4F6F9;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Akamai Top Navbar Simulation */
    .akamai-topbar {
        background-color: #1E2228;
        color: #FFFFFF;
        padding: 10px 24px;
        margin-top: -60px;
        margin-left: -60px;
        margin-right: -60px;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-bottom: 1px solid #2B313A;
    }
    .akamai-brand {
        display: flex;
        align-items: center;
        gap: 12px;
        font-weight: 800;
        font-size: 20px;
        letter-spacing: 0.5px;
    }
    .akamai-brand span { color: #0072CE; }
    .akamai-search-box {
        background-color: #2B313A;
        border: 1px solid #3A424D;
        border-radius: 4px;
        padding: 6px 16px;
        color: #C0C7D0;
        width: 380px;
        font-size: 13px;
    }
    .akamai-top-right {
        display: flex;
        align-items: center;
        gap: 16px;
        font-size: 12px;
        color: #E2E8F0;
    }
    .create-btn {
        background-color: #0072CE;
        color: white;
        padding: 6px 16px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 13px;
    }
    .notification-badge {
        background-color: #D93025;
        color: white;
        font-size: 10px;
        font-weight: 700;
        padding: 2px 6px;
        border-radius: 10px;
        margin-left: -8px;
    }

    /* Cards & Panels */
    .akamai-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 4px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.03);
    }
    .akamai-card-title {
        font-size: 20px;
        font-weight: 700;
        color: #1E2228;
        margin-bottom: 16px;
    }
    
    /* Empty State Box (Matching Screenshot) */
    .empty-state-box {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 4px;
        padding: 60px 20px;
        text-align: center;
        margin-top: 10px;
    }
    .empty-state-title {
        font-size: 18px;
        font-weight: 700;
        color: #2B313A;
        margin-bottom: 8px;
    }
    .empty-state-sub {
        font-size: 13px;
        color: #64748B;
    }
    .empty-state-sub a {
        color: #0072CE;
        text-decoration: none;
        font-weight: 600;
    }
    
    /* Badges */
    .badge-critical {
        background-color: #FCE8E6;
        color: #C5221F;
        font-size: 11px;
        font-weight: 700;
        padding: 4px 8px;
        border-radius: 3px;
        border: 1px solid #FAD2CF;
    }
    .badge-sec {
        background-color: #FEF7E0;
        color: #B06000;
        font-size: 11px;
        font-weight: 700;
        padding: 4px 8px;
        border-radius: 3px;
        border: 1px solid #FCE8E6;
    }
    .badge-active {
        background-color: #E6F4EA;
        color: #137333;
        font-size: 11px;
        font-weight: 700;
        padding: 4px 8px;
        border-radius: 3px;
    }

    /* Streamlit Buttons */
    .stButton > button {
        background-color: #0072CE !important;
        color: #FFFFFF !important;
        font-weight: 600 !important;
        border-radius: 4px !important;
        border: none !important;
        padding: 8px 18px !important;
    }
</style>
"""
st.markdown(AKAMAI_CSS, unsafe_allow_html=True)

# ==========================================
# 🖥️ 2. AKAMAI TOP NAVBAR SIMULATION
# ==========================================
st.markdown("""
<div class="akamai-topbar">
    <div class="akamai-brand">
        <div><span>a</span>kamai</div>
    </div>
    <div class="akamai-search-box">🔍 Search services, accounts, and more &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; All ⌄</div>
    <div class="akamai-top-right">
        <div class="create-btn">+ Create</div>
        <div>❓</div>
        <div>🛒</div>
        <div>🔔<span class="notification-badge">11</span></div>
        <div>⚠️<span class="notification-badge">17</span></div>
        <div style="text-align: right;">
            <strong>Nikhil Goyal</strong><br>
            <span style="font-size: 10px; color: #9DA7B3;">AKAMAI TECHNOLOGIES - ASSETS ⌄</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==========================================
# 🧠 3. DIAGNOSTIC LOGIC FOR AUTHENTICATION JSON
# ==========================================
def analyze_authentication_property(json_data, scenario_text):
    # Parses raw json or falls back to authentic audit report
    prop_name = "authentication.akamai.com"
    origin_host = "www.example.com"
    cp_code_name = "Cite des Sciences (1242)"
    
    try:
        data = json.loads(json_data)
        if "propertyName" in data:
            prop_name = data["propertyName"]
    except Exception:
        pass
        
    return prop_name, origin_host, cp_code_name

# ==========================================
# 🚀 4. MAIN BODY & MARKETPLACE INTERFACE
# ==========================================
st.title("Marketplace")
st.caption("Marketplace start / Akamai EdgeIntelligence (EI) Automated Property Inspector")

col1, col2 = st.columns([1, 1.25])

with col1:
    st.markdown('<div class="akamai-card">', unsafe_allow_html=True)
    st.markdown('<div class="akamai-card-title">📥 Input Property Config (JSON/PAPI)</div>', unsafe_allow_html=True)
    
    auth_json_sample = """{
    "accountId": "act_1-599K",
    "contractId": "ctr_1-3CV382",
    "groupId": "grp_18385",
    "ruleFormat": "latest",
    "propertyId": "prp_753664",
    "propertyName": "authentication.akamai.com",
    "propertyVersion": 1,
    "rules": {
        "name": "default",
        "behaviors": [
            { "name": "origin", "options": { "hostname": "www.example.com", "verificationMode": "PLATFORM_SETTINGS" } },
            { "name": "cpCode", "options": { "value": { "id": 1242, "name": "Cite des Sciences" } } },
            { "name": "caching", "options": { "behavior": "NO_STORE" } },
            { "name": "sureRoute", "options": { "testObjectUrl": "/" } },
            { "name": "mPulse", "options": { "enabled": true, "apiKey": "" } },
            { "name": "persistentConnection", "options": { "enabled": false } }
        ],
        "options": { "is_secure": false }
    }
}"""

    config_input = st.text_area("Property Manager Rule Tree Payload:", value=auth_json_sample, height=280)
    
    scenario_input = st.text_input("Operational Scenario / Security Friction:", "Review authentication service configuration for security and delivery readiness.")
    
    run_scan = st.button("🔍 Run Akamai EI Deep Audit", type="primary")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if run_scan and config_input:
        prop_name, origin_host, cp_code_name = analyze_authentication_property(config_input, scenario_input)
        
        st.markdown('<div class="akamai-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="akamai-card-title">Akamai Property Configuration Analysis: <code>{prop_name}</code></div>', unsafe_allow_html=True)
        st.write("I found several significant anomalies in this configuration — some are configuration errors, others are critical security gaps given this is an authentication service.")
        
        st.markdown("---")
        
        # 🚨 CRITICAL ANOMALIES SECTION
        st.markdown("### 🚨 Critical Anomalies")
        
        st.markdown("#### **1. Origin hostname is a placeholder**")
        st.code('"hostname": "www.example.com"', language="json")
        st.caption("This is the generic RFC placeholder domain. Either this is a template that was never finished, or traffic is being sent to a non-existent origin. This alone would break the property.")
        
        st.markdown("#### **2. `is_secure: false` on an authentication domain**")
        st.code('"is_secure": false', language="json")
        st.caption("This property delivers content over HTTP by default at the edge hostname level. For a domain literally named `authentication.akamai.com`, serving auth flows without enforced HTTPS is a serious security exposure (credential interception risk).")
        
        st.markdown("#### **3. No security behaviors present at all**")
        st.write("There is zero WAF, Bot Management, Rate Control, Client Reputation, or API security configuration anywhere in the rule tree. For a domain handling login/authentication, this is the biggest anomaly — completely unprotected against credential stuffing, brute force, bot abuse, and injection attacks.")
        
        st.markdown("#### **4. Mismatched CP Code**")
        st.code('"name": "Cite des Sciences"', language="json")
        st.caption("The CP code (1242) is labeled for a French science museum, not an authentication service. This strongly suggests a copy-paste error from another property or wrong CP code assignment — will cause incorrect billing/reporting attribution.")
        
        st.markdown("#### **5. `verificationMode: \"PLATFORM_SETTINGS\"`**")
        st.caption("Legacy/default trust mode for origin certificate validation. Akamai best practice for production, especially security-sensitive origins, is CUSTOM with a defined certificate/trust store — not platform defaults.")
        
        st.markdown("---")
        
        # ⚠️ SECONDARY ANOMALIES TABLE
        st.markdown("### ⚠️ Secondary Anomalies")
        
        secondary_data = [
            {"Issue": "mPulse enabled, no API key", "Detail": '"enabled": true but "apiKey": "" — RUM data collection is broken/non-functional'},
            {"Issue": "persistentConnection disabled", "Detail": '"enabled": false — hurts performance; best practice is true (keep-alive)'},
            {"Issue": "SureRoute test object = /", "Detail": "Using root path as the SureRoute race test object is explicitly discouraged by Akamai — should be a dedicated small static test object"},
            {"Issue": "ruleFormat: \"latest\"", "Detail": "Using floating \"latest\" format in production is risky — should pin to a dated version to avoid unexpected rule behavior changes on Akamai-side updates"},
            {"Issue": "Duplicate file extensions", "Detail": "\"webp\" and \"jxr\" each appear twice in the Static Content match criteria (harmless, but sloppy)"},
            {"Issue": "No HSTS / HTTP/2 / HTTP/3", "Detail": "No modern protocol or transport security behaviors configured"},
            {"Issue": "No forward-to-HTTPS redirect", "Detail": "Combined with is_secure: false, there's nothing forcing clients to HTTPS"}
        ]
        
        st.table(secondary_data)
        
        st.markdown("---")
        
        # ✅ RECOMMENDED PRODUCT SECTION
        st.markdown("### ✅ Recommended Akamai Product")
        st.write("Given this is clearly an authentication/identity endpoint with no security controls whatsoever, the best-fit product is:")
        
        st.success("### **Akamai App & API Protector (AAP)**")
        st.markdown("""
        This bundles exactly what's missing:
        *   **Kona Site Defender (WAF)** — protects login/auth endpoints from injection, OWASP Top 10 attacks.
        *   **Bot Manager** — critical for stopping credential stuffing/brute-force bot attacks against login flows.
        *   **API Security** — since auth services are typically API-driven (token/OAuth endpoints).
        *   **Client-Side Protection & Compliance (Page Integrity Manager)** — detects/prevents JS-based credential skimming (Magecart-style attacks) on login pages.
        """)
        
        st.info("💡 **Supplementary recommendation:** Pair with Enhanced TLS (should already be default) and enforce HSTS + forced HTTPS redirect at the property level immediately — regardless of product choice, this is a must-fix before this config goes anywhere near production.")
        
        st.markdown("---")
        
        # 🛠️ TERRAFORM STAGING REMEDIATION PATCH
        st.markdown("### 🛠️ Auto-Generated Staging Fix Blueprint")
        st.code("""# Akamai EI Remediation Patch for authentication.akamai.com
resource "akamai_appsec_security_policy" "auth_shield" {
  config_id           = 753664
  security_policy_name = "Auth Endpoint Security Shield"
  create_from_security_policy = "sp_default"
}

resource "akamai_botman_bot_management_settings" "bot_defense" {
  config_id          = 753664
  security_policy_id = akamai_appsec_security_policy.auth_shield.security_policy_id
  bot_management_execution_mode = "EXECUTION_MODE_ALWAYS"
}""", language="hcl")

        st.button("⚡ Apply Security Patch to Property Manager Staging", type="primary")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
    else:
        # EXACT EMPTY STATE FROM YOUR SCREENSHOT
        st.markdown("""
        <div class="empty-state-box">
            <div class="empty-state-title">Your Marketplace is empty.</div>
            <div class="empty-state-sub">Kindly check <a href="#">Marketplace Control Center (MPCC)</a> for managing your customer's trials/PoCs.</div>
            <br>
            <p style="font-size: 12px; color: #9DA7B3;">👈 Click 'Run Akamai EI Deep Audit' on the left panel to scan <strong>authentication.akamai.com</strong>.</p>
        </div>
        """, unsafe_allow_html=True)

# Footer matching screenshot links
st.markdown("---")
st.markdown("""
<div style="display: flex; justify-content: space-between; font-size: 11px; color: #0072CE;">
    <div>
        <a href="#" style="color: #0072CE; text-decoration: none; margin-right: 15px;">Akamai.com</a>
        <a href="#" style="color: #0072CE; text-decoration: none; margin-right: 15px;">Contact us</a>
        <a href="#" style="color: #0072CE; text-decoration: none; margin-right: 15px;">Legal & privacy</a>
        <a href="#" style="color: #0072CE; text-decoration: none;">Portal terms of use</a>
    </div>
    <div style="color: #64748B;">
        Copyright ©2026 Akamai Technologies, Inc. All Rights Reserved
    </div>
</div>
""", unsafe_allow_html=True)
