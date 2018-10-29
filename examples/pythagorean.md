---
math:
  variables:
    - x = Int("x")
    - y = Int("y")
    - z = Int("z")
  constraints:
    - x * x + y * y == z * z
    - x > 0
    - y > 0
    - z > 0
    - x <= 20
    - y <= 20
    - z <= 20
---

{x} ^ 2 + {y} ^ 2 = z ^ 2
What is z?

Answer {z}
