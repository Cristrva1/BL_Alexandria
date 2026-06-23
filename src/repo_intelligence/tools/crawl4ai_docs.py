from __future__ import annotations

import asyncio

from crawl4ai import AsyncWebCrawler


async def crawl_markdown(url: str) -> str:
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url)
        return result.markdown or ""


def crawl_url(url: str) -> str:
    return asyncio.run(crawl_markdown(url))
