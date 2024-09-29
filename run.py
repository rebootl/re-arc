#!/usr/bin/env python3
#
#
#

from main import demo_generator, generate_dataset



examples=[
    'dbc1a6ce',
    '2281f1f4',
    'c1d99e64',
    '623ea044',
    '1190e5a7',
    '5614dbcf',
    '05269061',
    '1c786137',
    '2204b7a8',
    '23581191', # 10
    '8be77c9e',
    '6d0aefbc',
    '74dd1130',
    '62c24649',
    '6150a2bd',
    '6fa7a44f',
    '8d5021e8',
    '0520fde7',
    '46442a0e',
    '1b2d62fb', # 20
    '3428a4f5',
    '42a50994',
    '8f2ea7aa',
    '7fe24cdd',
    '85c4e7cd',
    '8e5a5113',
    '4c4377d9',
    'a65b410d',
    '5168d44c',
    'a9f96cdd', # 30
    '9172f3a0',
    '67a423a3',
    'db3e9e38',
    '9dfd6313',
    '746b3537',
    '75b8110e',
    '1cf80156',
    '28bf18c6',
    '22eb0ac0',
    '4258a5f9', # 40
    '1e0a9b12',
    '9565186b',
    '6e02f1e3',
    '2dc579da',
    '2dee498d',
    '508bd3b6',
    '88a62173',
    '3aa6fb7a',
    '3ac3eb23',
    'c3e719e8', # 50
    '29c11459',
    '23b5c85d',
    '1bfc4729',
    '47c1f68c',
    '178fcbfb',
    'ae4f1146',
    '3de23699',
    '7ddcd7ec',
    '5c2c9af4',
    '0b148d64', # 60
    'beb8660c',
    '8d510a79',
    '7468f01a',
    '09629e4f',
    '4347f46a',
    '6d58a25d',
    '363442ee',
    '855e0971',
    '137eaa0f',
    '31aa019c', # 70
    '2bee17df',
    '50cb2852',
    '662c240a',
    'e8593010',
    'd9f24cd1',
    '90c28cc7',
    '321b1fc6',
    '6455b5f5',
    '4c5c2cf0',
    '56ff96f3', # 80
    '2c608aff',
    'e98196ab',
    'c9f8e694',
    'eb5a1d5d',
    '82819916',
    '5daaa586',
    '68b16354',
    'bb43febb',
    '9ecd008a',
    'f25ffba3', # 90
    '3bdb4ada',
    '2013d3e2',
    'aabf363d',
    'd037b0a7',
    'e26a3af2',
    'b8825c91',
    'ba97ae07',
    'c909285e',
    'd511f180',
    'd0f5fe59', # 100

    # '4612dd53',
    # 'd631b094',
    # 'd5d6de2d',
    # '5117e062',
    # '7fe24cdd',
    # '228f6490',
    # '3428a4f5',
    # '0dfd9992', # OK
]

# for e in examples:
#     demo_generator(e)

generate_dataset('data-10', 15, 1000, examples=examples)
