# DigiDoubt
DigiDoubt is a privacy and quality driven ai-article-website detector used to create blocklists. 

See the DigiDoubt block-list for DNS blocking at: https://github.com/mklemmingen/StopTheToken

The Blocklist includes high-probability ai-generated websites.

"NewsGuard analysts identified the AI-generated websites through keyword searches for phrases commonly produced by AI chatbots. 
The searches were conducted on the search engines Google, Bing, and DuckDuckGo, as well as a media monitoring platform. 
The analysts then verified that the sites were mostly or entirely generated by AI by examining other content for AI phrases and inputting articles into the AI text classifier GPTZero."
   - McKenzie Sadeghi and Lorenzo Arvanitis, May, 2023 in News Guard: "Rise of the Newsbots: AI-Generated News Websites Proliferating Online" access on 31st July 2023 

This tool aims to recreate the aforementioned structure used by NewsGuard Analysts, as well as snoop out any discrepancies in the impressum of a website.


## Please be aware that Ai-Generation, Misinformation and Scams are always evolving. Use this tool in combination with a good pinch of doubt. 
## Studies have indicated that articles by non-english natives are disproportionetly flagged as AI.

Basically, the tool judges a website by mutiple weighted criteria and if the summed up criteria points are high enough, the website gets put on the positive_urls-list. 

### To-Do

   - it takes the search result in DuckDuckGo for popular topics and checks each article-based website that is not specifically on the whitelist (wikipedia trusted sources).
   -  It does so for the first 5 pages on the search engine results each time.
        - the popular topics are curled regularly from google Trends (US-EN, since AI-Websites seem to focus on here), as to keep it future-proof and up-to-date.
        - topics also additionally included other search trends that are simply all-time favorites and have nothing to do with current/on-going events 
    
   - For each website, there are multiple steps the tool goes through. To see how all the steps went, you can see the log file.
        - check about-it webpage to detect discrepancies and/or sloppiness in creation.
        - check age of website using waybackmachine-api.
        - background check article editor. If a generic name was given or if person is deemed fake, points are added to the Doubt-Count.
        - check website structure for generic/similiar layout to known ai-generated webpages.
    
   - for each flagged website, some key metadata is written to the logfile. A further down the line To-Do will be to find the ties between ai-generated websites to flag more efficiently. 
         
   - the program can run endlessly, put can be configured to only run at certain times/intervalls and through specific categories.

  

### Project Structure

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
│       └── dd/mm/yy_hh/mm.txt
│
└── .git
```
     
### For the time being, all results of this tool are manually checked and added to the blocklist. 
### I suggest running this tools in a VPN-protected environment or in conjunction with PiVPN and a configured Pihole. 

### Terminalbased. also writing to log.files

## SOURCES

For finding similiar html structures - thank you to matiskay

https://github.com/matiskay/html-similarity

