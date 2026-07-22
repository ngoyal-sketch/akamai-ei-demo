import streamlit as st
import json

st.set_page_config(page_title="Akamai EI | Configuration Intelligence Engine", layout="wide")

# ==========================================
# AKAMAI CONTROL CENTER HEADER (matches screenshot 2)
# ==========================================
st.markdown("""
<style>
    .stApp { background-color: #F4F6F9; }
    .akamai-topbar {
        background-color: #000000;
        margin: -60px -60px 0 -60px;
        padding: 14px 30px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .akamai-left { display: flex; align-items: center; gap: 14px; }
    .akamai-grid-icon {
        display: inline-grid;
        grid-template-columns: 8px 8px;
        gap: 3px;
    }
    .akamai-grid-icon div { width: 8px; height: 8px; background-color: #0072CE; border-radius: 2px; }
    .akamai-wordmark { color: white; font-size: 18px; font-weight: 700; letter-spacing: 0.3px; }
    .akamai-search {
        background-color: #1E1E1E;
        color: #999;
        padding: 8px 16px;
        border-radius: 4px;
        font-size: 13px;
        width: 320px;
    }
    .akamai-create-btn {
        background-color: #0072CE;
        color: white;
        padding: 7px 16px;
        border-radius: 4px;
        font-size: 13px;
        font-weight: 600;
    }
    .akamai-user { color: white; font-size: 12px; text-align: right; line-height: 1.3; }
    .akamai-pagehead {
        margin: 0 -60px 25px -60px;
        padding: 24px 30px 0 30px;
    }
    .akamai-pagehead h1 { font-size: 30px; font-weight: 800; color: #1A1A1A; margin-bottom: 4px; }
    .akamai-pagehead p { color: #5F6B7A; font-size: 14px; }

    .akamai-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 22px;
        margin-bottom: 18px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.06);
    }
    .akamai-card h3 { color: #1A1A1A; font-size: 15px; font-weight: 700; margin-bottom: 12px; border-bottom: 1px solid #EEE; padding-bottom: 8px;}

    .obs-item { background-color:#F0F7FF; border-left: 4px solid #0072CE; padding: 10px 14px; margin-bottom: 8px; border-radius: 4px; color:#1A1A1A; font-size: 14px;}
    .opt-item { background-color:#FFF8E1; border-left: 4px solid #F59E0B; padding: 10px 14px; margin-bottom: 8px; border-radius: 4px; color:#1A1A1A; font-size: 14px;}
    .rec-item { background-color:#E8F5E9; border-left: 4px solid #2E7D32; pad
