
def argmax(values):
    N = len(values)
    if N == 0:
        raise ValueError('attempt to get argmax of an empty sequence')

    # Initialise the maximum location and value
    imax = 0
    vmax = values[0]

    # Loop through the sequence to find the maximum
    for i in range(1, N):
        v = values[i]
        # If the current value is greater than the maximum found so far,
        # update the maximum location and value
        if v > vmax:
            imax = i
            vmax = v

    return imax

if __name__ == '__main__':
    print(argmax([1,12,-7,9,2]))
