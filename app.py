
import streamlit as st
import pandas as pd

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="PC Builder Pro",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. CUSTOM UI DESIGN
# ==========================================

st.markdown("""
<style>
    .stApp {
        background-color: #0b0e14;
        color: #f1f5f9;
    }

    [data-testid="stSidebar"] {
        background-color: #111827;
    }

    .main-title {
        font-size: 38px;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 0;
    }

    .subtitle {
        color: #94a3b8;
        font-size: 15px;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 21px;
        font-weight: 700;
        color: #a78bfa;
        margin-bottom: 12px;
    }

    .total-price {
        font-size: 34px;
        font-weight: 800;
        color: #a78bfa;
    }

    div[data-testid="stMetric"] {
        background: #151b2a;
        border: 1px solid #30394d;
        padding: 15px;
        border-radius: 12px;
    }

    div.stButton > button {
        background-color: #7c3aed;
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 600;
    }

    div.stButton > button:hover {
        background-color: #6d28d9;
        color: white;
    }

    hr {
        border-color: #30394d;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. COMPONENT DATABASE
# ==========================================

cpu_options = {
    "Intel Core i3-12100": {
        "price": 6500,
        "socket": "LGA1700",
        "integrated_graphics": True
    },
    "Intel Core i5-12400": {
        "price": 9500,
        "socket": "LGA1700",
        "integrated_graphics": True
    },
    "AMD Ryzen 5 5600": {
        "price": 8500,
        "socket": "AM4",
        "integrated_graphics": False
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
    },
    "MSI B550M PRO-VDH WiFi": {
        "price": 6050,
        "socket": "AM4",
        "ram_type": "DDR4"
    }
}

gpu_options = {
    "Integrated Graphics": {
        "price": 0,
        "recommended_psu": 300
    },
    "NVIDIA RTX 4060": {
        "price": 18000,
        "recommended_psu": 550
    },
    "AMD Radeon RX 7600": {
        "price": 16000,
        "recommended_psu": 550
    }
}

ram_options = {
    "8GB DDR4": {
        "price": 1800,
        "type": "DDR4"
    },
    "16GB DDR4": {
        "price": 3200,
        "type": "DDR4"
    },
    "32GB DDR4": {
        "price": 6000,
        "type": "DDR4"
    },
    "Lexar Thor 16GB (2x8GB) DDR4 3200MHz": {
        "price": 6400,
        "type": "DDR4"
    }
}

storage_options = {
    "256GB SSD": 1500,
    "512GB SSD": 2500,
    "1TB SSD": 4000,
    "ADATA Legend 860 1TB NVMe PCIe 4.0": 10200
}

psu_options = {
    "450W PSU": {
        "price": 2200,
        "wattage": 450
    },
    "550W PSU": {
        "price": 3000,
        "wattage": 550
    },
    "650W PSU": {
        "price": 4000,
        "wattage": 650
    },
    "750W PSU": {
        "price": 5500,
        "wattage": 750
    },
    "Cougar Atlas 650W 80+ Bronze": {
        "price": 3200,
        "wattage": 650
    }
}

case_options = {
    "Basic Micro-ATX Case": 2500,
    "Mid-Tower Case": 3500
}

# ==========================================
# 4. DEFAULT BUILD AND RESET
# ==========================================

defaults = {
    "cpu": "AMD Ryzen 5 5600",
    "motherboard": "MSI B550M PRO-VDH WiFi",
    "gpu": "NVIDIA RTX 4060",
    "ram": "Lexar Thor 16GB (2x8GB) DDR4 3200MHz",
    "storage": "ADATA Legend 860 1TB NVMe PCIe 4.0",
    "psu": "Cougar Atlas 650W 80+ Bronze",
    "case": "Basic Micro-ATX Case",
    "budget": 50000
}


def reset_build():
    for key, value in defaults.items():
        st.session_state[key] = value


for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ==========================================
# 5. HEADER
# ==========================================

st.markdown(
    '<p class="main-title">🖥️ PC BUILDER PRO</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Build your dream PC. '
    'Choose components, check compatibility, '
    'and calculate your budget.</p>',
    unsafe_allow_html=True
)

st.divider()

# ==========================================
# 6. SIDEBAR
# ==========================================

with st.sidebar:
    st.markdown("## ⚙️ Build Settings")

    st.number_input(
        "Your Budget (₱)",
        min_value=0,
        step=1000,
        key="budget"
    )

    st.caption("Set your maximum PC build budget.")

    st.divider()

    st.markdown("### Build Information")
    st.write("Currency: Philippine Peso (₱)")
    st.write("Platform: Desktop PC")
    st.write("Version: 2.0")

    st.divider()

    st.button(
        "🔄 Reset Build",
        on_click=reset_build,
        use_container_width=True
    )

# ==========================================
# 7. COMPONENT SELECTION
# ==========================================

left_column, right_column = st.columns([1.5, 1])

with left_column:
    st.markdown(
        '<p class="section-title">🔧 Select Your Components</p>',
        unsafe_allow_html=True
    )

    with st.container(border=True):
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🧠 Processor")

            cpu_name = st.selectbox(
                "Choose CPU",
                list(cpu_options.keys()),
                key="cpu"
            )

            st.caption(f"₱{cpu_options[cpu_name]['price']:,}")

        with col2:
            st.markdown("### 🧩 Motherboard")

            motherboard_name = st.selectbox(
                "Choose Motherboard",
                list(motherboard_options.keys()),
                key="motherboard"
            )

            st.caption(
                f"₱{motherboard_options[motherboard_name]['price']:,}"
            )

        st.divider()

        col3, col4 = st.columns(2)

        with col3:
            st.markdown("### 🎮 Graphics Card")

            gpu_name = st.selectbox(
                "Choose GPU",
                list(gpu_options.keys()),
                key="gpu"
            )

            st.caption(f"₱{gpu_options[gpu_name]['price']:,}")

        with col4:
            st.markdown("### 💾 Memory")

            ram_name = st.selectbox(
                "Choose RAM",
                list(ram_options.keys()),
                key="ram"
            )

            st.caption(f"₱{ram_options[ram_name]['price']:,}")

        st.divider()

        col5, col6 = st.columns(2)

        with col5:
            st.markdown("### 📀 Storage")

            storage_name = st.selectbox(
                "Choose Storage",
                list(storage_options.keys()),
                key="storage"
            )

            st.caption(f"₱{storage_options[storage_name]:,}")

        with col6:
            st.markdown("### ⚡ Power Supply")

            psu_name = st.selectbox(
                "Choose PSU",
                list(psu_options.keys()),
                key="psu"
            )

            st.caption(f"₱{psu_options[psu_name]['price']:,}")

        st.divider()

        st.markdown("### 🖥️ Computer Case")

        case_name = st.selectbox(
            "Choose Case",
            list(case_options.keys()),
            key="case"
        )

        st.caption(f"₱{case_options[case_name]:,}")

# ==========================================
# 8. GET SELECTED COMPONENTS
# ==========================================

cpu = cpu_options[cpu_name]
motherboard = motherboard_options[motherboard_name]
gpu = gpu_options[gpu_name]
ram = ram_options[ram_name]
psu = psu_options[psu_name]

components = [
    ("CPU", cpu_name, cpu["price"]),
    ("Motherboard", motherboard_name, motherboard["price"]),
    ("GPU", gpu_name, gpu["price"]),
    ("RAM", ram_name, ram["price"]),
    ("Storage", storage_name, storage_options[storage_name]),
    ("Power Supply", psu_name, psu["price"]),
    ("Case", case_name, case_options[case_name])
]

total_price = sum(price for _, _, price in components)

# ==========================================
# 9. BUILD SUMMARY
# ==========================================

with right_column:
    st.markdown(
        '<p class="section-title">📋 Build Summary</p>',
        unsafe_allow_html=True
    )

    with st.container(border=True):
        st.markdown("### Estimated Total")

        st.markdown(
            f'<p class="total-price">₱{total_price:,}</p>',
            unsafe_allow_html=True
        )

        st.divider()

        for component, name, price in components:
            st.markdown(f"**{component}**")
            st.caption(name)
            st.write(f"₱{price:,}")

        st.divider()

        remaining = st.session_state.budget - total_price

        st.metric(
            "Remaining Budget",
            f"₱{remaining:,}"
        )

        if remaining >= 0:
            st.success("Your build is within budget!")
        else:
            st.error(
                f"Your build exceeds your budget by ₱{abs(remaining):,}."
            )

# ==========================================
# 10. COMPATIBILITY CHECK
# ==========================================

st.divider()

st.markdown(
    '<p class="section-title">🔍 Compatibility Check</p>',
    unsafe_allow_html=True
)

issues = []
warnings = []

# CPU and motherboard socket
if cpu["socket"] != motherboard["socket"]:
    issues.append(
        "CPU and motherboard sockets do not match."
    )

# RAM compatibility
if ram["type"] != motherboard["ram_type"]:
    issues.append(
        "RAM type is not supported by the selected motherboard."
    )

# Integrated graphics check
if (
    gpu_name == "Integrated Graphics"
    and not cpu["integrated_graphics"]
):
    issues.append(
        "The selected CPU has no integrated graphics. "
        "Choose a dedicated GPU."
    )

# PSU recommendation
if psu["wattage"] < gpu["recommended_psu"]:
    warnings.append(
        f"The selected GPU has a suggested PSU rating of "
        f"{gpu['recommended_psu']}W or higher. "
        "Your selected PSU may be insufficient."
    )

check1, check2 = st.columns(2)

with check1:
    if issues:
        st.error("❌ Compatibility Issues Found")

        for issue in issues:
            st.write(f"• {issue}")
    else:
        st.success("✅ Basic compatibility checks passed.")

with check2:
    if warnings:
        st.warning("⚠️ Power Supply Warning")

        for warning in warnings:
            st.write(f"• {warning}")
    else:
        st.success("✅ PSU meets the suggested wattage rating.")

# ==========================================
# 11. DETAILED BUILD TABLE
# ==========================================

st.divider()

st.markdown(
    '<p class="section-title">📊 Detailed Price Breakdown</p>',
    unsafe_allow_html=True
)

build_data = pd.DataFrame(
    components,
    columns=["Component", "Selected Product", "Price (₱)"]
)

st.dataframe(
    build_data,
    use_container_width=True,
    hide_index=True
)

st.markdown(f"### Total Build Cost: ₱{total_price:,}")

# ==========================================
# 12. DOWNLOAD BUILD SUMMARY
# ==========================================

csv_data = build_data.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Build Summary",
    data=csv_data,
    file_name="my_pc_build.csv",
    mime="text/csv",
    use_container_width=True
)

# ==========================================
# 13. FOOTER
# ==========================================

st.divider()

st.caption(
    "PC Builder Pro | Sample prices in Philippine pesos. "
    "Prices and specifications should be verified with actual "
    "retailers and manufacturer documentation before purchasing."
)
