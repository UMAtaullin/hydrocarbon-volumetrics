import matplotlib.pyplot as plt


def plot_well_profile(depth, curves, title="ГИС-Кривые"):
    """Построение профиля скважины"""
    fig, axes = plt.subplots(1, len(curves), figsize=(12, 8))
    for i, (name, data) in enumerate(curves.items()):
        ax = axes[i]
        ax.plot(data, depth, linewidth=0.5)
        ax.set_title(name)
        ax.grid()
    plt.suptitle(title)
    plt.tight_layout()
    return fig
