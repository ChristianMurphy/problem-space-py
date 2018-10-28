from inflect import engine
from problem_space.dz3 import dynamicSolver


def main():
    p = engine()

    # Question template
    q = "{n1} has {x} {x_o}, {n2} has {y} {y_o}, how many {z_o} are there total?\nAnswer {z}\n\n"
    o = "pear"
    n1 = "Steven"
    n2 = "Elizabeth"

    for s in dynamicSolver(
        ['x = Int("x")', 'y = Int("y")', 'z = Int("z")'],
        ["x + y == z", "x > 0", "y > 0", "z > 0", "x <= 10", "y <= 10", "z <= 10"],
    ):
        print(
            q.format(
                n1=n1,
                n2=n2,
                x=s["x"],
                x_o=p.plural_noun(o, s["x"]),
                y=s["y"],
                y_o=p.plural_noun(o, s["y"]),
                z=s["z"],
                z_o=p.plural_noun(o, s["z"]),
            )
        )
