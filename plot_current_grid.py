import matplotlib.pyplot as plt


def plot_current_grid(grid, ships):
    # extarct coorsinates and status
    for i in ships:
        x = int(i[0])
        y = int(i[1])
        z = float(i[2])
        grid[x, y] = z

    # plot
    fig = plt.matshow(grid)
    plt.colorbar()
    plt.show()
    return (grid)