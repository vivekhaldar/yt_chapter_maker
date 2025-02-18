# YouTube Chapter Maker

A Python tool that automatically generates YouTube chapters and title suggestions from SRT transcripts using GPT-4.

## Features

- Generates timestamped chapter markers from video transcripts
- Suggests engaging, non-clickbait titles for your video
- Supports SRT format transcripts
- Outputs in YouTube-compatible format

## Prerequisites

- Python 3.11 or higher
- OpenAI API key
- SRT format transcript of your video

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/yt_chapter_maker.git
cd yt_chapter_maker
```

2. Install the package and its dependencies:
```bash
uv sync
```

3. Set up your OpenAI API key:
```bash
export OPENAI_API_KEY='your-api-key-here'
```

## Usage

Basic usage:
```bash
uv run yt_chapter_maker --input ~/repos/gh/color_edit/paper_mindmap.edited.srt
```

You can invoke the tool without cloning the repo using "uvx" as follows:

```bash
uvx --from git+https://github.com/vivekhaldar/yt_chapter_maker  yt_chapter_maker --input ~/repos/gh/color_edit/vibecoding.edited.srt
```

Options:
- `--input`: Path to your SRT transcript file (required)
- `--output`: Path to save the output file (optional, defaults to stdout)
- `--verbose`: Enable debug logging

## Output Format

The tool generates two sections:

### Chapters
Formatted as YouTube-compatible chapter markers:
```
00:00 Introduction
02:15 Main Topic
05:30 Conclusion
```

### Suggested Titles
A list of 10 engaging, non-clickbait title suggestions for your video.

