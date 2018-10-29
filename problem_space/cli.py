from inflect import engine
from problem_space.dz3 import dynamicSolver
from frontmatter import Frontmatter
from click import command, option


@command()
@option("-i", "--input", required=True, help="File to load.")
def main(input):
    file = Frontmatter.read_file(input)

    p = engine()

    for s in dynamicSolver(
        file["attributes"]["math"]["variables"],
        file["attributes"]["math"]["constraints"],
    ):
        values = {}
        if "constants" in file["attributes"]:
            values = {**file["attributes"]["constants"], **s}
        else:
            values = s

        if "pluralize" in file["attributes"]:
            for e in file["attributes"]["pluralize"]:
                values[e["destination"]] = p.plural_noun(
                    values[e["source"]], values[e["counter"]]
                )

        print(file["body"].format(**values))
