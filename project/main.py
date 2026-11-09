"""Run the supplied demo or the interactive console."""

import argparse

from smartcare.console import run_menu, run_demo


def main() -> None:
    """Run the demo, or the interactive menu with --interactive."""
    parser = argparse.ArgumentParser(
        description='SmartCare teaching application',
    )
    parser.add_argument('--interactive', action='store_true')
    args = parser.parse_args()
    if args.interactive:
        run_menu()
    else:
        run_demo()
if __name__ == '__main__':
    main()

