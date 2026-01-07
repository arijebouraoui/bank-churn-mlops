# app_streamlit.py
import streamlit as st
import requests
import json
import plotly.graph_objects as go

# Page config
st.set_page_config(
    page_title="Bank Churn Prediction",
    page_icon="🏦",
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

# Header
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<h1>🏦 Bank Churn Predictor</h1>", unsafe_allow_html=True)
    st.markdown("### Predict customer churn risk with AI-powered analytics")

st.markdown("---")

# Sidebar
with st.sidebar:
    st.markdown("## 📊 Model Info")
    st.info("""
    **Model:** Random Forest Classifier
    
    **Accuracy:** 85%+
    
    **Features:** 10 customer attributes
    
    **Deployed on:** Azure Container Apps
    """)
    
    st.markdown("---")
    st.markdown("## 🔗 Quick Links")
    st.markdown("- [API Docs](https://bank-churn-api.victoriousmoss-65485a03.francecentral.azurecontainerapps.io/docs)")
    st.markdown("- [GitHub](https://github.com/arijebouraoui/bank-churn-mlops)")

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
        predict_button = st.button("🔮 PREDICT CHURN RISK", use_container_width=True)
    
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
        
        # YOUR CORRECT URL
        url = "https://bank-churn-api.victoriousmoss-65485a03.francecentral.azurecontainerapps.io/predict"
        
        with st.spinner("🔄 Analyzing customer data..."):
            try:
                response = requests.post(url, json=payload)
                result = response.json()
                
                # Display results
                st.markdown("### 📊 Prediction Results")
                
                # Metrics
                col1, col2, col3 = st.columns(3)
                
                churn_prob = result["churn_probability"]
                prediction = result["prediction"]
                risk_level = result["risk_level"]
                
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
                    - Immediate retention strategy required
                    - Offer personalized incentives
                    - Schedule customer service call
                    """)
                elif risk_level == "Medium":
                    st.warning("""
                    **Medium Risk Customer** 🟡
                    - Monitor account activity
                    - Send engagement campaigns
                    - Offer loyalty rewards
                    """)
                else:
                    st.success("""
                    **Low Risk Customer** 🟢
                    - Continue standard service
                    - Maintain satisfaction surveys
                    """)
                
            except Exception as e:
                st.error(f"❌ Error calling API: {e}")

with tab2:
    st.markdown("### 📁 Batch Prediction")
    st.info("Upload a CSV file with multiple customers for bulk analysis")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        st.success("✅ File uploaded successfully! Feature coming soon...")

with tab3:
    st.markdown("### ℹ️ About This Application")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 🎯 Purpose
        Predict bank customer churn using ML.
        
        #### 🔧 Technology Stack
        - **Frontend:** Streamlit
        - **Backend API:** FastAPI
        - **ML Model:** Random Forest
        - **Cloud:** Azure Container Apps
        """)
    
    with col2:
        st.markdown("""
        #### 📊 Model Features
        - Credit Score
        - Age & Tenure
        - Account Balance
        - Number of Products
        - Geographic Location
        """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>Made with ❤️ using Streamlit | Powered by Azure</div>",
    unsafe_allow_html=True
)