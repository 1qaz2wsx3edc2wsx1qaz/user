import streamlit as st

st.title("ユーザー情報")

# セッション状態の初期化（重複とバグを削除）
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'kokuseki' not in st.session_state:
    st.session_state.kokuseki = ""
if 'grade' not in st.session_state:
    st.session_state.grade = ""
if 'hobbies' not in st.session_state:
    st.session_state.hobbies = []  # multiselectはリストで初期化すると安全です
if 'seibetu' not in st.session_state:
    st.session_state.syokugyou = ""
if 'syokugyou' not in st.session_state:
    st.session_state.sykugyou = ""


# 入力フォームの配置
name = st.text_input("名前")
kokuseki = st.text_input("国籍")
grade = st.selectbox("学年",
    ["", "小学五年", "小学六年", "中学一年", "中学二年", "中学三年", "社会人"])
hobbies = st.multiselect("趣味",  # 「l」を削除
    ["読書", "スポーツ", "ゲーム", "音楽", "絵画", "ドライブ", "その他"]) # カンマを追加
syokugyou = st.selectbox("職業",
    ["apple", "google", "Microsoft", "サラリーマン", "先生", "バイト", "パート", "ニート", "その他"])
seibetu = st.selectbox("性別",
    ["男", "女", "その他"])

# 保存ボタンの処理
if st.button("情報を保存"):
    st.session_state.user_name = name
    st.session_state.kokuseki = kokuseki
    st.session_state.grade = grade
    st.session_state.hobbies = hobbies
    st.session_state.syokugyou = syokugyou
    st.session_state.seibetu = seibetu
    st.success("情報を保存したぞ❕")

        # 職業に合わせたおもしろ演出
    if syokugyou in ["apple", "google", "Microsoft"]:
        st.balloons() # エリートには風船を飛ばす！
        st.info("す・す・すげえ！IT企業のエリートだ！")
    elif syokugyou == "ニート":
        st.warning("お家最高！でもたまには外に出ようね！")
            # 👇ここを新しく追加したよ！バイトかパートだったら応援する！
    elif syokugyou in ["サラリーマン", "先生", "バイト", "パート"]:
        st.success("🔥 今日の頑張りが未来を作る！出世目指してファイトだー！")


    else:
        # 「その他」や「未選択」のときは普通のメッセージ
        st.write("情報をしっかり登録したよ！")
