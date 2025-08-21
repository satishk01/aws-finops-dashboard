import argparse
import sys
from collections import defaultdict
from typing import Dict, List, Optional

import boto3
from rich.console import Console

from aws_finops_dashboard.dashboard_runner import run_dashboard

console = Console()


def main() -> int:
    """Entry point for the module when run directly."""
    from aws_finops_dashboard.cli import main as cli_main_entry

    return cli_main_entry()


if __name__ == "__main__":
    sys.exit(main())
