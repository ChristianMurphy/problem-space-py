from z3 import Int, Or, sat, Solver
from inflect import engine

p = engine()

# Question template
q = "{n1} has {x} {x_o}, {n2} has {y} {y_o}, how many {z_o} are there total?\nAnswer {z}\n\n"
o = "pear"
n1 = "Steven"
n2 = "Elizabeth"


# Set question contstraints
s = Solver()
x = Int("x")
y = Int("y")
z = Int("z")

s.add(x + y == z)
s.add(x > 0)
s.add(y > 0)
s.add(z > 0)
s.add(x <= 10)
s.add(y <= 10)
s.add(z <= 10)

# While there are still more questions
while s.check() == sat:
    # print question and answer
    print(
        q.format(
            n1=n1,
            n2=n2,
            x=s.model()[x],
            x_o=p.plural_noun(o, s.model()[x]),
            y=s.model()[y],
            y_o=p.plural_noun(o, s.model()[y]),
            z=s.model()[z],
            z_o=p.plural_noun(o, s.model()[z]),
        )
    )

    # don't repeat questions
    s.add(Or(x != s.model()[x], y != s.model()[y], z != s.model()[z]))
