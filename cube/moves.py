#!/bin/python3.8

swaps_table = {
    'R' : [
        [ # peiceType == 0: corner swaps

            # Urb - uFr  |  Ufr - UrB  |  uRf - uRb
            [1, 9],         [2, 16],      [12, 13],

            [2, 10],        [9, 21],      [12, 15],

            [10, 22],       [19, 21],     [14, 15]
        ],

        [ # peiceType == 1: edge swaps

            [1, 19],        [12, 13],

            [1, 9],         [12, 15],

            [9, 21],        [14, 15]
        ]
    ],

    'U' : [
        [ # peiceType == 0: corner swaps
            [1, 2],[9, 13],[12, 16],

            [0, 1],[4, 16],[13, 17],

            [0, 3],[4, 8],[5, 17]
        ],

        [ # peiceType == 1: edge swaps
            [1, 2],
            [8, 12],

            [0, 1],
            [12, 16],

            [0, 3],
            [4, 16],
        ]
    ],

    'L' : [
        [ # peiceType == 0: corner swaps
            [0, 8],[3, 17],[4, 5],

            [0, 18],[17, 23],[4, 7],

            [11, 23],[20, 18],[6, 7]
        ],

        [ # peiceType == 1: edge swaps
            [3, 11],[4, 5],

            [3, 17],[4, 7],

            [17, 23],[6, 7]
        ]
    ],

    'D' : [
        [ # peiceType == 0: corner swaps
            [6, 18],[7, 11],[20, 23],

            [7, 19],[14, 18],[22, 23],

            [10, 14],[15, 19],[21, 22]
        ],

        [ # peiceType == 1: edge swaps
            [6, 10],[20, 23],

            [6, 18],[22, 23],

            [14, 18],[21, 22],
        ]
    ],

    'F' : [
        [ # peiceType == 0: corner swaps
            [2, 15],[12, 21],[9, 10],

            [2, 5],[3, 12],[8, 9],

            [3, 6],[5, 20],[8, 11]
        ],

        [ # peiceType == 1: edge swaps
            [20, 15],[9, 10],

            [2, 15],[8, 9],

            [2, 5],[8, 11]
        ]
    ],

    'B' : [
        [ # peiceType == 0: corner swaps
            [1, 14],[13, 22],[16, 19],

            [14, 23],[7, 22],[18, 19],

            [0, 7],[4, 23],[17, 18]
        ],

        [ # peiceType == 1: edge swaps
            [0, 13],[16, 19],

            [13, 22],[18, 19],

            [7, 22],[17, 18]
        ]
    ]
}

pieces = {
    'edges' : {
        0 : 16,
        1 : 12,
        2 : 8,
        3 : 4,

        4 : 3,
        5 : 11,
        6 : 23,
        7 : 17,

        8 : 2,
        9 : 15,
        10 : 20,
        11 : 5,

        12 : 1,
        13 : 19,
        14 : 21,
        15 : 9,

        16 : 0,
        17 : 7,
        18 : 22,
        19 : 13,

        20 : 10,
        21 : 14,
        22 : 18,
        23 : 6,
    }
}