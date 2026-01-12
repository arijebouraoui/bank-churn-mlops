# app_streamlit.py
import streamlit as st
import requests
import json
import plotly.graph_objects as go
import os

# Configuration - Read from environment variables
USE_AZURE = os.getenv("USE_AZURE", "True").lower() == "true"

if USE_AZURE:
    API_URL = os.getenv("API_URL", "https://bank-churn.victoriousmoss-65485a03.francecentral.azurecontainerapps.io")
else:
    API_URL = os.getenv("API_URL", "http://localhost:8000")

# Page config
st.set_page_config(
    page_title="Bank Churn Prediction v2 - Enhanced Azure",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        height: 3rem;
        border-radius: 0.5rem;
        font-size: 1.2rem;
        font-weight: bold;
        border: none;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #FF6B6B;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(255, 75, 75, 0.3);
    }
    h1 {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: 800;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================
# BANNER ÉNORME AZURE DEPLOYMENT V2
# ============================================================
st.markdown("""
    <div style='
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 15px;
        margin-bottom: 30px;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        border: 3px solid #FFD700;
    '>
        <h1 style='color: white; margin: 0; font-size: 2.5em; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);'>
            ☁️ AZURE CLOUD PRODUCTION DEPLOYMENT v2.0
        </h1>
        <p style='color: white; margin: 15px 0 10px 0; font-size: 1.3em; font-weight: bold;'>
            🌐 Backend API: Deployed on Microsoft Azure Container Apps
        </p>
        <p style='color: #FFD700; margin: 10px 0; font-size: 1.1em; font-weight: bold;'>
            📍 Region: France Central | Status: Live & Operational | Version: 2.0 🆕
        </p>
        <div style='
            background: rgba(255,255,255,0.2);
            padding: 15px;
            border-radius: 10px;
            margin-top: 15px;
        '>
            <p style='color: white; margin: 0; font-size: 0.95em; font-family: monospace;'>
                Production URL: https://bank-churn.victoriousmoss-65485a03.francecentral.azurecontainerapps.io
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Test de connectivité Azure en temps réel
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🌐 Azure Connection")
    with st.spinner("Testing..."):
        try:
            response = requests.get(f"{API_URL}/health", timeout=5)
            if response.status_code == 200:
                st.success("✅ **CONNECTED**")
                st.caption("Azure API is online")
            else:
                st.warning(f"⚠️ Status: {response.status_code}")
        except:
            st.error("❌ Connection failed")

with col2:
    st.markdown("### ⚡ Response Time")
    try:
        import time
        start = time.time()
        requests.get(f"{API_URL}/health", timeout=5)
        elapsed = (time.time() - start) * 1000
        st.info(f"**{elapsed:.0f} ms**")
        st.caption("Azure latency")
    except:
        st.error("N/A")

with col3:
    st.markdown("### 🚀 Environment")
    st.success("**☁️ AZURE CLOUD v2.0**")
    st.caption("Production mode")

st.markdown("---")

# Header
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<h1>🏦 Bank Churn Predictor v2.0</h1>", unsafe_allow_html=True)
    st.markdown("### Predict customer churn risk with AI-powered analytics")

st.markdown("---")

# Sidebar
with st.sidebar:
    st.markdown("## ☁️ Azure Deployment Info")
    st.info(f"""
    **🌐 Environment:** Azure Cloud
    
    **📍 Region:** France Central
    
    **🔗 API Endpoint:**
    {API_URL}
    
    **✅ Status:** Production
    
    **🤖 Model:** Random Forest v2
    
    **📊 Accuracy:** 85%+
    
    **🆕 Version:** 2.0 Enhanced
    """)
    
    st.markdown("---")
    st.markdown("## 🔗 Quick Links")
    st.markdown("- [Azure API Docs](https://bank-churn.victoriousmoss-65485a03.francecentral.azurecontainerapps.io/docs)")
    st.markdown("- [GitHub Repo](https://github.com/arijebouraoui/bank-churn-mlops)")
    st.markdown("- [Azure Portal](https://portal.azure.com)")

# Main content
tab1, tab2, tab3 = st.tabs(["🎯 Prediction", "📈 Batch Analysis", "ℹ️ About"])

with tab1:
    st.markdown("### Customer Information")
    
    # Input fields in columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 👤 Personal Details")
        age = st.slider("Age", 18, 100, 40)
        tenure = st.slider("Tenure (years)", 0, 15, 5)
        geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
        
    with col2:
        st.markdown("#### 💳 Financial Info")
        credit_score = st.slider("Credit Score", 300, 850, 650)
        balance = st.number_input("Account Balance ($)", 0, 300000, 60000, step=1000)
        estimated_salary = st.number_input("Estimated Salary ($)", 0, 200000, 50000, step=1000)
        
    with col3:
        st.markdown("#### 🏦 Banking Details")
        num_products = st.selectbox("Number of Products", [1, 2, 3, 4])
        has_cr_card = st.radio("Has Credit Card?", ["Yes", "No"], horizontal=True)
        is_active_member = st.radio("Active Member?", ["Yes", "No"], horizontal=True)
    
    st.markdown("---")
    
    # Convert inputs
    has_cr_card = 1 if has_cr_card == "Yes" else 0
    is_active_member = 1 if is_active_member == "Yes" else 0
    geography_germany = 1 if geography == "Germany" else 0
    geography_spain = 1 if geography == "Spain" else 0
    
    # Prediction button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        predict_button = st.button("🔮 PREDICT CHURN RISK (Azure API v2)", use_container_width=True)
    
    if predict_button:
        payload = {
            "CreditScore": credit_score,
            "Age": age,
            "Tenure": tenure,
            "Balance": balance,
            "NumOfProducts": num_products,
            "HasCrCard": has_cr_card,
            "IsActiveMember": is_active_member,
            "EstimatedSalary": estimated_salary,
            "Geography_Germany": geography_germany,
            "Geography_Spain": geography_spain
        }
        
        # API call
        predict_url = f"{API_URL}/predict"
        
        with st.spinner("☁️ Sending request to Azure Container Apps..."):
            try:
                response = requests.post(predict_url, json=payload, timeout=10)
                
                if response.status_code == 200:
                    result = response.json()
                    
                    # Success banner
                    st.success("✅ Prediction received from Azure Cloud v2.0!")
                    
                    # Display results
                    st.markdown("### 📊 Prediction Results")
                    
                    # Metrics
                    col1, col2, col3 = st.columns(3)
                    
                    churn_prob = result.get("churn_probability", 0)
                    prediction = result.get("prediction", 0)
                    
                    # Calculate risk level
                    if churn_prob < 0.3:
                        risk_level = "Low"
                    elif churn_prob < 0.7:
                        risk_level = "Medium"
                    else:
                        risk_level = "High"
                    
                    with col1:
                        st.metric("Churn Probability", f"{churn_prob * 100:.2f}%")
                    
                    with col2:
                        status = "⚠️ WILL CHURN" if prediction == 1 else "✅ WILL STAY"
                        st.metric("Prediction", status)
                    
                    with col3:
                        risk_color = {"Low": "🟢", "Medium": "🟡", "High": "🔴"}
                        st.metric("Risk Level", f"{risk_color.get(risk_level, '⚪')} {risk_level}")
                    
                    # Gauge chart
                    fig = go.Figure(go.Indicator(
                        mode="gauge+number+delta",
                        value=churn_prob * 100,
                        domain={'x': [0, 1], 'y': [0, 1]},
                        title={'text': "Churn Risk Score", 'font': {'size': 24}},
                        delta={'reference': 50, 'increasing': {'color': "red"}},
                        gauge={
                            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
                            'bar': {'color': "darkblue"},
                            'bgcolor': "white",
                            'borderwidth': 2,
                            'bordercolor': "gray",
                            'steps': [
                                {'range': [0, 30], 'color': '#90EE90'},
                                {'range': [30, 70], 'color': '#FFD700'},
                                {'range': [70, 100], 'color': '#FF6B6B'}
                            ],
                            'threshold': {
                                'line': {'color': "red", 'width': 4},
                                'thickness': 0.75,
                                'value': 90
                            }
                        }
                    ))
                    
                    fig.update_layout(height=400, margin=dict(l=20, r=20, t=50, b=20))
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Recommendations
                    st.markdown("### 💡 Recommendations")
                    if risk_level == "High":
                        st.error("""
                        **High Risk Customer** 🔴
                        - ⚡ Immediate retention strategy required
                        - 🎁 Offer personalized incentives
                        - 📞 Schedule customer service call
                        - 💰 Consider special offers or discounts
                        """)
                    elif risk_level == "Medium":
                        st.warning("""
                        **Medium Risk Customer** 🟡
                        - 👀 Monitor account activity closely
                        - 📧 Send targeted engagement campaigns
                        - 🎉 Offer loyalty rewards
                        - 📊 Review service quality
                        """)
                    else:
                        st.success("""
                        **Low Risk Customer** 🟢
                        - ✅ Continue standard service
                        - 📋 Maintain satisfaction surveys
                        - 🌟 Potential for upselling opportunities
                        """)
                    
                    # API info - TRÈS VISIBLE
                    st.markdown("---")
                    st.markdown("### ☁️ Azure API Call Details")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.info(f"""
                        **🌐 API Endpoint:**
                        {predict_url}
                        
                        **⏱️ Response Time:**
                        {response.elapsed.total_seconds():.3f} seconds
                        
                        **✅ Status Code:**
                        {response.status_code} (Success)
                        """)
                    
                    with col2:
                        st.success(f"""
                        **☁️ Cloud Provider:**
                        Microsoft Azure
                        
                        **📍 Region:**
                        France Central
                        
                        **🚀 Service:**
                        Container Apps v2.0
                        """)
                    
                else:
                    st.error(f"❌ Azure API Error: Status Code {response.status_code}")
                    st.json(response.json())
                    
            except requests.exceptions.Timeout:
                st.error("⏱️ Request timeout. Azure API took too long to respond.")
            except requests.exceptions.ConnectionError:
                st.error(f"❌ Connection Error: Could not reach Azure API")
                st.error(f"URL: {API_URL}")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

with tab2:
    st.markdown("### 📁 Batch Prediction (Azure API)")
    st.info("Upload a CSV file with multiple customers for bulk analysis via Azure")
    
    st.markdown("**Expected CSV format:**")
    st.code("""
CreditScore,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary,Geography_Germany,Geography_Spain
650,40,5,60000,2,1,1,50000,0,0
700,35,3,75000,1,1,0,60000,1,0
    """, language="csv")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        st.success("✅ File uploaded successfully!")
        st.info("🚧 Batch prediction feature coming soon...")

with tab3:
    st.markdown("### ℹ️ About This Application")
    
    # Deployment info prominent
    st.markdown("""
    <div style='
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        color: white;
    '>
        <h3 style='color: white; margin-top: 0;'>☁️ Cloud Deployment Architecture v2.0</h3>
        <p><strong>Backend API:</strong> Deployed on Microsoft Azure Container Apps</p>
        <p><strong>Frontend UI:</strong> Streamlit v2.0 deployed on Azure Container Apps</p>
        <p><strong>Integration:</strong> UI calls Azure API for all predictions</p>
        <p><strong>Region:</strong> France Central</p>
        <p><strong>Status:</strong> ✅ Production-ready and operational</p>
        <p><strong>Version:</strong> 2.0 Enhanced 🆕</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 🎯 Purpose
        Predict bank customer churn using machine learning deployed on Azure Cloud.
        
        #### 🔧 Technology Stack
        - **Frontend:** Streamlit v2.0 (Python)
        - **Backend API:** FastAPI on Azure
        - **ML Model:** Random Forest Classifier
        - **ML Tracking:** MLflow
        - **Cloud:** Azure Container Apps
        - **CI/CD:** GitHub Actions
        """)
    
    with col2:
        st.markdown("""
        #### 📊 Model Features
        - Credit Score (300-850)
        - Age (18-100)
        - Tenure (0-15 years)
        - Account Balance
        - Number of Products (1-4)
        - Credit Card Status
        - Active Member Status
        - Estimated Salary
        - Geographic Location
        """)
    
    st.markdown("---")
    
    st.markdown("### 🏗️ Deployment Architecture")
    
    st.markdown("""
    **Full Azure Cloud Deployment v2.0:**
    
    1. **UI/Frontend (Streamlit v2.0)** → Azure Container Apps
       - Interactive web interface
       - Publicly accessible
       - Auto-scaling
       - Enhanced version
    
    2. **API/Backend (FastAPI)** → Azure Container Apps
       - Public REST API
       - Scalable and reliable
       - 24/7 availability
       - Production-ready
    
    **Professional MLOps architecture with both services on Azure Cloud!**
    """)

# Footer
st.markdown("---")

# FOOTER TRÈS VISIBLE
st.markdown("""
    <div style='
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        color: white;
    '>
        <h3 style='color: white; margin: 0;'>☁️ Powered by Microsoft Azure</h3>
        <p style='margin: 10px 0;'>
            <strong>Production API:</strong> Azure Container Apps (France Central)<br/>
            <strong>Status:</strong> ✅ Live and Operational<br/>
            <strong>Version:</strong> 2.0 Enhanced 🆕<br/>
            <strong>Project:</strong> Made with ❤️ by Arije Bouraoui
        </p>
    </div>
""", unsafe_allow_html=True)