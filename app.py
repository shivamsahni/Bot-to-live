from flask import Flask, request
from pymessenger.bot import Bot

bot = Bot("EAAc9R88QxNcBAEEVnAmZBXn5CBuAVHn5bs6hW2iBbzUdXnCBi8oNkZCW29zZCM11ZAeLM1ZBBPIwCmGJrcV8S3eRuCqkuo1os1aCnzOZCPZBaxLIY1AS0hczJRFUA8zcEFw9LCboz7vpx4zoyY66yjHWA0HZCsHkaFn5kslzV5CZAMh1UUGTd9MLV")

app = Flask(__name__)

@app.route("/", methods=["GET"])
def verify():
    if request.args.get("hub.challenge"):
        return request.args.get("hub.challenge")
    else:
        return "Please run in Facebook messenger"

@app.route("/", methods=["POST"])
def message():
    data = request.get_json()
    print(data)

    if data.get('entry'):
        for entry in data['entry']:
            if entry.get('messaging'):
                for messaging in entry["messaging"]:
                    if messaging.get('sender'):
                        user = messaging["sender"]["id"]

                        if messaging["message"].get("text"):
                            text = messaging["message"]["text"] + " by jarvis"
                            bot.send_text_message(user, text)

                        if messaging["message"].get("attachments"):
                            for attachments in messaging["message"]["attachments"]:
                                link = attachments["payload"]["url"]
                                bot.send_image_url(user, link)

    return "message recieved"

@app.after_request
def add_header(response):

    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

#app.run()
