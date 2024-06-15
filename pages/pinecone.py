import streamlit as st
if "PINECONE_API_KEY" not in st.session_state:
    st.session_state['PINECONE_API_KEY'] = ""

if "PINECONE_ENVIRONMENT" not in st.session_state:
    st.session_state['PINECONE_ENVIRONMENT'] = ""

st.set_page_config(page_title="PINECONE Settings", layout="wide")
st.title("PINECONE setting")
pipnecone_key = st.text_input("PINECONE Key", value=st.session_state['PINECONE_API_KEY'], max_chars=None, key=None,
                            type='default')
pipnecone_environment = st.text_input("PINECONE ENVIRONMENT", value=st.session_state['PINECONE_ENVIRONMENT'], max_chars=None, key=None,
                            type='default')
saved = st.button('Save')
if saved:
    st.session_state['PINECONE_API_KEY'] = pipnecone_key
    st.session_state['PINECONE_ENVIRONMENT'] = pipnecone_environment