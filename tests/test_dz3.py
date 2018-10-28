from problem_space.dz3 import dynamicSolver


def test_single_variable_single_answer():
    solution = list(dynamicSolver(["x = Int('x')"], ["x == 1"]))
    assert solution == [{"x": 1}]


def test_single_variable_multiple_answers():
    solution = list(dynamicSolver(["x = Int('x')"], ["x > 0", "x < 3"]))
    assert solution == [{"x": 1}, {"x": 2}]


def test_multiple_variables_single_answer():
    solution = list(
        dynamicSolver(["x = Int('x')", "y = Int('y')"], ["x == 0", "y == 1"])
    )
    assert solution == [{"x": 0, "y": 1}]


def test_multiple_variables_multiple_answers():
    solution = list(
        dynamicSolver(
            ["x = Int('x')", "y = Int('y')"], ["x > 0", "x < 3", "y > 0", "y < 3"]
        )
    )
    assert solution == [
        {"x": 1, "y": 1},
        {"x": 2, "y": 2},
        {"x": 2, "y": 1},
        {"x": 1, "y": 2},
    ]
