#!/usr/bin/env python3
"""
Test script to verify Amazon scraper on a single product
"""

from amazon_scraper import AmazonScraper

# Test with the example ASIN from row 2
test_asin = 'B07GFT91Z1'
expected_price = 89.99

print(f"Testing scraper with ASIN: {test_asin}")
print("Browser will open - you can watch the scraping process")
print("="*60)

scraper = AmazonScraper(headless=False)  # Run with visible browser
try:
    data = scraper.scrape_product(test_asin, expected_price)
    
    print('\n' + '='*60)
    print('SCRAPED DATA')
    print('='*60)
    for key, value in data.items():
        print(f'{key:20s}: {value}')
    print('='*60)
    
    input("\nPress Enter to close browser and exit...")
    
finally:
    scraper.close()
