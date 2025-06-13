from dotenv import load_dotenv

load_dotenv()
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# 環境変数をロード
load_dotenv()

# LLM応答を取得する関数
def get_llm_response(input_text, expert_type):
    # 専門家の種類に応じたシステムメッセージを設定
    if expert_type == "プログラマー":
        system_message = "You are a programming expert. Provide detailed and accurate programming advice."
    elif expert_type == "医療関係者":
        system_message = "You are a medical expert. Provide detailed and accurate medical advice."
    else:
        system_message = "You are a helpful assistant."

    # LangChainのLLMを初期化
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    # メッセージを構築
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=input_text),
    ]

    # LLMからの応答を取得
    result = llm(messages)
    return result.content

# Streamlitアプリの構築
st.title("専門家に質問できるAIツール")
st.write("このツールでは、以下の手順でAIに質問できます：")
st.markdown("""
1. 入力フォームに質問を入力してください。
2. ラジオボタンでAIに振る舞わせたい専門家の種類を選択してください。
3. 「送信」ボタンを押すと、AIからの回答が表示されます。
""")

# 入力フォーム
input_text = st.text_input("質問を入力してください:")

# ラジオボタンで専門家の種類を選択
expert_type = st.radio(
    "AIに振る舞わせたい専門家の種類を選択してください:",
    ("プログラマー", "医療関係者")
)

# 送信ボタン
if st.button("送信"):
    if input_text.strip() == "":
        st.warning("質問を入力してください。")
    else:
        # LLMからの応答を取得
        response = get_llm_response(input_text, expert_type)
        # 結果を表示
        st.subheader("AIからの回答:")
        st.write(response)