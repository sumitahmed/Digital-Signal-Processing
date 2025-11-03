import matplotlib.pyplot as plt

# Flow of signal processing blocks
flow = ["Analog", "AAF", "Sampler", "Quantizer", "Encoder", 
        "Hold", "LPF", "Analog Out"]
x = range(len(flow))

# Create figure
plt.figure(figsize=(10, 2))

# Draw arrows and text boxes
for i in x:
    plt.plot([i, i+1], [0, 0], 'k-', lw=1.5)  # connecting line
    plt.plot(i + 1, 0, marker='>', color='k')  # arrowhead
    plt.text(i + 0.5, 0.1, flow[i], ha='center', fontsize=10, 
             bbox=dict(facecolor='lightgreen', edgecolor='black', boxstyle='round,pad=0.3'))

# Final output label
plt.text(len(flow) + 0.1, 0.1, flow[-1], ha='left', fontsize=10, 
         bbox=dict(facecolor='lightgreen', edgecolor='black', boxstyle='round,pad=0.3'))

# Hide axes
plt.axis('off')
plt.title("Analog → Digital → Analog Signal Chain", fontsize=12)
plt.tight_layout()
plt.show()
