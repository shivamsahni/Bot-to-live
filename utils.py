from wit import Wit

# access_token = "LV4DBABXSZAGZ76HL45QD34DXAZ2LDG4"
#
# client = Wit(access_token)

wit = Wit("LV4DBABXSZAGZ76HL45QD34DXAZ2LDG4")           # pasting access_token copied from wit.ai site for our app & pasting it here

def wit_response(text_message):
    resp = wit.message(text_message)
    entity = None
    value = None
    try:
        entity = list(resp["entities"])[0]
        value = resp['entities'][entity][0]['value']
    except:
        pass
    return (entity, value)

#print(wit_response("bhai kya kar rha hai"))

