import africastalking

username = "sandbox"
api_key = "0400606da5dc0bb3c11596d85d645b5f419c2e845b766750b22d8b8f0d6a5a34"

africastalking.initialize(username, api_key)

airtime = africastalking.Airtime

phone_number = "+254742079321"
currency_code = "KES" #Change this to your country's code
amount = 900

try:
    response = airtime.send(phone_number=phone_number, amount=amount, currency_code=currency_code)
    print(response)
except Exception as e:
    print(f"Encountered an error while sending airtime. More error details below\n {e}")


