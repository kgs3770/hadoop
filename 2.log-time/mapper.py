import sys
import re

# 54.36.149.41 - - [22/Jan/2019:03:56:14 +0330] "GET /filter/27|13%20%D9%85%DA%AF%D8%A7%D9%BE%DB%8C%DA%A9%D8%B3%D9%84,27|%DA%A9%D9%85%D8%AA%D8%B1%20%D8%A7%D8%B2%205%20%D9%85%DA%AF%D8%A7%D9%BE%DB%8C%DA%A9%D8%B3%D9%84,p53 HTTP/1.1" 200 30577 "-" "Mozilla/5.0 (compatible; AhrefsBot/6.1; +http://ahrefs.com/robot/)" "-"
# :03:56:14
time_pattern = re.compile(r':(\d{2}):(\d{2}):(\d{2})')

for line in sys.stdin:
    line = line.strip()

    match = time_pattern.search(line)
    
    if match:
        hour = match.group(1)
        print(f'{hour}\t1')

