try:
    from utils.bolt_init_helper import app
    from utils.bolt_helpers import get_channel_history
    from service.commands.scan_command import analyze_historical_scores
except ImportError:
    from ..utils.bolt_init_helper import app
    from ..utils.bolt_helpers import get_channel_history


@app.command("/scan")
def scan_build_history(ack, body) -> None:
    """Get history of slack channel and put in datastore

    Args:
        ack ([type]): [description]
        body ([type]): message payload
    """
    ack(f"starting the scan :wink:")

    channel_id = body["channel_id"]   
    analyze_historical_scores(channel_id)
