import statistics
teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

average_temperature = [statistics.mean(hodnota) for hodnota in teploty]
morning_temperature = [hodnota[0] for hodnota in teploty]
night_temperature = [hodnota[3] for hodnota in teploty]

noon_night_temperature = [[hodnota[1], hodnota[3]] for hodnota in teploty]