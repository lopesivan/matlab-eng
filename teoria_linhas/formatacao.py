#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://stackoverflow.com/questions/15733772/convert-float-number-to-string-with-engineering-notation-with-si-prefixe-in-py
import math

def ToSI(d):
  incPrefixes = ['k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']
  decPrefixes = ['m', 'µ', 'n', 'p', 'f', 'a', 'z', 'y']

  degree = int(math.floor(math.log10(math.fabs(d)) / 3))

  prefix = ''

  if degree!=0:
    ds = degree/math.fabs(degree)
    if ds == 1:
      if degree - 1 < len(incPrefixes):
        prefix = incPrefixes[degree - 1]
      else:
        prefix = incPrefixes[-1]
        degree = len(incPrefixes)

    elif ds == -1:
      if -degree - 1 < len(decPrefixes):
        prefix = decPrefixes[-degree - 1]
      else:
        prefix = decPrefixes[-1]
        degree = -len(decPrefixes)

    scaled = float(d * math.pow(1000, -degree))

    s = "{scaled} {prefix}".format(scaled=scaled, prefix=prefix)

  else:
    s = "{d}".format(d=d)

  return(s)

if __name__ == "__main__":
  d = 23392342.1
  print(ToSI(d))
