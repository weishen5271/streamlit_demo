import streamlit as st
import json
from zhipuai import ZhipuAI

def main():
    client = None
    if "OPENAI_API_KEY" not in st.session_state:
        st.session_state["OPENAI_API_KEY"] = ""
    elif st.session_state["OPENAI_API_KEY"] != "":
        #chat = ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"])
        client = ZhipuAI(api_key=st.session_state['OPENAI_API_KEY'])
    if "PINECONE_API_KEY" not in st.session_state:
        st.session_state["PINECONE_API_KEY"] = ""

    if "PINECONE_ENVIRONMENT" not in st.session_state:
        st.session_state["PINECONE_ENVIRONMENT"] = ""

    st.set_page_config(page_title="Welcome to ASL", layout="wide")

    st.title("🤠 Welcome to ASL")

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    if client:
        with st.container():
            st.header("Chat with GPT")
            for message in st.session_state["messages"]:
                if isinstance(message, HumanMessage):
                    with st.chat_message("user"):
                        st.markdown(message.content)
                elif isinstance(message, AIMessage):
                    with st.chat_message("assistant"):
                        st.markdown(message.content)
            prompt = st.chat_input("Type something...")
            if prompt:
                st.session_state["messages"].append({"role": "user", "content": prompt})
                messages = st.session_state["messages"]
                with st.chat_message("user"):
                    st.markdown(prompt)
                print(messages)
                response = client.chat.completions.create(
                    model="glm-3-turbo",  # 填写需要调用的模型名称
                    messages = messages
                )
                ai_message = response.choices[0].message.model_dump_json()
                st.session_state["messages"].append(json.loads(ai_message))
                with st.chat_message("assistant"):
                    print(ai_message)
                    ai_message_json = json.loads(ai_message)
                    st.markdown(ai_message_json['content'])
    else:
        with st.container():
            st.warning("Please set your OpenAI API key in the settings page.")

if __name__ == '__main__':
    main()