from flask import Flask, request
import util
import whatsappservice
import chatgptservice

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
        
        text = util.GetTextUser(message)
        responseGPT = chatgptservice.GetResponse(text)
        
        if responseGPT != "error":
            data = util.TextFormatMessage(responseGPT,number)
        else:
            data = util.TextMessage("Sorry, a problem occured ",number)
        
        whatsappservice.SendMessageWhasapp(data)
        
        # ProcessMessage(text,number)
        # print(text)
        
        return "EVENT_RECEIVED"
        
    except Exception as e:
        return "EVENT_RECEIVED"

def ProcessMessage(text,number):
    text  = text.lower()
    listData = []
    
    if "hi" in text or "option" in text:
        data = util.TextMessage("Hello, how can I help you?",number)
        dataMenu = util.ListMessage(number)
        
        listData.append(data)
        listData.append(dataMenu)
        
    elif "thank" in text:
        data = util.TextMessage("Thank you for contacting me",number)
        
    elif "agency" in text:
        data = util.TextFormatMessage("This is out agency",number)
        dataLocation = util.LocationMessage(number)
        listData.append(data)
        listData.append(dataLocation)
    elif "contact" in text:
        data = util.TextFormatMessage("*Contact center:\n00788956*",number)
        listData.append(data)
    
    elif "buy" in text:
        data = util.ButtonMessage(number)
        listData.append(data)
    elif "sell" in text:
        data = util.ButtonMessage(number)
        listData.append(data)
        
    elif "sign up" in text:
        data = util.TextFormatMessage("Enter this link to register: ",number)
        listData.append(data)
    elif "log in" in text:
        data = util.TextFormatMessage("Enter this link to log in: ",number)
        listData.append(data)
    
    else:
        data = util.TextMessage("I'm sorry, I can't undestand you",number)
        listData.append(data)
    
    for item in listData:
        whatsappservice.SendMessageWhasapp(item)

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