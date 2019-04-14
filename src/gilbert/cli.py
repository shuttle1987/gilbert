import argparse

from pathlib import Path

from .site import Site


def main():
    parser = argparse.ArgumentParser(prog='gilbert', description="Gilber static site generator")
    parser.add_argument('--root', '-r', type=Path, default=Path.cwd(),
                        help="Root of site data [defaults to CWD]")
    parser.add_argument('action', choices=['init', 'render', 'watch'])

    args = parser.parse_args()

    site = Site(args.root)

    if args.action == 'init':
        site.init()
    elif args.action == 'render':
        site.render()
    elif args.action == 'watch':
        site.watch()
