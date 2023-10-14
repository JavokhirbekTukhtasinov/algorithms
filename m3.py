from scipy import stats


x = [1, 2, 3, 4, 3, 23, 4, 23, 4, 23, 4, 3, 4, 34, 3, 4]


# median = np.median(x)
mode = stats.mode(x)
print(mode)
