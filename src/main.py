#!/usr/bin/env python3

import argparse
import json
import logging
import os
import sys
from pathlib import Path

from llm_orchestrator import LLMOrchestrator
from processor import process_llm_response
from exceptions import ChapterMakerError

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def setup_argparse():
    parser = argparse.ArgumentParser(
        description="Generate YouTube chapters and titles from SRT transcript"
    )
    parser.add_argument(
        "--input", type=str, required=True, help="Path to input SRT file"
    )
    parser.add_argument("--output", type=str, help="Path to output file (optional)")
    parser.add_argument("--verbose", action="store_true", help="Enable debug logging")
    return parser


def read_srt_file(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        raise ChapterMakerError(f"Error reading SRT file: {str(e)}")


def write_output(content: dict, output_path: str = None):
    try:
        json_content = json.dumps(content, indent=2)
        if output_path:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(json_content)
        else:
            print(json_content)
    except Exception as e:
        raise ChapterMakerError(f"Error writing output file: {str(e)}")


def main():
    parser = setup_argparse()
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    try:
        # Validate API key
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ChapterMakerError("OPENAI_API_KEY environment variable not set")

        # Read input file
        srt_content = read_srt_file(args.input)

        # Initialize LLM orchestrator
        llm = LLMOrchestrator(api_key)

        # Generate chapters
        logger.info("Generating chapters...")
        chapters_response = llm.generate_chapters(srt_content)
        chapters = process_llm_response(chapters_response, response_type="chapters")

        # Generate titles
        logger.info("Generating titles...")
        titles_response = llm.generate_titles(srt_content)
        titles = process_llm_response(titles_response, response_type="titles")

        # Format output as JSON
        output = {
            "chapters": chapters,
            "suggested_titles": titles.split("\n") if isinstance(titles, str) else titles
        }

        # Write or print output
        write_output(output, args.output)
        logger.info("Processing completed successfully")

    except ChapterMakerError as e:
        logger.error(str(e))
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        if args.verbose:
            logger.exception(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
