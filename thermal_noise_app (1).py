import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

st.set_page_config(
    page_title="Thermal Noise Visual Analyzer",
    page_icon="📡",
    layout="wide"
)

kB = 1.380649e-23

st.title("📡 Thermal Noise Visual Analyzer")
st.markdown("**Team: Decode the Noise** | Automation & Robotics | SRM KTR Campus | QtHack04")
st.markdown("---")

st.latex(r"V_{rms} = \sqrt{4 \cdot k_B \cdot T \cdot R \cdot \Delta f}")

st.sidebar.header("⚙️ Parameters")
T = st.sidebar.slider("Temperature T (K)", min_value=10, max_value=1000, value=300, step=10)
R = st.sidebar.slider("Resistance R (Ω)", min_value=100, max_value=100000, value=10000, step=100)
df = st.sidebar.slider("Bandwidth Δf (Hz)", min_value=1000, max_value=1000000, value=100000, step=1000)

V_rms = np.sqrt(4 * kB * T * R * df)
V_rms_nV = V_rms * 1e9
PSD = 4 * kB * T * R
power = kB * T

col1, col2, col3 = st.columns(3)
col1.metric("V_rms (noise voltage)", f"{V_rms_nV:.3f} nV")
col2.metric("Power Spectral Density", f"{PSD:.2e} V²/Hz")
col3.metric("Total Noise Power", f"{power:.2e} W")

st.markdown("---")

plt.style.use('dark_background')
fig = plt.figure(figsize=(16, 10), facecolor='#0E1117')
gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.45, wspace=0.35)

BLUE   = '#4C9BE8'
TEAL   = '#2ECC9A'
AMBER  = '#F0A500'
CORAL  = '#E05A3A'
PURPLE = '#9B8BF4'

# 1. Time-domain waveform (full width top)
ax0 = fig.add_subplot(gs[0, :])
n_samples = 500
noise = np.random.normal(0, V_rms_nV, n_samples)
t_axis = np.arange(n_samples)
ax0.plot(t_axis, noise, color=BLUE, linewidth=0.8, alpha=0.9)
ax0.axhline(V_rms_nV, color=TEAL, linestyle='--', linewidth=1.2, label=f'+V_rms = {V_rms_nV:.2f} nV')
ax0.axhline(-V_rms_nV, color=CORAL, linestyle='--', linewidth=1.2, label=f'-V_rms = -{V_rms_nV:.2f} nV')
ax0.set_title("Time-Domain Noise Waveform (Gaussian White Noise)", color='white', fontsize=13, pad=10)
ax0.set_xlabel("Sample", color='#AAAAAA', fontsize=10)
ax0.set_ylabel("Voltage (nV)", color='#AAAAAA', fontsize=10)
ax0.tick_params(colors='#888888')
ax0.legend(fontsize=9, framealpha=0.3)
ax0.set_facecolor('#161B22')
for spine in ax0.spines.values():
    spine.set_edgecolor('#333333')

# 2. V_noise vs Temperature
ax1 = fig.add_subplot(gs[1, 0])
T_range = np.linspace(10, 1000, 200)
V_T = np.sqrt(4 * kB * T_range * R * df) * 1e9
ax1.plot(T_range, V_T, color=BLUE, linewidth=2)
ax1.axvline(T, color=AMBER, linestyle='--', linewidth=1.2, label=f'T={T}K')
ax1.scatter([T], [V_rms_nV], color=AMBER, s=60, zorder=5)
ax1.set_title("V_noise vs Temperature", color='white', fontsize=11)
ax1.set_xlabel("T (K)", color='#AAAAAA', fontsize=9)
ax1.set_ylabel("V_rms (nV)", color='#AAAAAA', fontsize=9)
ax1.tick_params(colors='#888888')
ax1.legend(fontsize=9, framealpha=0.3)
ax1.set_facecolor('#161B22')
for spine in ax1.spines.values():
    spine.set_edgecolor('#333333')

# 3. V_noise vs Resistance
ax2 = fig.add_subplot(gs[1, 1])
R_range = np.linspace(100, 100000, 300)
V_R = np.sqrt(4 * kB * T * R_range * df) * 1e9
ax2.plot(R_range, V_R, color=TEAL, linewidth=2)
ax2.axvline(R, color=AMBER, linestyle='--', linewidth=1.2, label=f'R={R}Ω')
ax2.scatter([R], [V_rms_nV], color=AMBER, s=60, zorder=5)
ax2.set_title("V_noise vs Resistance", color='white', fontsize=11)
ax2.set_xlabel("R (Ω)", color='#AAAAAA', fontsize=9)
ax2.set_ylabel("V_rms (nV)", color='#AAAAAA', fontsize=9)
ax2.tick_params(colors='#888888')
ax2.legend(fontsize=9, framealpha=0.3)
ax2.set_facecolor('#161B22')
for spine in ax2.spines.values():
    spine.set_edgecolor('#333333')

# 4. V_noise vs Bandwidth
ax3 = fig.add_subplot(gs[1, 2])
df_range = np.linspace(1000, 1000000, 300)
V_df = np.sqrt(4 * kB * T * R * df_range) * 1e9
ax3.plot(df_range / 1e3, V_df, color=PURPLE, linewidth=2)
ax3.axvline(df / 1e3, color=AMBER, linestyle='--', linewidth=1.2, label=f'Δf={df/1e3:.0f}kHz')
ax3.scatter([df / 1e3], [V_rms_nV], color=AMBER, s=60, zorder=5)
ax3.set_title("V_noise vs Bandwidth", color='white', fontsize=11)
ax3.set_xlabel("Δf (kHz)", color='#AAAAAA', fontsize=9)
ax3.set_ylabel("V_rms (nV)", color='#AAAAAA', fontsize=9)
ax3.tick_params(colors='#888888')
ax3.legend(fontsize=9, framealpha=0.3)
ax3.set_facecolor('#161B22')
for spine in ax3.spines.values():
    spine.set_edgecolor('#333333')

st.pyplot(fig)
plt.close()

st.markdown("---")
st.subheader("📊 Power Spectral Density (White Noise)")
fig2, ax4 = plt.subplots(figsize=(14, 3), facecolor='#0E1117')
freqs = np.linspace(1000, 1000000, 500)
psd_vals = np.full_like(freqs, PSD)
ax4.fill_between(freqs / 1e3, psd_vals * 1e20, alpha=0.35, color=CORAL)
ax4.plot(freqs / 1e3, psd_vals * 1e20, color=CORAL, linewidth=2)
ax4.set_title(f"PSD = 4·kB·T·R = {PSD:.2e} V²/Hz  (flat across all frequencies — white noise)", color='white', fontsize=11)
ax4.set_xlabel("Frequency (kHz)", color='#AAAAAA', fontsize=10)
ax4.set_ylabel("PSD (×10⁻²⁰ V²/Hz)", color='#AAAAAA', fontsize=10)
ax4.tick_params(colors='#888888')
ax4.set_facecolor('#161B22')
for spine in ax4.spines.values():
    spine.set_edgecolor('#333333')
st.pyplot(fig2)
plt.close()

st.markdown("---")
st.caption("Thermal Noise Visual Analyzer | Team Decode the Noise | QtHack04 — SRM KTR Campus")
