import httpx
from parsel import Selector


class AsyncNewsScraper:
    START_URL = 'https://ru.sputnik.kg/'
    URL = 'https://ru.sputnik.kg/news/'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    LINK_XPATH = '//a[@class="list__title"]/@href'

    async def fetch_data(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(url=self.URL, headers=self.HEADERS)
            return response.text

    def parse_data(self, text):
        tree = Selector(text=text)
        links = tree.xpath(self.LINK_XPATH).getall()

        for link in links:
            print(self.START_URL + link)
        return links

    async def scrape(self):
        text = await self.fetch_data()
        self.parse_data(text)


if __name__ == "__main__":
    scraper = AsyncNewsScraper()
    import asyncio
    asyncio.run(scraper.scrape())