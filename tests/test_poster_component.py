import time
from threading import Thread

import requests

from poster.component import Poster


def test_send_message():
    poster = Poster(resource_dir="resources")
    thread = Thread(target=poster.run, daemon=True)
    thread.start()
    time.sleep(5)
    res = requests.get(f"http://localhost:{poster.port}/poster.html")
    assert res.status_code == 200
