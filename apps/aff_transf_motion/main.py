from apps.aff_transf_motion.config import read_config
from apps.aff_transf_motion.input import read_input
from apps.aff_transf_motion.simulation import simulate

if __name__ == "__main__":
    (transform, primitives) = read_input()
    config = read_config()
    simulate(transform, primitives, config)
