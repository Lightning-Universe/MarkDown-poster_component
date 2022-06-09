import logging

import lightning as L
from mkposters import mkposter

logger = logging.getLogger(__name__)


class Poster(L.LightningWork):
    """
    :param resource_dir: The directory containing the Markdown file.
    :param code_style: The style of code blocks.
    :param background_color: Background color for the poster.
    :param parallel: Whether the Work is parallel.
    """

    def __init__(
            self,
            resource_dir: str,
            code_style: str = "github",
            background_color: str = "#F6F6EF",
            **kwargs
    ):
        super().__init__(parallel=True, **kwargs)
        self.resource_dir = resource_dir
        self.code_style = code_style
        self.background_color = background_color

    def run(self):
        mkposter(
            datadir=self.resource_dir,
            background_color=self.background_color,
            code_style=self.code_style,
            port=self.port,
        )
