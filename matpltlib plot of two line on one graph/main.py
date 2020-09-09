import matplotlib.pyplot as linePlot

x1 = [1, 2, 4, 6.5, 9]
y1 = [6, 4, 9, 7, 10]

linePlot.plot(x1, y1, color = 'red', label = "Line1")

x2 = [1, 4.5, 6, 8, 9]
y2 = [9, 6, 9, 6, 9]

linePlot.plot(x2, y2, color = 'blue', label = "Line 2")

linePlot.legend()

linePlot.xlabel("x-axis")
linePlot.ylabel("y-axis")

linePlot.title("Two line on same graph")

linePlot.show()