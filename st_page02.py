import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time

# Page Configuration
st.set_page_config(
    page_title="Enterprise Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
    }
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 18px;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# Generate realistic data
@st.cache_data
def generate_sales_data():
    dates = pd.date_range(end=datetime.now(), periods=365, freq='D')
    regions = ['North America', 'Europe', 'Asia Pacific', 'Latin America', 'Middle East']
    products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    
    data = []
    for date in dates:
        for region in regions:
            for product in products:
                data.append({
                    'Date': date,
                    'Region': region,
                    'Product': product,
                    'Sales': np.random.randint(1000, 50000),
                    'Units': np.random.randint(10, 500),
                    'Cost': np.random.randint(500, 30000),
                    'Customer_Satisfaction': round(np.random.uniform(3.5, 5.0), 2),
                    'Returns': np.random.randint(0, 50)
                })
    
    return pd.DataFrame(data)

@st.cache_data
def generate_customer_data():
    segments = ['Enterprise', 'Mid-Market', 'SMB', 'Startup']
    industries = ['Technology', 'Healthcare', 'Finance', 'Retail', 'Manufacturing']
    
    data = []
    for i in range(500):
        data.append({
            'Customer_ID': f'CUST{i:04d}',
            'Company': f'Company {i}',
            'Segment': np.random.choice(segments),
            'Industry': np.random.choice(industries),
            'Annual_Revenue': np.random.randint(50000, 5000000),
            'Employees': np.random.randint(10, 10000),
            'Contract_Value': np.random.randint(5000, 500000),
            'Churn_Risk': np.random.choice(['Low', 'Medium', 'High'], p=[0.6, 0.3, 0.1]),
            'NPS_Score': np.random.randint(0, 100),
            'Account_Age_Days': np.random.randint(30, 1825)
        })
    
    return pd.DataFrame(data)

@st.cache_data
def generate_inventory_data():
    warehouses = ['WH-NY', 'WH-LA', 'WH-CHI', 'WH-HOU', 'WH-PHX']
    products = [f'SKU-{i:04d}' for i in range(50)]
    
    data = []
    for warehouse in warehouses:
        for product in products:
            data.append({
                'Warehouse': warehouse,
                'SKU': product,
                'Stock': np.random.randint(0, 1000),
                'Reorder_Point': np.random.randint(50, 200),
                'Lead_Time_Days': np.random.randint(7, 30),
                'Unit_Cost': round(np.random.uniform(10, 500), 2),
                'Last_Restocked': datetime.now() - timedelta(days=np.random.randint(1, 60))
            })
    
    return pd.DataFrame(data)

# Load data
df_sales = generate_sales_data()
df_customers = generate_customer_data()
df_inventory = generate_inventory_data()

# Sidebar Navigation
with st.sidebar:
    st.image("https://via.placeholder.com/150x50/667eea/ffffff?text=LOGO", use_container_width=True)
    st.title("🎛️ Control Center")
    
    page = st.radio(
        "Navigation",
        ["📊 Executive Dashboard", "📈 Sales Analytics", "👥 Customer Intelligence", 
         "📦 Inventory Management", "🤖 AI Predictions", "⚙️ System Settings"],
        label_visibility="collapsed"
    )
    
    st.divider()
    
    # Global Filters
    st.subheader("🔍 Global Filters")
    date_range = st.date_input(
        "Date Range",
        value=(datetime.now() - timedelta(days=90), datetime.now()),
        max_value=datetime.now()
    )
    
    selected_regions = st.multiselect(
        "Regions",
        options=df_sales['Region'].unique(),
        default=df_sales['Region'].unique()
    )
    
    st.divider()
    
    # Quick Actions
    st.subheader("⚡ Quick Actions")
    if st.button("📥 Export Data", use_container_width=True):
        st.toast("✅ Data exported successfully!", icon="📥")
    
    if st.button("🔄 Refresh Dashboard", use_container_width=True):
        st.cache_data.clear()
        st.rerun()
    
    if st.button("📧 Email Report", use_container_width=True):
        with st.spinner("Sending report..."):
            time.sleep(1)
        st.success("✅ Report sent!")
    
    st.divider()
    
    # User Info
    st.caption("👤 John Doe | Admin")
    st.caption(f"🕐 {datetime.now().strftime('%Y-%m-%d %H:%M')}")

# Filter data based on selections
mask = (df_sales['Date'].dt.date >= date_range[0]) & (df_sales['Date'].dt.date <= date_range[1])
df_filtered = df_sales[mask & df_sales['Region'].isin(selected_regions)]

# PAGE 1: Executive Dashboard
if page == "📊 Executive Dashboard":
    st.title("📊 Executive Dashboard")
    st.markdown("*Real-time business intelligence and key performance indicators*")
    
    # KPI Metrics Row
    col1, col2, col3, col4, col5 = st.columns(5)
    
    total_sales = df_filtered['Sales'].sum()
    total_units = df_filtered['Units'].sum()
    avg_satisfaction = df_filtered['Customer_Satisfaction'].mean()
    total_profit = (df_filtered['Sales'] - df_filtered['Cost']).sum()
    
    with col1:
        st.metric("Total Revenue", f"${total_sales:,.0f}", f"+{np.random.randint(5,15)}%")
    with col2:
        st.metric("Units Sold", f"{total_units:,}", f"+{np.random.randint(3,12)}%")
    with col3:
        st.metric("Avg Satisfaction", f"{avg_satisfaction:.2f}/5.0", f"+{np.random.uniform(0.1,0.5):.2f}")
    with col4:
        st.metric("Net Profit", f"${total_profit:,.0f}", f"+{np.random.randint(8,20)}%")
    with col5:
        st.metric("Active Customers", f"{len(df_customers):,}", f"+{np.random.randint(2,8)}%")
    
    st.divider()
    
    # Charts Row 1
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📈 Revenue Trend Over Time")
        daily_sales = df_filtered.groupby('Date')['Sales'].sum().reset_index()
        fig = px.line(daily_sales, x='Date', y='Sales', 
                      title='Daily Revenue Performance',
                      labels={'Sales': 'Revenue ($)', 'Date': 'Date'})
        fig.update_traces(line_color='#667eea', line_width=3)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🌍 Revenue by Region")
        region_sales = df_filtered.groupby('Region')['Sales'].sum().reset_index()
        fig = px.pie(region_sales, values='Sales', names='Region',
                     color_discrete_sequence=px.colors.sequential.Viridis)
        st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    # Charts Row 2
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📦 Product Performance")
        product_sales = df_filtered.groupby('Product')['Sales'].sum().sort_values(ascending=True).reset_index()
        fig = px.bar(product_sales, x='Sales', y='Product', orientation='h',
                     color='Sales', color_continuous_scale='Bluered')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("😊 Customer Satisfaction by Product")
        satisfaction_data = df_filtered.groupby('Product')['Customer_Satisfaction'].mean().reset_index()
        fig = px.bar(satisfaction_data, x='Product', y='Customer_Satisfaction',
                     color='Customer_Satisfaction', color_continuous_scale='RdYlGn')
        st.plotly_chart(fig, use_container_width=True)
    
    # Recent Activity
    st.divider()
    st.subheader("🔔 Recent Activity & Alerts")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("📊 New sales report generated")
    with col2:
        st.warning("⚠️ 3 inventory items below threshold")
    with col3:
        st.success("✅ Q4 targets achieved")

# PAGE 2: Sales Analytics
elif page == "📈 Sales Analytics":
    st.title("📈 Advanced Sales Analytics")
    
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "🎯 Performance", "🔍 Deep Dive", "📋 Reports"])
    
    with tab1:
        col1, col2, col3 = st.columns(3)
        with col1:
            metric_type = st.selectbox("Metric", ["Sales", "Units", "Profit"])
        with col2:
            group_by = st.selectbox("Group By", ["Region", "Product", "Date"])
        with col3:
            chart_type = st.selectbox("Chart Type", ["Line", "Bar", "Area"])
        
        st.divider()
        
        if group_by == "Date":
            grouped = df_filtered.groupby('Date')[metric_type if metric_type != "Profit" else 'Sales'].sum().reset_index()
        else:
            grouped = df_filtered.groupby(group_by)[metric_type if metric_type != "Profit" else 'Sales'].sum().reset_index()
        
        if chart_type == "Line":
            fig = px.line(grouped, x=grouped.columns[0], y=grouped.columns[1])
        elif chart_type == "Bar":
            fig = px.bar(grouped, x=grouped.columns[0], y=grouped.columns[1], color=grouped.columns[1])
        else:
            fig = px.area(grouped, x=grouped.columns[0], y=grouped.columns[1])
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Detailed table
        st.subheader("📋 Detailed Data")
        st.dataframe(
            df_filtered.head(100),
            use_container_width=True,
            hide_index=True,
            column_config={
                "Sales": st.column_config.NumberColumn("Sales", format="$%d"),
                "Customer_Satisfaction": st.column_config.ProgressColumn("Satisfaction", min_value=0, max_value=5),
            }
        )
    
    with tab2:
        st.subheader("🎯 Sales Performance Comparison")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Heatmap
            heatmap_data = df_filtered.groupby(['Region', 'Product'])['Sales'].sum().reset_index()
            heatmap_pivot = heatmap_data.pivot(index='Product', columns='Region', values='Sales')
            
            fig = go.Figure(data=go.Heatmap(
                z=heatmap_pivot.values,
                x=heatmap_pivot.columns,
                y=heatmap_pivot.index,
                colorscale='Viridis'
            ))
            fig.update_layout(title="Sales Heatmap: Product vs Region")
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Sunburst chart
            sunburst_data = df_filtered.groupby(['Region', 'Product'])['Sales'].sum().reset_index()
            fig = px.sunburst(sunburst_data, path=['Region', 'Product'], values='Sales',
                            title='Hierarchical Sales Distribution')
            st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.subheader("🔍 Deep Dive Analysis")
        
        # Statistical summary
        st.write("**Statistical Summary**")
        summary_stats = df_filtered[['Sales', 'Units', 'Cost', 'Customer_Satisfaction']].describe()
        st.dataframe(summary_stats, use_container_width=True)
        
        st.divider()
        
        # Correlation analysis
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Scatter Analysis**")
            fig = px.scatter(df_filtered, x='Units', y='Sales', color='Region',
                           size='Customer_Satisfaction', hover_data=['Product'],
                           title='Sales vs Units Correlation')
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.write("**Distribution Analysis**")
            fig = px.histogram(df_filtered, x='Sales', nbins=50, 
                             title='Sales Distribution',
                             color_discrete_sequence=['#667eea'])
            st.plotly_chart(fig, use_container_width=True)
    
    with tab4:
        st.subheader("📋 Generate Custom Report")
        
        with st.form("report_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                report_type = st.selectbox("Report Type", ["Summary", "Detailed", "Executive"])
                include_charts = st.checkbox("Include Charts", value=True)
            
            with col2:
                format_type = st.selectbox("Format", ["PDF", "Excel", "CSV"])
                email_report = st.checkbox("Email Report", value=False)
            
            if st.form_submit_button("Generate Report", use_container_width=True):
                with st.spinner("Generating report..."):
                    progress_bar = st.progress(0)
                    for i in range(100):
                        time.sleep(0.01)
                        progress_bar.progress(i + 1)
                
                st.success(f"✅ {report_type} report generated in {format_type} format!")
                st.balloons()

# PAGE 3: Customer Intelligence
elif page == "👥 Customer Intelligence":
    st.title("👥 Customer Intelligence Hub")
    
    col1, col2, col3, col4 = st.columns(4)
    
    total_customers = len(df_customers)
    high_risk = len(df_customers[df_customers['Churn_Risk'] == 'High'])
    avg_contract = df_customers['Contract_Value'].mean()
    avg_nps = df_customers['NPS_Score'].mean()
    
    with col1:
        st.metric("Total Customers", f"{total_customers:,}")
    with col2:
        st.metric("High Churn Risk", f"{high_risk}", "⚠️")
    with col3:
        st.metric("Avg Contract Value", f"${avg_contract:,.0f}")
    with col4:
        st.metric("Avg NPS Score", f"{avg_nps:.1f}")
    
    st.divider()
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🎯 Customer Segmentation")
        segment_data = df_customers.groupby('Segment').agg({
            'Customer_ID': 'count',
            'Contract_Value': 'sum',
            'Annual_Revenue': 'mean'
        }).reset_index()
        
        fig = px.scatter(df_customers, x='Employees', y='Annual_Revenue',
                        color='Segment', size='Contract_Value',
                        hover_data=['Company', 'Industry'],
                        title='Customer Segmentation Analysis',
                        log_x=True, log_y=True)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("⚠️ Churn Risk Distribution")
        churn_data = df_customers['Churn_Risk'].value_counts().reset_index()
        churn_data.columns = ['Risk Level', 'Count']
        
        colors = {'Low': '#00ff00', 'Medium': '#ffaa00', 'High': '#ff0000'}
        fig = px.pie(churn_data, values='Count', names='Risk Level',
                     color='Risk Level', color_discrete_map=colors)
        st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    # Customer table with advanced filtering
    st.subheader("🔍 Customer Explorer")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        filter_segment = st.multiselect("Segment", df_customers['Segment'].unique(), default=df_customers['Segment'].unique())
    with col2:
        filter_industry = st.multiselect("Industry", df_customers['Industry'].unique(), default=df_customers['Industry'].unique())
    with col3:
        filter_risk = st.multiselect("Churn Risk", df_customers['Churn_Risk'].unique(), default=df_customers['Churn_Risk'].unique())
    
    filtered_customers = df_customers[
        (df_customers['Segment'].isin(filter_segment)) &
        (df_customers['Industry'].isin(filter_industry)) &
        (df_customers['Churn_Risk'].isin(filter_risk))
    ]
    
    st.dataframe(
        filtered_customers,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Contract_Value": st.column_config.NumberColumn("Contract Value", format="$%d"),
            "Annual_Revenue": st.column_config.NumberColumn("Annual Revenue", format="$%d"),
            "NPS_Score": st.column_config.ProgressColumn("NPS Score", min_value=0, max_value=100),
            "Churn_Risk": st.column_config.TextColumn("Churn Risk")
        }
    )

# PAGE 4: Inventory Management
elif page == "📦 Inventory Management":
    st.title("📦 Inventory Management System")
    
    # Inventory KPIs
    col1, col2, col3, col4 = st.columns(4)
    
    total_stock = df_inventory['Stock'].sum()
    low_stock = len(df_inventory[df_inventory['Stock'] < df_inventory['Reorder_Point']])
    total_value = (df_inventory['Stock'] * df_inventory['Unit_Cost']).sum()
    avg_lead_time = df_inventory['Lead_Time_Days'].mean()
    
    with col1:
        st.metric("Total Stock Units", f"{total_stock:,}")
    with col2:
        st.metric("Low Stock Items", f"{low_stock}", "⚠️" if low_stock > 10 else "✅")
    with col3:
        st.metric("Total Inventory Value", f"${total_value:,.0f}")
    with col4:
        st.metric("Avg Lead Time", f"{avg_lead_time:.1f} days")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Stock Levels by Warehouse")
        warehouse_stock = df_inventory.groupby('Warehouse')['Stock'].sum().reset_index()
        fig = px.bar(warehouse_stock, x='Warehouse', y='Stock', 
                     color='Stock', color_continuous_scale='Blues')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("⚠️ Items Needing Reorder")
        low_stock_items = df_inventory[df_inventory['Stock'] < df_inventory['Reorder_Point']]
        reorder_by_warehouse = low_stock_items.groupby('Warehouse').size().reset_index()
        reorder_by_warehouse.columns = ['Warehouse', 'Count']
        
        fig = px.pie(reorder_by_warehouse, values='Count', names='Warehouse',
                     title=f'Total: {low_stock} items')
        st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    # Inventory table
    st.subheader("📋 Inventory Details")
    
    warehouse_filter = st.multiselect("Filter by Warehouse", 
                                     df_inventory['Warehouse'].unique(),
                                     default=df_inventory['Warehouse'].unique())
    
    filtered_inventory = df_inventory[df_inventory['Warehouse'].isin(warehouse_filter)]
    
    # Highlight low stock items
    def highlight_low_stock(row):
        if row['Stock'] < row['Reorder_Point']:
            return ['background-color: #ffcccc'] * len(row)
        return [''] * len(row)
    
    st.dataframe(
        filtered_inventory.head(50),
        use_container_width=True,
        hide_index=True,
        column_config={
            "Unit_Cost": st.column_config.NumberColumn("Unit Cost", format="$%.2f"),
            "Stock": st.column_config.ProgressColumn("Stock Level", min_value=0, max_value=1000),
        }
    )

# PAGE 5: AI Predictions
elif page == "🤖 AI Predictions":
    st.title("🤖 AI-Powered Predictions & Insights")
    
    tab1, tab2, tab3 = st.tabs(["📈 Sales Forecast", "👥 Churn Prediction", "💡 Recommendations"])
    
    with tab1:
        st.subheader("📈 Sales Forecasting Model")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            forecast_days = st.slider("Forecast Period (Days)", 7, 90, 30)
            confidence_interval = st.select_slider("Confidence Interval", [80, 90, 95, 99], value=95)
        
        with col2:
            model_type = st.radio("Model Type", ["Linear", "Exponential", "Prophet"])
        
        if st.button("🚀 Generate Forecast", use_container_width=True):
            with st.spinner("Training AI model..."):
                progress = st.progress(0)
                for i in range(100):
                    time.sleep(0.02)
                    progress.progress(i + 1)
            
            # Generate forecast data
            last_date = df_filtered['Date'].max()
            future_dates = pd.date_range(start=last_date + timedelta(days=1), periods=forecast_days)
            
            # Simulate forecast
            base_value = df_filtered.groupby('Date')['Sales'].sum().tail(30).mean()
            trend = np.linspace(0, forecast_days * 100, forecast_days)
            noise = np.random.normal(0, 5000, forecast_days)
            forecast = base_value + trend + noise
            
            forecast_df = pd.DataFrame({
                'Date': future_dates,
                'Forecast': forecast,
                'Upper_Bound': forecast * 1.1,
                'Lower_Bound': forecast * 0.9
            })
            
            # Plot forecast
            fig = go.Figure()
            
            # Historical data
            historical = df_filtered.groupby('Date')['Sales'].sum().reset_index()
            fig.add_trace(go.Scatter(x=historical['Date'], y=historical['Sales'],
                                    name='Historical', line=dict(color='blue')))
            
            # Forecast
            fig.add_trace(go.Scatter(x=forecast_df['Date'], y=forecast_df['Forecast'],
                                    name='Forecast', line=dict(color='red', dash='dash')))
            
            # Confidence interval
            fig.add_trace(go.Scatter(x=forecast_df['Date'], y=forecast_df['Upper_Bound'],
                                    fill=None, mode='lines', line_color='lightgray',
                                    showlegend=False))
            fig.add_trace(go.Scatter(x=forecast_df['Date'], y=forecast_df['Lower_Bound'],
                                    fill='tonexty', mode='lines', line_color='lightgray',
                                    name=f'{confidence_interval}% Confidence'))
            
            fig.update_layout(title='Sales Forecast with Confidence Interval',
                            xaxis_title='Date', yaxis_title='Sales ($)')
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Forecast metrics
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Predicted Revenue", f"${forecast_df['Forecast'].sum():,.0f}")
            with col2:
                st.metric("Growth Rate", f"+{np.random.randint(5, 15)}%")
            with col3:
                st.metric("Model Accuracy", f"{np.random.randint(85, 95)}%")
    
    with tab2:
        st.subheader("👥 Customer Churn Prediction")
        
        st.info("🤖 AI Model analyzing customer behavior patterns...")
        
        # Select customer for analysis
        customer_id = st.selectbox("Select Customer", df_customers['Customer_ID'].unique())
        
        if st.button("🔍 Analyze Churn Risk", use_container_width=True):
            customer = df_customers[df_customers['Customer_ID'] == customer_id].iloc[0]
            
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.write("**Customer Profile**")
                st.write(f"**Company:** {customer['Company']}")
                st.write(f"**Segment:** {customer['Segment']}")
                st.write(f"**Industry:** {customer['Industry']}")
                st.write(f"**Contract Value:** ${customer['Contract_Value']:,}")
                st.write(f"**NPS Score:** {customer['NPS_Score']}")
                
                churn_prob = np.random.uniform(0.1, 0.8)
                risk_level = "High" if churn_prob > 0.6 else "Medium" if churn_prob > 0.3 else "Low"
                
                if risk_level == "High":
                    st.error(f"⚠️ Churn Risk: {risk_level} ({churn_prob*100:.1f}%)")
                elif risk_level == "Medium":
                    st.warning(f"⚠️ Churn Risk: {risk_level} ({churn_prob*100:.1f}%)")
                else:
                    st.success(f"✅ Churn Risk: {risk_level} ({churn_prob*100:.1f}%)")
            
            with col2:
                st.write("**Risk Factors Analysis**")
                
                factors = pd.DataFrame({
                    'Factor': ['Engagement Score', 'Payment History', 'Support Tickets', 'Product Usage', 'Contract Age'],
                    'Impact': [np.random.randint(60, 95) for _ in range(5)]
                })
                
                fig = px.bar(factors, x='Impact', y='Factor', orientation='h',
                           color='Impact', color_continuous_scale='RdYlGn_r',
                           title='Churn Risk Factors')
                st.plotly_chart(fig, use_container_width=True)
                
                st.write("**Recommended Actions:**")
                st.write("- 📞 Schedule account review call")
                st.write("- 🎁 Offer loyalty discount")
                st.write("- 📚 Provide additional training")
                st.write("- 🤝 Assign dedicated account manager")
    
    with tab3:
        st.subheader("💡 AI-Generated Recommendations")
        
        st.write("### 🎯 Strategic Insights")
        
        insights = [
            {"title": "Market Opportunity", "description": "Asia Pacific shows 23% growth potential", "priority": "High", "icon": "🌏"},
            {"title": "Product Optimization", "description": "Product C has declining satisfaction scores", "priority": "Medium", "icon": "📦"},
            {"title": "Customer Retention", "description": "15 high-value customers at churn risk", "priority": "High", "icon": "⚠️"},
            {"title": "Inventory Alert", "description": "23 items below reorder point", "priority": "Medium", "icon": "📊"},
            {"title": "Pricing Strategy", "description": "Competitor pricing analysis suggests 5% increase opportunity", "priority": "Low", "icon": "💰"}
        ]
        
        for insight in insights:
            with st.container(border=True):
                col1, col2, col3 = st.columns([1, 6, 2])
                
                with col1:
                    st.markdown(f"<h1>{insight['icon']}</h1>", unsafe_allow_html=True)
                
                with col2:
                    st.write(f"**{insight['title']}**")
                    st.write(insight['description'])



# streamlit run st_page02.py