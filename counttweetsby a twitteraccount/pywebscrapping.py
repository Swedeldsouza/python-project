from bs4 import BeautifulSoup
import requests

handle = input('Input your account name on Twitter: ')
temp = requests.get('https://twitter.com/'+handle)
bs = BeautifulSoup(temp.text,'lxml')

try:
    tweet_box = bs.find('li',{'class':'ProfileNav-item ProfileNav-item--tweets is-active'})
    tweets= tweet_box.find('a').find('span',{'class':'ProfileNav-value'})
    print("{} tweets {} number of tweets.".format(handle,tweets.get('data-count')))

except:
    print('Account name not found...')