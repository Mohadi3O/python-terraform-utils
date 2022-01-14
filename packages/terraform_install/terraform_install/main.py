# std
import argparse

# internal
from .cli.root import root


parser = argparse.ArgumentParser(description='terraform-install')
parser.set_defaults(func=root)


def main():
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
