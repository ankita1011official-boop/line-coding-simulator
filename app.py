import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Line Coding Simulator",
    page_icon="📡",
    layout="wide"
)

st.title("📡 Polar & Bipolar Line Coding Simulator")
st.write(
    "Enter a binary sequence and visualize its Polar NRZ-L and Bipolar AMI waveforms."
)

bits = st.text_input(
    "Enter Binary Sequence",
    value="10110010",
    help="Enter only 0 and 1."
)

if not bits:
    st.warning("Please enter a binary sequence.")
    st.stop()

if any(bit not in "01" for bit in bits):
    st.error("Invalid input! Please enter only 0 and 1.")
    st.stop()

# Polar NRZ-L: 0 -> -V, 1 -> +V
polar = [1 if bit == "1" else -1 for bit in bits]

# Bipolar AMI: 0 -> 0 V, each 1 alternates +V and -V
bipolar = []
last_polarity = -1

for bit in bits:
    if bit == "0":
        bipolar.append(0)
    else:
        last_polarity = -last_polarity
        bipolar.append(last_polarity)

def make_waveform(values):
    x, y = [], []
    for i, value in enumerate(values):
        x.extend([i, i + 1])
        y.extend([value, value])
    return x, y

def plot_waveform(values, title, rule):
    x, y = make_waveform(values)

    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(x, y, linewidth=2)
    ax.axhline(0, linewidth=0.8)

    # Bit boundary lines
    for i in range(len(bits) + 1):
        ax.axvline(i, linewidth=0.6, alpha=0.35)

    ax.set_xlim(0, len(bits))
    ax.set_ylim(-1.5, 1.5)
    ax.set_xticks([i + 0.5 for i in range(len(bits))])
    ax.set_xticklabels(list(bits))
    ax.set_yticks([-1, 0, 1])
    ax.set_yticklabels(["−V", "0", "+V"])
    ax.set_xlabel("Bit")
    ax.set_ylabel("Voltage")
    ax.set_title(title)
    ax.grid(True, axis="y", alpha=0.3)

    st.write(f"**Rule:** {rule}")
    st.pyplot(fig)
    plt.close(fig)

st.subheader("Input Binary Sequence")
st.code(bits)

col1, col2 = st.columns(2)

with col1:
    st.metric("Number of bits", len(bits))

with col2:
    st.metric("Number of 1s", bits.count("1"))

st.divider()

st.subheader("1. Polar NRZ-L")
plot_waveform(
    polar,
    "Polar NRZ-L",
    "0 → −V and 1 → +V"
)

st.subheader("2. Bipolar AMI")
plot_waveform(
    bipolar,
    "Bipolar AMI",
    "0 → 0 V and successive 1s alternate +V and −V"
)

st.divider()

st.subheader("Encoding Values")

table_data = {
    "Bit": list(bits),
    "Polar NRZ-L": ["+V" if x == 1 else "−V" for x in polar],
    "Bipolar AMI": [
        "+V" if x == 1 else "−V" if x == -1 else "0 V"
        for x in bipolar
    ],
}

st.table(table_data)

st.info(
    "Polar NRZ-L uses two voltage levels. Bipolar AMI uses three levels "
    "(+V, 0 V, and −V), with each binary 1 alternating polarity."
)

st.caption("Line Coding Simulator • Python + Streamlit + Matplotlib")
