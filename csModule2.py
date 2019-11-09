import numpy as np
import math
from slacker import Slacker
import os
import base64
grade_name = os.environ['grade_name']

with open('token.txt') as f:
    token = f.readline()
# Checkpoints

key = 'hello hello'

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

token = decode(key, token)


def checkpoint1(cp1):
    # cp1 function
    test_1 = [3, 4, 2, 5, 4, 6, 1, 1, 2]
    test_2 = [0, 0, 0, 0, 0]
    test_3 = [5, 10, 2, 3, 5, 7, 9, 0, 16]

    expected_1 = 10
    expected_2 = 0
    expected_3 = 16

    actual_1 = cp1(test_1)
    actual_2 = cp1(test_2)
    actual_3 = cp1(test_3)

    assert expected_1 == actual_1, \
        "Checkpoint 1 Failed!\nInput:\n%r\nExpected:\n%r\nGot:\n%r" \
        % (test_1, expected_1, actual_1)

    assert expected_2 == actual_2, \
        "Checkpoint 1 Failed!\nInput:\n%r\nExpected:\n%r\nGot:\n%r" \
        % (test_2, expected_2, actual_2)

    assert expected_3 == actual_3, \
        "Checkpoint 1 Failed!\nInput:\n%r\nExpected:\n%r\nGot:\n%r" \
    % (test_3, expected_3, actual_3)
    send('checkpoint 1')
    print("Checkpoint 1 Passed!")


def checkpoint2(cp2):
    # cp2 function
    test_1 = ([3, 4, 2, 5, 4, 6, 1, 1, 2], 5)
    test_2 = ([0, 0, 0, 0, 0], 1)
    test_3 = ([5, 10, 2, 3, 5, 7, 9, 7, 16], 7)

    expected_1 = 1
    expected_2 = 0
    expected_3 = 2

    actual_1 = cp2(*test_1)
    actual_2 = cp2(*test_2)
    actual_3 = cp2(*test_3)

    assert expected_1 == actual_1, \
        "Checkpoint 2 Failed!\nInput:\n%r\nExpected:\n%r\nGot:\n%r" \
        % (test_1, expected_1, actual_1)

    assert expected_2 == actual_2, \
        "Checkpoint 2 Failed!\nInput:\n%r\nExpected:\n%r\nGot:\n%r" \
        % (test_2, expected_2, actual_2)

    assert expected_3 == actual_3, \
        "Checkpoint 2 Failed!\nInput:\n%r\nExpected:\n%r\nGot:\n%r" \
        % (test_3, expected_3, actual_3)
    send('checkpoint 2')
    print("Checkpoint 2 Passed!")


def checkpoint3(cp3):
    # cp3 function
    test_1 = (2, 5)
    test_2 = (3, 3)
    test_3 = (6, 10)

    expected_1 = 2 * 3 * 4 * 5
    expected_2 = 3
    expected_3 = 6 * 7 * 8 * 9 * 10

    actual_1 = cp3(test_1[0])(test_1[1])
    actual_2 = cp3(test_2[0])(test_2[1])
    actual_3 = cp3(test_3[0])(test_3[1])

    assert expected_1 == actual_1, \
        "Checkpoint 3 Failed!\nInput:\n%r->%r\nExpected:\n%r\nGot:\n%r" \
        % (test_1[0], test_1[1], expected_1, actual_1)

    assert expected_2 == actual_2, \
        "Checkpoint 3 Failed!\nInput:\n%r->%r\nExpected:\n%r\nGot:\n%r" \
        % (test_2[0], test_2[1], expected_2, actual_2)

    assert expected_3 == actual_3, \
        "Checkpoint 3 Failed!\nInput:\n%r->%r\nExpected:\n%r\nGot:\n%r" \
        % (test_3[0], test_3[1], expected_3, actual_3)
    send('checkpoint 3')
    print("Checkpoint 3 Passed!")


def checkpoint4(cp4):
    # cp4 function
    # assert
    expected = [(1, 30), (2, 55), (3, 35), (4, 16), (5, 14)]
    actual = cp4

    assert expected == actual, \
        "Checkpoint 4 Failed!\nExpected:\n%r\nGot:\n%r" \
        % (expected, actual)
    send('checkpoint 4')
    print("Checkpoint 4 Passed!")


def checkpoint5(cp5):
    # cp5 string
    assert (("[" not in cp5) and ("]" not in cp5)), \
        "Checkpoint 5 Failed!\nHint: Disney."
    send('checkpoint 5')
    print("Checkpoint 5 Passed!")

def checkpoint6(cp6):
    # cp6 string
    assert (("[" not in cp6) and ("]" not in cp6)), \
        "Checkpoint 6 Failed!\nHint: Disney."
    send('checkpoint 6')
    print("Checkpoint 6 Passed!")


def checkpoint7(cp7):
    # cp7 function
    test_1 = [[1, 2, 3], [2, 3], [4], [5, 6]]
    test_2 = [[]]
    test_3 = [[1, 2, 3], [4], [5, 6], [7, 8, 9], [10], [11], []]

    expected_1 = [1, 2, 3, 2, 3, 4, 5, 6]
    expected_2 = []
    expected_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    actual_1 = cp7(test_1)
    actual_2 = cp7(test_2)
    actual_3 = cp7(test_3)

    assert expected_1 == actual_1, \
        "Checkpoint 7 Failed!\nInput:\n%r\nExpected:\n%r\nGot:\n%r" \
        % (test_1, expected_1, actual_1)

    assert expected_2 == actual_2, \
        "Checkpoint 7 Failed!\nInput:\n%r\nExpected:\n%r\nGot:\n%r" \
        % (test_2, expected_2, actual_2)

    assert expected_3 == actual_3, \
        "Checkpoint 7 Failed!\nInput:\n%r\nExpected:\n%r\nGot:\n%r" \
        % (test_3, expected_3, actual_3)
    send('checkpoint 7')
    print("Checkpoint 7 Passed!")


def checkpoint8(cp8):
    # cp8 list
    assert cp8 == [88, 44, 42, 4, 4, 2.0, 5 / 6], "Checkpoint 8 Failed!\nTry again."
    send('checkpoint 8')
    print("Checkpoint 8 passed!")


# def checkpoint9(cp9):
#     assert


# def checkpoint10(cp10):
#     assert


# Exercises
def exercise1(e1):
    # e1 function
    assert e1() == [7,
                     9,
                     26,
                     30,
                     33,
                     53,
                     55,
                     70,
                     72,
                     73,
                     74,
                     83,
                     101,
                     106,
                     110,
                     111,
                     119,
                     126,
                     138,
                     142,
                     145,
                     152,
                     156,
                     157,
                     165,
                     166,
                     171,
                     172,
                     173,
                     174,
                     177,
                     178,
                     193,
                     203,
                     206,
                     208,
                     210,
                     213,
                     215,
                     218,
                     220,
                     222,
                     227,
                     228,
                     234,
                     235,
                     236,
                     239,
                     241,
                     252,
                     262,
                     263,
                     269,
                     270,
                     271,
                     274,
                     281,
                     287,
                     290,
                     291,
                     295,
                     315,
                     317,
                     319,
                     328,
                     329,
                     338,
                     340,
                     348,
                     352,
                     359,
                     360,
                     365,
                     366,
                     369,
                     370,
                     377,
                     378,
                     382,
                     383,
                     384,
                     386,
                     387,
                     393,
                     394,
                     401,
                     404,
                     409,
                     410,
                     411,
                     414,
                     418,
                     421,
                     424,
                     425,
                     427,
                     428,
                     430,
                     432,
                     433,
                     437,
                     454,
                     457,
                     460,
                     463,
                     470,
                     476,
                     478,
                     485,
                     499,
                     500,
                     509,
                     510,
                     517,
                     530,
                     535,
                     540,
                     550,
                     564,
                     581,
                     584,
                     592,
                     594,
                     596,
                     597,
                     604,
                     605,
                     613,
                     623,
                     626,
                     630,
                     638,
                     643,
                     647,
                     652,
                     657,
                     659,
                     665,
                     667,
                     682,
                     685,
                     688,
                     699,
                     706,
                     713,
                     716,
                     719,
                     726,
                     728,
                     730,
                     731,
                     741,
                     744,
                     745,
                     746,
                     761,
                     768,
                     778,
                     781,
                     787,
                     791,
                     808,
                     811,
                     819,
                     830,
                     831,
                     833,
                     836,
                     843,
                     849,
                     851,
                     857,
                     861,
                     884,
                     895,
                     897,
                     901,
                     904,
                     913,
                     916,
                     917,
                     925,
                     927,
                     929,
                     933,
                     954,
                     955,
                     957,
                     963,
                     969,
                     972,
                     975,
                     976,
                     981,
                     993,
                     1000,
                     1001,
                     1009,
                     1018,
                     1028,
                     1030,
                     1034,
                     1036,
                     1038,
                     1048,
                     1057,
                     1062,
                     1063,
                     1064,
                     1069,
                     1074,
                     1077,
                     1078,
                     1081,
                     1082,
                     1087,
                     1088,
                     1108,
                     1116,
                     1122,
                     1124,
                     1131,
                     1132,
                     1134,
                     1136,
                     1138,
                     1141,
                     1143,
                     1152,
                     1157,
                     1159,
                     1162,
                     1168,
                     1170,
                     1171,
                     1173,
                     1176,
                     1180,
                     1182,
                     1187,
                     1195,
                     1196,
                     1211,
                     1215,
                     1220,
                     1223,
                     1243,
                     1254,
                     1257,
                     1258,
                     1264,
                     1268,
                     1275,
                     1278,
                     1280,
                     1287,
                     1297,
                     1312,
                     1320,
                     1321,
                     1328,
                     1337,
                     1341,
                     1346,
                     1350,
                     1351,
                     1354,
                     1371,
                     1374,
                     1378,
                     1382,
                     1394,
                     1395,
                     1399,
                     1402,
                     1404,
                     1406,
                     1412,
                     1417,
                     1422,
                     1427,
                     1428,
                     1431,
                     1432,
                     1441,
                     1443,
                     1447,
                     1455,
                     1463,
                     1474,
                     1477,
                     1478,
                     1483,
                     1502,
                     1508,
                     1511,
                     1516,
                     1518,
                     1524,
                     1525,
                     1526,
                     1528,
                     1537,
                     1542,
                     1543,
                     1546,
                     1554,
                     1557,
                     1560,
                     1563,
                     1567,
                     1572,
                     1575,
                     1576,
                     1589,
                     1602,
                     1603,
                     1616,
                     1618,
                     1620,
                     1621,
                     1626,
                     1629,
                     1630,
                     1633,
                     1636,
                     1638,
                     1647,
                     1654,
                     1657,
                     1667,
                     1669,
                     1685,
                     1687,
                     1708,
                     1710,
                     1717,
                     1727,
                     1728,
                     1729,
                     1735,
                     1736,
                     1747,
                     1751,
                     1756,
                     1757,
                     1769,
                     1782,
                     1787,
                     1792,
                     1793,
                     1797,
                     1799,
                     1802,
                     1821,
                     1822,
                     1831,
                     1833,
                     1841,
                     1850,
                     1855,
                     1864,
                     1868,
                     1870,
                     1872,
                     1874,
                     1880,
                     1889,
                     1899,
                     1902,
                     1903,
                     1907,
                     1909,
                     1912,
                     1915,
                     1916,
                     1927,
                     1928,
                     1932,
                     1938,
                     1942,
                     1943,
                     1953,
                     1957,
                     1961,
                     1973,
                     1976,
                     1979,
                     1984,
                     1990,
                     1992,
                     1993,
                     1996,
                     1997,
                     2004,
                     2006,
                     2010,
                     2016,
                     2028,
                     2034,
                     2035,
                     2043,
                     2049,
                     2051,
                     2052,
                     2053,
                     2055,
                     2058,
                     2086,
                     2090,
                     2102,
                     2103,
                     2104,
                     2112,
                     2114,
                     2120,
                     2126,
                     2127,
                     2129,
                     2141,
                     2147,
                     2154,
                     2161,
                     2168,
                     2171,
                     2172,
                     2173,
                     2181,
                     2193,
                     2205,
                     2207,
                     2210,
                     2218,
                     2225,
                     2227,
                     2230,
                     2241,
                     2247,
                     2249,
                     2263,
                     2268,
                     2269,
                     2270,
                     2280,
                     2284,
                     2292,
                     2295,
                     2296,
                     2303,
                     2315,
                     2318,
                     2325,
                     2330,
                     2331,
                     2338,
                     2343,
                     2348,
                     2349,
                     2352,
                     2354,
                     2356,
                     2365,
                     2366,
                     2367,
                     2369,
                     2370,
                     2375,
                     2385,
                     2386,
                     2394,
                     2408,
                     2409,
                     2412,
                     2414,
                     2416,
                     2417,
                     2418,
                     2419,
                     2427,
                     2428,
                     2431,
                     2437,
                     2447,
                     2449,
                     2457,
                     2460,
                     2465,
                     2469,
                     2476,
                     2484,
                     2509,
                     2510,
                     2511,
                     2513,
                     2520,
                     2521,
                     2523,
                     2524,
                     2533,
                     2534,
                     2535,
                     2541,
                     2545,
                     2547,
                     2548,
                     2549,
                     2556,
                     2558,
                     2563,
                     2564,
                     2568,
                     2575,
                     2576,
                     2581,
                     2585,
                     2586,
                     2588,
                     2593,
                     2595,
                     2597,
                     2621,
                     2623,
                     2624,
                     2631,
                     2640,
                     2650,
                     2651,
                     2654,
                     2658,
                     2660,
                     2666,
                     2683,
                     2684,
                     2696,
                     2703,
                     2705,
                     2712,
                     2714,
                     2731,
                     2734,
                     2736,
                     2745,
                     2747,
                     2748,
                     2751,
                     2757,
                     2758,
                     2768,
                     2771,
                     2776,
                     2780,
                     2783,
                     2784,
                     2785,
                     2790,
                     2793,
                     2801,
                     2803,
                     2809,
                     2810,
                     2813,
                     2823,
                     2833,
                     2834,
                     2835,
                     2845,
                     2848,
                     2854,
                     2855,
                     2856,
                     2862,
                     2863,
                     2864,
                     2871,
                     2879,
                     2889,
                     2891,
                     2904,
                     2908,
                     2910,
                     2914,
                     2915,
                     2921,
                     2929,
                     2933,
                     2934,
                     2951], \
        "Exercise 1 Failed!\nTry again."
    send('Exercise 1')
    print("Exercise 1 passed!")
    
def send(exercise):
    slack = Slacker(token)
    if slack.api.test().successful:
        print(
            f"Grader connection successful.")
    else:
        print('Grading error: try running cell again.')

    msg = f'{grade_name} has finished {exercise}.'
    print(msg)
    r = slack.chat.post_message(channel='cs-module-2-2',
                text=msg,
                username='ULAB Grade-bot',
                )
    r.successful
    return #don't want it to send more slack messages by accident


def exercise2(e2):
    assert e2() == ['NN Ser d',
                     'HD 116029 b',
                     'HD 24040 b',
                     'HD 200964 b',
                     'HD 141937 b',
                     'MOA-2009-BLG-387L b',
                     'GJ 649 b',
                     'HD 132406 b',
                     'HD 38529 c',
                     'HD 126614 A b',
                     'HD 177830 b',
                     'HD 38283 b',
                     'HD 217786 b',
                     'HD 73267 b',
                     'HD 147513 b',
                     'HD 72659 b',
                     'HD 1605 b',
                     'HD 197037 b',
                     'HD 70642 b',
                     'HD 142 b',
                     'GJ 328 b',
                     'HD 67087 b',
                     'HD 102329 b',
                     'HD 159868 b',
                     'HD 114783 b',
                     'epsilon Ret b',
                     'HD 168443 c',
                     'Kepler-1635 b',
                     'HD 81040 b',
                     'HD 208527 b',
                     'HD 95089 b',
                     'HD 114729 b',
                     'HD 142415 b',
                     'HD 114386 b',
                     '7 CMa b',
                     'HD 152581 b',
                     'HD 13908 c',
                     'HD 31253 b',
                     'HD 183263 c',
                     'HD 192310 c',
                     'HD 1690 b',
                     'HD 28185 b',
                     'HIP 97233 b',
                     'HD 23127 b',
                     'gamma Leo A b',
                     'NN Ser c',
                     'HD 11506 b',
                     'HD 34445 b',
                     'HD 125612 b',
                     '42 Dra b',
                     'HD 153950 b',
                     'HD 204313 d',
                     'HD 50554 b',
                     'HD 13189 b',
                     'GJ 832 b',
                     'alpha Ari b',
                     'HD 210702 b',
                     'mu Ara b',
                     'TYC 1422-614-1 c',
                     'HD 73526 c',
                     'HD 108341 b',
                     '14 Her b',
                     'OGLE-05-169L b',
                     'HD 171238 b',
                     'GJ 849 b',
                     'HD 164922 b',
                     'tau Gru b',
                     'HD 96063 b',
                     'HD 5608 b',
                     'HD 86264 b',
                     'HD 37124 d',
                     'HD 204313 b',
                     '24 Sex c',
                     'HD 60532 c',
                     'HD 79498 b',
                     'HD 181433 c',
                     'HD 6718 b',
                     'HD 33636 b',
                     'HD 240237 b',
                     'HD 11977 b',
                     'HD 73534 b',
                     'HD 164604 b',
                     'OGLE-05-071L b',
                     'HD 37124 c',
                     'HD 217107 c',
                     'HD 13931 b',
                     'HD 155358 c',
                     '81 Cet b',
                     'HD 32963 b',
                     'HD 136118 b',
                     'HD 5319 b',
                     'HD 75898 b',
                     '16 Cyg B b',
                     'HD 213240 b',
                     'HD 33844 b',
                     'HD 74156 c',
                     'WASP-47 c',
                     'HD 38801 b',
                     'HD 132563 B b',
                     'HD 207832 c',
                     'HD 173416 b',
                     'HD 39091 b',
                     'Kepler-1636 b',
                     'HD 7449 b',
                     'OGLE-2006-BLG-109L c',
                     'HD 216437 b',
                     'HD 82943 b',
                     'HD 220773 b',
                     'HD 159868 c',
                     'HD 100777 b',
                     'HD 222582 b',
                     'HD 128311 b',
                     'HD 181433 d',
                     'HD 4208 b',
                     'HD 5388 b',
                     '11 UMi b',
                     'HD 4732 c',
                     'kappa CrB b',
                     'HD 204941 b',
                     'HD 196050 b',
                     'HD 111232 b',
                     'HD 180902 b',
                     'BD +48 738 b',
                     'NGC 2423 3 b',
                     'HD 50499 b',
                     'HD 154857 c',
                     'HD 2039 b',
                     'HD 187085 b',
                     'HD 175167 b',
                     'NGC 4349 127 b',
                     'GJ 676 A b',
                     'HD 47186 c',
                     'HIP 14810 d',
                     'HD 142245 b',
                     'HD 30177 b',
                     'bet Cnc b',
                     'HD 190647 b',
                     'HD 106270 b',
                     'HD 30856 b',
                     'HD 24064 b',
                     'HD 48265 b',
                     'HD 89307 b',
                     'HD 163607 c',
                     'HD 4313 b',
                     'HR 8799 b',
                     'HD 45350 b',
                     'HD 148427 b',
                     'epsilon Tau b',
                     'epsilon Eri b',
                     'HD 20782 b',
                     'HD 65216 b',
                     'omega Ser b',
                     'HD 16175 b',
                     'HD 98219 b',
                     'HD 11964 b',
                     'Kepler-421 b',
                     'mu Leo b',
                     'HD 139357 b',
                     'HD 8535 b',
                     'HD 4203 b',
                     'Fomalhaut b',
                     'HD 23079 b',
                     'HD 154345 b',
                     'mu Ara c',
                     'HD 7199 b',
                     'Kepler-849 b',
                     'HD 290327 b',
                     'HD 169830 c',
                     '47 UMa c',
                     'HD 85390 b',
                     'HIP 57274 d',
                     'HD 221287 b',
                     'HD 192699 b',
                     'HD 181342 b',
                     'HD 131496 b',
                     'HD 44219 b',
                     '75 Cet b',
                     'HD 220074 b',
                     'HIP 2247 b',
                     'BD +20 2457 c',
                     'HD 22781 b',
                     'HD 120084 b',
                     'HD 95127 b',
                     'HD 95872 b',
                     'HD 5319 c',
                     'eta Cet b',
                     'HD 215497 c',
                     'HD 33564 b',
                     'bet UMi b',
                     'HD 134987 c',
                     'iota Dra b',
                     'HD 108874 b',
                     'HD 4732 b',
                     'HD 23596 b',
                     'Kepler-1630 b',
                     'HD 25171 b',
                     'HD 10697 b',
                     'HD 33844 c',
                     'HD 113337 b',
                     'BD +20 2457 b',
                     'HD 99706 b',
                     'HD 202206 c',
                     'HD 206610 b',
                     'HD 12661 c',
                     'HD 28254 b',
                     'HD 210277 b',
                     'HR 8799 c',
                     '55 Cnc d',
                     'HD 155233 b',
                     'HD 148156 b',
                     'HD 222155 b',
                     'HD 117207 b',
                     'HD 156846 b',
                     'HR 8799 d',
                     'HD 158038 b',
                     'GJ 179 b',
                     'HD 143361 b',
                     'Kepler-68 d',
                     'Kepler-1632 b',
                     'HD 128311 c',
                     'HD 18742 b',
                     'HD 167042 b',
                     '6 Lyn b',
                     'HD 180314 b',
                     'HD 17092 b',
                     'HD 108874 c',
                     'HD 200964 c',
                     'HD 10180 h',
                     'HD 33142 b',
                     'HD 99109 b',
                     'HD 10647 b',
                     'HD 170469 b',
                     'HD 196885 b',
                     '24 Sex b',
                     'HD 190228 b',
                     'OGLE-2006-BLG-109L b',
                     'HD 181720 b',
                     'HD 156411 b',
                     'OGLE-05-390L b',
                     'Kepler-432 c',
                     'HD 4113 b',
                     'HD 87883 b',
                     'HD 10180 g',
                     'HD 66428 b',
                     'HD 136418 b',
                     'beta Pic b',
                     'GJ 163 d',
                     'HD 188015 b',
                     'gamma Cep b',
                     'HD 1605 c',
                     'HR 8799 e',
                     'HD 82886 b',
                     'HD 2952 b',
                     'HD 28678 b',
                     'HD 96167 b',
                     'HD 37605 c',
                     'HD 183263 b',
                     '11 Com b',
                     'Kepler-419 c',
                     'beta Gem b',
                     '47 UMa b',
                     'HD 240210 b',
                     'eta Cet c',
                     'HD 96127 b',
                     'HD 16760 b',
                     'HD 30562 b',
                     'epsilon CrB b',
                     'omicron UMa b',
                     'HD 11755 b',
                     'HD 190360 b',
                     'HAT-P-13 c',
                     'HD 75784 b',
                     'HD 108863 b',
                     'HD 10442 b',
                     'HD 1502 b',
                     'HD 142022 b',
                     'HD 212771 b',
                     'HD 187123 c',
                     'HD 131664 b',
                     'HD 147018 c',
                     'HD 114613 b',
                     'HD 154857 b',
                     'HD 19994 b',
                     'HD 106252 b',
                     '18 Del b',
                     'HD 171028 b',
                     'upsilon And d'], \
         "Exercise 2 Failed!\nTry again."
    send('Exercise 2')
    print("Exercise 2 passed!")


def exercise3(e3):
    assert e3() == "Kepler-20 b", "Exercise 3 Failed!\nTry again."
    send('exercise 3')
    print("Exercise 3 passed!")


def exercise4(e4):
    assert e4 == 358.43803576517166, "Exercise 4 Failed!\nTry again."
    send('exercise 4')
    print("Exercise 4 passed!")


def exercise5(e5):
    assert e5() == "Morton", "Exercise 5 Failed!\nTry again."
    print("Exercise 5 passed!")
    send('exercise 5')


# All
def test_all(cp1, cp2, cp3, cp4, cp5, cp6, cp7, cp8, e1, e2, e3, e4):
    checkpoint1(cp1)
    checkpoint2(cp2)
    checkpoint3(cp3)
    checkpoint4(cp4)
    checkpoint5(cp5)
    checkpoint6(cp6)
    checkpoint7(cp7)
    checkpoint8(cp8)

    exercise1(e1)
    exercise2(e2)
    exercise3(e3)
    exercise4(e4)
    
