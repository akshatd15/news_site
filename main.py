import requests
import mail

api_key = "a1a8fc4bb8034d5788694eb91aa02692"

url = "https://newsapi.org/v2/everything?q=tesla&from=2023-05-2" \
          "6&sortBy=publishedAt&apiKey=a1a8fc4bb8034d5788694eb91aa02692"

# Make request
r = requests.get(url)

# Got a dictionary with data
content = r.json()

# access the article, title and description
body = ""
for article in content["articles"]:
    if article["description"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
mail.send_mail(message=body)