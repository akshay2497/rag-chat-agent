from scraper import crawl_pages
import os

def main():
    base_url = "https://react.dev/"
    # base_url = "https://developer.mozilla.org/en-US/docs/Web/JavaScript"
    print("Starting to scrape the documentation site...")

    # Call the crawler function to scrape the data
    scraped_data = crawl_pages(base_url)

    # Optional: Store the scraped data in ChromaDB
    from embeddings import ingest_to_chroma
    ingest_to_chroma(scraped_data)
    print("Scraping and embedding complete!")


if __name__ == "__main__":
    main()