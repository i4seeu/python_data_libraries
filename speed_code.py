import time
from numba import jit
import numpy as np
@jit(nopython=True)
def sum2dimensional(np_array):
    array_rows, array_columns = np_array.shape
    result = 0.0
    for i in range(array_rows):
        for j in range(array_columns):
            result += np_array[i,j]
    return result
def main():
    np_array = np.arange(100000000).reshape(10000, 10000)
    print("sum calculation: {}".format(sum2dimensional(np_array)))

if __name__ == '__main__':
    # method of time module in Python is used to get the current processor time as a floating point number expressed in seconds
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    diff_time = end_time - start_time
    result = time.strftime("%H:%M:%S", time.gmtime(diff_time))
    print("program runtime: {}".format(result))