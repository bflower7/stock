import streamlit as st

def calculate_profit(buy_price, current_price, shares):
    investment = buy_price * shares
    current_value = current_price * shares
    profit = current_value - investment
    return profit, (profit / investment) * 100

# Streamlit 앱 UI
st.title("💹 주식 수익률 계산기 (순수 Python)")

buy_price = st.number_input("📉 매수 가격 (1주당)", min_value=0.0, value=50000.0, step=100.0)
current_price = st.number_input("📈 현재 가격 (1주당)", min_value=0.0, value=60000.0, step=100.0)
shares = st.number_input("🧾 보유 주식 수", min_value=1, value=10, step=1)

if st.button("수익률 계산"):
    profit, profit_rate = calculate_profit(buy_price, current_price, shares)
    st.subheader("📊 결과")
    st.write(f"총 수익금: {profit:,.0f} 원")
    st.write(f"수익률: {profit_rate:.2f}%")


