import streamlit as st
import random

# 1. 일본어 동사 데이터 (기초 10개)
verbs = [
    {"jp": "たべる", "kr": "먹다"},
    {"jp": "のむ", "kr": "마시다"},
    {"jp": "いく", "kr": "가다"},
    {"jp": "くる", "kr": "오다"},
    {"jp": "みる", "kr": "보다"},
    {"jp": "きく", "kr": "듣다"},
    {"jp": "はなす", "kr": "말하다"},
    {"jp": "かう", "kr": "사다"},
    {"jp": "よむ", "kr": "읽다"},
    {"jp": "かく", "kr": "쓰다"},
]

# 2. Streamlit UI
st.title("🇯🇵 일본어 동사 퀴즈")

# 퀴즈 출제용 무작위 동사
quiz = random.choice(verbs)
correct_answer = quiz["kr"]

# 오답 후보 생성
options = [v["kr"] for v in random.sample(verbs, 3) if v["kr"] != correct_answer]
if correct_answer not in options:
    options[random.randint(0, 2)] = correct_answer
random.shuffle(options)

st.markdown(f"### ❓ 아래 일본어 동사의 뜻은 무엇일까요?")
st.markdown(f"**➡ {quiz['jp']}**")

selected = st.radio("정답을 선택하세요", options)

if st.button("제출하기"):
    if selected == correct_answer:
        st.success("✅ 정답입니다! 잘했어요!")
    else:
        st.error(f"❌ 오답입니다. 정답은 **{correct_answer}** 입니다.")
