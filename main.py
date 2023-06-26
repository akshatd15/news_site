import requests
import mail

api_key = "a1a8fc4bb8034d5788694eb91aa02692"
topic = "tesla"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-05-26&" \
      "sortBy=publishedAt&" \
      "apiKey=a1a8fc4bb8034d5788694eb91aa02692&" \
      "language=en"

# Make request
r = requests.get(url)

# Got a dictionary with data
content = r.json()

# access the article, title and description
body = ""
for article in content["articles"][:20]:
    if article["description"] is not None:
        body = body + article["title"] + "\n" + article["description"] + "\n" + \
               article["url"] + 2 * "\n"

msg = f"""\
Subject: Today's News
{body}"""

msg = msg.encode("utf-8")
mail.send_mail(message=msg)
