def lambda_handler(event, context):
    return {
        "message": "✅ Deployed via GitHub Actions!",
        "event": event
    }