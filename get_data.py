import requests
import json
from tqdm import tqdm
import time
from datetime import date
from http import cookiejar

class BlockAll(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False

class DataGetter():
    def __init__(self, into_sentences=False):
        self.into_sentences = into_sentences
    
    def inject_url(self, query, size, start_date, end_date):
        page_size = int(size)
        page = 1
        start = (page - 1) * page_size
        url = 'http://138.201.139.21/articles?q={}&published_before={}&published_after={}&lang={}&size={}&offset={}'.format(
            query,
            end_date,
            start_date,
            'en',
            page_size,
            start,
        )
        #print(url)
        return url

    def query_inject(self, query, size, start_date, end_date):
        search_tic = time.time()
        
        s = requests.Session()
        s.cookies.set_policy(BlockAll())
        req = s.get(self.inject_url(query, size, start_date, end_date))
        
        print(req)
        print("Articles returned in {} seconds.".format(time.time()-search_tic))
        
        self.text = []
        count = 1

        for article in tqdm(req.json()['hits']):
            print("ArtNo: {}".format(count))
            print("Title: " + article["title"])
            print("  URL: " + article["url"])
            print("   ID: " + article["id"])
            print(" Date: " + article["published"])

            #res = requests.get(url="http://localhost:9200/_search?q=" +
            #                article["id"])
            try:
                # Get the text from json
                #print(article['body'])
                sent = article['body'].replace('\n', ' ').replace('\r', '.')
                if self.into_sentences == True:
                    # Split text into sentences
                    sent = nltk.tokenize.sent_tokenize(sent)

                self.text.append(sent)

            except:
                print(req)
            
            count += 1

    def to_file(self, filename):
        with open(filename, "w") as text_file:
            for art in self.text:
                text_file.write(art + '\n')

            

if __name__ == "__main__":
    data = DataGetter()
    data.query_inject(
        query="joe+biden",
        size="10",
        start_date="1900-01-01",
        end_date=date.today().strftime("%Y-%m-%d")
    )
    data.to_file("topics/jo_biden.txt")




