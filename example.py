import lightning as L

from poster import Poster


class YourComponent(L.LightningFlow):
    def __init__(self):
        super().__init__()
        self.poster = Poster(resource_dir="resources")

    def run(self):
        self.poster.run()

    def configure_layout(self):
        return {"name": "Poster", "content": self.poster.url + "/poster.html"}


if __name__ == '__main__':
    app = L.LightningApp(YourComponent())
