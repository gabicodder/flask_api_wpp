import openai

def GetResponse(text):
    try:
        openai.api_key = ""
        result = openai.Completion.create(model = "text-davinci-003",
                                          prompt=text,
                                          n=1,
                                          max_token=500)
        response = result.choice[0].text
        return response
    
    except Exception as ex:
        print(ex)
        return "error"