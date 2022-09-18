from scipy.signal import filtfilt, iirnotch, cheby2


def notch(data):
    # Create/view notch filter
    samp_freq = 10000  # Sample frequency (Hz)
    notch_freq = 50.0  # Frequency to be removed from signal (Hz)
    quality_factor = 30.0  # Quality factor
    b_notch, a_notch = iirnotch(notch_freq, quality_factor, samp_freq)

    y = filtfilt(b_notch, a_notch, data)
    return y


def cheby_filter_low(data):
    b, a = cheby2(4, 40, 1000, 'low', fs=10000)
    y = filtfilt(b, a, data)
    return y


def cheby_filter_high(data):
    b, a = cheby2(4, 40, 5, 'high', fs=10000)
    y = filtfilt(b, a, data)
    return y