import os
from dotenv import load_dotenv
from slack_bolt.adapter.socket_mode import SocketModeHandler
from pathlib import Path

try:
    from utils.bolt_init_helper import app
    from controller import events
    from store.scores import create_scores_store
except ImportError:
    from .utils.bolt_init_helper import app
    from .controller import events
    from .store.scores import create_scores_store

load_dotenv()

score_file = Path(r"data/scores.json")
if not score_file.is_file():
    create_scores_store()

if __name__ == "__main__":
    SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN")).start()
