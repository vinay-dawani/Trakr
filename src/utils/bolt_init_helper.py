import os
from dotenv import load_dotenv
from slack_bolt import App

load_dotenv()

# Initialization of the slack app
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
)