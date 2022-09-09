from decouple import config
import requests


class NewsFeed:
    base_url = "https://newsapi.org/v2/everything"
    api_key = config('NEWS_API_KEY')
    search_in = "title"

    def __init__(self, interest, from_date, to_date, language):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def _url(self):
        url = f"{self.base_url}?q={self.interest}" \
              f"&searchIn={self.search_in}" \
              f"&from={self.from_date}" \
              f"&to={self.to_date}" \
              f"&language={self.language}" \
              f"&apiKey={self.api_key}"
        return url

    def get(self):
        response = requests.get(self._url())
        content = response.json()
        articles = content['articles']

        email_body = ''
        for article in articles:
            email_body += f"{article['title']}\n{article['url']}\n\n"
        return email_body

if __name__ == '__main__':
    new_feed = NewsFeed(interest='disney', from_date='2022-09-07', to_date='2022-09-09', language='en')
    print(new_feed.get())