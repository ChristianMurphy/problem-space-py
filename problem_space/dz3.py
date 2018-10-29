from z3 import *
from typing import Iterator, Dict, Callable


def modelToDict(model: Dict) -> Dict:
    """converts z3 keys to string keys"""
    dict = {}
    for key in model:
        dict[str(key)] = model[key]
    return dict


def noRepeat(locals: Dict, model: Dict) -> Callable:
    """creates a new constraint to prevent repeat values"""

    def createConstraint(key):
        return locals[key] != model[locals[key]]

    return Or(*map(createConstraint, locals))


def dynamicSolver(
    variables: Iterator[str], contraints: Iterator[str]
) -> Iterator[Dict]:
    """returns a list of solutions to the given constraints"""
    s = Solver()
    z3Locals = {}
    # generate z3 variables
    for var in variables:
        # FIXME: find a better way to define the variables than dynamically
        # executing Python strings
        exec(
            '{var} = {type}("{var}")'.format(var=var, type=variables[var]),
            globals(),
            z3Locals,
        )
    # add constraints to solver
    for contraint in contraints:
        # FIXME: find a better way to define the constraints than dynamically
        # evaluating Python strings
        s.add(eval(contraint, globals(), z3Locals))
    # find all solutions
    while s.check() == sat:
        yield modelToDict(s.model())
        s.add(noRepeat(z3Locals, s.model()))
