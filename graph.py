import matplotlib as mpl
import matplotlib.pyplot as plt
def plot_v_t():
    f = open('stats.txt', 'r')
    i=0
    x =[]
    y = []
    for line in f:
        if i == 1 :
            vx = float(line.split()[3])
            vy = float(line.split()[4])
            v = (vx**2+vy**2)**0.5
            y.append(v)
            x.append(float(line.split()[0]))
        i = 1
    fig, ax = plt.subplots()
    ax.plot(x,  y)      
    ax.set(xlabel='time (s)', ylabel='velocity (м/с)',
       title='v (t)')
    ax.locator_params(tight=True, axis = 'x', nbins=10)
    ax.locator_params(tight=True, axis = 'y', nbins=10)
    ax.grid()
    fig.savefig("test.png")
    plt.tight_layout()
    plot_v_t()

def plot_r_t():
    f = open('stats.txt', 'r')
    i=0
    x =[]
    y = []
    for line in f:
        if i == 1 :
            d_x = float(line.split()[1])
            d_y = float(line.split()[2])
            r = (d_x**2+d_y**2)**0.5
            y.append(r)
            x.append(float(line.split()[0]))
        i = 1
    fig, ax = plt.subplots()
    ax.plot(x,  y)      
    ax.set(xlabel='time (c)', ylabel='distance (м)',
       title='r (t)')
    ax.locator_params(tight=True, axis = 'x', nbins=10)
    ax.locator_params(tight=True, axis = 'y', nbins=10)
    ax.grid()
    fig.savefig("test.png")
    plt.tight_layout()
    plot_r_t()

def plot_v_r():
    f = open('stats.txt', 'r')
    i=0
    x =[]
    y = []
    for line in f:
        if i == 1 :
            vx = float(line.split()[3])
            vy = float(line.split()[4])
            d_x = float(line.split()[1])
            d_y = float(line.split()[2])
            v = (vx**2+vy**2)**0.5
            r = (d_x**2+d_y**2)**0.5
            y.append(v)
            x.append(r)
        i = 1
    fig, ax = plt.subplots()
    ax.plot(x,  y)      
    ax.set(xlabel='distance (м)', ylabel='velocity (м/c)',
       title='r (t)')
    ax.locator_params(tight=True, axis = 'x', nbins=10)
    ax.locator_params(tight=True, axis = 'y', nbins=10)
    ax.grid()
    fig.savefig("test.png")
    plt.tight_layout()
    plot_v_r()
