#!/usr/bin/env python3
import sys

greeted = "mundo"

if sys.argv[1]:
    greeted = sys.argv[1]

sys.stdout.write("Hola {}!".format(greeted))
