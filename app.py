import streamlit as st
import json

# ==========================================
# ⚙️ 1. PAGE SETUP & CORPORATE STYLING
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
# 🧠 2. DYNAMIC JSON PARSER & ANOMALY ENGINE
# ==========================================
def parse_and_inspect_json(raw_json_str):
    critical_anomalies = []
    secondary_anomalies = []
    detected_behaviors = []
    property_name = "Unknown Property"
    origin_host = "Unknown Host"
    is_secure = None
    
    try:
        data = json.loads(raw_json_str)
    except Exception as e:
        return None, [f"Invalid JSON Format: {str(e)}"], [], [], "Unknown", "Unknown"

    # Extract Metadata
    property_name = data.get("propertyName", "Unassigned Property")
    
    # Traverse Rule Tree Recursively
    def traverse(node):
        nonlocal origin_host, is_secure
        
        if isinstance(node, dict):
            # Check is_secure flag
            if "options" in node and isinstance(node["options"], dict):
                if "is_secure" in node["options"]:
                    is_secure = node["options"]["is_secure"]
                    
            # Check Behaviors
            if "behaviors" in node and isinstance(node["behaviors"], list):
                for b in node["behaviors"]:
                    if isinstance(b, dict) and "name" in b:
                        b_name = b["name"]
                        detected_behaviors.append(b_name)
                        opts = b.get("options", {})
                        
                        # Inspect Origin
                        if b_name == "origin":
                            origin_host = opts.get("hostname", "Not Defined")
                            if "example.com" in origin_host or "localhost" in origin_host:
                                critical_anomalies.append({
                                    "title": "1. Origin hostname is a placeholder",
                                    "code": f'"hostname": "{origin_host}"',
                                    "desc": "This is a generic RFC placeholder domain. Either this is an unfinished template or traffic is being sent to a non-existent origin."
                                })
                            if opts.get("verificationMode") == "PLATFORM_SETTINGS":
                                critical_anomalies.append({
                                    "title": "Origin Certificate Verification Mode is Default",
                                    "code": '"verificationMode": "PLATFORM_SETTINGS"',
                                    "desc": "Legacy/default trust mode for origin cert validation. Akamai best practice for production is CUSTOM with a defined trust store."
                                })
                                
                        # Inspect CP Code
                        if b_name == "cpCode":
                            val = opts.get("value", {})
                            cp_name = val.get("name", "")
                            if "auth" in property_name.lower() and "science" in cp_name.lower():
                                critical_anomalies.append({
                                    "title": "Mismatched CP Code Assignment",
                                    "code": f'"name": "{cp_name}"',
                                    "desc": f"CP code ({val.get('id')}) is labeled '{cp_name}', which does not match the property function ({property_name}). Suggests copy-paste error."
                                })
                                
                        # Inspect mPulse
                        if b_name == "mPulse":
                            if opts.get("enabled") and not opts.get("apiKey"):
                                secondary_anomalies.append({
                                    "Issue": "mPulse enabled without API key",
                                    "Detail": '"enabled": true but "apiKey": "" — RUM data collection is broken/non-functional'
                                })
                                
                        # Inspect Persistent Connection
                        if b_name == "persistentConnection":
                            if opts.get("enabled") is False:
                                secondary_anomalies.append({
                                    "Issue": "persistentConnection disabled",
                                    "Detail": '"enabled": false — hurts performance; best practice is true (keep-alive)'
                                })
                                
                        # Inspect SureRoute
                        if b_name == "sureRoute":
                            if opts.get("testObjectUrl") == "/":
                                secondary_anomalies.append({
                                    "Issue": "SureRoute test object set to root /",
                                    "Detail": "Using root path as test object is explicitly discouraged — should be a dedicated static test object."
                                })

            # Check Criteria for Duplicates
            if "criteria" in node and isinstance(node["criteria"], list):
                for c in node["criteria"]:
                    if isinstance(c, dict) and "options" in c:
                        vals = c["options"].get("values", [])
                        if len(vals) != len(set(vals)):
                            duplicates = list(set([x for x in vals if vals.count(x) > 1]))
                            secondary_anomalies.append({
                                "Issue": "Duplicate entries in criteria match list",
                                "Detail": f"Duplicated values found: {duplicates}"
                            })

            # Check Children Recursively
            if "children" in node and isinstance(node["children"], list):
                for child in node["children"]:
                    traverse(child)
                    
            if "rules" in node:
                traverse(node["rules"])

    traverse(data)
    
    # Check is_secure condition
    if is_secure is False:
        critical_anomalies.append({
            "title": f"is_secure: false on sensitive domain ({property_name})",
            "code": '"is_secure": false',
            "desc": "Delivers content over HTTP by default. Serving authentication or dynamic user flows without enforced HTTPS is a serious security exposure."
        })
        secondary_anomalies.append({
            "Issue": "No forward-to-HTTPS redirect behavior",
            "Detail": "Combined with is_secure: false, nothing forces client connections to HTTPS."
        })

    # Check for Security Behaviors
    sec_behaviors = ["botmanagement", "webapplicationfirewall", "appsec", "ratecontrol"]
    has_security = any(b.lower() in sec_behaviors for b in detected_behaviors)
    
    if not has_security:
        critical_anomalies.append({
            "title": "No security behaviors present in property rule tree",
            "code": "// Missing: botManagement, webApplicationFirewall, rateControl",
            "desc": "Zero WAF, Bot Management, or API security configurations detected. Origin is completely unprotected against credential stuffing, brute force, and layer-7 attacks."
        })

    # Check ruleFormat
    if data.get("ruleFormat") == "latest":
        secondary_anomalies.append({
            "Issue": 'ruleFormat set to floating "latest"',
            "Detail": "Using floating 'latest' in production is risky — pin to a dated version to avoid unexpected Akamai updates."
        })

    return data, critical_anomalies, secondary_anomalies, list(set(detected_behaviors)), property_name, origin_host

# ==========================================
# 🚀 3. MAIN MARKETPLACE UI LAYOUT
# ==========================================
st.title("Marketplace")
st.caption("Marketplace start / Akamai EdgeIntelligence (EI) Dynamic Property Inspector")

col1, col2 = st.columns([1, 1.25])

with col1:
    st.markdown('<div class="akamai-card">', unsafe_allow_html=True)
    st.markdown('<div class="akamai-card-title">📥 Paste Akamai Property JSON</div>', unsafe_allow_html=True)
    
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
        "options": { "is_secure": false },
        "children": [
            {
                "name": "Static Content",
                "criteria": [
                    { "name": "fileExtension", "options": { "values": ["jpg", "png", "webp", "webp"] } }
                ]
            }
        ]
    }
}"""

    config_input = st.text_area("PAPI Rule Tree JSON Input:", value=auth_json_sample, height=320)
    run_scan = st.button("🔍 Run Dynamic JSON Inspection", type="primary")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if run_scan and config_input:
        data, criticals, secondaries, behaviors, prop_name, origin_host = parse_and_inspect_json(config_input)
        
        if data is None:
            st.error("Error parsing JSON string. Please verify JSON formatting.")
        else:
            st.markdown('<div class="akamai-card">', unsafe_allow_html=True)
            st.markdown(f'<div class="akamai-card-title">Akamai Property Analysis: <code>{prop_name}</code></div>', unsafe_allow_html=True)
            st.write(f"Dynamic inspection complete for target origin: **`{origin_host}`**. Detected **{len(criticals)} critical anomalies** and **{len(secondaries)} secondary configuration warnings**.")
            
            st.markdown("---")
            
            # 🚨 CRITICAL ANOMALIES (DYNAMICALLY GENERATED)
            st.markdown("### 🚨 Critical Anomalies")
            if criticals:
                for idx, item in enumerate(criticals, 1):
                    st.markdown(f"#### **{idx}. {item['title']}**")
                    st.code(item['code'], language="json")
                    st.caption(item['desc'])
            else:
                st.success("No critical security or routing anomalies detected.")
                
            st.markdown("---")
            
            # ⚠️ SECONDARY ANOMALIES TABLE (DYNAMICALLY GENERATED)
            st.markdown("### ⚠️ Secondary Anomalies")
            if secondaries:
                st.table(secondaries)
            else:
                st.info("No secondary performance or best-practice warnings found.")
                
            st.markdown("---")
            
            # ✅ DYNAMIC PRODUCT RECOMMENDATION
            st.markdown("### ✅ Recommended Akamai Product")
            
            if "auth" in prop_name.lower() or len(criticals) > 2:
                rec_product = "Akamai App & API Protector (AAP)"
                st.success(f"### **{rec_product}**")
                st.markdown("""
                This bundles exactly what is missing in the analyzed JSON:
                *   **Kona Site Defender (WAF)** — protects origin endpoints from OWASP Top 10 injection attacks.
                *   **Bot Manager** — stops credential stuffing/brute-force attacks.
                *   **API Security** — monitors OAuth / API token endpoints.
                *   **Client-Side Protection** — guards against credential skimming scripts.
                """)
            else:
                rec_product = "Akamai Ion + EdgeWorkers"
                st.success(f"### **{rec_product}**")
                st.write("Recommended to optimize edge delivery performance and offload origin compute.")

            # 🛠️ DYNAMIC TERRAFORM PATCH
            st.markdown("### 🛠️ Auto-Generated Staging Fix Blueprint")
            st.code(f"""# Akamai EI Remediation Blueprint for {prop_name}
resource "akamai_appsec_security_policy" "dynamic_shield" {{
  config_id           = 984120
  security_policy_name = "EI Protection Shield"
  create_from_security_policy = "sp_default"
}}

resource "akamai_botman_bot_management_settings" "bot_defense" {{
  config_id          = 984120
  security_policy_id = akamai_appsec_security_policy.dynamic_shield.security_policy_id
  target_hostname    = "{origin_host}"
  execution_mode     = "EXECUTION_MODE_ALWAYS"
}}""", language="hcl")

            st.button(f"⚡ Provision {rec_product} in Shadow Mode", type="primary")
            st.markdown('</div>', unsafe_allow_html=True)
            
    else:
        st.markdown("""
        <div class="empty-state-box">
            <div class="empty-state-title">Your Marketplace is empty.</div>
            <div class="empty-state-sub">Kindly check <a href="#">Marketplace Control Center (MPCC)</a> for managing your customer's trials/PoCs.</div>
            <br>
            <p style="font-size: 12px; color: #9DA7B3;">👈 Paste any Akamai PAPI JSON on the left and click 'Run Dynamic JSON Inspection' to perform a live scan.</p>
        </div>
        """, unsafe_allow_html=True)
