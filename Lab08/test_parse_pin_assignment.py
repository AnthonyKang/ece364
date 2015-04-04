#!/usr/bin/env python3.4
# encoding: utf-8

import sys
import os
import vtools

# STEP 2:
# Write the parse_pin_assignment() function in vtools:
assign_tests={".D(Q)":False, ".foo(_88_)":False, "zing(zaz)":True, "$99(bin12)":True, ".Goldfarb(win98":True, ".K((66))":True}
assign_tests_valid={"D":"Q", "foo":"_88_"}

for k in assign_tests:
    print('Testing: parse_pin_assignment("{}")'.format(k))
    ex = False
    ok = True
    try:
        r = vtools.parse_pin_assignment(k)
        if r[0] not in assign_tests_valid:
            print("ERROR: parse_pin_assignment() produced invalid assignment.")
            ok = False
        elif assign_tests_valid[r[0]] != r[1]:
            print("ERROR: parse_pin_assignment() produced invalid assignment. Returned {0}, expected ({1}, {}2)".format(r, r[0], assign_tests_valid[r[0]]))
            ok = False

    except Exception as e:
        ex = True

    if ex and ex != assign_tests[k]:
        print("ERROR: parse_pin_assignment() incorrectly raised an exception!")
        ok = False

    elif not ex and ex != assign_tests[k]:
        print("ERROR: parse_pin_assignment() did not raise an exception when one was expected! ")
        ok = False

    if ok:
        print("OK")

