# msn-news-scraper
A python method that scrapes news articles from MSN

### Summary
The traditional python html based web scrapers (i.e. lxml) don't work because of the dynamic way that MSN News loads their pages. 
Selenium still does the trick, but it's suuuuuuuper slow. That's why I created this library. It uses the common API patterns for MSN news and works to scrape their news pages for the news articles and does so in ~200ms.

### Dependencies
- Beautiful Soup (bs4)
- requests
