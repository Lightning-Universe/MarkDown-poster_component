<!---:lai-name: Slack Messenger--->

<div align="center">
<img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/lai.png" width="200px">

A Lightning component to create Markdown Poster

<img src="https://github.com/PyTorchLightning/markdown-poster/raw/main/resources/preview.png">

______________________________________________________________________

![Tests](https://github.com/PyTorchLightning/LAI-slack-messenger/actions/workflows/ci-testing.yml/badge.svg)

</div>

# About

This component lets you make posters from Markdown to the Lightning app.


----

## Use the component

<!---:lai-use:--->

```python
import lightning as L
from poster import Poster


class CustomPosterApp(L.LightningFlow):
    def __init__(self):
        super().__init__()
        self.poster = Poster(resource_dir="resources")

    def run(self):
        self.poster.run()

    def configure_layout(self):
        return {"name": "Poster", "content": self.poster.url + "/poster.html"}


if __name__ == '__main__':
    app = L.LightningApp(CustomPosterApp())
```

## install

Use these instructions to install:

#### Lightning CLI

```lightning install component lightning/markdown-poster```

#### Manual

```bash
git clone https://github.com/PyTorchLightning/markdown-poster.git
cd markdown-poster
pip install -r requirements.txt
pip install -e .
```

> **Note**: [This component isn't compatible with Windows](https://github.com/patrick-kidger/mkposters#assumptions).

Learn more about this [here](https://github.com/patrick-kidger/mkposters)
