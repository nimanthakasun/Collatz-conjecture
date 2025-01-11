import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    hist_array = np.array([1])
    cc_upperbound = 500

    for input_val in range(1,cc_upperbound):
        # input_val = 5528
        result_array = np.array([input_val])
        # print(result_array)
        while input_val > 1:
            if input_val % 2 ==0:
                input_val = input_val // 2
            else:
                input_val = 3 * input_val +1

            result_array = np.append(result_array,[input_val])

        plt.figure("Answers movement")
        plt.title("Answers movement")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        x = np.arange(0, result_array.size)
        plt.plot(x, result_array, color="blue",linewidth=0.5)
        hist_array = np.append(hist_array,[result_array.size])

    # Frequncies chart
    plt.figure("Number of Iterations")
    plt.title("Number of Iterations")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.bar(range(0,hist_array.size), hist_array)

    plt.show()