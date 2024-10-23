import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
plt.plot(x, y)
plt.title('Simple Sine Wave Plot')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.savefig('plot.png')
print("Plot saved as plot.png")