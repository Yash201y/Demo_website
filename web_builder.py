import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Affordable Web Solutions",
    page_icon="🌐",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .service-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin-bottom: 1rem;
    }
    .price-tag {
        font-size: 2rem;
        color: #667eea;
        font-weight: bold;
    }
    .feature-list {
        list-style-type: none;
        padding-left: 0;
    }
    .feature-list li:before {
        content: "✓ ";
        color: #28a745;
        font-weight: bold;
        margin-right: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="main-header">
        <h1>🌐 Affordable Web Solutions</h1>
        <p>Professional Websites at Unbeatable Prices</p>
    </div>
""", unsafe_allow_html=True)

# Introduction
st.write("## Why Choose Us?")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 💰 Cost-Effective")
    st.write("Get professional websites without breaking the bank. Our streamlined process keeps costs low while maintaining quality.")

with col2:
    st.markdown("### ⚡ Fast Delivery")
    st.write("Quick turnaround times mean your website goes live faster. Most projects completed within 1-2 weeks.")

with col3:
    st.markdown("### 🎨 Custom Design")
    st.write("Unique designs tailored to your brand. No cookie-cutter templates, just websites that stand out.")

st.write("---")

# Pricing Packages
st.write("## Our Packages")

pkg_col1, pkg_col2, pkg_col3 = st.columns(3)

with pkg_col1:
    st.markdown("""
        <div class="service-card">
            <h3>Starter Package</h3>
            <div class="price-tag">$299</div>
            <p><i>Perfect for small businesses & portfolios</i></p>
            <ul class="feature-list">
                <li>Up to 5 pages</li>
                <li>Responsive design</li>
                <li>Contact form</li>
                <li>Basic SEO</li>
                <li>1 month support</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with pkg_col2:
    st.markdown("""
        <div class="service-card">
            <h3>Professional Package</h3>
            <div class="price-tag">$599</div>
            <p><i>Ideal for growing businesses</i></p>
            <ul class="feature-list">
                <li>Up to 10 pages</li>
                <li>Premium design</li>
                <li>CMS integration</li>
                <li>Advanced SEO</li>
                <li>Blog setup</li>
                <li>3 months support</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with pkg_col3:
    st.markdown("""
        <div class="service-card">
            <h3>Enterprise Package</h3>
            <div class="price-tag">$1,299</div>
            <p><i>For established businesses</i></p>
            <ul class="feature-list">
                <li>Unlimited pages</li>
                <li>Custom features</li>
                <li>E-commerce ready</li>
                <li>Premium SEO</li>
                <li>Analytics setup</li>
                <li>6 months support</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

st.write("---")

# Contact Form
st.write("## Get Your Free Quote")

with st.form("contact_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Full Name *")
        email = st.text_input("Email Address *")
        phone = st.text_input("Phone Number")
    
    with col2:
        company = st.text_input("Company/Business Name")
        package = st.selectbox(
            "Interested Package *",
            ["Select a package", "Starter Package", "Professional Package", "Enterprise Package", "Custom Solution"]
        )
        budget = st.selectbox(
            "Your Budget",
            ["Select budget range", "Under $500", "$500 - $1,000", "$1,000 - $2,000", "Above $2,000"]
        )
    
    project_details = st.text_area("Tell us about your project *", height=150)
    
    submitted = st.form_submit_button("Submit Request")
    
    if submitted:
        if name and email and package != "Select a package" and project_details:
            st.success("✅ Thank you! We'll get back to you within 24 hours.")
            st.balloons()
        else:
            st.error("❌ Please fill in all required fields (*)")

st.write("---")

# Additional Features Section
st.write("## What Makes Us Different?")

feature_col1, feature_col2 = st.columns(2)

with feature_col1:
    st.write("### 🔧 Our Process")
    st.write("""
    1. **Consultation** - We understand your needs
    2. **Design** - Create mockups for your approval
    3. **Development** - Build your website
    4. **Testing** - Ensure everything works perfectly
    5. **Launch** - Go live with ongoing support
    """)

with feature_col2:
    st.write("### 📊 Technologies We Use")
    st.write("""
    - **Frontend**: HTML5, CSS3, JavaScript, React
    - **Backend**: Python, Node.js, PHP
    - **CMS**: WordPress, Webflow, Custom
    - **E-commerce**: Shopify, WooCommerce
    - **Hosting**: AWS, Digital Ocean, Vercel
    """)

# Footer
st.write("---")
st.markdown("""
    <div style="text-align: center; padding: 2rem 0; color: #6c757d;">
        <p>📧 Email: info@affordablewebsolutions.com | 📱 Phone: +1 (555) 123-4567</p>
        <p>© 2024 Affordable Web Solutions. All rights reserved.</p>
    </div>
""", unsafe_allow_html=True)
