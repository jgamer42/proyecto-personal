#!/bin/bash
cd ..
source env/bin/activate
cd news_feed

scrapy crawl desde_linux
scrapy crawl pmo_informatica
scrapy crawl real_python
scrapy crawl we_live_security
scrapy crawl hacks4all
scrapy crawl free_code_camp
deactivate