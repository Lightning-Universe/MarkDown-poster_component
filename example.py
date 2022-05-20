import lightning as L

from poster import Poster


class YourComponent(L.LightningFlow):
    def __init__(self):
        super().__init__()
        self.poster = Poster(resource_path="resources")

    def run(self):
        self.poster.run()


if __name__ == '__main__':
    app = L.LightningApp(YourComponent())
