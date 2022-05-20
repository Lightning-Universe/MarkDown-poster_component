<!---:lai-name: Slack Messenger--->

<div align="center">
<img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/lai.png" width="200px">

A Lightning component to send a message on Slack
______________________________________________________________________

![Tests](https://github.com/PyTorchLightning/LAI-slack-messenger/actions/workflows/ci-testing.yml/badge.svg)

</div>

# About
This component lets you render Markdown page to the Lightning app.


----

## Use the component

<!---:lai-use:--->
```python
import lightning as L
from poster import Poster

class YourComponent(L.LightningFlow):
    def __init__(self):
        super().__init__()
        self.poster = Poster(resource_path="resources/poster.md")

    def run(self):
        self.poster.run()
```

## install
Use these instructions to install:

<!---:lai-install:--->
```bash
git clone https://github.com/PyTorchLightning/markdown-poster.git
cd markdown-poster
pip install -r requirements.txt
pip install -e .
```
