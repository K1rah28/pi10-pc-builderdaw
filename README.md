
# 🖥️ PC Builder Pro

PC Builder Pro is a Python-based web application built with Streamlit that allows users to customize their desktop PC builds, estimate component costs, and check basic hardware compatibility.

## Features

- **Component Selection:** Choose a CPU, motherboard, GPU, RAM, storage, power supply, and computer case.
- **Budget Calculator:** Set a budget and calculate the total build cost and remaining balance.
- **Compatibility Checker:** Check CPU and motherboard socket compatibility, RAM type compatibility, integrated graphics availability, and PSU wattage recommendations.
- **Build Summary:** View a detailed breakdown of selected components and their prices.
- **CSV Export:** Download your PC build summary for reference.
- **Reset Build:** Restore the default component selections and budget.

## Technologies Used

- Python
- Streamlit
- Pandas
- GitHub

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
   ```

2. Navigate to the project directory:

   ```bash
   cd YOUR-REPOSITORY
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   streamlit run app.py
   ```

5. Open the local URL displayed in your terminal to use the application.

## Project Structure

```text
PC-Builder-Pro/
├── app.py
├── requirements.txt
└── README.md
```

## Disclaimer

The component prices and specifications are sample data provided for educational purposes. Actual prices and hardware compatibility should be verified with manufacturers and retailers before purchasing.

## Authors

Developed as a Computer Fundamentals and Programming (CFP) project.
