#!/bin/env python3
import math
#begin

Numbers = {int, float}

def to_number(fraction):
    return fraction[0]/fraction[1]

def to_exponent(number, precision=math.inf):
    if num_or_frac in Numbers:
        number = num_or_frac
    else:
        raise TypeError("to_exponenet: number is not of type number")
    pow = round(math.log(number,10))
    result = number * 10**pow
    powstr = str(pow)
    if pow >= 0:
        powstr = "+" + powstr
    if precision != math.inf:
        result = round(result, precision)
    return str(result) + "e" + powstr

if __name__ == "__main__":
    parser = __import__("argparse").ArgumentParser()
    parser.add_argument("--start", "-s", type=int, default=1, min=1, help="Which divisor to start at (default=1) \# 3/(1) == 3")
    parser.add_argument("--max-cycles", "-c", type=int, default=5000, min=1, help="Max cycles to check for. This is linear")
    parser.add_argument("--max-count", "-N", type=int, default=-1, min=0, help="Max improved fractions to output. This is exponential")
    args = parser.parse_known_args()

    for r in find_fractions(start=args.start_divisor, end=args.start_divisor+args.max_cycles):
        r["number"] = round(r["number"],9)
        print(r)

def find_fractions(start, end, number_as_exponent=False, max_count=math.inf)):
    count = 0
    for i in range(start, end, 2):
        fraction = ((round(math.pi*i),i),0)
        number = to_number(fraction)
        fraction = {"fraction":fraction[0], "delta": to_exponent(math.pi - number), "number": number}
        if abs(fraction[1]) < abs(min[1]):
            min = fraction
            yield min
            count += 1
        if count >= max_count:
            break
