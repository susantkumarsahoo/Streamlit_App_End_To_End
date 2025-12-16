import streamlit as st
import pandas as pd
import numpy as np
import datetime

# Page config
st.set_page_config(page_title="Page Features Demo", layout="wide", initial_sidebar_state="collapsed")

# Header with columns
col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    st.title("🚀 Streamlit Page Features Demo")
with col2:
    st.metric("Active Users", "1,234", "+12%")
with col3:
    st.metric("Revenue", "$56K", "+8%")

st.divider()

# 1. TABS FEATURE
tab1, tab2, tab3, tab4 = st.tabs(["📊 Dashboard", "📝 Forms", "🎨 Visuals", "⚡ Advanced"])

with tab1:
    st.header("Dashboard View")
    
    # KPI Cards in columns
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Sales", "$45.2K", "+5.3%", delta_color="normal")
    col2.metric("Orders", "342", "-2%", delta_color="inverse")
    col3.metric("Customers", "1,234", "+15%")
    col4.metric("Conversion", "3.2%", "+0.5%")
    
    st.subheader("Data Table")
    # Sample data
    df = pd.DataFrame({
        'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard'],
        'Sales': [120, 340, 89, 56, 234],
        'Revenue': [24000, 68000, 8900, 11200, 11700],
        'Status': ['✅ Active', '✅ Active', '⚠️ Low Stock', '✅ Active', '❌ Out']
    })
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    # Progress bars
    st.subheader("Progress Tracking")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Q1 Target Progress")
        st.progress(0.75, text="75% Complete")
    with col2:
        st.write("Customer Satisfaction")
        st.progress(0.92, text="92% Satisfaction")

with tab2:
    st.header("Interactive Forms")
    
    with st.form("demo_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Full Name", placeholder="Enter your name")
            email = st.text_input("Email", placeholder="your@email.com")
            age = st.number_input("Age", 18, 100, 25)
        
        with col2:
            country = st.selectbox("Country", ["USA", "India", "UK", "Canada", "Australia"])
            interests = st.multiselect("Interests", ["Tech", "Sports", "Music", "Travel", "Food"])
            subscribe = st.checkbox("Subscribe to newsletter")
        
        message = st.text_area("Message", placeholder="Your message here...", height=100)
        rating = st.slider("Rate your experience", 1, 5, 3)
        
        submit = st.form_submit_button("Submit Form", use_container_width=True)
        
        if submit:
            st.success(f"✅ Thank you {name}! Form submitted successfully!")
            st.balloons()

with tab3:
    st.header("Visual Elements")
    
    # Expanders
    with st.expander("📈 View Chart Example", expanded=True):
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['Series A', 'Series B', 'Series C']
        )
        st.line_chart(chart_data)
    
    with st.expander("🗺️ View Map Example"):
        map_data = pd.DataFrame(
            np.random.randn(100, 2) / [50, 50] + [19.07, 72.87],
            columns=['lat', 'lon']
        )
        st.map(map_data, size=20)
    
    # Alert boxes
    st.subheader("Alert Messages")
    col1, col2 = st.columns(2)
    with col1:
        st.success("✅ Success message!")
        st.info("ℹ️ Info message!")
    with col2:
        st.warning("⚠️ Warning message!")
        st.error("❌ Error message!")
    
    # Code display
    st.subheader("Code Display")
    st.code("""
def hello_world():
    print("Hello, Streamlit!")
    return "Welcome"
    """, language="python")

with tab4:
    st.header("Advanced Features")
    
    # Container
    with st.container(border=True):
        st.subheader("📦 Container Example")
        st.write("This content is inside a bordered container!")
        
        col1, col2, col3 = st.columns(3)
        col1.button("Action 1", use_container_width=True)
        col2.button("Action 2", use_container_width=True)
        col3.button("Action 3", use_container_width=True)
    
    st.divider()
    
    # Columns with different content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📊 Sample Chart")
        chart_data = pd.DataFrame(
            np.random.randn(50, 3),
            columns=["Revenue", "Costs", "Profit"]
        )
        st.area_chart(chart_data)
    
    with col2:
        st.subheader("🎯 Quick Stats")
        st.metric("Total", "8,234")
        st.metric("Average", "164.7")
        st.metric("Median", "142")
        
        if st.button("Refresh Data", use_container_width=True):
            st.rerun()
    
    st.divider()
    
    # Spinners and status
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Show Spinner"):
            with st.spinner("Processing..."):
                import time
                time.sleep(2)
            st.success("Done!")
    
    with col2:
        if st.button("Show Status"):
            with st.status("Running tasks...", expanded=True) as status:
                st.write("Loading data...")
                import time
                time.sleep(1)
                st.write("Processing...")
                time.sleep(1)
                status.update(label="Complete!", state="complete")
    
    with col3:
        if st.button("Toast Message"):
            st.toast("🎉 Action successful!", icon="✅")

# Footer
st.divider()
col1, col2, col3 = st.columns(3)
with col1:
    st.caption("⏰ Last updated: " + datetime.datetime.now().strftime("%H:%M:%S"))
with col2:
    st.caption("👤 User: Demo User")
with col3:
    st.caption("🌐 Version: 1.0.0")


# streamlit run st_page01.py