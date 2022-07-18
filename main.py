"""There is a main modul to check python's features."""
from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-u', '--user')
    args = parser.parse_args()
    print(f"Start as user: {args.user}")
