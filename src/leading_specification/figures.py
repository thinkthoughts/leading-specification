
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from .styles import FIGURE_DPI, LABEL_SIZE, LINE_WIDTH, TITLE_SIZE

def save_figure(path):
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output, dpi=FIGURE_DPI, bbox_inches="tight")
    return output

def plot_engineering_grammar(context, path):
    labels = ["Constraint", "Connected lanes", "Engineering objects", "State variables", "Observations", "Trailing indicators"]
    plt.figure(figsize=(8,9)); ax=plt.gca(); ax.axis("off")
    ys=np.linspace(.82,.18,len(labels))
    for i,(label,y) in enumerate(zip(labels,ys)):
        ax.add_patch(plt.Rectangle((.24,y-.045),.52,.09,fill=False,linewidth=LINE_WIDTH))
        ax.text(.5,y,label,ha="center",va="center",fontsize=LABEL_SIZE)
        if i<len(labels)-1:
            ax.annotate("",xy=(.5,ys[i+1]+.055),xytext=(.5,y-.055),arrowprops=dict(arrowstyle="->",linewidth=LINE_WIDTH))
    ax.text(.5,.94,context.specification.engineering_statement,ha="center",fontsize=TITLE_SIZE,fontweight="bold")
    return save_figure(path)

def plot_construction_sequence(context, path):
    seq=list(context.specification.construction_sequence)
    xs=np.linspace(.08,.92,len(seq))
    plt.figure(figsize=(13,4.5)); ax=plt.gca(); ax.axis("off")
    for i,(x,label) in enumerate(zip(xs,seq)):
        ax.add_patch(plt.Rectangle((x-.055,.45),.11,.18,fill=False,linewidth=LINE_WIDTH))
        ax.text(x,.54,label,ha="center",va="center",fontsize=9)
        if i<len(seq)-1:
            ax.annotate("",xy=(xs[i+1]-.065,.54),xytext=(x+.065,.54),arrowprops=dict(arrowstyle="->",linewidth=LINE_WIDTH))
    ax.text(.5,.90,"Construction Sequence",ha="center",fontsize=TITLE_SIZE,fontweight="bold")
    return save_figure(path)
