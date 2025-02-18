# YouTube Chapter Maker - Engineering Design Document

## 1. Introduction

This document provides a detailed engineering design for the YouTube Chapter Maker tool. The design is detailed enough for a junior software engineer to implement and is based on Python and uv for project and dependency management. The tool runs as a command-line script, processing SRT formatted transcripts to generate chapters and video titles using the GPT-4O LLM. The LLM API key will be provided via an environment variable.

## 2. Overall Architecture

The system is composed of the following modules:

- **Input Module**: Handles file reading and input validation for SRT files.
- **SRT Handling**: Supplies the raw SRT content to the LLM for chapter and timestamp extraction.
- **LLM Orchestrator**: Manages communication with GPT-4O. Sends prompts for chapter and title generation and handles API responses.
- **Processing Engine**: Processes LLM responses by formatting chapters and titles into the required YouTube format.
- **Output Module**: Handles output formatting and either prints results to the terminal or writes them to an output file.
- **Error Handling Module**: Catches and logs errors from various modules, including API errors, parsing errors, and invalid input formats.

Each module is designed to be decoupled from the others to facilitate easy replacement and future enhancements.

## 3. Detailed Module Design

### 3.1. Input Module

- **Responsibilities**:
  - Accept a file path via command-line arguments.
  - Read the SRT file content. (Assume the input is a valid SRT file; no additional validation is required.)

- **Implementation Details**:
  - Use Python's built-in file handling.
  - Simply read the entire file content and pass it directly to the LLM without parsing or validation.

### 3.2. SRT Handling

- **Responsibilities**:
  - Instead of parsing the SRT file into structured blocks, directly supply the raw SRT content to the LLM for chapter and timestamp extraction.

- **Implementation Details**:
  - Remove any explicit SRT parsing or validation logic.
  - The complete SRT text is concatenated with the chapter extraction prompt and sent to the LLM.

### 3.3. LLM Orchestrator

- **Responsibilities**:
  - Formulate prompts for GPT-4O for chapter marker generation and title suggestions.
  - Append the SRT content to the chapter generation prompt as per product spec.
  - Handle API responses, including errors and retries in case of connectivity issues.

- **Implementation Details**:
  - Use Python's requests or http.client libraries to interact with the GPT-4O API.
  - The API key is provided through an environment variable (e.g., `OPENAI_API_KEY`).
  - Define separate methods for sending chapter generation prompt and title generation prompt.
  - Implement retry/backoff logic when API calls fail.

### 3.4. Processing Engine

- **Responsibilities**:
  - Extract and format chapter markers from the LLM response.
  - Format the output to adhere to the YouTube chapter format:
    
      MM:SS Chapter Title

- **Implementation Details**:
  - Validate that chapter markers follow the expected timestamp format using regex.
  - Structure the output in two sections: chapters list and titles list.

### 3.5. Output Module

- **Responsibilities**:
  - Display the final results to the terminal and optionally write them to an output file.

- **Implementation Details**:
  - Use Python's print functions and file I/O as necessary.
  - Ensure the output format is human-readable and easily parsable if needed.

### 3.6. Error Handling Module

- **Responsibilities**:
  - Capture errors during SRT reading/parsing, API communication, and response formatting.
  - Log detailed error messages to aid debugging.
  - Exit gracefully if any module returns an error.

- **Implementation Details**:
  - Use Python's try/except structures.
  - Use the logging module to log errors with details such as timestamps and error descriptions.

## 4. Project Configuration and Dependency Management

- **Technology Stack**:
  - Language: Python (version 3.x recommended)
  - Project Management: uv (for dependency management and project scaffolding)

- **Dependencies**:
  - For API requests: `requests` library.
  - For logging: Python’s built-in `logging` module.
  - Other dependencies to be managed via uv (specify in project configuration files as needed).

- **Environment Setup**:
  - Ensure that the `OPENAI_API_KEY` environment variable is set in the environment where the script is executed.

## 5. Command-Line Interface (CLI)

The tool will be executed from the command line. Example usage:

    python chapter_maker.py --input path/to/transcript.srt [--output output.txt]

### CLI Arguments:

- `--input`: Path to the input SRT file. (Required)
- `--output`: Path to the output file. If not provided, output is printed to the terminal.
- `--verbose`: Optional flag to enable debug logging.

## 6. API Integration

- **LLM API (GPT-4O)**:
  - Endpoint: Defined by the GPT-4O API documentation.
  - Authentication: Via API key in the environment variable `OPENAI_API_KEY`.
  - Prompts:
    - **Chapter Generation**: "I will give you a video transcript in SRT format. Come up with logical chapter markers with timestamp and title, in youtube format." Followed by the appended SRT content.
    - **Title Generation**: "suggest 10 short catchy titles for a youtube video with this content. but i don't want them to be cheesy or sound like clickbait."
  - Response Handling: Implement JSON parsing and validation to handle potential errors or discrepancies in the response format.

## 7. Testing Strategy

### 7.1. Unit Tests

- **Input Module**: Test with valid and invalid SRT files.
- **SRT Handling**: Test with a variety of SRT samples to ensure the raw content is correctly passed to the LLM.
- **LLM Orchestrator**: Use mocked responses to simulate API replies.
- **Processing Engine**: Validate that chapter markers adhere to YouTube format and that titles are formatted correctly.

### 7.2. Integration Tests

- End-to-end tests using sample SRT files to ensure that the entire workflow produces the expected output.
- Simulate API errors and validate that the error handling module captures and logs errors appropriately.

## 8. Logging and Monitoring

- **Logging**: Use Python's `logging` module to record key steps and errors. Logs should be configurable (e.g., debug mode vs normal mode).
- **Monitoring**: While not in the initial scope, consider adding basic performance logging (e.g., API response time, file processing time) for future enhancements.

## 9. Future Enhancements

- **Batch Processing**: Extend the CLI to process multiple SRT files in one run.
- **Customization**: Allow users to customize prompts via configuration files.
- **GUI Integration**: Consider a web interface or desktop GUI for non-command line users in future iterations.
- **Caching**: Implement caching of API results to reduce calls for repeated inputs.

## 10. Summary

This engineering design document outlines a modular, robust, and well-structured approach to implementing the YouTube Chapter Maker tool. By following this design, the junior software engineer should have clear guidance on how to build the application using Python, uv, and the GPT-4O API. All components have well-defined responsibilities, proper error handling, and considerations for future scalability and maintainability.
