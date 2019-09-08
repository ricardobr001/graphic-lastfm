import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.dates as mdates
import datetime as dt

def plotGraphic(colors, dates, bandsCounter, topBands, user, filename):
    mpl.cycler(color=colors)
    x_axis = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in dates]

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%Y'))

    for y_axis in bandsCounter:
        plt.plot(x_axis, y_axis)

    plt.xlabel('Month/Year')
    plt.ylabel('Scrobbles')

    plt.legend(topBands, loc='upper left', fontsize='x-small')

    plt.title(user + "'s top 10 artists scrobbles")
    plt.gcf().autofmt_xdate()
    plt.savefig(filename)

    return filename

if __name__ == '__main__':
    user = 'ricardobr001'
    filename = 'last.png'
    colors   = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'cyan', 'pink', 'grey', 'palevioletred']
    topBands = ['slipknot', 'linkin park', 'trivium', 'estrons', 'blink-182', 'blood command', 'bring me the horizon', 'a day to remember', 'marmozets', 'rammstein']
    dates    = ['10/17/2017', '11/17/2017', '12/17/2017', '01/17/2018', '02/17/2018', '03/17/2018', '04/17/2018', '05/17/2018', '06/17/2018', '07/17/2018', '08/17/2018', '09/17/2018', '10/17/2018', '11/17/2018', '12/17/2018', '02/17/2019', '03/17/2019', '04/17/2019', '05/17/2019', '06/17/2019', '07/17/2019', '08/17/2019', '09/17/2019']

    bandsCounter = [
        [0, 17, 50,  61,  81, 122, 168, 197, 220,  236,  246,  255,  345,  383,  588,  700,  775,  868, 1117, 1457, 1660, 2466, 2587], # slipknot
        [0, 32, 81, 127, 238, 442, 540, 631, 776, 1019, 1214, 1344, 1458, 1470, 1483, 1533, 1581, 1609, 1722, 1729, 1761, 1761, 1761], # linkin park
        [0,  8, 21,  37,  59,  75, 104, 165, 260,  364,  447,  481,  618,  649,  800,  912,  952, 1124, 1246, 1260, 1357, 1397, 1472], # trivium
        [0,  0,  0,   0,   0,   0,   0,   0,   0,    0,    0,    0,    0,    0,    0,    0,  248,  468,  625,  946, 1105, 1300, 1300], # estrons
        [0, 11, 36,  75, 167, 239, 272, 314, 366,  447,  499,  548,  587,  591,  653,  729,  823,  996, 1030, 1189, 1261, 1291, 1293], # blink-182
        [0, 0,   0,   0,   0,   0,   0,   0,   0,    0,    0,    0,    0,    0,    0,    0,  101,  302,  578,  910, 1036, 1268, 1279], # blood command
        [0, 1,   3,   4,   6,   6,   6,   6,   7,    7,    7,    8,   11,   11,   11,   11,   11,  128,  289,  520,  925, 1192, 1219], # bring me the horizon 
        [0, 14, 22,  29,  37,  62,  89, 113, 129,  146,  174,  205,  253,  307,  312,  322,  350,  382,  405,  439,  768,  946, 1083], # a day to remember
        [0,  0,  0,   0,   0,   0,   0,   0,   0,    0,    0,    0,    0,   54,  164,  218,  295,  352,  360,  484,  838,  891,  897], # marmozets
        [0,  7, 24,  46,  48,  62,  71,  95,  95,   97,  111,  124,  149,  149,  154,  154,  178,  198,  339,  480,  661,  783,  806] # rammstein
    ]

    file = plotGraphic(colors, dates, bandsCounter, topBands, user, filename)
    print('Graphic saved as ' + file)
