def simulate(config):

    if not config["database"]["tables"]:
        return {
            "status": "failed",
            "message": "No database tables"
        }

    if not config["api"]["endpoints"]:
        return {
            "status": "failed",
            "message": "No API endpoints"
        }

    return {
        "status": "success",
        "message": "Application configuration is executable"
    }