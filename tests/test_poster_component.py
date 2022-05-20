from threading import Thread
import time
import requests
from poster.component import Poster


def test_send_message():
    poster = Poster(resource_path="resources")
    thread = Thread(target=poster.run, daemon=True)
    thread.start()
    time.sleep(5)
    assert poster.ready
    res = requests.get(f"http://localhost:{poster.port}/poster.html")
    assert res.status_code == 200
