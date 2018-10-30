from inflect import engine
from functools import partial
from itertools import chain
from problem_space.dz3 import dynamicSolver


def constants(template, values):
    yield {**values, **template["attributes"]["constants"]}


def pluralize(template, values):
    p = engine()
    for e in template["attributes"]["pluralize"]:
        values[e["destination"]] = p.plural_noun(
            values[e["source"]], values[e["counter"]]
        )
    yield values


def math(template, values):
    return dynamicSolver(
        template["attributes"]["math"]["variables"],
        template["attributes"]["math"]["constraints"],
    )


def problemSpace(values={}, template={}, plugins=[math, constants, pluralize]):
    if len(plugins) == 0:
        return [template["body"].format(**values)]

    plugin, *rest = plugins

    nextProblem = partial(problemSpace, template=template, plugins=rest)

    if plugin.__name__ in template["attributes"]:
        return chain(*map(nextProblem, plugin(template, values)))
    else:
        return nextProblem(values)
