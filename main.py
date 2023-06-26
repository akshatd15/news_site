import requests

api_key = "a1a8fc4bb8034d5788694eb91aa02692"

url = "https://newsapi.org/v2/everything?q=tesla&from=2023-05-2" \
      "6&sortBy=publishedAt&apiKey=a1a8fc4bb8034d5788694eb91aa02692"

# Make request
r = requests.get(url)

# Got a dictionary with data
content = r.json()

# access the article, title and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])