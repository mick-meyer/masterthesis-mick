import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, axes = plt.subplots(3, 1, figsize=(12,5), sharex=True, dpi=300)

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
horizon = 4
overlap = 1

# --- Perfect foresight ---
axes[0].add_patch(
    patches.Rectangle((0, 0.4), 12, 0.2,
                      edgecolor="black", facecolor="skyblue", alpha=0.7)
)
axes[0].vlines([0,12], ymin=0.65, ymax=0.75, colors="blue")
axes[0].hlines(0.75, 0, 12, colors="blue")
axes[0].text(6, 0.8, "Horizon", ha="center", va="bottom", fontsize=11, color="blue")

axes[0].set_ylim(0,1)
axes[0].set_xlim(0,12)
axes[0].set_yticks([])
axes[0].set_ylabel("Perfect\nForesight", rotation=0, labelpad=50, fontsize=12, va="center")

# --- Rolling horizon with Overlap ---
start = 0
block = 0
while start < 12:
    rect = patches.Rectangle((start, 0.4), horizon, 0.2,
                             edgecolor="black", facecolor="lightgreen", alpha=0.7)
    axes[1].add_patch(rect)


    axes[1].hlines(0.75, start, start+horizon, colors="green")

    start += (horizon - overlap)
    block += 1

# Overlaps (always down)
start = 0
while start + horizon < 12:
    x0 = start + horizon - overlap
    axes[1].vlines([x0, x0+overlap], ymin=0.2, ymax=0.3, colors="darkgreen")
    axes[1].hlines(0.2, x0, x0+overlap, colors="darkgreen")
    axes[1].text(x0 + overlap/2, 0.15, "Overlap", ha="center", va="top", fontsize=10, color="darkgreen")
    start += (horizon - overlap)

axes[1].set_ylim(0,1)
axes[1].set_xlim(0,12)
axes[1].set_yticks([])
axes[1].set_ylabel("Rolling\nHorizon\nwith Overlap", rotation=0, labelpad=50, fontsize=12, va="center")

# --- Rolling horizon without Overlap ---
start = 0
while start < 12:
    rect = patches.Rectangle((start, 0.4), horizon, 0.2,
                             edgecolor="black", facecolor="orange", alpha=0.7)
    axes[2].add_patch(rect)
    axes[2].vlines([start, start+horizon], ymin=0.65, ymax=0.75, colors="darkorange")
    axes[2].hlines(0.75, start, start+horizon, colors="darkorange")
    axes[2].text(start + horizon/2, 0.8, "Horizon", ha="center", va="bottom", fontsize=10, color="darkorange")
    start += horizon

axes[2].set_ylim(0,1)
axes[2].set_xlim(0,12)
axes[2].set_yticks([])
axes[2].set_ylabel("Rolling\nHorizon\nwithout Overlap", rotation=0, labelpad=50, fontsize=12, va="center")
axes[2].set_xlabel("Year 2019", fontsize=12)
axes[2].set_xticks(range(0,12))
axes[2].set_xticklabels(months)

plt.tight_layout()
plt.show()
