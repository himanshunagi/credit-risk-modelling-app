import streamlit as st
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
from prediction_helper import predict  # Ensure this is correctly linked to your prediction_helper.py

# Set the page configuration and title with enhanced styling
st.set_page_config(
    page_title="RiskLens: Credit Risk Modelling", 
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    /* Main container styling */
    .main > div {
        padding-top: 2rem;
    }
    
    /* Header styling */
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        margin: -1rem -1rem 2rem -1rem;
        border-radius: 0 0 20px 20px;
        color: white;
    }
    
    .main-header h1 {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-header p {
        font-size: 1.2rem;
        opacity: 0.9;
        margin: 0;
    }
    
    /* Form section styling */
    .form-section {
        background: rgba(255,255,255,0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.1);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.2);
    }
    
    .section-title {
        color: #ffffff !important;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        text-align: center;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #667eea;
    }
    
    /* Input styling */
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > select {
        border-radius: 10px !important;
        border: 2px solid rgba(255,255,255,0.2) !important;
        background: rgba(255,255,255,0.9) !important;
        color: #333 !important;
        padding: 0.75rem !important;
        font-size: 1rem !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
    }
    
    .stNumberInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #667eea !important;
        background: white !important;
        box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.2) !important;
    }
    
    /* Label styling */
    .stNumberInput > label,
    .stSelectbox > label {
        font-weight: 600 !important;
        color: #ffffff !important;
        font-size: 1rem !important;
        margin-bottom: 0.5rem !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3) !important;
    }
    
    /* Ratio display styling */
    .ratio-display {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        box-shadow: 0 4px 15px rgba(79, 172, 254, 0.3);
    }
    
    .ratio-display h3 {
        margin: 0 0 0.5rem 0;
        font-size: 1rem;
        opacity: 0.9;
    }
    
    .ratio-display .value {
        font-size: 2rem;
        font-weight: 700;
        margin: 0;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #ff6b6b, #ffa500) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 1rem 2rem !important;
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.4) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(255, 107, 107, 0.6) !important;
    }
    
    /* Results styling */
    .results-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        margin-top: 2rem;
        color: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .result-card {
        background: rgba(255,255,255,0.15);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        margin-bottom: 1rem;
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .result-title {
        font-size: 1rem;
        opacity: 0.9;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .result-value {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
    }
    
    /* Rating colors */
    .rating-poor { color: #ff6b6b !important; }
    .rating-average { color: #ffa500 !important; }
    .rating-good { color: #51cf66 !important; }
    .rating-excellent { color: #4c6ef5 !important; }
    
    /* Hide Streamlit elements and fix containers */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Fix Streamlit container backgrounds */
    .stApp > div:first-child {
        background: transparent;
    }
    
    /* Remove default Streamlit backgrounds */
    .block-container {
        background: transparent !important;
    }
    
    /* Fix columns background */
    [data-testid="column"] {
        background: transparent !important;
    }
    
    /* Fix white backgrounds in dark mode */
    div[data-testid="stVerticalBlock"] > div {
        background: transparent !important;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>📊 RiskLens</h1>
    <p>Advanced Credit Risk Assessment & Modeling Platform</p>
</div>
""", unsafe_allow_html=True)

# Personal Information Section
st.markdown('<div class="form-section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">👤 Personal Information</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    age = st.number_input('Age', min_value=18, step=1, max_value=100, value=28, help="Applicant's age in years")
with col2:
    income = st.number_input('Annual Income (₹)', min_value=0, value=1200000, help="Annual income in Indian Rupees")
with col3:
    loan_amount = st.number_input('Loan Amount (₹)', min_value=0, value=2560000, help="Requested loan amount")

st.markdown('</div>', unsafe_allow_html=True)

# Loan Details Section
st.markdown('<div class="form-section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">💰 Loan Details</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

# Calculate and display Loan to Income Ratio
loan_to_income_ratio = loan_amount / income if income > 0 else 0
with col1:
    st.markdown(f"""
    <div class="ratio-display">
        <h3>Loan to Income Ratio</h3>
        <p class="value">{loan_to_income_ratio:.2f}</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    loan_tenure_months = st.number_input('Loan Tenure (months)', min_value=1, step=1, value=36, help="Loan duration in months")
with col3:
    loan_type = st.selectbox('Loan Type', ['Unsecured', 'Secured'], help="Type of loan security")

col4, col5, col6 = st.columns(3)
with col4:
    loan_purpose = st.selectbox('Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'], help="Purpose of the loan")
with col5:
    residence_type = st.selectbox('Residence Type', ['Owned', 'Rented', 'Mortgage'], help="Type of residence")
with col6:
    num_open_accounts = st.number_input('Open Loan Accounts', min_value=1, max_value=4, step=1, value=2, help="Number of currently open loan accounts")

st.markdown('</div>', unsafe_allow_html=True)

# Financial Metrics Section
st.markdown('<div class="form-section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">📈 Financial Metrics</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    avg_dpd_per_delinquency = st.number_input('Average DPD', min_value=0, value=20, help="Average Days Past Due per delinquency")
with col2:
    delinquency_ratio = st.number_input('Delinquency Ratio (%)', min_value=0, max_value=100, step=1, value=30, help="Percentage of delinquent payments")
with col3:
    credit_utilization_ratio = st.number_input('Credit Utilization Ratio (%)', min_value=0, max_value=100, step=1, value=30, help="Percentage of credit limit used")

st.markdown('</div>', unsafe_allow_html=True)

# Calculate Risk Button
st.markdown('<br>', unsafe_allow_html=True)
if st.button('🔍 Calculate Credit Risk', help="Click to assess credit risk and generate score"):
    with st.spinner('Analyzing credit risk...'):
        try:
            # Call the predict function from the helper module
            probability, credit_score, rating = predict(
                age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
                delinquency_ratio, credit_utilization_ratio, num_open_accounts,
                residence_type, loan_purpose, loan_type
            )
            
            # Determine rating class for styling
            rating_class = f"rating-{rating.lower()}"
            
            # Display results in an attractive format
            st.markdown(f"""
            <div class="results-container">
                <h2 style="text-align: center; margin-bottom: 2rem; font-size: 2rem;">📊 Credit Assessment Results</h2>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f"""
                <div class="result-card">
                    <div class="result-title">Default Probability</div>
                    <div class="result-value" style="color: #ff6b6b;">{probability:.2%}</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="result-card">
                    <div class="result-title">Credit Score</div>
                    <div class="result-value" style="color: #4facfe;">{credit_score}</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown(f"""
                <div class="result-card">
                    <div class="result-title">Credit Rating</div>
                    <div class="result-value {rating_class}">{rating}</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Additional insights
            st.markdown('<br>', unsafe_allow_html=True)
            
            # Risk interpretation
            if probability < 0.1:
                risk_msg = "✅ **Low Risk** - Excellent creditworthiness"
                risk_color = "#51cf66"
            elif probability < 0.25:
                risk_msg = "⚠️ **Moderate Risk** - Good creditworthiness with some caution"
                risk_color = "#ffa500"
            else:
                risk_msg = "🚨 **High Risk** - Significant credit risk identified"
                risk_color = "#ff6b6b"
            
            st.markdown(f"""
            <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 10px; 
                        border-left: 4px solid {risk_color}; margin: 1rem 0;">
                <h4 style="color: {risk_color}; margin: 0;">{risk_msg}</h4>
            </div>
            """, unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"Error calculating risk: {str(e)}")
            st.info("Please check your prediction_helper.py file and ensure all dependencies are installed.")

# Footer
st.markdown('<br><br>', unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; opacity: 0.7; padding: 2rem;">
    <p>🚀 Powered by Advanced Machine Learning Algorithms</p>
    <p><em>RiskLens - Making Credit Decisions Smarter</em></p>
</div>
""", unsafe_allow_html=True)