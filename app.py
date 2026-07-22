import streamlit as st
import json
import io

# ==========================================
# ⚙️ 1. PAGE SETUP & STYLING
# ==========================================
st.set_page_config(page_title="Akamai EI | Configuration Intelligence Engine", layout="wide", initial_sidebar_state="expanded")

AKAMAI_CSS = """
<style>
    .stApp { background-color: #F4F6F9; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
    .akamai-header { background-color: #1E2228; color: #FFFFFF; padding: 14px 24px; border-bottom: 2px solid #0072CE; margin-top: -60px; margin-left: -60px; margin-right: -60px; margin-bottom: 25px; display: flex; justify-content: space-between; align-items:center; }
    .akamai-logo { font-weight: 800; font-size: 20px; color: #FFFFFF; }
    .akamai-logo span { color: #0072CE; }
    .akamai-card { background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 20px; margin-bottom: 16px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
    .akamai-card-header { font-size: 16px; font-weight: 700; color: #1E2228; margin-bottom: 10px; border-bottom: 1px solid #EEE; padding-bottom: 8px;}
    .stButton > button { background-color: #0072CE !important; color: #FFFFFF !important; font-weight: 600 !important; border-radius: 5px !important;}
    .feature-pill { display:inline-block; background-color:#0072CE; color:white; padding:5px 12px; border-radius:14px; font-size:12px; margin:4px 4px 4px 0; }
    .obs-item { background-color:#F8FAFC; border-left: 3px solid #0072CE; padding: 10px 14px; margin-bottom: 8px; border-radius: 4px; font-size: 14px;}
    .opt-item { background-color:#FFF8E1; border-left: 3px solid #F59E0B; padding: 10px 14px; margin-bottom: 8px; border-radius: 4px; font-size: 14px;}
    .rec-item { background-color:#E8F5E9; border-left: 3px solid #2E7D32; padding: 10px 14px; margin-bottom: 8px; border-radius: 4px; font-size: 14px;}
    .sev-high { color:#C62828; font-weight:700; }
    .sev-med { color:#B06000; font-weight:700; }
    .sev-low { color:#2E7D32; font-weight:700; }
</style>
"""
st.markdown(AKAMAI_CSS, unsafe_allow_html=True)

# ==========================================
# 🧠 2. BEHAVIOR / CRITERIA NAME NORMALIZER
# ==========================================
FRIENDLY_NAMES = {
    "origin": "Origin Server Routing",
    "caching": "Caching Policy",
    "gzip_response": "Gzip Compression",
    "gzipresponse": "Gzip Compression",
    "http2": "HTTP/2 Prioritization",
    "sureroute": "SureRoute Performance Optimization",
    "adaptiveacceleration": "Adaptive Acceleration",
    "prefetch": "Prefetching",
    "prefetchable": "Prefetching",
    "tls": "TLS/SSL Enforcement",
    "allowpost": "POST Method Handling",
    "cpcode": "CP Code Reporting",
    "botmanagement": "Bot Management Hook",
    "bot_management": "Bot Management Hook",
    "webapplicationfirewall": "WAF Routing Hook",
    "edgeworkers": "EdgeWorkers Execution",
    "imagemanager": "Image & Video Manager",
    "redirect": "Redirect Rules",
    "redirectplus": "Redirect Rules",
    "modifyoutgoingrequestheader": "Custom Request Headers",
    "modifyoutgoingresponseheader": "Custom Response Headers",
    "corssupport": "CORS Support",
    "allowedmethods": "Allowed HTTP Methods",
    "rapid": "Rapid Blue/Green Deployment",
    "mpulse": "mPulse Real User Monitoring",
    "datastream2": "DataStream 2 Log Delivery",
    "clientreputation": "Client Reputation / Rate Controls",
    "ratecontrol": "Rate Controls",
    "mtls": "Mutual TLS",
    "http_strict_transport_security": "HSTS Enforcement",
    "hsts": "HSTS Enforcement",
    "downstreamcache": "Downstream Cache Control",
    "tieredDistribution".lower(): "Tiered Distribution",
    "failaction": "Origin Failover Handling",
    "sitefailover": "Origin Failover Handling",
    "cachekeyqueryparams": "Cache Key Query Param Handling",
}

def friendly(name):
    key = str(name).lower().replace(" ", "").replace("-", "").replace("_", "")
    for k, v in FRIENDLY_NAMES.items():
        if k.replace("_", "").replace("-", "") == key:
            return v
    return str(name).replace
