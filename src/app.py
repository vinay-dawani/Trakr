import os
from dotenv import load_dotenv
from slack_bolt.adapter.socket_mode import SocketModeHandler

try:
    from utils.bolt_init_helper import app
    from controller import events
except ImportError:
    from .utils.bolt_init_helper import app
    from .controller import events

load_dotenv()


if __name__ == "__main__":
    SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN")).start()
