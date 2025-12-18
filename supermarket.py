import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set page config
st.set_page_config(
    page_title="Multi-Language Business Dashboard",
    page_icon="📊",
    layout="wide"
)

# ===================== MULTI-LANGUAGE SUPPORT =====================
# Language dictionary
LANGUAGES = {
    "English": {
        "title": "Business Intelligence Dashboard",
        "upload": "Upload Excel File",
        "upload_desc": "Upload an Excel file (.xlsx or .xls). The app will automatically detect date, numeric, and categorical columns and show analytical charts.",
        "drag_drop": "Drag and drop file here",
        "file_limit": "Limit 200MB per file • XLSX, XLS",
        "processing": "Processing data...",
        "data_preview": "Data Preview",
        "kpi_section": "Key Performance Indicators",
        "charts_section": "Analytical Charts",
        "total_records": "Total Records",
        "total_columns": "Total Columns",
        "date_columns": "Date Columns",
        "numeric_columns": "Numeric Columns",
        "data_types": "Data Types Overview",
        "missing_values": "Missing Values",
        "time_series": "Time Series Analysis",
        "distribution": "Distribution Analysis",
        "correlation": "Correlation Matrix",
        "category_analysis": "Category Analysis",
        "top_categories": "Top Categories",
        "download_data": "Download Processed Data",
        "select_date_col": "Select Date Column",
        "select_value_col": "Select Value Column",
        "select_category_col": "Select Category Column",
        "no_date_col": "No date column detected",
        "no_numeric_col": "No numeric column detected",
        "no_category_col": "No categorical column detected",
        "error": "Error",
        "success": "Success",
        "file_uploaded": "File uploaded successfully",
        "select_language": "Select Language",
        "reset": "Reset",
        "filter_data": "Filter Data",
        "apply_filter": "Apply Filter",
        "clear_filter": "Clear Filter",
        "data_summary": "Data Summary",
        "insights": "Insights",
        "trend": "Trend",
        "comparison": "Comparison",
        "forecast": "Forecast"
    },
    "Indonesia": {
        "title": "Dasbor Bisnis Inteligensi",
        "upload": "Unggah File Excel",
        "upload_desc": "Unggah file Excel (.xlsx atau .xls). Aplikasi akan mendeteksi kolom tanggal, numerik, dan kategorikal secara otomatis dan menampilkan grafik analitis.",
        "drag_drop": "Seret dan lepas file di sini",
        "file_limit": "Batas 200MB per file • XLSX, XLS",
        "processing": "Memproses data...",
        "data_preview": "Pratinjau Data",
        "kpi_section": "Indikator Kinerja Utama",
        "charts_section": "Grafik Analitis",
        "total_records": "Total Data",
        "total_columns": "Total Kolom",
        "date_columns": "Kolom Tanggal",
        "numeric_columns": "Kolom Numerik",
        "data_types": "Ringkasan Tipe Data",
        "missing_values": "Nilai Kosong",
        "time_series": "Analisis Deret Waktu",
        "distribution": "Analisis Distribusi",
        "correlation": "Matriks Korelasi",
        "category_analysis": "Analisis Kategori",
        "top_categories": "Kategori Teratas",
        "download_data": "Unduh Data Hasil Olahan",
        "select_date_col": "Pilih Kolom Tanggal",
        "select_value_col": "Pilih Kolom Nilai",
        "select_category_col": "Pilih Kolom Kategori",
        "no_date_col": "Tidak ada kolom tanggal terdeteksi",
        "no_numeric_col": "Tidak ada kolom numerik terdeteksi",
        "no_category_col": "Tidak ada kolom kategorikal terdeteksi",
        "error": "Error",
        "success": "Berhasil",
        "file_uploaded": "File berhasil diunggah",
        "select_language": "Pilih Bahasa",
        "reset": "Reset",
        "filter_data": "Filter Data",
        "apply_filter": "Terapkan Filter",
        "clear_filter": "Hapus Filter",
        "data_summary": "Ringkasan Data",
        "insights": "Insights",
        "trend": "Tren",
        "comparison": "Perbandingan",
        "forecast": "Perkiraan"
    },
    "中文": {
        "title": "商业智能仪表板",
        "upload": "上传 Excel 文件",
        "upload_desc": "上传 Excel 文件（.xlsx 或 .xls）。应用将自动检测日期、数值和分类列，并显示分析图表。",
        "drag_drop": "拖放文件到此处",
        "file_limit": "每文件限制 200MB • XLSX, XLS",
        "processing": "处理数据中...",
        "data_preview": "数据预览",
        "kpi_section": "关键绩效指标",
        "charts_section": "分析图表",
        "total_records": "总记录数",
        "total_columns": "总列数",
        "date_columns": "日期列",
        "numeric_columns": "数值列",
        "data_types": "数据类型概览",
        "missing_values": "缺失值",
        "time_series": "时间序列分析",
        "distribution": "分布分析",
        "correlation": "相关矩阵",
        "category_analysis": "类别分析",
        "top_categories": "顶级类别",
        "download_data": "下载处理后的数据",
        "select_date_col": "选择日期列",
        "select_value_col": "选择数值列",
        "select_category_col": "选择分类列",
        "no_date_col": "未检测到日期列",
        "no_numeric_col": "未检测到数值列",
        "no_category_col": "未检测到分类列",
        "error": "错误",
        "success": "成功",
        "file_uploaded": "文件上传成功",
        "select_language": "选择语言",
        "reset": "重置",
        "filter_data": "筛选数据",
        "apply_filter": "应用筛选",
        "clear_filter": "清除筛选",
        "data_summary": "数据摘要",
        "insights": "洞察",
        "trend": "趋势",
        "comparison": "比较",
        "forecast": "预测"
    }
}

# Initialize session state for language
if 'language' not in st.session_state:
    st.session_state.language = "English"

# Language selector in sidebar
with st.sidebar:
    st.title("🌍 Language / 语言 / Bahasa")
    selected_language = st.selectbox(
        LANGUAGES[st.session_state.language]["select_language"],
        options=list(LANGUAGES.keys()),
        index=list(LANGUAGES.keys()).index(st.session_state.language)
    )
    
    if selected_language != st.session_state.language:
        st.session_state.language = selected_language
        st.rerun()
    
    st.markdown("---")
    lang = LANGUAGES[st.session_state.language]

# ===================== MAIN APP =====================
st.title(f"📊 {lang['title']}")
st.markdown("---")

# File upload section
st.header(f"📁 {lang['upload']}")
st.write(lang['upload_desc'])

uploaded_file = st.file_uploader(
    lang['drag_drop'],
    type=['xlsx', 'xls'],
    help=lang['file_limit']
)

# Initialize session state for data
if 'df' not in st.session_state:
    st.session_state.df = None
if 'processed' not in st.session_state:
    st.session_state.processed = False

# Cache function for loading data
@st.cache_data
def load_excel_file(uploaded_file):
    """Cache function to load Excel file"""
    return pd.read_excel(uploaded_file, engine='openpyxl')

# Process uploaded file
if uploaded_file is not None:
    try:
        with st.spinner(lang['processing']):
            # Read Excel file with caching
            df = load_excel_file(uploaded_file)
            st.session_state.df = df
            st.session_state.processed = True
            
            st.success(f"✅ {lang['file_uploaded']}: {uploaded_file.name}")
            
    except Exception as e:
        st.error(f"❌ {lang['error']}: {str(e)}")
        st.info("💡 Tip: Install openpyxl with: `pip install openpyxl`")

# Display dashboard if data is available
if st.session_state.processed and st.session_state.df is not None:
    df = st.session_state.df.copy()
    
    # ===================== DATA PREVIEW =====================
    st.header(f"🔍 {lang['data_preview']}")
    
    # Data filters in sidebar
    with st.sidebar:
        st.header(f"🔧 {lang['filter_data']}")
        
        # Column type filters
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        date_cols = df.select_dtypes(include=['datetime', 'datetime64']).columns.tolist()
        categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
        
        # Convert potential date columns
        for col in df.columns:
            try:
                df[col] = pd.to_datetime(df[col], errors='ignore')
                if df[col].dtype == 'datetime64[ns]' and col not in date_cols:
                    date_cols.append(col)
            except:
                continue
        
        # Numeric filter
        if numeric_cols:
            selected_numeric = st.multiselect(
                f"📈 {lang['select_value_col']}",
                numeric_cols,
                default=numeric_cols[:min(2, len(numeric_cols))]
            )
        else:
            selected_numeric = []
            st.warning(lang['no_numeric_col'])
        
        # Date filter
        if date_cols:
            selected_date = st.selectbox(
                f"📅 {lang['select_date_col']}",
                date_cols
            )
        else:
            selected_date = None
            st.warning(lang['no_date_col'])
        
        # Categorical filter
        if categorical_cols:
            selected_category = st.selectbox(
                f"🏷️ {lang['select_category_col']}",
                categorical_cols
            )
        else:
            selected_category = None
            st.warning(lang['no_category_col'])
        
        # Row limit
        row_limit = st.slider("Rows to display", 5, 100, 10, key="row_limit_slider")
        
        # Show/Hide charts toggle
        show_all_charts = st.checkbox("Show all charts", value=True, key="show_charts_toggle")
    
    # Display filtered data preview
    st.dataframe(df.head(row_limit), use_container_width=True)
    
    # ===================== KPI SECTION =====================
    st.header(f"📈 {lang['kpi_section']}")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(lang['total_records'], len(df))
    
    with col2:
        st.metric(lang['total_columns'], len(df.columns))
    
    with col3:
        date_col_count = len(date_cols)
        st.metric(lang['date_columns'], date_col_count)
    
    with col4:
        numeric_col_count = len(numeric_cols)
        st.metric(lang['numeric_columns'], numeric_col_count)
    
    # Additional metrics row
    col5, col6, col7, col8 = st.columns(4)
    
    with col5:
        missing_total = df.isnull().sum().sum()
        st.metric(lang['missing_values'], missing_total)
    
    with col6:
        duplicate_rows = df.duplicated().sum()
        st.metric("Duplicate Rows", duplicate_rows)
    
    with col7:
        memory_usage = df.memory_usage(deep=True).sum() / 1024 / 1024
        st.metric("Memory Usage (MB)", f"{memory_usage:.2f}")
    
    with col8:
        if numeric_cols:
            avg_numeric = df[numeric_cols].mean().mean()
            st.metric("Avg Numeric Value", f"{avg_numeric:.2f}")
        else:
            st.metric("Avg Numeric Value", "N/A")
    
    st.markdown("---")
    
    # ===================== CHARTS SECTION =====================
    st.header(f"📊 {lang['charts_section']}")
    
    # Chart 1: Data Types Distribution
    if show_all_charts or st.checkbox("Show Data Types Chart", value=True, key="chart1_toggle"):
        st.subheader(f"1. {lang['data_types']}")
        dtype_counts = df.dtypes.value_counts().reset_index()
        dtype_counts.columns = ['Data Type', 'Count']
        
        fig1 = px.pie(
            dtype_counts, 
            values='Count', 
            names='Data Type',
            title=f"{lang['data_types']}",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        st.plotly_chart(fig1, use_container_width=True)
    
    # Chart 2: Time Series Analysis (if date column exists)
    if selected_date and selected_numeric and (show_all_charts or st.checkbox("Show Time Series Chart", value=True, key="chart2_toggle")):
        st.subheader(f"2. {lang['time_series']}")
        
        # Aggregate by date
        time_series_df = df.groupby(selected_date)[selected_numeric].sum().reset_index()
        
        if selected_numeric:
            fig2 = px.line(
                time_series_df, 
                x=selected_date, 
                y=selected_numeric[0],
                title=f"{lang['trend']}: {selected_numeric[0]} by {selected_date}",
                markers=True
            )
            
            # Add trendline
            fig2.update_traces(mode='lines+markers')
            
            st.plotly_chart(fig2, use_container_width=True)
    
    # Chart 3: Distribution Analysis
    if selected_numeric and (show_all_charts or st.checkbox("Show Distribution Charts", value=True, key="chart3_toggle")):
        st.subheader(f"3. {lang['distribution']}")
        
        col_chart3_1, col_chart3_2 = st.columns(2)
        
        with col_chart3_1:
            # Histogram
            fig3a = px.histogram(
                df, 
                x=selected_numeric[0],
                title=f"Histogram of {selected_numeric[0]}",
                nbins=30,
                color_discrete_sequence=['#636EFA']
            )
            st.plotly_chart(fig3a, use_container_width=True)
        
        with col_chart3_2:
            # Box plot
            fig3b = px.box(
                df, 
                y=selected_numeric[0],
                title=f"Box Plot of {selected_numeric[0]}",
                color_discrete_sequence=['#00CC96']
            )
            st.plotly_chart(fig3b, use_container_width=True)
    
    # Chart 4: Correlation Matrix
    if len(selected_numeric) > 1 and (show_all_charts or st.checkbox("Show Correlation Matrix", value=True, key="chart4_toggle")):
        st.subheader(f"4. {lang['correlation']}")
        
        corr_matrix = df[selected_numeric].corr()
        
        fig4 = px.imshow(
            corr_matrix,
            text_auto=True,
            aspect="auto",
            color_continuous_scale='RdBu_r',
            title=f"{lang['correlation']} Matrix",
            labels=dict(color="Correlation")
        )
        st.plotly_chart(fig4, use_container_width=True)
    
    # Chart 5: Category Analysis
    if selected_category and selected_numeric and (show_all_charts or st.checkbox("Show Category Analysis", value=True, key="chart5_toggle")):
        st.subheader(f"5. {lang['category_analysis']}")
        
        col_chart5_1, col_chart5_2 = st.columns(2)
        
        with col_chart5_1:
            # Top categories bar chart
            top_categories = df[selected_category].value_counts().head(10).reset_index()
            top_categories.columns = [selected_category, 'Count']
            
            fig5a = px.bar(
                top_categories,
                x=selected_category,
                y='Count',
                title=f"{lang['top_categories']} ({selected_category})",
                color='Count',
                color_continuous_scale='Viridis'
            )
            st.plotly_chart(fig5a, use_container_width=True)
        
        with col_chart5_2:
            # Category vs numeric value
            category_avg = df.groupby(selected_category)[selected_numeric[0]].mean().reset_index()
            category_avg = category_avg.sort_values(selected_numeric[0], ascending=False).head(10)
            
            fig5b = px.bar(
                category_avg,
                x=selected_category,
                y=selected_numeric[0],
                title=f"Avg {selected_numeric[0]} by {selected_category}",
                color=selected_numeric[0],
                color_continuous_scale='Plasma'
            )
            st.plotly_chart(fig5b, use_container_width=True)
    
    # ===================== DATA SUMMARY & INSIGHTS =====================
    st.markdown("---")
    st.header(f"💡 {lang['insights']}")
    
    col_insight1, col_insight2 = st.columns(2)
    
    with col_insight1:
        st.subheader(f"📋 {lang['data_summary']}")
        
        summary_stats = []
        
        # Basic stats
        summary_stats.append(f"**{lang['total_records']}**: {len(df)}")
        summary_stats.append(f"**{lang['total_columns']}**: {len(df.columns)}")
        summary_stats.append(f"**{lang['missing_values']}**: {df.isnull().sum().sum()}")
        
        if numeric_cols:
            summary_stats.append(f"**{lang['numeric_columns']}**: {len(numeric_cols)}")
            summary_stats.append(f"**Total numeric values**: {df[numeric_cols].sum().sum():,.2f}")
        
        if date_cols:
            summary_stats.append(f"**{lang['date_columns']}**: {len(date_cols)}")
            if len(date_cols) > 0:
                date_range = f"{df[date_cols[0]].min().date()} to {df[date_cols[0]].max().date()}"
                summary_stats.append(f"**Date range**: {date_range}")
        
        for stat in summary_stats:
            st.write(f"• {stat}")
    
    with col_insight2:
        st.subheader(f"🔍 Quick {lang['insights']}")
        
        insights = []
        
        # Generate insights based on data
        if missing_total > 0:
            insights.append(f"⚠️ **There are {missing_total} missing values** - Consider data imputation")
        
        if duplicate_rows > 0:
            insights.append(f"⚠️ **There are {duplicate_rows} duplicate rows** - Consider removing duplicates")
        
        if numeric_cols and len(selected_numeric) > 0:
            try:
                skewness = df[selected_numeric[0]].skew()
                if abs(skewness) > 1:
                    skew_type = "positive" if skewness > 0 else "negative"
                    insights.append(f"📊 **Data is {skew_type} skewed** (skewness: {skewness:.2f})")
            except:
                pass
        
        if selected_date and selected_numeric and len(df) > 1:
            try:
                first_val = df[selected_numeric[0]].iloc[0]
                last_val = df[selected_numeric[0]].iloc[-1]
                if first_val != 0:
                    growth = (last_val - first_val) / first_val * 100
                    insights.append(f"📈 **Growth: {growth:.2f}%** for {selected_numeric[0]}")
            except:
                pass
        
        if not insights:
            insights.append("✅ **Data looks good** - No significant data quality issues")
            insights.append("✅ **Normal distribution** - Numeric data is well distributed")
            insights.append("✅ **No outliers** - All values are within reasonable range")
        
        for insight in insights:
            st.write(f"• {insight}")
    
    # ===================== DATA DOWNLOAD =====================
    st.markdown("---")
    st.header(f"💾 {lang['download_data']}")
    
    # Create processed data
    processed_df = df.copy()
    
    # Convert to CSV for download
    csv_data = processed_df.to_csv(index=False).encode('utf-8')
    
    col_dl1, col_dl2, col_dl3 = st.columns(3)
    
    with col_dl1:
        st.download_button(
            label="📥 Download as CSV",
            data=csv_data,
            file_name="processed_data.csv",
            mime="text/csv",
            help="Download the processed data as CSV file",
            key="download_csv"
        )
    
    with col_dl2:
        # Excel download
        try:
            # Create Excel in memory
            import io
            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                processed_df.to_excel(writer, index=False, sheet_name='Data')
                
                # Add summary sheet
                summary_data = {
                    'Metric': [lang['total_records'], lang['total_columns'], 
                              lang['missing_values'], lang['date_columns']],
                    'Value': [len(df), len(df.columns), df.isnull().sum().sum(), len(date_cols)]
                }
                pd.DataFrame(summary_data).to_excel(writer, index=False, sheet_name='Summary')
            
            buffer.seek(0)
            
            st.download_button(
                label="📥 Download as Excel",
                data=buffer,
                file_name="processed_data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                help="Download the processed data as Excel file",
                key="download_excel"
            )
        except Exception as e:
            st.info(f"Install openpyxl for Excel download: `pip install openpyxl`")
            st.error(f"Excel error: {str(e)}")
    
    with col_dl3:
        if st.button(f"🔄 {lang['reset']}", use_container_width=True, key="reset_button"):
            st.session_state.df = None
            st.session_state.processed = False
            st.rerun()

else:
    # Show sample data or instructions
    st.info(f"👆 {lang['upload_desc']}")
    
    # Display sample data structure
    st.markdown("### 📋 Example Data Structure")
    sample_data = {
        'Date': pd.date_range('2024-01-01', periods=5),
        'Sales': [1000, 1500, 800, 2000, 1200],
        'Quantity': [10, 15, 8, 20, 12],
        'Category': ['A', 'B', 'A', 'C', 'B'],
        'Region': ['North', 'South', 'North', 'East', 'West']
    }
    sample_df = pd.DataFrame(sample_data)
    st.dataframe(sample_df, use_container_width=True)
    
    st.markdown("""
    **Ideal data should include:**
    - 📅 At least one date column
    - 🔢 At least one numeric column
    - 🏷️ At least one categorical column
    """)

# ===================== FOOTER =====================
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns(3)

with footer_col1:
    st.markdown("**Multi-Language Business Dashboard**")
    st.markdown("v2.0 • Powered by Streamlit")

with footer_col2:
    st.markdown("**Features:**")
    st.markdown("• 📊 5+ Interactive Charts")
    st.markdown("• 🌍 3 Languages")
    st.markdown("• 📈 Auto Data Detection")

with footer_col3:
    st.markdown("**Instructions:**")
    st.markdown("1. Upload Excel file")
    st.markdown("2. Select language")
    st.markdown("3. Explore insights")

# Add custom CSS for better appearance
st.markdown("""
<style>
    .stMetric {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #4e8cff;
    }
    .stDownloadButton > button {
        width: 100%;
    }
    .stButton > button {
        width: 100%;
    }
    h1, h2, h3 {
        color: #1f77b4;
    }
</style>
""", unsafe_allow_html=True)

# Debug info in sidebar
with st.sidebar:
    st.markdown("---")
    st.markdown("**Debug Info:**")
    st.write(f"Data loaded: {st.session_state.processed}")
    st.write(f"File uploaded: {uploaded_file is not None}")
    st.write(f"Data shape: {st.session_state.df.shape if st.session_state.df is not None else 'No data'}")
