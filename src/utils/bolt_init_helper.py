import os
from dotenv import load_dotenv
from pathlib import Path
from slack_bolt import App

# load_dotenv(dotenv_path=Path(r".prod.env"))
load_dotenv()

# Initialization of the slack app
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
)
