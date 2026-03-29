# Thermal Noise Visual Analyzer 📡

**Team:** Decode the Noise  
**Department:** Automation and Robotics  
**Campus:** SRM KTR Campus  
**Event:** QtHack04  

## Team Members
- N. Sharanya
- Ansridhan Anandhan
- I Anisha
- CH. Harshavardhan

---

## Problem Statement
Build an interactive visual analyzer that models and visualizes thermal noise voltage based on the Johnson-Nyquist formula.

## Formula
```
V_rms = sqrt(4 · kB · T · R · Δf)
```
Where:
- `kB` = 1.38 × 10⁻²³ J/K (Boltzmann constant)
- `T` = Temperature (Kelvin)
- `R` = Resistance (Ohms)
- `Δf` = Bandwidth (Hz)

---

## Features
- Live sliders for Temperature, Resistance, and Bandwidth
- Time-domain noise waveform (Gaussian white noise)
- V_noise vs Temperature graph
- V_noise vs Resistance graph
- V_noise vs Bandwidth graph
- Power Spectral Density (PSD) plot

---

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/thermal-noise-analyzer.git
cd thermal-noise-analyzer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
python -m streamlit run thermal_noise_app.py
```

### 4. Open in browser
```
http://localhost:8501
```

---

## Tech Stack
- Python
- Streamlit
- NumPy
- Matplotlib
