# YouTube Chapter Maker - Product Requirement Document (PRD)

## 1. Overview

The YouTube Chapter Maker is a script/tool designed to automatically generate chapter markers and catchy video titles for YouTube content. The main workflow leverages a language model (LLM) to process an SRT formatted transcript and produce:

- Logical chapter markers in the form of timestamps and titles.
- A list of 10 short, catchy video titles that are not cheesy or clickbait.

This PRD is intended for a senior software engineer to create a detailed engineering design document, which can then be implemented unambiguously by a junior software engineer.

## 2. Goals & Objectives

- **Automate Chapter Generation:** Transform a video transcript in SRT format into logical chapters with proper timestamp markers and descriptive titles.
- **Title Generation:** Generate 10 short, concise, and appealing video titles based on the transcript content, ensuring they don't appear clickbait.
- **Integration Ready:** Provide a script that can be integrated into existing video processing workflows and adjusted in the future based on user feedback and additional features.

## 3. Background & Rationale

Currently, the process of manually extracting chapters and generating video titles is time-consuming and prone to inconsistency. Leveraging the LLM's capabilities will help automate this process, improve content quality, and streamline video publication workflows.

## 4. Functional Requirements

1. **Input Processing:**
   - Accept an SRT formatted file/string as input which contains timestamps and dialogue details.
   - Validate the input to ensure it conforms to the SRT standard.

2. **Chapter Extraction Module:**
   - Use an LLM with the primary prompt:
     > "I will give you a video transcript in SRT format. Come up with logical chapter markers with timestamp and title, in youtube format."
   - Append the SRT to the prompt to extract relevant segments and generate chapter markers.
   - The LLM should return the right chapter timestamps and titles.
   - Return chapters in the format YouTube uses for chapter markers.
   - **Output Format:** The chapter markers should adhere to the YouTube chapter format. Each chapter is represented on a new line in the following format:

         MM:SS Chapter Title

     For example:

         00:00 Introduction & Research Questions
         02:00 AI Tools Usage Distribution
         02:36 Critical Thinking Patterns
         03:54 Key Finding: Confidence vs Critical Thinking
         04:34 Impact on Cognitive Load
         05:38 Effort Analysis Across Activities
         06:30 Shifting Nature of Knowledge Work
         07:19 Conclusion

3. **Title Generation Module:**
   - After the chapter creation, trigger the LLM with the prompt:
     > "suggest 10 short catchy titles for a youtube video with this content. but i don't want them to be cheesy or sound like clickbait."
   - Accept the output and structure it for further usage or display.

4. **Output Formatting:**
   - The final output should include two sections: the list of chapters (with timestamps and titles) and the list of 10 suggested video titles.
   - Outputs should be in a human-readable format that can be readily copied or parsed.

5. **Error Handling:**
   - Provide clear error messages for invalid SRT formats.
   - Gracefully handle LLM errors or connectivity issues.

## 5. Non-Functional Requirements

- **Performance:** The script should process transcripts of moderate length (typical video length) in under a few seconds depending on LLM response time.
- **Reliability:** Ensure that the tool fails gracefully if the LLM does not return a valid output.
- **Modularity:** Modules should be decoupled (e.g., input parsing, chapter generation, title generation) to facilitate future enhancements or replacement of the LLM provider.
- **Scalability:** Should handle videos of various lengths and adaptable to additional features (e.g., language translation, additional metadata extraction).
- **Usability:** Command-line arguments should be clear and documented, providing a straightforward user experience.

## 6. Technical Considerations

- **Programming Language:** The initial version can be implemented in a suitable scripting language such as Python or Node.js.
- **API Integration:** Use an appropriate LLM API (such as OpenAI API) with proper error handling and response parsing.
- **SRT Parsing:** Leverage an existing library or implement a parser to accurately process SRT files.
- **Logging:** Implement logging for debugging and monitoring purposes.
- **Configuration:** Allow configurable parameters (like API keys, input/output file paths, and verbosity levels) via a configuration file or command-line arguments.

## 7. System Architecture

- **Input Module:** Responsible for reading and validating SRT files.
- **LLM Orchestrator:** Interface between the script and the LLM API, sending appropriate prompts and receiving responses.
- **Processing Engine:** Parses the response from the LLM, formats the chapters, and titles.
- **Output Module:** Writes the processed results to a file or prints to the terminal.
- **Error Handler:** Catches and logs errors, and provides meaningful messages to the user.

## 8. Testing & Validation

- **Unit Tests:** 
   - For SRT parsing functionality, valid/invalid input handling.
   - For output formatting given a mocked LLM response.
- **Integration Tests:** 
   - Using sample SRT files and mock LLM responses to validate end-to-end processing.
- **User Acceptance Testing (UAT):**
   - Validate that the generated chapters and titles match the required format and quality.

## 9. Deployment Considerations

- **Environment:** Should run in environments where Python/Node.js is available along with access to the internet to call the LLM API.
- **Configurations:** Sensitive information (like API keys) should be stored securely (e.g., environment variables or a secure vault).

## 10. Future Enhancements

- Expand functionality to support multiple languages.
- Introduce customization of prompts by end-users.
- Provide a GUI or web interface for users not comfortable with the command line.
- Add caching of results to reduce API calls for repeated inputs.

## 11. Open Questions

- What is the expected rate limit for LLM API calls, and how can retries/backoff be implemented in case of throttling?
- Should the tool support batch processing of multiple transcript files?
- Are there any specific formatting standards or metadata requirements from YouTube that should be adhered to in the chapters?

## 12. Milestones

1. Requirements finalization and detailed design sign-off.
2. Initial implementation of SRT parsing and basic LLM integration.
3. End-to-end testing with sample SRT files.
4. Code review and refactoring based on internal feedback.
5. Documentation and deployment packaging.

## 13. Appendix

- References to SRT file format documentation.
- Links to chosen LLM API documentation and usage guidelines.

---

This document serves as the initial product requirements for the YouTube Chapter Maker tool. Further revisions may be needed as feedback is provided during the design and implementation phases.
