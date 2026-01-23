#!/usr/bin/env python3
"""
Clean up widdershins-generated Markdown files:
- Remove HTML tags and comments
- Fix duplicate headings
- Replace example URLs
- Clean up structure
"""

import re
import sys
from pathlib import Path

def clean_markdown(content, module_name):
    # Remove HTML comments
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    
    # Remove anchor tags but keep the text
    content = re.sub(r'<a[^>]*>(.*?)</a>', r'\1', content)
    
    # Convert HTML headings to Markdown
    content = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1', content, flags=re.IGNORECASE)
    content = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1', content, flags=re.IGNORECASE)
    content = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1', content, flags=re.IGNORECASE)
    content = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1', content, flags=re.IGNORECASE)
    
    # Convert <aside> to blockquote
    content = re.sub(r'<aside[^>]*class="success"[^>]*>\s*(.*?)\s*</aside>', r'> \1', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<aside[^>]*>\s*(.*?)\s*</aside>', r'> \1', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove any remaining HTML tags
    content = re.sub(r'<[^>]+>', '', content)
    
    # Replace example.com URLs with actual base URL
    content = re.sub(r'https://example\.com', 'https://lcd.twilight.org', content)
    
    # Fix duplicate H1 headings - keep only the first one, convert others to H2
    lines = content.split('\n')
    result = []
    h1_count = 0
    first_h1_found = False
    
    for line in lines:
        if line.startswith('# '):
            if not first_h1_found:
                # Replace first H1 with proper module title
                result.append(f'# Twilight Chain API — {module_name.replace("-", " ").title()}')
                first_h1_found = True
            else:
                # Convert subsequent H1s to H2s
                result.append(line.replace('# ', '## ', 1))
        elif line.strip() == '> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.':
            # Remove this generic message
            continue
        else:
            result.append(line)
    
    content = '\n'.join(result)
    
    # Clean up multiple consecutive empty lines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Remove leading/trailing whitespace from each line
    lines = content.split('\n')
    content = '\n'.join(line.rstrip() for line in lines)
    
    return content.strip() + '\n'

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/clean_widdershins.py <markdown_file>")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"File not found: {file_path}")
        sys.exit(1)
    
    # Extract module name from filename
    module_name = file_path.stem.replace('_chain_', '')
    
    # Read, clean, and write
    content = file_path.read_text(encoding='utf-8')
    cleaned = clean_markdown(content, module_name)
    file_path.write_text(cleaned, encoding='utf-8')
    
    print(f"✓ Cleaned {file_path}")
    print(f"  Module: {module_name}")