import streamlit as st

st.title("ユーザー情報表示")

# session_stateからデータを取得して表示
if ('user_name' in st.session_state and st.session_state.user_name):
    st.success("保存されている情報:")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("名前",st.session_state.user_name)
        st.metric("国籍",st.session_state.kokuseki)
        st.metric("学年",st.session_state.grade)
        st.metric("職業",st.session_state.syokugyou)
        st.metric("性別",st.session_state.seibetu)
    with col2:
        if st.session_state.get('hobbies'):
            st.write('**趣味:**')
            for hobby in st.session_state.hobbies:
                st.write(f"• {hobby}")
        else:
            st.write("**趣味:** 未設定")



else:
    st.error(" ユーザー情報が設定されていません")
    st.write("メインページで情報を入力してください")