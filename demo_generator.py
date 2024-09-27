#!/usr/bin/env python3
#
#
#

import sys
from main import demo_generator, generate_dataset

if len(sys.argv) != 2:
    print('Usage: demo_generator.py <problem_name>')
    sys.exit(1)

name = sys.argv[1]
demo_generator(name)
