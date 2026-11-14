import requests

url = 'https://api.otp.dev/v1/verifications'
headers = {
    'X-OTP-Key':    '{YOUR_API_KEY}',
    'accept':       'application/json',
    'content-type': 'application/json',
}
payload = {
    'data': {
        'channel':     'sms',
        'sender':      'GetOTP',
        'phone':       '60123456789',
        'template':    '6d16aa9d-bf19-4141-8169-48b46d972fc6',
        'code_length': 4,
    }
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())