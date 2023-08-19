def GetTextUser(message):
    text = ""
    typeMessage = message["type"]
    
    if typeMessage == "text":
        text = (message["text"])["body"]
    
    elif typeMessage == "interactive":
        interactiveObject = message["interactive"]
        typeInteractive = interactiveObject["type"]
        
        if typeInteractive == "button_reply":
            text = (interactiveObject["button_reply"])["title"]
        elif typeInteractive == "list_reply":
            text = (interactiveObject["list_reply"])["title"]
        else:
            print("sin mensaje")
    
    else:
        print("sin mensaje")
    
    return text

def TextMessage(text,number):
    data = {
            "messaging_product":"whatsapp",
            "to": number,
            "text":{
                "body":text
            },
            "type": "text"
        }
    return data

def TextFormatMessage(number):
    data = {
            "messaging_product":"whatsapp",
            "to": number,
            "type": "text",
            "text":{
                "body":"*Informacion importante* \n_Necesitas enviar tu correo_\n~Pero tiene que estar~\n```en diferente formato```"
            },
            
        }
    return data

def ImageMessage(number):
    data = {
            "messaging_product":"whatsapp",
            "to": number,
            "type": "image",
            "image":{
                "link":"https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/image_whatsapp.png"
            },
            
        }
    return data

def AudioMessage(number):
    data = {
            "messaging_product":"whatsapp",
            "to": number,
            "type": "audio",
            "audio":{
                "link":"https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/audio_whatsapp.mp3"
            },
            
        }
    return data

def VideoMessage(number):
    data = {
            "messaging_product":"whatsapp",
            "to": number,
            "type": "video",
            "video":{
                "link":"https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/video_whatsapp.mp4"
            },
            
        }
    return data

def DocumentMessage(number):
    data = {
            "messaging_product":"whatsapp",
            "to": number,
            "type": "document",
            "document":{
                "link":"https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/document_whatsapp.pdf"
            },
            
        }
    return data

def LocationMessage(number):
    data = {
            "messaging_product":"whatsapp",
            "to": number,
            "type": "location",
            "location":{
                "latitude":"-2.143782703517996",
                "longitude":"-79.88426791858473",
                "name":"José Joaquín de Olmedo International Airport",
                "address":"V428+P6X, Av. de las Américas, Guayaquil 090513"
            },
            
        }
    return data

def ListMessage(number):
    data = {
    "messaging_product": "whatsapp",
    "to": number,
    "type": "interactive",
    "interactive": {
        "type": "list",
        "body": {
            "text": "✅ I have these options"
        },
        "footer": {
            "text": "Select an option"
        },
        "action": {
            "button": "See options",
            "sections": [
                {
                    "title": "Buy and sell products",
                    "rows": [
                        {
                            "id": "main-buy",
                            "title": "Buy",
                            "description": "Buy the best product your home"
                        },
                        {
                            "id": "main-sell",
                            "title": "Sell",
                            "description": "Sell your products"
                        }
                    ]
                },
                {
                    "title": "📍center of attention",
                    "rows": [
                        {
                            "id": "main-agency",
                            "title": "Agency",
                            "description": "Your can visit our agency"
                        },
                        {
                            "id": "main-contact",
                            "title": "Contact center",
                            "description": "One of our agents will assist you"
                        }
                    ]
                }
            ]
        }
    }
}
    return data