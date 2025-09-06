import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from ydata_profiling.config import Settings
import os

st.set_page_config(page_title='Data Profiler', layout='wide')

# --- Helper functions ---
def get_filesize(file):
    size_bytes = os.path.getsize(file.name) if hasattr(file, 'name') else len(file.read())
    size_mb = size_bytes / (1024**2)
    return size_mb

def validate_file(file):
    filename = file.name
    _, ext = os.path.splitext(filename)
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
    uploaded_file = st.file_uploader("Upload .csv, .xlsx files not exceeding 10 MB")
    if uploaded_file is not None:
        st.write('Modes of Operation')
        minimal = st.checkbox('Do you want minimal report ?')
        display_mode = st.radio(
            'Display mode:',
            options=('Primary', 'Dark', 'Orange')
        )

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
            with st.spinner('Generating Report...'):
                # Configure theme
                if display_mode == "Dark":
                    config = Settings(plot={"theme": "dark"})
                elif display_mode == "Orange":
                    config = Settings(plot={"theme": "orange"})
                else:
                    config = Settings()

                pr = ProfileReport(df, minimal=minimal, config=config)

            st_display_profile(pr)
        else:
            st.error(f'Maximum allowed filesize is 10 MB. But received {filesize:.2f} MB')
    else:
        st.error('Kindly upload only .csv or .xlsx file')
else:
    st.title('📊 Data Profiler')
    st.info('Upload your data in the left sidebar to generate profiling report')
