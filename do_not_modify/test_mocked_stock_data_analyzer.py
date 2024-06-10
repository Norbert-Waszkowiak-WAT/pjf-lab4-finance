import unittest
from unittest.mock import patch, MagicMock

from stock_data_analyzer import StockDataAnalyzer


class TestMockedStockDataAnalyzer(unittest.TestCase):
    @patch('requests.get')
    def setUp(self, mock_get):
        # Mock the API response
        mock_response = MagicMock()
        mock_response.json.return_value = {"results":[
            {'v': 81964874.0, 'vw': 185.9465, 'o': 187.15, 'c': 185.64, 'h': 188.44, 'l': 183.885, 't': 1704171600000,
             'n': 1008871},
            {'v': 58414460.0, 'vw': 184.3226, 'o': 184.22, 'c': 184.25, 'h': 185.88, 'l': 183.43, 't': 1704258000000,
             'n': 656853},
            {'v': 71878670.0, 'vw': 182.0183, 'o': 182.15, 'c': 181.91, 'h': 183.0872, 'l': 180.88, 't': 1704344400000,
             'n': 712692},
            {'v': 62371161.0, 'vw': 181.474, 'o': 181.99, 'c': 181.18, 'h': 182.76, 'l': 180.17, 't': 1704430800000,
             'n': 682334},
            {'v': 59144470.0, 'vw': 184.3702, 'o': 182.085, 'c': 185.56, 'h': 185.6, 'l': 181.5, 't': 1704690000000,
             'n': 669173},
            {'v': 42841809.0, 'vw': 184.3706, 'o': 183.92, 'c': 185.14, 'h': 185.15, 'l': 182.73, 't': 1704776400000,
             'n': 538180},
            {'v': 46192908.0, 'vw': 185.2509, 'o': 184.35, 'c': 186.19, 'h': 186.4, 'l': 183.92, 't': 1704862800000,
             'n': 554777},
            {'v': 49128408.0, 'vw': 185.0604, 'o': 186.54, 'c': 185.59, 'h': 187.05, 'l': 183.62, 't': 1704949200000,
             'n': 584008},
            {'v': 40477782.0, 'vw': 185.8199, 'o': 186.06, 'c': 185.92, 'h': 186.74, 'l': 185.19, 't': 1705035600000,
             'n': 477050},
            {'v': 65076641.0, 'vw': 182.8866, 'o': 182.16, 'c': 183.63, 'h': 184.26, 'l': 180.934, 't': 1705381200000,
             'n': 767281},
            {'v': 47317433.0, 'vw': 181.9201, 'o': 181.27, 'c': 182.68, 'h': 182.93, 'l': 180.3, 't': 1705467600000,
             'n': 594632},
            {'v': 77722754.0, 'vw': 187.9358, 'o': 186.09, 'c': 188.63, 'h': 189.14, 'l': 185.83, 't': 1705554000000,
             'n': 787233},
            {'v': 68887985.0, 'vw': 190.6149, 'o': 189.33, 'c': 191.56, 'h': 191.95, 'l': 188.82, 't': 1705640400000,
             'n': 682663},
            {'v': 60131852.0, 'vw': 193.9891, 'o': 192.3, 'c': 193.89, 'h': 195.33, 'l': 192.26, 't': 1705899600000,
             'n': 718107},
            {'v': 42355590.0, 'vw': 194.8203, 'o': 195.02, 'c': 195.18, 'h': 195.75, 'l': 193.8299, 't': 1705986000000,
             'n': 533093},
            {'v': 53631316.0, 'vw': 195.2063, 'o': 195.42, 'c': 194.5, 'h': 196.38, 'l': 194.34, 't': 1706072400000,
             'n': 594714}, {'v': 54822126.0, 'vw': 194.7337, 'o': 195.22, 'c': 194.17, 'h': 196.2675, 'l': 193.1125,
                            't': 1706158800000, 'n': 644526},
            {'v': 44587111.0, 'vw': 193.1207, 'o': 194.27, 'c': 192.42, 'h': 194.76, 'l': 191.94, 't': 1706245200000,
             'n': 534165},
            {'v': 47145622.0, 'vw': 191.2954, 'o': 192.01, 'c': 191.73, 'h': 192.2, 'l': 189.58, 't': 1706504400000,
             'n': 599513},
            {'v': 55836970.0, 'vw': 188.7927, 'o': 190.94, 'c': 188.04, 'h': 191.8, 'l': 187.47, 't': 1706590800000,
             'n': 690705},
            {'v': 55467803.0, 'vw': 185.3525, 'o': 187.04, 'c': 184.4, 'h': 187.095, 'l': 184.35, 't': 1706677200000,
             'n': 679844},
            {'v': 64885408.0, 'vw': 185.5688, 'o': 183.985, 'c': 186.86, 'h': 186.95, 'l': 183.82, 't': 1706763600000,
             'n': 820977},
            {'v': 102527680.0, 'vw': 184.744, 'o': 179.86, 'c': 185.85, 'h': 187.33, 'l': 179.25, 't': 1706850000000,
             'n': 1108465},
            {'v': 69654320.0, 'vw': 187.6824, 'o': 188.15, 'c': 187.68, 'h': 189.25, 'l': 185.84, 't': 1707109200000,
             'n': 804748},
            {'v': 43490759.0, 'vw': 188.4788, 'o': 186.86, 'c': 189.3, 'h': 189.31, 'l': 186.7695, 't': 1707195600000,
             'n': 530825},
            {'v': 53438955.0, 'vw': 189.3803, 'o': 190.64, 'c': 189.41, 'h': 191.05, 'l': 188.61, 't': 1707282000000,
             'n': 596088},
            {'v': 40962046.0, 'vw': 188.3032, 'o': 189.385, 'c': 188.32, 'h': 189.535, 'l': 187.35, 't': 1707368400000,
             'n': 521464},
            {'v': 45155216.0, 'vw': 189.0056, 'o': 188.65, 'c': 188.85, 'h': 189.99, 'l': 188, 't': 1707454800000,
             'n': 544714},
            {'v': 41781934.0, 'vw': 187.5914, 'o': 188.415, 'c': 187.15, 'h': 188.67, 'l': 186.79, 't': 1707714000000,
             'n': 585515},
            {'v': 56529529.0, 'vw': 185.0421, 'o': 185.77, 'c': 185.04, 'h': 186.21, 'l': 183.5128, 't': 1707800400000,
             'n': 644015},
            {'v': 54617917.0, 'vw': 183.6207, 'o': 185.32, 'c': 184.15, 'h': 185.53, 'l': 182.44, 't': 1707886800000,
             'n': 679072},
            {'v': 65434496.0, 'vw': 182.8487, 'o': 183.55, 'c': 183.86, 'h': 184.49, 'l': 181.35, 't': 1707973200000,
             'n': 756083},
            {'v': 49752465.0, 'vw': 182.7317, 'o': 183.42, 'c': 182.31, 'h': 184.85, 'l': 181.665, 't': 1708059600000,
             'n': 611770},
            {'v': 53574453.0, 'vw': 181.1005, 'o': 181.79, 'c': 181.56, 'h': 182.43, 'l': 180, 't': 1708405200000,
             'n': 712335},
            {'v': 41496371.0, 'vw': 181.9941, 'o': 181.94, 'c': 182.32, 'h': 182.8888, 'l': 180.66, 't': 1708491600000,
             'n': 522492},
            {'v': 52284192.0, 'vw': 183.8372, 'o': 183.48, 'c': 184.37, 'h': 184.955, 'l': 182.46, 't': 1708578000000,
             'n': 613892},
            {'v': 44926677.0, 'vw': 182.9876, 'o': 185.01, 'c': 182.52, 'h': 185.04, 'l': 182.23, 't': 1708664400000,
             'n': 549250},
            {'v': 40867421.0, 'vw': 181.3213, 'o': 182.24, 'c': 181.16, 'h': 182.76, 'l': 180.65, 't': 1708923600000,
             'n': 615639},
            {'v': 54318851.0, 'vw': 181.8192, 'o': 181.1, 'c': 182.63, 'h': 183.9225, 'l': 179.56, 't': 1709010000000,
             'n': 669751},
            {'v': 48943139.0, 'vw': 181.1915, 'o': 182.51, 'c': 181.42, 'h': 183.12, 'l': 180.13, 't': 1709096400000,
             'n': 596442},
            {'v': 136682597.0, 'vw': 180.6781, 'o': 181.27, 'c': 180.75, 'h': 182.57, 'l': 179.53, 't': 1709182800000,
             'n': 813073},
            {'v': 73450582.0, 'vw': 179.0322, 'o': 179.55, 'c': 179.66, 'h': 180.53, 'l': 177.38, 't': 1709269200000,
             'n': 911077},
            {'v': 81505451.0, 'vw': 174.8938, 'o': 176.15, 'c': 175.1, 'h': 176.9, 'l': 173.79, 't': 1709528400000,
             'n': 1167166},
            {'v': 94702355.0, 'vw': 170.3234, 'o': 170.76, 'c': 170.12, 'h': 172.04, 'l': 169.62, 't': 1709614800000,
             'n': 1108820},
            {'v': 68568907.0, 'vw': 169.5506, 'o': 171.06, 'c': 169.12, 'h': 171.24, 'l': 168.68, 't': 1709701200000,
             'n': 896297},
            {'v': 71763761.0, 'vw': 169.3619, 'o': 169.15, 'c': 169, 'h': 170.73, 'l': 168.49, 't': 1709787600000,
             'n': 825405},
            {'v': 76267041.0, 'vw': 171.5322, 'o': 169, 'c': 170.73, 'h': 173.7, 'l': 168.94, 't': 1709874000000,
             'n': 925213},
            {'v': 60139473.0, 'vw': 172.9273, 'o': 172.94, 'c': 172.75, 'h': 174.38, 'l': 172.05, 't': 1710129600000,
             'n': 793618},
            {'v': 59813522.0, 'vw': 172.8726, 'o': 173.15, 'c': 173.23, 'h': 174.03, 'l': 171.01, 't': 1710216000000,
             'n': 735065},
            {'v': 52488692.0, 'vw': 171.3457, 'o': 172.77, 'c': 171.13, 'h': 173.185, 'l': 170.76, 't': 1710302400000,
             'n': 647120},
            {'v': 72913507.0, 'vw': 173.0899, 'o': 172.91, 'c': 173, 'h': 174.3078, 'l': 172.05, 't': 1710388800000,
             'n': 806014},
            {'v': 121752699.0, 'vw': 171.8002, 'o': 171.17, 'c': 172.62, 'h': 172.62, 'l': 170.285, 't': 1710475200000,
             'n': 771387},
            {'v': 75606556.0, 'vw': 175.4587, 'o': 175.57, 'c': 173.72, 'h': 177.71, 'l': 173.52, 't': 1710734400000,
             'n': 866430},
            {'v': 55215244.0, 'vw': 175.4779, 'o': 174.34, 'c': 176.08, 'h': 176.605, 'l': 173.03, 't': 1710820800000,
             'n': 636058},
            {'v': 53423102.0, 'vw': 177.2239, 'o': 175.72, 'c': 178.67, 'h': 178.67, 'l': 175.09, 't': 1710907200000,
             'n': 641653},
            {'v': 106181270.0, 'vw': 172.7231, 'o': 177.05, 'c': 171.37, 'h': 177.49, 'l': 170.84, 't': 1710993600000,
             'n': 1224985},
            {'v': 71146138.0, 'vw': 172.0464, 'o': 171.76, 'c': 172.28, 'h': 173.05, 'l': 170.06, 't': 1711080000000,
             'n': 736378},
            {'v': 54288328.0, 'vw': 170.7132, 'o': 170.565, 'c': 170.85, 'h': 171.94, 'l': 169.45, 't': 1711339200000,
             'n': 727686},
            {'v': 57388449.0, 'vw': 170.323, 'o': 170, 'c': 169.71, 'h': 171.42, 'l': 169.58, 't': 1711425600000,
             'n': 684303},
            {'v': 60263665.0, 'vw': 172.5879, 'o': 170.41, 'c': 173.31, 'h': 173.6, 'l': 170.11, 't': 1711512000000,
             'n': 670629},
            {'v': 65671690.0, 'vw': 171.3942, 'o': 171.75, 'c': 171.48, 'h': 172.23, 'l': 170.51, 't': 1711598400000,
             'n': 648026},
            {'v': 46240500.0, 'vw': 170.0696, 'o': 171.19, 'c': 170.03, 'h': 171.25, 'l': 169.475, 't': 1711944000000,
             'n': 676830},
            {'v': 49297581.0, 'vw': 168.8967, 'o': 169.08, 'c': 168.84, 'h': 169.34, 'l': 168.2302, 't': 1712030400000,
             'n': 608914},
            {'v': 47691715.0, 'vw': 169.8623, 'o': 168.79, 'c': 169.65, 'h': 170.68, 'l': 168.58, 't': 1712116800000,
             'n': 571286},
            {'v': 53682486.0, 'vw': 170.1029, 'o': 170.29, 'c': 168.82, 'h': 171.92, 'l': 168.82, 't': 1712203200000,
             'n': 630783},
            {'v': 42104826.0, 'vw': 169.6415, 'o': 169.59, 'c': 169.58, 'h': 170.39, 'l': 168.95, 't': 1712289600000,
             'n': 540854},
            {'v': 37425513.0, 'vw': 168.6637, 'o': 169.03, 'c': 168.45, 'h': 169.2, 'l': 168.24, 't': 1712548800000,
             'n': 549987},
            {'v': 42451209.0, 'vw': 169.1566, 'o': 168.7, 'c': 169.67, 'h': 170.08, 'l': 168.35, 't': 1712635200000,
             'n': 541699},
            {'v': 49691936.0, 'vw': 167.9914, 'o': 168.8, 'c': 167.78, 'h': 169.09, 'l': 167.11, 't': 1712721600000,
             'n': 647587},
            {'v': 91053075.0, 'vw': 172.6956, 'o': 168.34, 'c': 175.04, 'h': 175.46, 'l': 168.16, 't': 1712808000000,
             'n': 828408},
            {'v': 101282386.0, 'vw': 176.3413, 'o': 174.26, 'c': 176.55, 'h': 178.36, 'l': 174.21, 't': 1712894400000,
             'n': 960229},
            {'v': 70733115.0, 'vw': 174.19, 'o': 175.36, 'c': 172.69, 'h': 176.63, 'l': 172.5, 't': 1713153600000,
             'n': 846703},
            {'v': 71583932.0, 'vw': 170.0693, 'o': 171.75, 'c': 169.38, 'h': 173.76, 'l': 168.27, 't': 1713240000000,
             'n': 834229},
            {'v': 48503680.0, 'vw': 169.018, 'o': 169.61, 'c': 168, 'h': 170.65, 'l': 168, 't': 1713326400000,
             'n': 598926},
            {'v': 40735511.0, 'vw': 167.4157, 'o': 168.03, 'c': 167.04, 'h': 168.64, 'l': 166.55, 't': 1713412800000,
             'n': 553162},
            {'v': 66084170.0, 'vw': 165.1519, 'o': 166.21, 'c': 165, 'h': 166.4, 'l': 164.075, 't': 1713499200000,
             'n': 754706},
            {'v': 46488244.0, 'vw': 165.9694, 'o': 165.515, 'c': 165.84, 'h': 167.26, 'l': 164.77, 't': 1713758400000,
             'n': 610286},
            {'v': 46956672.0, 'vw': 166.5052, 'o': 165.35, 'c': 166.9, 'h': 167.05, 'l': 164.92, 't': 1713844800000,
             'n': 554862},
            {'v': 47007455.0, 'vw': 168.4251, 'o': 166.54, 'c': 169.02, 'h': 169.3, 'l': 166.21, 't': 1713931200000,
             'n': 584920},
            {'v': 48858902.0, 'vw': 169.4307, 'o': 169.525, 'c': 169.89, 'h': 170.61, 'l': 168.1511, 't': 1714017600000,
             'n': 608795},
            {'v': 44014087.0, 'vw': 170.0062, 'o': 169.88, 'c': 169.3, 'h': 171.34, 'l': 169.18, 't': 1714104000000,
             'n': 563857},
            {'v': 66891905.0, 'vw': 174.3826, 'o': 173.37, 'c': 173.5, 'h': 176.03, 'l': 173.1, 't': 1714363200000,
             'n': 808166},
            {'v': 64066593.0, 'vw': 172.1915, 'o': 173.33, 'c': 170.33, 'h': 174.99, 'l': 170, 't': 1714449600000,
             'n': 647398},
            {'v': 48416441.0, 'vw': 170.7483, 'o': 169.58, 'c': 169.3, 'h': 172.705, 'l': 169.11, 't': 1714536000000,
             'n': 648581},
            {'v': 91402452.0, 'vw': 174.57, 'o': 172.51, 'c': 173.03, 'h': 173.415, 'l': 170.89, 't': 1714622400000,
             'n': 944012},
            {'v': 160948084.0, 'vw': 184.3811, 'o': 186.645, 'c': 183.38, 'h': 187, 'l': 182.66, 't': 1714708800000,
             'n': 1468448},
            {'v': 75883763.0, 'vw': 181.8762, 'o': 182.354, 'c': 181.71, 'h': 184.2, 'l': 180.42, 't': 1714968000000,
             'n': 898724},
            {'v': 74139796.0, 'vw': 182.7881, 'o': 183.45, 'c': 182.4, 'h': 184.9, 'l': 181.32, 't': 1715054400000,
             'n': 747423},
            {'v': 43762264.0, 'vw': 182.4746, 'o': 182.85, 'c': 182.74, 'h': 183.07, 'l': 181.45, 't': 1715140800000,
             'n': 518558},
            {'v': 47493785.0, 'vw': 183.9877, 'o': 182.56, 'c': 184.57, 'h': 184.66, 'l': 182.11, 't': 1715227200000,
             'n': 550949},
            {'v': 48525869.0, 'vw': 183.0992, 'o': 184.9, 'c': 183.05, 'h': 185.09, 'l': 182.13, 't': 1715313600000,
             'n': 558732},
            {'v': 68586935.0, 'vw': 186.2008, 'o': 185.435, 'c': 186.28, 'h': 187.1, 'l': 184.62, 't': 1715572800000,
             'n': 726471},
            {'v': 50551025.0, 'vw': 187.1838, 'o': 187.51, 'c': 187.43, 'h': 188.3, 'l': 186.29, 't': 1715659200000,
             'n': 559445},
            {'v': 67561123.0, 'vw': 189.651, 'o': 187.91, 'c': 189.72, 'h': 190.65, 'l': 187.37, 't': 1715745600000,
             'n': 727552},
            {'v': 51938566.0, 'vw': 190.1107, 'o': 190.47, 'c': 189.84, 'h': 191.095, 'l': 189.6601, 't': 1715832000000,
             'n': 566892},
            {'v': 39819440.0, 'vw': 189.925, 'o': 189.51, 'c': 189.87, 'h': 190.81, 'l': 189.18, 't': 1715918400000,
             'n': 478115},
            {'v': 43637717.0, 'vw': 191.0833, 'o': 189.325, 'c': 191.04, 'h': 191.9199, 'l': 189.01, 't': 1716177600000,
             'n': 566877},
            {'v': 41192656.0, 'vw': 192.2516, 'o': 191.09, 'c': 192.35, 'h': 192.73, 'l': 190.9201, 't': 1716264000000,
             'n': 502712},
            {'v': 33510741.0, 'vw': 191.4481, 'o': 192.265, 'c': 190.9, 'h': 192.8231, 'l': 190.27, 't': 1716350400000,
             'n': 452301},
            {'v': 48553611.0, 'vw': 188.2595, 'o': 190.98, 'c': 186.88, 'h': 191, 'l': 186.625, 't': 1716436800000,
             'n': 573924},
            {'v': 35429737.0, 'vw': 189.7127, 'o': 188.82, 'c': 189.98, 'h': 190.58, 'l': 188.0404, 't': 1716523200000,
             'n': 492815},
            {'v': 51021752.0, 'vw': 190.8353, 'o': 191.51, 'c': 189.99, 'h': 193, 'l': 189.1, 't': 1716868800000,
             'n': 702124},
            {'v': 51934816.0, 'vw': 191.1313, 'o': 189.61, 'c': 190.29, 'h': 192.247, 'l': 189.51, 't': 1716955200000,
             'n': 603438},
            {'v': 48211467.0, 'vw': 191.4073, 'o': 190.76, 'c': 191.29, 'h': 192.18, 'l': 190.63, 't': 1717041600000,
             'n': 568919},
            {'v': 71937580.0, 'vw': 191.5904, 'o': 191.44, 'c': 192.25, 'h': 192.57, 'l': 189.91, 't': 1717128000000,
             'n': 618138}]}

        mock_get.return_value = mock_response

        self.analyzer = StockDataAnalyzer('test_api_key', 'test_ticker', '2024-01-01', '2024-05-31')

    def test_calculate_average_price(self):
        self.assertAlmostEqual(self.analyzer.calculate_average_price(), 180.2, places=1)

    def test_calculate_max_price(self):
        self.assertAlmostEqual(self.analyzer.calculate_max_price(), 196.38, places=2)

    def test_calculate_min_price(self):
        self.assertAlmostEqual(self.analyzer.calculate_min_price(), 164.075, places=2)

    def test_calculate_volume(self):
        self.assertAlmostEqual(self.analyzer.calculate_volume(), 6296577716, places=0)

    def test_calculate_price_change(self):
        self.assertAlmostEqual(self.analyzer.calculate_price_change(), 5.099999999999994, places=4)

    def test_calculate_price_change_percentage(self):
        self.assertAlmostEqual(self.analyzer.calculate_price_change_percentage(), 2.725, places=3)


if __name__ == '__main__':
    unittest.main()
