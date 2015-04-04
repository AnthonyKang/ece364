#!/usr/bin/env python3.4

import sys
import os
import vtools

# STEP 1:
# Write the is_valid_name() function in vtools:

names_test={"U1":True, "_U2":True, "1Goldfarb2":True, "__88__":True, "%U2":False, "*99_":False, "What?":False}

for k in names_test:
    test = vtools.is_valid_name(k)
    expected = names_test[k]

    print('Testing: is_valid_name("{}")'.format(k))

    if test != expected:
        print("ERROR: is_valid_name() returned {}, expected {}".format(test, expected))
    else:
        print("OK")
