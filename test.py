#!/usr/bin/env python3

import algorithms

julie = algorithms.Counter("Julie")
tdog = algorithms.Counter("T-Dog")
julie.inc()
tdog.inc()
tdog.inc()
tdog.inc()
print(str(julie.count))
print(str(tdog.count))
