import lightning as L

from poster import Poster


class CustomPosterApp(L.LightningFlow):
    def __init__(self):
        super().__init__()
        self.poster = Poster(resource_dir="resources", cloud_compute=L.CloudCompute())

    def run(self):
        self.poster.run()

    def configure_layout(self):
        return {"name": "Poster", "content": self.poster.url + "/poster.html"}


if __name__ == '__main__':
    app = L.LightningApp(CustomPosterApp())
