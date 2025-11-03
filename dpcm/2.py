import matplotlib.pyplot as plt

# Define block labels and positions
blocks = [
    "Analog Signal", "Anti-Aliasing Filter", "Sampler", "Quantizer",
    "Encoder", "Decoder", "Prediction", "Hold Circuit", "LPF", "Reconstructed Signal"
]

# Create figure and axis
fig, ax = plt.subplots(figsize=(16, 3))
y = 0

# Plot blocks and arrows
for i, block in enumerate(blocks):
    x = i * 2.5  # spacing between blocks
    ax.text(x, y, block, ha='center', va='center', fontsize=9,
            bbox=dict(facecolor='lightblue', edgecolor='black', boxstyle='round,pad=0.3'))
    
    # Draw arrow to next block
    if i < len(blocks) - 1:
        ax.annotate('', xy=(x + 1.2, y), xytext=(x + 0.9, y),
                    arrowprops=dict(arrowstyle='->', lw=1.5, color='black'))

# Formatting
ax.set_xlim(-1, len(blocks) * 2.5)
ax.set_ylim(-1, 1)
ax.axis('off')
plt.title("DPCM Signal Processing Chain", fontsize=12)
plt.tight_layout()
plt.show()
