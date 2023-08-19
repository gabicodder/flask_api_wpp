import requests
import json

def SendMessageWhasapp(data):
    try:
        token = "78ushdashd823239445dfsdfsdf"
        api_url = "" #link del api de facebook

        headers = {"Content-Type": "application/json", "Authorization": "Bearer "+ token}
        response = requests.post(api_url, data=json.dumps(data), headers=headers)
        
        if response.status_code == 200:
            return True
        else:
            return False
        
    except Exception as exception:
        print(exception)
        return False
        