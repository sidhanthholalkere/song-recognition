# %%

def generate_fingerprint(peaks, fanout_num):
    """

    Parameters:
        peaks : List[Tuple[int, int]]
            (row, col) index pair for each local peak location

        fanout_num : int
            number of peaks to connect to

    Return:
        fingerprint : List[Tuple(float, float, float)]
            (freq of initial peak, freq of peak fanned out to, time elapsed between peaks
    """
    fingerprint = []
    for index in range(len(peaks) - fanout_num):
        for i in range(fanout_num):
            fingerprint.append(peaks[index, 0], peaks[index + i, 0], peaks[index + i, 1] - peaks[index, 1])
    return fingerprint
