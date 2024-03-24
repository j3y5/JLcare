#Twilio test

from twilio.rest import Client

account_sid = 'AC0a82268498d2a7adf179cb9815cc5466'
auth_token = '17e26adf54d766bccc5d5e50aa3daf65'
twilio_number = "+447700101921"
body_message = "Test Message."
phone_number = int(input("enter phone number: "))

client = Client(account_sid, auth_token)


message = client.messages.create(
    body=body_message,
    from_=twilio_number,
    to=phone_number
                 )

print(message.body)
