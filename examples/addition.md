---
z3:
  variables:
    - x = Int("x")
    - y = Int("y")
    - z = Int("z")
  constraints:
    - x + y == z
    - x > 0
    - y > 0
    - z > 0
    - x <= 10
    - y <= 10
    - z <= 10
  limit: 100
---
