def generate_schemas(design):

    entities = design.get("entities", [])
    roles = design.get("roles", [])

    # DATABASE
    database = {
        "tables": []
    }

    for entity in entities:
        database["tables"].append({
            "name": entity.lower() + "s",
            "fields": ["id", "name"]
        })

    # API
    api = {
        "endpoints": []
    }

    for entity in entities:
        api["endpoints"].append({
            "path": f"/{entity.lower()}s",
            "method": "GET"
        })

    # UI
    ui = {
        "pages": []
    }

    for entity in entities:
        ui["pages"].append({
            "name": entity,
            "components": ["table", "form"]
        })

    # AUTH
    auth = {
        "roles": {}
    }

    for role in roles:
        auth["roles"][role] = ["view", "create"]

    return {
        "database": database,
        "api": api,
        "ui": ui,
        "auth": auth
    }