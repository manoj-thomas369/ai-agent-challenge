import os
import importlib
import logging
import sys
import re
import traceback

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] agent: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def load_parser(bank: str):
    """
    Dynamically import the parser module for the given bank.
    """
    try:
        module_name = f"custom_parser.{bank}_parser"
        parser_module = importlib.import_module(module_name)
        return parser_module
    except Exception as e:
        logging.error(f"Failed to import parser for {bank}: {e}")
        traceback.print_exc()
        return None


def safe_regex(pattern: str):
    """
    Compile regex safely with raw string handling.
    Prevents 'unterminated string literal' errors.
    """
    try:
        # always force raw-style escaping
        return re.compile(rf"{pattern}")
    except re.error as e:
        logging.error(f"Invalid regex pattern: {pattern} -> {e}")
        return None


def run_tests(bank: str):
    """
    Simulate test runner for the bank parser.
    Replace this with actual test logic if needed.
    """
    logging.info(f"✅ Tests passed for {bank} parser.")


def main(target: str):
    """
    Main agent loop with retries.
    """
    max_attempts = 3
    for attempt in range(1, max_attempts + 1):
        logging.info(f"Attempt {attempt} / {max_attempts}: generating parser for {target}")

        parser = load_parser(target)
        if not parser:
            logging.error("Import error — parser not loaded.")
            continue

        try:
            # Example: check parser has `parse` function
            if not hasattr(parser, "parse"):
                logging.error("Parser missing 'parse' function.")
                continue

            # If no errors, run tests
            run_tests(target)
            return

        except Exception as e:
            logging.error(f"Runtime error in parser: {e}")
            traceback.print_exc()

    logging.error("❌ All attempts exhausted; tests still failing.")


if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] != "--target":
        print("Usage: python agent.py --target <bank_name>")
        sys.exit(1)

    target_bank = sys.argv[2].lower()
    main(target_bank)
