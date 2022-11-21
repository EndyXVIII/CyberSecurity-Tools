import base64

def base64ToText(t):
    return base64.b64decode(t).decode('UTF-8')

s = "UHl0aG9uIGlzIGZ1bg=="
print(base64ToText(s))