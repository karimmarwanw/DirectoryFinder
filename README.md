# DirBuster - Python Directory Bruteforcer

DirBuster is a simple Python script that performs directory brute-forcing on a target URL. It uses a wordlist to find hidden or unlinked directories based on HTTP status codes.

## Features

- Checks URLs from a wordlist
- Accepts common HTTP status codes (200, 301, 403, etc.)
- Custom User-Agent to avoid basic blocking
- Simple and beginner-friendly

## Example Output

Enter the URL: https://httpbin.org  
https://httpbin.org / get /  
https://httpbin.org / html /  
https://httpbin.org / ip /  
https://httpbin.org / headers /

## How It Works

For each line in `common.txt`, the script sends a GET request to:  
<target_url>/<word>  
If the response status code is in the list of accepted codes, it prints the URL.

## Accepted Status Codes

200, 204, 301, 302, 307, 401, 403, 405

## Requirements

- Python 3.x  
- requests library

Install with:

pip install requests

## Usage

python DirBuster.py

Then enter the target URL when prompted (example: https://example.com).  
Make sure `common.txt` exists in the same directory.

## Wordlist Format

The `common.txt` file should look like this:

admin  
login  
dashboard  
uploads  
get  
html

You can also use a wordlist from SecLists:  
https://github.com/danielmiessler/SecLists

## Notes

- Use only on sites you have permission to test.  
- Large scans may be slow; consider adding threading.  
- Handle responsibly and ethically.

## Roadmap Ideas

- [ ] Add threading  
- [ ] Add progress bar  
- [ ] Resume support  
- [ ] Save results to a file  
- [ ] Use CLI arguments for options

## Author

Made by Karim Marwan  
https://github.com/karimmarwanw

## Disclaimer

This tool is for educational use or authorized penetration testing only.  
Do not scan websites you do not own or have explicit permission to test.
