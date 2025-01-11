import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    hist_array = np.array([1])
    cc_upperbound = 200

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
        hist_array = np.append(hist_array,[result_array.size])

    # print(result_array)
    print(hist_array.size)

    # Line graph
    # plt.title("Iteration")
    # plt.xlabel("X axis")
    # plt.ylabel("Y axis")
    # x = np.arange(0, result_array.size)
    # plt.plot(x, result_array, color="red")

    # Histogram
    plt.title("Iteration Histogram")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    # x = np.arange(0, hist_array.size)
    plt.bar(range(0,hist_array.size), hist_array)

    plt.show()