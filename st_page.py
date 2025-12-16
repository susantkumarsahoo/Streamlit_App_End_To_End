import streamlit as st
import datetime

# Page config
st.set_page_config(page_title="Sidebar Features Demo", layout="wide")

# SIDEBAR - All features
with st.sidebar:
    st.title("🎛️ Control Panel")
    
    # 1. Navigation Menu
    st.header("📍 Navigation")
    page = st.radio("Go to:", ["Home", "Analytics", "Settings", "About"])
    
    st.divider()
    
    # 2. User Profile Section
    st.header("👤 User Profile")
    username = st.text_input("Username", "John Doe")
    role = st.selectbox("Role", ["Admin", "User", "Guest"])
    
    st.divider()
    
    # 3. Filter Options
    st.header("🔍 Filters")
    date_range = st.date_input("Date Range", [datetime.date(2024, 1, 1), datetime.date.today()])
    category = st.multiselect("Categories", ["Tech", "Business", "Sports", "Entertainment"], default=["Tech"])
    price_range = st.slider("Price Range", 0, 1000, (100, 500))
    
    st.divider()
    
    # 4. Settings/Preferences
    st.header("⚙️ Preferences")
    theme = st.toggle("Dark Mode", value=False)
    notifications = st.checkbox("Enable Notifications", value=True)
    auto_refresh = st.number_input("Auto-refresh (seconds)", 5, 60, 10)
    
    st.divider()
    
    # 5. File Upload
    st.header("📤 Upload")
    uploaded_file = st.file_uploader("Upload File", type=['csv', 'xlsx', 'txt'])
    
    st.divider()
    
    # 6. Action Buttons
    st.header("⚡ Actions")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Apply", use_container_width=True):
            st.success("Applied!")
    with col2:
        if st.button("🔄 Reset", use_container_width=True):
            st.info("Reset!")
    
    st.divider()
    
    # 7. Download Section
    st.header("💾 Export")
    export_format = st.radio("Format:", ["CSV", "JSON", "PDF"], horizontal=True)
    st.download_button("⬇️ Download", "Sample data", "data.csv", use_container_width=True)

# MAIN CONTENT
st.title(f"📊 {page} Page")

# Display selections
st.subheader("Current Settings:")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("User", username)
    st.metric("Role", role)
    
with col2:
    st.metric("Categories", len(category))
    st.metric("Price Min", f"${price_range[0]}")
    
with col3:
    st.metric("Dark Mode", "On" if theme else "Off")
    st.metric("Price Max", f"${price_range[1]}")

st.divider()

# Page-specific content
if page == "Home":
    st.write("### Welcome to the Dashboard! 👋")
    st.info("Use the sidebar to navigate and configure your preferences.")
    
elif page == "Analytics":
    st.write("### Analytics Overview 📈")
    st.success(f"Showing data for categories: {', '.join(category)}")
    
elif page == "Settings":
    st.write("### System Settings ⚙️")
    st.warning(f"Auto-refresh set to {auto_refresh} seconds")
    
elif page == "About":
    st.write("### About This App ℹ️")
    st.markdown("""
    **Sidebar Features Included:**
    - 📍 Navigation menu
    - 👤 User profile
    - 🔍 Multiple filters
    - ⚙️ Preferences & toggles
    - 📤 File upload
    - ⚡ Action buttons
    - 💾 Export options
    """)

# Footer
st.divider()
st.caption(f"Notifications: {'🔔 Enabled' if notifications else '🔕 Disabled'} | Theme: {'🌙 Dark' if theme else '☀️ Light'} | Export: {export_format}")



# streamlit run st_page.py