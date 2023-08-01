# DigiDoubt
DigiDoubt is a privacy and quality driven ai-article-website detector used to create blocklists. 

See the DigiDoubt block-list for DNS blocking at: https://github.com/mklemmingen/DigiDoubt_blocklist

The Blocklist includes high-probability ai-generated websites.

"NewsGuard analysts identified the AI-generated websites through keyword searches for phrases commonly produced by AI chatbots. 
The searches were conducted on the search engines Google, Bing, and DuckDuckGo, as well as a media monitoring platform. 
The analysts then verified that the sites were mostly or entirely generated by AI by examining other content for AI phrases and inputting articles into the AI text classifier GPTZero."
   - McKenzie Sadeghi and Lorenzo Arvanitis, May, 2023 in News Guard: "Rise of the Newsbots: AI-Generated News Websites Proliferating Online" access on 31st July 2023 

This tool aims to recreate the aforementioned structure used by NewsGuard Analysts, as well as snoop out any discrepancies in the impressum of a website.
For now, please be aware that the tool only handles english articles.

It there was a mistake, If it was done uncarefully, this tool tries to snoop it out.

All API-Tools are only used to determine website age as well as deep article recognition. 
The API`s in usage are of the Wayback Machine as well as, choosable by the User, a quick-lookup of the article body text in GPTZero. 

## Please be aware that Ai-Generation, Misinformation and Scams are always evolving. Use this tool in combination with a good pinch of doubt. 
## Studies have indicated that articles by non-english natives are disproportionetly flagged as AI.

Basically, the tool judges a website by mutiple weighted criteria and if the summed up criteria points are high enough, the website gets put on the blocklist.
   - it takes the search result in DuckDuckGo for popular topics and checks each article-content-based website that is not on the whitelist. It does so for the first 5 pages on the search engine results each time.
   -    - the popular topics are curled regularly, as to keep it future-proof and up-to-date.
         
   - the program can run endlessly, put can be configured to only run at certain times/intervalls and through specific categories.

   - For each website, there are multiple steps the tool goes through. To see how all the steps went, you can see the log file.

```css
DigiDoubt
│
├── src
│   ├── main.py
│   ├── search_engine.py
│   ├── website_scraper.py
│   ├── ai_phrases.py
│   └── judge.py
│
├── data
│   ├── positive_urls.txt
│   └── logs
│       └── logs.txt
│
└── .git
```
     
## For the time being, all results of this tool are manually checked and added to the blocklist. 
