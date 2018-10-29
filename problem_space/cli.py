from inflect import engine
from problem_space.dz3 import dynamicSolver
from frontmatter import Frontmatter


def main():
    file = Frontmatter.read_file("examples/addition.md")

    print(file["body"])

    p = engine()

    # Question template
    q = "{n1} has {x} {x_o}, {n2} has {y} {y_o}, how many {z_o} are there total?\nAnswer {z}\n\n"
    o = "pear"
    n1 = "Steven"
    n2 = "Elizabeth"

    for s in dynamicSolver(
        file["attributes"]["math"]["variables"],
        file["attributes"]["math"]["constraints"],
    ):
        values = {**file["attributes"]["constants"], **s}

        for e in file["attributes"]["pluralize"]:
            values[e["destination"]] = p.plural_noun(
                values[e["source"]], values[e["counter"]]
            )

        print(file["body"].format(**values))
