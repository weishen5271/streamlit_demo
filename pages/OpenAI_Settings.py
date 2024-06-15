import streamlit as st
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state['OPENAI_API_KEY'] = ""

st.set_page_config(page_title="OpenAI Settings",layout="wide")
st.title("OpenAI Settings")
open_ai_key = st.text_input("API Key",value=st.session_state['OPENAI_API_KEY'],max_chars=None,key=None,type='default')
saved = st.button('Save')
if saved:
    st.session_state['OPENAI_API_KEY'] = open_ai_key