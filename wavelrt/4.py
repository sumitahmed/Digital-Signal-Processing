import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, ArrowStyle
import matplotlib.patches as mpatches

# Create figure and axes
fig, ax = plt.subplots(figsize=(12, 3))
ax.axis('off')

# Define block positions and labels
blocks = [
    {"label": "Input Signal", "xy": (0.05, 0.5)},
    {"label": "Filter (LP/HP)", "xy": (0.25, 0.5)},
    {"label": "Downsample", "xy": (0.45, 0.5)},
    {"label": "Repeat", "xy": (0.65, 0.5)},
    {"label": "Reconstruct Signal", "xy": (0.85, 0.5)},
]

# Draw blocks
for block in blocks:
    ax.add_patch(FancyBboxPatch(
        (block["xy"][0], block["xy"][1] - 0.1), 0.15, 0.2,
        boxstyle="round,pad=0.02", edgecolor="black", facecolor="lightblue"
    ))
    ax.text(block["xy"][0] + 0.075, block["xy"][1],
            block["label"], ha="center", va="center", fontsize=10)

# Draw arrows between blocks
for i in range(len(blocks) - 1):
    start = blocks[i]["xy"]
    end = blocks[i + 1]["xy"]
    ax.annotate("",
                xy=(end[0], end[1]),
                xytext=(start[0] + 0.15, start[1]),
                arrowprops=dict(arrowstyle="->", lw=1.5))

plt.tight_layout()
plt.show()
