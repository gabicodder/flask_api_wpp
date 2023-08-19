from flask import Flask, request
import util
import whatsappservice

app = Flask(__name__)
@app.route('/welcome',methods=['GET'])
def index():
    return 'welcome developer'

@app.route('/whatsapp',methods=['GET'])
def VerifyToken():
    
    try:
        accessToken = "78ushdashd823239445dfsdfsdf"
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        
        if token != None and challenge != None and token == accessToken:
            return challenge
        else:
            return "",400
    except:
        return "",400

@app.route('/whatsapp',methods=['POST'])
def ReceivedMessage():
    try:
        body = request.get_json()
        entry = (body["entry"])[0]
        changes = (entry["changes"])[0]
        value = changes["value"]
        message = (value["messages"])[0]
        number = message["from"]
        
        ProcessMessage(text,number)
        text = util.GetTextUser(message)
        print(text)
        
        return "EVENT_RECEIVED"
        
    except Exception as e:
        return "EVENT_RECEIVED"

def ProcessMessage(text,number):
    text  = text.lower()
    
    if "hi" in text:
        data = util.TextMessage("Hello, how can I help you?",number)
    elif "thank" in text:
        data = util.TextMessage("Thank you for contacting me",number)
    else:
        data = util.TextMessage("I'm sorry, I can't undestand you",number)
    
    whatsappservice.SendMessageWhasapp(data)

def GenerateMessage(text, number):
    
    if "text" in text:
        data = util.TextMessage("Text",number)
    if "format" in text:
        data = util.TextFormatMessage(number)
    if "image" in text:
        data = util.ImageMessage(number)
    if "video" in text:
        data = util.VideoMessage(number)
    if "audio" in text:
        data = util.AudioMessage(number)
    if "document" in text:
        data = util.DocumentMessage(number)
    if "location" in text:
        data = util.LocationMessage(number)
    if "button" in text:
        data = util.ButtonMessage(number)
    if "list" in text:
        data = util.ListMessage(number)
    
    whatsappservice.SendMessageWhasapp(data)
    

if(__name__=="__main__"):
    app.run()