<!---:lai-name: Slack Messenger--->

<div align="center">
<img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/lai.png" width="200px">

A Lightning component to create Markdown Poster

<img src="https://github.com/PyTorchLightning/markdown-poster/raw/main/resources/preview.jpeg">

______________________________________________________________________

[![Lightning](https://img.shields.io/badge/-Lightning-792ee5?logo=pytorchlightning&logoColor=white)](https://lightning.ai)
![license](https://img.shields.io/badge/License-Apache%202.0-blue.svg)
[![CI testing](https://github.com/Lightning-Universe/MarkDown-poster_component/actions/workflows/ci-testing.yml/badge.svg?event=push)](https://github.com/Lightning-Universe/MarkDown-poster_component/actions/workflows/ci-testing.yml)

</div>

# About

This component lets you make posters from Markdown to the Lightning app.

______________________________________________________________________

## Use the component

<!---:lai-use:--->

```python
from lightning.app import LightningFlow, LightningApp
from poster import Poster


class CustomPosterApp(LightningFlow):
    def __init__(self):
        super().__init__()
        self.poster = Poster(resource_dir="resources")

    def run(self):
        self.poster.run()

    def configure_layout(self):
        return {"name": "Poster", "content": self.poster.url + "/poster.html"}


if __name__ == "__main__":
    app = LightningApp(CustomPosterApp())
```

## install

Use these instructions to install:

#### Lightning CLI

`lightning install component lightning/lit-markdown-poster`

#### Manual

```bash
git clone https://github.com/PyTorchLightning/markdown-poster.git
cd markdown-poster
pip install -e .
```

> **Note**: [This component isn't compatible with Windows](https://github.com/patrick-kidger/mkposters#assumptions).

Learn more about this [here](https://github.com/patrick-kidger/mkposters)
