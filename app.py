from lightning.app import CloudCompute, LightningApp, LightningFlow

from poster import Poster


class CustomPosterApp(LightningFlow):
    def __init__(self):
        super().__init__()
        self.poster = Poster(resource_dir="resources", cloud_compute=CloudCompute())

    def run(self):
        self.poster.run()

    def configure_layout(self):
        return {"name": "Poster", "content": self.poster.url + "/poster.html"}


if __name__ == "__main__":
    app = LightningApp(CustomPosterApp())
