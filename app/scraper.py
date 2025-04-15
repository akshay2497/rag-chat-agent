import requests
from bs4 import BeautifulSoup


def crawl_pages(base_url):
    visited = set()
    to_visit = [base_url]
    data = []

    while to_visit:
        url = to_visit.pop()
        if url in visited:
            continue
        visited.add(url)

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            page_text = soup.get_text(separator="\n", strip=True)
            data.append((url, page_text))

            for a_tag in soup.find_all('a', href=True):
                href = a_tag['href']
                if href.startswith('/'):
                    full_url = 'https://react.dev' + href
                    if full_url not in visited:
                        to_visit.append(full_url)
        except Exception as e:
            print(f"Failed to fetch {url}: {e}")

    return data  # [(url, text), ...]