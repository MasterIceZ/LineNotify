# 2021 - Borworntat Dendumrongkul

class Notify :
    _version = "1.0.0"
    _token = ""
    def __init__(self, _token=""):
        self.token = _token

    def version(self):
        return self._version
    
    def setKey(self, token):
        try:
            self._token = token
            return True
        except:
            return False
    def send_sticker(self, pack, idx):
        payload = {
            'message': " ",
            'stickerPackageId': pack,
            'stickerId': idx
        }
        return self.send(payload)

    def send_message(self, msg):
        payload = { 'message': msg }
        return self.send(payload)
    
    def send(self, payload, file=None):
        if self._token != "":
            import requests
            url = "https://notify-api.line.me/api/notify"
            tok = self._token
            headers = {
                "Authorization": "Bearer " + tok
            }
            r = requests.post(url, headers=headers, data=payload, files=file)
            return True
        else:
            return False
