def run_track_1_analysis(raw_json, business_issue):
    """Deep-Insight Mode: Scans the JSON Config."""
    try:
        data = json.loads(raw_json)
    except Exception:
        return ["Invalid JSON format provided."], ["Please ensure valid configuration data."], "N/A", "N/A", ""

    prop_name = data.get("propertyName", "Custom Property")
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
    observations = [f"Analyzed configuration for **{prop_name}** routing to origin `{origin_host}`."]
    if not is_secure: observations.append("The `is_secure` flag is set to false, permitting unencrypted HTTP edge traffic.")
    if "botmanagement" not in behaviors: observations.append("There are zero active Layer-7 Bot Management behaviors attached to this rule tree.")
    
    recommendations = []
    # NEW LOGIC: Handling Bot/Scraper specific issues
    if any(keyword in issue_lower for keyword in ["bot", "scraper", "stuffing"]) or "auth" in prop_name.lower():
        recommendations.append("Implement behavior-based bot mitigation at the edge proxy to filter automated threats before origin impact.")
    # NEW LOGIC: Handling DDoS/Security specific attacks
    elif any(keyword in issue_lower for keyword in ["ddos", "attack", "security", "waf", "hack"]):
        recommendations.append("Deploy robust Layer-7 Web Application Firewall and volumetric DDoS mitigation to absorb attacks at the edge.")
    # Handling Performance issues
    if "slow" in issue_lower or "performance" in issue_lower or "offload" in issue_lower:
        recommendations.append("Offload dynamic routing logic or token validation to serverless edge compute to reduce origin latency.")
    if not recommendations:
        recommendations.append("Apply Layer-7 application security controls and optimize edge delivery caching rules.")

    product, pitch, tf_code = generate_pitch_and_code(issue_lower, origin_host, prop_name)
    return observations, recommendations, product, pitch, tf_code


def generate_pitch_and_code(issue_lower, target_host, prop_name):
    """Generates the Pillar C 90% Pre-Configured Artifact."""
    
    # 1. BOT & SCRAPER USE CASES
    if any(keyword in issue_lower for keyword in ["bot", "scraper", "stuffing"]) or "auth" in prop_name.lower():
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

    # 2. DDOS & WAF USE CASES
    elif any(keyword in issue_lower for keyword in ["ddos", "attack", "security", "waf"]):
        product = "Akamai App & API Protector (AAP)"
        pitch = "AAP provides industry-leading Web Application Firewall and DDoS protection, instantly absorbing volumetric attacks and blocking malicious requests at the edge before they can overwhelm your origin servers."
        tf_code = f"""# 90% Pre-Configured Trial Blueprint (Pillar C)
# Mode: Shadow / Monitor-Only (Zero Production Impact)
resource "akamai_appsec_security_policy" "ei_trial_ddos_shield" {{
  config_id           = "auto_detected_config"
  security_policy_name = "EI DDoS and WAF Shield"
  create_from_security_policy = "sp_default"
}}"""

    # 3. PERFORMANCE & LATENCY USE CASES (Default)
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
