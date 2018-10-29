from inflect import engine
from problem_space.dz3 import dynamicSolver


def applyContants(template, values):
    if "constants" in template["attributes"]:
        return {**values, **template["attributes"]["constants"]}
    return values


def applyPluralization(template, values):
    if "pluralize" in template["attributes"]:
        p = engine()
        for e in template["attributes"]["pluralize"]:
            values[e["destination"]] = p.plural_noun(
                values[e["source"]], values[e["counter"]]
            )
    return values


def problemSpace(template):
    values = {}

    if "math" in template["attributes"]:
        for s in dynamicSolver(
            template["attributes"]["math"]["variables"],
            template["attributes"]["math"]["constraints"],
        ):
            values = s
            values = applyContants(template, values)
            values = applyPluralization(template, values)

            yield template["body"].format(**values)
    else:
        values = applyContants(template, values)
        values = applyPluralization(template, values)

        yield template["body"].format(**values)
