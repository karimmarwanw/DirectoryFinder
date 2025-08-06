import requests

def directories(url):
    accepted_codes = [200, 204, 301, 302, 307, 401, 403, 405]
    headers = {"User-Agent": "Mozilla/5.0"}

    with open ("common.txt") as wordlist:
        for line in wordlist:
            line = line.strip()
            response = requests.get(f"{url}/{line}", headers=headers, timeout=5)
            if response.status_code in accepted_codes:
                print(f"{url} / {line} /")

def main():
    url = input("Enter the URL: ")
    directories(url)

if __name__ == "__main__":
    main()