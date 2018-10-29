from problem_space.core import problem_space
from click import command, option
from frontmatter import Frontmatter


@command()
@option("-i", "--input", required=True, help="File to load.")
def main(input):
    template = Frontmatter.read_file(input)

    for solution in problem_space(template):
        print(solution)
