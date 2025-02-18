import re
from typing import List
from exceptions import ChapterMakerError

def validate_timestamp(timestamp: str) -> bool:
    """Validate that a timestamp is in MM:SS format"""
    pattern = r'^\d{2}:\d{2}$'
    return bool(re.match(pattern, timestamp))

def process_llm_response(response: str, response_type: str) -> str:
    if response_type == "chapters":
        # Split response into lines and process
        lines = [line.strip() for line in response.split('\n') if line.strip()]
        processed_lines = []
        
        for line in lines:
            # Look for timestamp pattern at start of line (MM:SS or HH:MM:SS)
            match = re.match(r'^(\d{2}:\d{2}(?::\d{2})?\s+.+)$', line)
            if match:
                processed_lines.append(match.group(1))
        
        if not processed_lines:
            raise ChapterMakerError("No valid chapter markers found in LLM response")
        
        return '\n'.join(processed_lines)

    elif response_type == "titles":
        # Split response into lines and clean up
        lines = [line.strip() for line in response.split('\n') if line.strip()]
        # Remove any numbering or bullet points at the start
        lines = [re.sub(r'^[\d\-\.\s•]+', '', line).strip() for line in lines]
        
        if not lines:
            raise ChapterMakerError("No valid titles found in LLM response")
        
        return '\n'.join(f"{i+1}. {title}" for i, title in enumerate(lines[:10]))
    
    else:
        raise ChapterMakerError(f"Unknown response type: {response_type}")