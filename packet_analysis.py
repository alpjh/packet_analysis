import math
from matplotlib import pyplot


def char_iterator(filename):
    with open(filename, "rb") as f:
        content = f.read()
    for char in content:
        yield char


def show_graph(x_list, y_list, title):
    pyplot.plot(x_list, y_list)
    pyplot.title(title)
    pyplot.xlabel("Address (byte)")
    pyplot.ylabel("Entropy")
    pyplot.show()


def show_entropy_graph(filename, space):
    count = [0] * 256
    x = []
    y = []
    time = 0

    for ch in char_iterator(filename):
        if ch is None:
            break
        count[ch] += 1
        time += 1

        if time % space == 0:
            e = 0.0
            for i in range(256):
                if count[i] == 0:
                    continue
                p = count[i] / space
                e += - p * math.log(p, 2)
            x.append(time)
            y.append(e)
            count = [0] * 256

    show_graph(x, y, filename)


def main():
    filename = "appcmd.exe"
    show_entropy_graph(filename, 100.0)


main()
