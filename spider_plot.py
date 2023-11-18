from matplotlib import pyplot as plt
import numpy as np

def spider_plot(x, labels=None, categories=None, colors=None, grids=0, save_path="plot.png"):
    if labels is not None:
        n = len(labels)
    else:
        n = len(x)
    if categories is not None:
        c = len(categories)
    else:
        c = len(x[0])
    if colors is None:
        colors = []
        for i in range(c):
            colors.append(plt.colormaps.get_cmap("hsv")(i / c))
    axis_calc_x = lambda i, c, factor=1.0, orig=50 : orig + orig * np.sin(i / c * 2 * np.pi) * factor
    axis_calc_y = lambda i, c, factor=1.0, orig=50 : orig + orig * np.cos(i / c * 2 * np.pi) * factor
    axis_coords = []
    for i in range(c):
        axis_coords.append((axis_calc_x(i, c), axis_calc_y(i, c)))
    axis_coords = np.array(axis_coords)
    plt.figure(figsize=(15, 15))
    for i in range(c):
        plt.plot([50, axis_coords[i, 0]], [50, axis_coords[i, 1]], color="silver")
        if categories is not None:
            plt.text(axis_calc_x(i, c, factor=1.05), axis_calc_y(i, c, factor=1.05), categories[i], ha='center', va='center')
    max_ = np.max(np.array(x), axis=0)
    if grids > 0:
        for i in range(1, grids + 1):
            plt.plot([axis_calc_x(j, c, factor=i / grids) for j in ([k for k in range(c)] + [0])], 
                        [axis_calc_y(j, c, factor=i / grids) for j in ([k for k in range(c)] + [0])], 
                        color="silver", linewidth=0.5)
    for i in range(n):
        plt.plot([axis_calc_x(j, c, factor=x[i][j] / max_[j]) for j in ([k for k in range(c)] + [0])], 
                 [axis_calc_y(j, c, factor=x[i][j] / max_[j]) for j in ([k for k in range(c)] + [0])], 
                 color=colors[i], marker="o", markersize=10, linewidth=4, label=labels[i] if labels is not None else None)
    if labels is not None:
        plt.legend()
    plt.xticks([])
    plt.yticks([])
    plt.savefig(save_path)
    plt.close()


spider_plot([[5, 6, 4, 3, 5], [2, 3, 2, 6.7, 1], [9, 8, 10, 1.5, 7]], 
            categories=["Speed", "Height", "Weight", "Durability", "Power"], 
            colors=["g", "y", "r"], 
            grids=4, 
            save_path="plot.png")
spider_plot([[5, 6, 4, 3, 5, 4, 2, 6], [2, 3, 2, 6.7, 1, 1.5, 2.2, 4.1], [9, 8, 10, 1.5, 7, 7.5, 4, 8]], 
            labels=["Alpha", "Bravo", "Charlie"], 
            categories=["Speed", "Height", "Weight", "Durability", "Intelligence", "Agility", "Power", "Creativity"], 
            colors=None, 
            grids=6, 
            save_path="plot2.png")
spider_plot([[3, 4, 3, 4], [2.5, 3, 2.6, 5.2], [1, 2, 1.1, 2.3], [4.5, 1.7, 3, 2]], 
            labels=["Alpha", "Bravo", "Charlie", "Delta"], 
            categories=["North", "East", "South", "West"], 
            colors=None, 
            grids=3, 
            save_path="plot3.png")

