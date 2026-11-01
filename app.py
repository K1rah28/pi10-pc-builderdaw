
import streamlit as st

st.set_page_config(
    page_title="PC Builder",
    page_icon="🖥️",
    layout="centered"
)

st.title("🖥️ Simple PC Builder")
st.write("Choose your computer components and calculate your build cost.")

# Component prices in Philippine pesos
cpu_options = {
    "Intel Core i3-12100": {
        "price": 6500,
        "socket": "LGA1700"
    },
    "Intel Core i5-12400": {
        "price": 9500,
        "socket": "LGA1700"
    },
    "AMD Ryzen 5 5600": {
        "price": 8500,
        "socket": "AM4"
    }
}

motherboard_options = {
    "H610M (LGA1700)": {
        "price": 4500,
        "socket": "LGA1700",
        "ram_type": "DDR4"
    },
    "B660M (LGA1700)": {
        "price": 6500,
        "socket": "LGA1700",
        "ram_type": "DDR4"
    },
    "A520M (AM4)": {
        "price": 4000,
        "socket": "AM4",
        "ram_type": "DDR4"
    }
}

gpu_options = {
    "Integrated Graphics": 0,
    "NVIDIA RTX 4060": 18000,
    "AMD Radeon RX 7600": 16000
}

ram_options = {
    "8GB DDR4": 1800,
    "16GB DDR4": 3200,
    "32GB DDR4": 6000
}

storage_options = {
    "256GB SSD": 1500,
    "512GB SSD": 2500,
    "1TB SSD": 4000
}

psu_options = {
    "450W PSU": 2200,
    "550W PSU": 3000,
    "650W PSU": 4000,
    "750W PSU": 5500
}

case_options = {
    "Basic Micro-ATX Case": 2500,
    "Mid-Tower Case": 3500
}

# Component selection
st.header("Choose Your Components")

cpu_name = st.selectbox("CPU", list(cpu_options.keys()))
cpu = cpu_options[cpu_name]

motherboard_name = st.selectbox(
    "Motherboard",
    list(motherboard_options.keys())
)
motherboard = motherboard_options[motherboard_name]

gpu_name = st.selectbox("GPU", list(gpu_options.keys()))
gpu_price = gpu_options[gpu_name]

ram_name = st.selectbox("RAM", list(ram_options.keys()))
ram_price = ram_options[ram_name]

storage_name = st.selectbox(
    "Storage",
    list(storage_options.keys())
)
storage_price = storage_options[storage_name]

psu_name = st.selectbox("Power Supply", list(psu_options.keys()))
psu_price = psu_options[psu_name]

case_name = st.selectbox("Case", list(case_options.keys()))
case_price = case_options[case_name]

# Calculate total cost
total_price = (
    cpu["price"]
    + motherboard["price"]
    + gpu_price
    + ram_price
    + storage_price
    + psu_price
    + case_price
)

# Compatibility checks
st.divider()
st.header("Compatibility Check")

compatibility_issues = []

if cpu["socket"] != motherboard["socket"]:
    compatibility_issues.append(
        "The selected CPU and motherboard sockets do not match."
    )

if motherboard["ram_type"] != "DDR4":
    compatibility_issues.append(
        "The selected RAM type does not match the motherboard."
    )

if compatibility_issues:
    for issue in compatibility_issues:
        st.error(issue)
else:
    st.success("CPU and motherboard socket compatibility check passed.")

# Build summary
st.divider()
st.header("Build Summary")

components = [
    ("CPU", cpu_name, cpu["price"]),
    ("Motherboard", motherboard_name, motherboard["price"]),
    ("GPU", gpu_name, gpu_price),
    ("RAM", ram_name, ram_price),
    ("Storage", storage_name, storage_price),
    ("Power Supply", psu_name, psu_price),
    ("Case", case_name, case_price)
]

for component, name, price in components:
    st.write(f"**{component}:** {name} — ₱{price:,}")

st.divider()
st.subheader(f"Estimated Total: ₱{total_price:,}")

st.caption(
    "Prices are sample estimates in Philippine pesos. "
    "Check actual prices and component specifications before purchasing."
)
