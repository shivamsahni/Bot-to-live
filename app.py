from flask import Flask, request
from pymessenger.bot import Bot
from utils import wit_response

bot = Bot("EAAc9R88QxNcBALnSoc0XalzqTbvNTXd4zXrxjoZCfLOCVUM6f9NmhF9HQ4QThCgryJloNW1tEKLGdpzgRVzlSWaRVWM0SqfZCuLbUpFPJ0uBcd87imoZBYhe7hOpvYm7E3UmioR0h2pXu1t00Tnxq2oNab2nzAXu9lCZAvlz8OnZBTZCGxFeSB")
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
                            #echoing the same text & adding "by jarvis" in the end
                            # text = messaging["message"]["text"] + " by jarvis"

                            #using wit for response

                            response = None
                            entity, value = wit_response(messaging["message"]["text"])
                            if entity == "newstype":
                                text = "I got it, u want {} news , i will provide u soon".format(str(value))
                            elif entity == "location":
                                text = "wow you are from {}".format(str(value))+" wait , i will provide u top news from {}.".format(str(value))
                            elif entity == "faltuquestion":
                                text = "nothing"

                            else:
                                text = "sorry but i didn't got u."

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
