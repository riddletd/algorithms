#!/usr/bin/env python3

import algorithms

counter = algorithms.Counter("Julie")
counter.inc()
counter.inc()
counter.inc()
counter.dec()
counter.inc()
print(str(counter.getCount()))
