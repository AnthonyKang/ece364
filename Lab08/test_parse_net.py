#!/usr/bin/env python3.4
# encoding: utf-8

import sys
import os
import vtools

# STEP 3:
# Write the parse_net() function in vtools:
tests={

    "DFFSR Q_int1_reg ( .D(serial_in), .CLK(clk), .R(1), .S(n5), .Q(Q_int1) )":
        ("DFFSR", "Q_int1_reg", (("D", "serial_in"), ("CLK", "clk"), ("R", "1"), ("S", "n5"), ("Q", "Q_int1"))),

    "OAI22X1     U11(.A(n32),.B(n5),.C(n3),.D(n6),.Y(n25))":
        ("OAI22X1", "U11", (("A", "n32"), ("B", "n5"), ("C", "n3"), ("D", "n6"), ("Y", "n25"))),

    # All of these should cause an exception:
    "BAD(.A(n32),.B(n5),.C(n3),.D(n6),.Y(n25))": (),
    ".A(n32),.B(n5),.C(n3),.D(n6),.Y(n25)": (),
    "TEST TEST((.A(n32),.B(n5),.C(n3),.D(n6),.Y(n25)))": (),
    "TEST $TEST(.A(n32),.B(n5),.C(n3),.D(n6),.Y(n25))": (),
    "TEST TEST(.A(n32),.B(n5),.C(n3),.D(n6),.Y(n25)))": (),
    "TEST TEST(.A(n32),.B(n5),.C(n3),.D(n6),.Y(n25)": ()
}

for k in tests:
    print('Testing: parse_net("{}")'.format(k))

    ex = False
    ok = True
    try:
        r = vtools.parse_net(k)
        if r != tests[k]:
            print("ERROR: parse_net() did not produce a correct result.")
            print("         Got: {}".format(r))
            print("    Expected: {}".format(tests[k]))

            ok = False

    except Exception as e:
        ex = True

    if ex and len(tests[k]) > 0:
        print("ERROR: parse_net() incorrectly raised an exception!")
        ok = False

    elif not ex and len(tests[k]) <= 0:
        print("ERROR: parse_net() did not raise an exception when one was expected! ")
        ok = False

    if ok:
        print("OK")

