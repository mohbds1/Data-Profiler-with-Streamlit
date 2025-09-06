import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from ydata_profiling.config import Settings

st.set_page_config(page_title='Data Profiler', layout='wide')

# --- Helper functions ---
def get_filesize(file):
    """Get file size in MB safely for Streamlit UploadedFile"""
    size_bytes = file.size
    size_mb = size_bytes / (1024**2)
    return size_mb

def validate_file(file):
    """Validate file extension"""
    filename = file.name
    _, ext = filename.rsplit('.', 1)
    ext = '.' + ext.lower()
    if ext in ('.csv', '.xlsx'):
        return ext
    return False

def st_display_profile(pr):
    """Embed ProfileReport in Streamlit app via HTML safely"""
    pr_html = pr.to_html()
    import streamlit.components.v1 as components
    components.html(pr_html, height=1000, scrolling=True)

# --- Sidebar ---
with st.sidebar:
    uploaded_file = st.file_uploader("Upload .csv or .xlsx files (Max 10 MB)")
    if uploaded_file is not None:
        minimal = st.checkbox('Do you want minimal report?')

# --- Main App ---
if uploaded_file is not None:
    ext = validate_file(uploaded_file)
    if ext:
        filesize = get_filesize(uploaded_file)
        if filesize <= 10:
            # Load file
            if ext == '.csv':
                df = pd.read_csv(uploaded_file)
            else:
                xl_file = pd.ExcelFile(uploaded_file)
                sheet_tuple = tuple(xl_file.sheet_names)
                sheet_name = st.sidebar.selectbox('Select the sheet', sheet_tuple)
                df = xl_file.parse(sheet_name)

            # Generate report
            with st.spinner('Generating Profiling Report...'):
                pr = ProfileReport(df, minimal=minimal)
            st_display_profile(pr)

        else:
            st.error(f'Maximum allowed filesize is 10 MB. Received: {filesize:.2f} MB')
    else:
        st.error('Kindly upload only .csv or .xlsx files')
else:
    st.title('📊 Data Profiler')
    st.info('Upload your data in the left sidebar to generate profiling report')
