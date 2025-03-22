#!/bin/bash

curl -X POST \
  -H "Content-Type: text/plain" \
  -H "Accept: application/json" \
  -d 'nodes
1: (0.0, 0.0)      (xy)
2: (200.0, 150.0)  ()
3: (400.0, 0.0)    (y)
loads
2 -> (2500.0, -3500.0)
bars
1: (1 -> 2) 25 20000000
2: (2 -> 3) 25 20000000
3: (1 -> 3) 25 20000000
' \
  http://localhost:8080/solve