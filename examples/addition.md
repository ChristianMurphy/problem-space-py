---
math:
  variables:
    x: Int
    y: Int
    z: Int
  constraints:
    - x + y == z
    - x > 0
    - y > 0
    - z > 0
    - x <= 10
    - y <= 10
    - z <= 10
constants:
  name_one: Elizabeth
  name_two: Frank
  object: Apple
pluralize:
  - source: object
    counter: x
    destination: object_x_pluralized
  - source: object
    counter: y
    destination: object_y_pluralized
  - source: object
    counter: y
    destination: object_z_pluralized
---

{name_one} has {x} {object_x_pluralized}, {name_two} has {y} {object_y_pluralized}, how many {object_z_pluralized} are there total?

Answer {z}
