import tweepy
import requests
import json
import time
import openai


consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


openai.api_key = "YOUR_OPENAI_API_KEY"


news_sources = ['https://www.bbc.com/news/rss.xml', 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml']


def fetch_news():
    for url in news_sources:
        response = requests.get(url)
        data = response.text
        news = json.loads(json.dumps(xmltodict.parse(data)))
        for item in news['rss']['channel']['item']:
            article_text = item['title'] + ' ' + item['description']
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Imagine that you have just become the CEO of a new unicorn start-up that focuses on delivering news and current events to people through Factual and engaging Twitter Tweets. As the leader of this company, it is up to you to create a clear and compelling message for your audience and develop a strategy for sharing your content and growing your brand on social media. Your goal is to build a loyal following of people who are passionate about staying informed and up-to-date on the latest news and events. You want to create a sense of community and engagement around your content, and to inspire people to take action and make a positive impact on the world. As the CEO of this unicorn startup, you have a unique opportunity to shape the future of media and journalism and make a real difference in the lives of people worldwide. With your creativity, vision, and leadership, you can build a successful and impactful company that changes the way people consume and engage with news and current events on social media. Read the news article given after this line and present important points about them in a conversational way. {article_text}",
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.7,
            )
            important_fact = response.choices[0].text
            tweet = important_fact.strip() + ' ' + item['link']
            api.update_status(tweet)
            time.sleep(60*60) 
        

fetch_news()
