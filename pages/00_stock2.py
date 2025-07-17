import streamlit as st

def calculate_avg_price(purchase_list):
    total_amount = 0
    total_shares = 0
    for price, qty in purchase_list:
        total_amount += price * qty
        total_shares += qty
    if total_shares == 0:
        return 0
    return total_amount / total_shares

def calculate_target_price(avg_price, target_return_percent):
    return avg_price * (1 + target_return_percent / 100)

st.title("📌 주식 평균 단가 & 목표가 계산기 (순수 Python)")

st.markdown("### 💵 매수 내역 입력")
num_purchases = st.number_input("매수 횟수", min_value=1, value=2, step=1)
purchase_data = []

for i in range(num_purchases):
    st.markdown(f"**[{i+1}번째 매수]**")
    price = st.number_input(f" - 매수가 (원)", key=f"price_{i}", min_value=0.0, step=100.0)
    qty = st.number_input(f" - 수량 (주)", key=f"qty_{i}", min_value=0, step=1)
    purchase_data.append((price, qty))

target_return = st.number_input("🎯 목표 수익률 (%)", min_value=0.0, value=10.0, step=1.0)

if st.button("📈 계산하기"):
    avg_price = calculate_avg_price(purchase_data)
    target_price = calculate_target_price(avg_price, target_return)

    st.subheader("✅ 결과")
    st.write(f"📊 평균 매수가: **{avg_price:,.2f} 원**")
    st.write(f"🚀 목표 매도가 (수익률 {target_return}%): **{target_price:,.2f} 원**")
