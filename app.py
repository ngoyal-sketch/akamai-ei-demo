import streamlit as st
import json

# ==========================================
# PAGE SETUP
# ==========================================
st.set_page_config(page_title="Akamai EI | Configuration Intelligence Engine", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #F4F6F9; }
    .akamai-header { background-color: #1E2228; color: white; padding: 14px 24px;
        border-bottom: 3px solid #0072CE; margin: -60px -60px 25px -60px; }
    .akamai-logo { font-weight: 800; font-size: 20px; }
    .akamai-logo span { color: #0072CE; }
    .obs-item { background-color:#F0F7FF; border-left: 4px solid #0072CE; padding: 10px 14px; margin-bottom: 8px; border-radius: 4px; }
    .opt-item { background-color:#FFF8E1; border-left: 4px solid #F59E0B; padding: 10px 14px; margin-bottom: 8px; border-radius: 4px; }
    .rec-item { background-color:#E8F5E9; border-left: 4px solid #2E7D32; padding: 10px 14px; margin-bottom: 8px; border-radius: 4px; }
</style>
<div class="akamai-header"><span class="akamai-logo"><span>a</span>kamai | EdgeIntelligence (EI)</span></div>
""", unsafe_allow_html=True)

st.title("🛡️ Akamai EI — Configuration Intelligence Engine")
st.caption("Upload or paste a Property Manager JSON. Get observations, optimization tips, and product recommendations.")

# ==========================================
# FRIENDLY NAME MAP
# ==========================================
FRIENDLY_NAMES = {
    "origin": "Origin Server Routing",
    "caching": "Caching Policy",
    "gzip_response": "Gzip Compression",
    "http2": "HTTP/2 Prioritization",
    "sureroute": "SureRoute Performance Optimization",
    "adaptiveacceleration": "Adaptive Acceleration",
    "prefetchable": "Prefetching",
    "allowpost": "POST Method Handling",
    "cpcode": "CP Code Reporting",
    "botmanagement": "Bot Management Hook",
    "webapplicationfirewall": "WAF Routing Hook",
    "edgeworkers": "EdgeWorkers Execution",
    "imagemanager": "Image & Video Manager",
    "redirect": "Redirect Rules",
    "corssupport": "CORS Support",
    "mpulse": "mPulse Real User Monitoring",
    "datastream2": "DataStream 2 Log Delivery",
    "ratecontrol": "Rate Controls",
    "hsts": "HSTS Enforcement",
    "tieredistribution": "Tiered Distribution",
    "sitefailover": "Origin Failover Handling",
}

def friendly(name):
    key = str(name).lower().replace("_", "").replace("-", "")
    for k, v in FRIENDLY_NAMES.items():
        if k.replace("_", "") == key:
            return v
    return str(name).replace("_", " ").title()

# ==========================================
# RECURSIVE JSON WALKER
# ==========================================
def walk_tree(node, behaviors, hostnames, all_behavior_objs):
    if isinstance(node, dict):
        if "behaviors" in node and isinstance(node["behaviors"], list):
            for b in node["behaviors"]:
                if isinstance(b, dict) and "name" in b:
                    bname = b["name"].lower()
                    behaviors.add(bname)
                    all_behavior_objs.append(b)
                    if bname == "origin" and isinstance(b.get("options"), dict):
                        h = b["options"].get("hostname")
                        if h:
                            hostnames.add(h)
        if "children" in node and isinstance(node["children"], list):
            for child in node["children"]:
                walk_tree(child, behaviors, hostnames, all_behavior_objs)
        if "rules" in node:
            walk_tree(node["rules"], behaviors, hostnames, all_behavior_objs)

def safe_parse(raw_text):
    behaviors, hostnames, objs = set(), set(), []
    valid = False
    try:
        data = json.loads(raw_text)
        valid = True
        walk_tree(data, behaviors, hostnames, objs)
    except Exception:
        valid = False
        low = raw_text.lower()
        for key in FRIENDLY_NAMES.keys():
            if key in low:
                behaviors.add(key)
    return valid, behaviors, hostnames, objs

# ==========================================
# ANALYSIS ENGINE
# ==========================================
def analyze(behaviors, hostnames, objs):
    observations = []
    optimizations = []
    recommendations = []

    host = list(hostnames)[0] if hostnames else "your-origin.example.com"
    observations.append(f"Detected origin hostname: **{host}**")
    observations.append(f"Total distinct behaviors detected: **{len(behaviors)}**")

    # ---- Caching checks ----
    caching_obj = next((b for b in objs if b.get("name","").lower() == "caching"), None)
    if caching_obj:
        behavior_val = str(caching_obj.get("options", {}).get("behavior", "")).upper()
        observations.append(f"Caching behavior set to: **{behavior_val or 'UNSET'}**")
        if behavior_val == "NO_STORE":
            optimizations.append("Caching is set to NO_STORE — every request hits your origin. Consider MAX_AGE caching for static/API-cacheable routes to reduce origin load.")
    else:
        optimizations.append("No explicit caching behavior found — define a caching policy instead of relying on defaults.")

    # ---- Compression ----
    if "gzip_response" not in behaviors and "gzip" not in behaviors:
        optimizations.append("Gzip/Brotli compression not detected — enabling compression can reduce payload size and improve load times.")
    else:
        observations.append("Compression (Gzip) is active.")

    # ---- HTTP/2 ----
    if "http2" not in behaviors:
        optimizations.append("HTTP/2 not explicitly detected — enabling it can improve multiplexed request performance.")
    else:
        observations.append("HTTP/2 prioritization is active.")

    # ---- Bot Management ----
    if "botmanagement" not in behaviors:
        recommendations.append({
            "product": "Akamai Bot Manager",
            "reason": "No Bot Management hook found in delivery config. Origin is exposed to scraper/credential-stuffing traffic with no edge-level scrubbing.",
            "terraform": f"""resource "akamai_botman_bot_management_settings" "ei_patch" {{
  config_id       = 984120
  target_hostname = "{host}"
  execution_mode  = "EXECUTION_MODE_ALWAYS"
}}"""
        })
    else:
        observations.append("Bot Management hook is present in delivery config.")

    # ---- WAF ----
    if "webapplicationfirewall" not in behaviors:
        recommendations.append({
            "product": "Akamai App & API Protector (WAAP)",
            "reason": "No WAF routing hook detected — Layer 7 attack surface (SQLi, XSS, DDoS) is not covered at the edge.",
            "terraform": """resource "akamai_appsec_configuration" "ei_waap" {
  mode = "PARALLEL_EVALUATION"
}"""
        })

    # ---- EdgeWorkers ----
    if "edgeworkers" not in behaviors:
        recommendations.append({
            "product": "Akamai EdgeWorkers",
            "reason": "No serverless edge logic detected — personalization/routing logic likely round-trips to origin, adding latency.",
            "terraform": f"""resource "akamai_edgeworkers" "ei_edge_node" {{
  name          = "edge_logic_{host.replace('.', '_')}"
  resource_tier = "200"
}}"""
        })
    else:
        observations.append("EdgeWorkers execution detected — edge compute logic is active.")

    # ---- Rate Controls ----
    if "ratecontrol" not in behaviors:
        optimizations.append("No rate control behavior detected — consider adding rate limiting on sensitive endpoints (login, checkout, search).")

    # ---- HSTS ----
    if "hsts" not in behaviors:
        optimizations.append("HSTS not detected — enforcing HSTS improves TLS security posture.")

    return observations, optimizations, recommendations, host

# ==========================================
# UI LAYOUT
# ==========================================
col1, col2 = st.columns([1, 1.3])

with col1:
    st.subheader("1️⃣ Provide Configuration")
    input_mode = st.radio("Input method:", ["Paste JSON", "Upload JSON file"], horizontal=True)

    sample_json = """{
  "rules": {
    "name": "default",
    "behaviors": [
      { "name": "origin", "options": { "hostname": "api.retailstore.com" } },
      { "name": "caching", "options": { "behavior": "NO_STORE" } }
    ],
    "children": [
      {
        "name": "API Rules",
        "behaviors": [
          { "name": "gzip_response", "options": { "behavior": "ALWAYS" } }
        ]
      }
    ]
  }
}"""

    raw_text = ""
    if input_mode == "Paste JSON":
        raw_text = st.text_area("Paste your Property JSON:", value=sample_json, height=300)
    else:
        uploaded = st.file_uploader("Upload .json file", type=["json"])
        if uploaded is not None:
            raw_text = uploaded.read().decode("utf-8")
        else:
            st
