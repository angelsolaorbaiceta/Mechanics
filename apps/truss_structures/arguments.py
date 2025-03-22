import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="Solves a truss structure")

    parser.add_argument(
        "--scale",
        help="scale applied to the geometry (for plotting)",
        default=2,
        type=float,
    )

    parser.add_argument(
        "--disp-scale",
        help="scale applied to the displacements (for plotting)",
        default=500,
        type=float,
    )

    parser.add_argument(
        "--load-scale",
        help="scale applied to the loads (for plotting)",
        default=0.02,
        type=float,
    )

    parser.add_argument(
        "--no-draw-original",
        help="Should draw the original geometry?",
        action="store_true",
    )

    return parser.parse_args()
