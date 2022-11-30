#import libraries 
import numpy as np 
import pandas as pd 
import streamlit as st 
import seaborn as sns 
from pandas_profiling import ProfileReport 
from streamlit_pandas_profiling import st_profile_report 

#webapp ka title 
st.write('''
# **Exploratory Data Analysis web application**
This app is developed by Zohair called **EDA app**
''')

#how to upload a file form PC

with st.sidebar.header("upload your dataset (.CSV)"):
    upload_file = st.sidebar.file_uploader("Upload uour file, ", type=["csv"])
    df = sns.load_dataset("titanic")
    st.sidebar.markdown("[Example CSV File](df)")
    
#profiling report 

if upload_file is not None:
    @st.cache
    def load_csv():
     csv = pd.read_csv(upload_file)
     return csv 
    
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DF**')
    st.write(df)
    st.write('---')
    st.header('**Profiling Report with pandas**')
    st_profile_report(pr)
else:
    st.info('Awaiting For CSV file')
    if st.button('Press to use example data'):
        #example
        @st.cache
        def load_data():
            a = pd.DataFrame(np.random.rand(100,5), columns=['age','banana','codanics'
                             ,'Denmark','Ear'])
            return a 
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DF**')
        st.write(df)
        st.write('---')
        st.header('**Profiling Report with pandas**')
        st_profile_report(pr)
        
    
        
          
    
    

    



