import argparse

parser = argparse.ArgumentParser(description='Motion planning simulation.')

parser.add_argument(
    '-g',
    '--generate',
    action="store_true",
    help='save current environment to disk.'
)

args = parser.parse_args()
