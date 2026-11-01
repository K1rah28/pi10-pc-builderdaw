
import streamlit as st

st.title("Simple PC Builder")
st.write("Choose your computer parts and calculate the total cost.")

# Prices are in Philippine pesos
cpu_prices = {
    "Intel Core i3": 5500,
    "Intel Core i5": 9500,
    "AMD Ryzen 5": 8500
}

cpu = st.selectbox("Choose a CPU", list(cpu_prices.keys()))

cpu_price = cpu_prices[cpu]

st.write("Selected CPU:", cpu)
st.write("CPU Price: ₱", cpu_price)
