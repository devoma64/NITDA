from pathlib import Path

path = Path('file_management/pi_digits.txt')
contents = path.read_text()
contents = contents.rstrip()
print(contents)