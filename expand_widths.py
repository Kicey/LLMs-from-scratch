import os
import re

def process_file(filepath, multiplier=2.0):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    def replace_match_px(match):
        width = int(match.group(1))
        new_width = int(width * multiplier)
        return f'width=\\"{new_width}px\\"'

    def replace_match_no_px(match):
        width = int(match.group(1))
        new_width = int(width * multiplier)
        return f'width=\\"{new_width}\\"'

    def replace_match_sq_px(match):
        width = int(match.group(1))
        new_width = int(width * multiplier)
        return f"width='{new_width}px'"

    def replace_match_sq_no_px(match):
        width = int(match.group(1))
        new_width = int(width * multiplier)
        return f"width='{new_width}'"

    new_content, n1 = re.subn(r'width=\\"(\d+)px\\"', replace_match_px, content)
    new_content, n2 = re.subn(r'width=\\"(\d+)\\"', replace_match_no_px, new_content)
    new_content, n3 = re.subn(r"width='(\d+)px'", replace_match_sq_px, new_content)
    new_content, n4 = re.subn(r"width='(\d+)'", replace_match_sq_no_px, new_content)
    
    if n1 > 0 or n2 > 0 or n3 > 0 or n4 > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    print("Expanding widths (x2.0)")
    count = 0
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith('.ipynb') and '.ipynb_checkpoints' not in root:
                filepath = os.path.join(root, file)
                if process_file(filepath, multiplier=2.0):
                    count += 1
                    print(f"Updated {filepath}")
    print(f"Processed {count} files.")

if __name__ == '__main__':
    main()
