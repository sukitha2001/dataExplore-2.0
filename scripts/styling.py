import matplotlib.pyplot as plt
import seaborn as sns
import os

def apply_custom_style():
    """Applies a custom publication-quality style to Matplotlib and Seaborn."""
    sns.set_theme(style="white")

    plt.rcParams.update({
    'font.family': 'RobotoMono Nerd Font Mono',
    'font.size': 20,
    'axes.titlesize': 20,
    'axes.labelsize': 20,
    'xtick.labelsize': 20,
    'ytick.labelsize': 20,
    'legend.fontsize': 20,
    'figure.titlesize': 20,

    # Turn ticks ON
    'xtick.bottom': True,
    'ytick.left': True,

    # Tick direction & size
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    'xtick.major.size': 8,
    'ytick.major.size': 8,
    'xtick.minor.size': 4,
    'ytick.minor.size': 4,

    # Minor ticks visibility
    'xtick.minor.visible': True,
    'ytick.minor.visible': True,

    # Grid
    'axes.grid': True,
    'grid.alpha': 0.25,
    'axes.axisbelow': True,
    })

def save_figure(
    fig,
    x_label=None,
    y_label=None,
    other_label=None,
    save_path="plots",
    save_format="svg",
    filename=None,
    dpi=300,
    transparent=False,
    to_title=lambda s: str(s).title() if s else ""
):
    """
    Saves a Matplotlib figure with a generated filename based on labels.
    """
    if not save_path:
        return None

    os.makedirs(save_path, exist_ok=True)

    # Construct filename
    name_parts = []
    if filename is not None:
        name_parts.append(filename)
    elif x_label:
        name_parts.append(to_title(x_label))
    
    if y_label:
        name_parts.append(f"VS {to_title(y_label)}")
    elif other_label:
        name_parts.append(to_title(other_label))
        
    filename = " ".join(name_parts) if name_parts else "plot"

    if transparent:
        filename += " Transparent"

    full_path = os.path.join(save_path, f"{filename}.{save_format}")

    fig.savefig(
        full_path,
        format=save_format,
        dpi=dpi,
        bbox_inches="tight",
        transparent=transparent
    )

    return full_path

def style_ax(
    ax,
    minor_ticks=True,
    show_top=False,
    show_right=False,
    major_grid=True,
    minor_grid=True,
    major_grid_style=None,
    minor_grid_style=None
):
    if major_grid_style is None:
        major_grid_style = dict(linestyle='--', linewidth=0.8, alpha=0.4)

    if minor_grid_style is None:
        minor_grid_style = dict(linestyle=':', linewidth=0.5, alpha=0.3)

    if minor_ticks:
        ax.minorticks_on()

    ax.tick_params(
        axis='both',
        which='both',
        top=show_top,
        right=show_right
    )

    if major_grid:
        ax.grid(True, which='major', **major_grid_style)

    if minor_grid:
        ax.grid(True, which='minor', **minor_grid_style)

    return ax


def style_legend(
    ax,
    loc='upper center',
    bbox_to_anchor=(0.5, 1.10),
    ncol=4,
    frameon=False,
    reverse=False
):
    labels = [t.get_text() for t in ax.legend_.texts]
    if reverse:
        labels = labels[::-1]
    
    ax.legend(
        labels=labels,
        loc=loc,
        bbox_to_anchor=bbox_to_anchor,
        ncol=ncol,
        frameon=frameon
    )
    return ax


# Automatically apply styling when this module is imported
apply_custom_style()