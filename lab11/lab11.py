import numpy as  np
import matplotlib.pyplot as plt
from matplotlib import animation

def square_wave(terms):
    fig = plt.figure()   # type: plt.Figure
    ax = fig.gca()       # type: plt.Axes
    ax.set_xlim(-np.pi , 3 * np.pi)
    ax.set_ylim(-2,2)
    ax.set_aspect("equal")

    circles = []  # type: list
    circles.append(plt.Circle((0,0), 4 / np.pi , fill=0))
    ax.add_artist(circles[0])

    lines = []
    lines.append(plt.Line2D([0, 4/np.pi], [0,0]))
    ax.add_artist(lines[0])

    for i in range(1 , terms):
        circles.append( plt.Circle((circles[i-1].radius, 0), 4 / ( (2*i + 1) * np.pi), fill=0))
        lines.append( plt.Line2D( [circles[i-1].radius , circles[i-1].radius + circles[i].radius] , [0,0] ))
        ax.add_artist(circles[i])
        ax.add_artist(lines[i])


    pencile = plt.Line2D([],[])
    ax.add_artist(pencile)
    steps = 200

    wave_x = np.linspace(np.pi , terms * np.pi ,steps)
    wave_y = np.zeros(steps)
    wave = plt.Line2D(wave_x , wave_y)
    ax.add_artist(wave)


    angles = np.linspace(0, 2 * np.pi , steps+1)[:steps]



    def update(frame):
        t = angles[frame]
        new_X = []
        new_Y = []
        new_X.append(circles[0].radius * np.cos(t))
        new_Y.append(circles[0].radius * np.sin(t))

        lines[0].set_data([0, new_X[0]],[0, new_Y[0]])

        for i in range(1 , len(circles)):
            new_X.append( new_X[i-1] + circles[i].radius * np.cos((2*i + 1) * t))
            new_Y.append(new_Y[i-1] + circles[i].radius * np.sin((2*i + 1) * t))
            lines[i].set_data([new_X[i-1],new_X[i]] , [new_Y[i-1],new_Y[i]])
            circles[i].set_center((new_X[i-1],new_Y[i-1]))


        pencile.set_data([new_X[-1], np.pi],[new_Y[-1], new_Y[-1]])

        wave_y[1:] = wave_y[:-1]
        wave_y[0] = new_Y[-1]
        wave.set_ydata(wave_y)
        return

    anim = animation.FuncAnimation(fig, update ,init_func=lambda :None , frames=200 , interval=200//steps)

    plt.show()




if __name__ == '__main__':
    square_wave(10)