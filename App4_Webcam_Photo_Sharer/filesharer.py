from filestack import Client


class FileShare:
    def __init__(self, api_key):
        self.api_key = api_key
        self.client = Client(self.api_key)

    def share(self, filepath):
        share_link = self.client.upload(filepath=filepath)
        return share_link.url
