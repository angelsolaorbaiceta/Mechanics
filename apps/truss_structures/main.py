import sys
import time

import apps.truss_structures.output as out
from apps.truss_structures.arguments import parse_arguments
from structures.parse.str_parse import parse_structure_from_lines

if __name__ == "__main__":
    arguments = parse_arguments()
    lines = sys.stdin.readlines()

    start_time = time.time()

    structure = parse_structure_from_lines(lines)
    solution = structure.solve_structure()

    out.save_solution_to_svg(solution, arguments)
    out.save_solution_to_text(solution)

    end_time = time.time()
    elapsed_secs = end_time - start_time
    print(f"Took {round(elapsed_secs, 3)} seconds to solve")
