from threading import Thread
import time
import requests
from poster.component import Poster


def test_send_message():
    poster = Poster(resource_path="resources")
    thread = Thread(target=poster.run, daemon=True)
    thread.start()
    time.sleep(2)
    res = requests.get(f"http://localhost:{poster.port}")
    assert res.status_code == 200
