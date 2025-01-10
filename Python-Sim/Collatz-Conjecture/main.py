import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    input_val = 53
    result_array = np.array([input_val])
    
    print(result_array)
    while input_val > 1:
        if input_val % 2 ==0:
            input_val = input_val // 2
        else:
            input_val = 3 * input_val +1

        result_array = np.append(result_array,[input_val])

    print(result_array)

    plt.title("Iteration")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    x = np.arange(0, result_array.size)
    plt.plot(x, result_array, color="red")

    plt.show()