def validate(config):

    errors = []

    # Database tables
    tables = [
        table["name"]
        for table in config["database"]["tables"]
    ]

    # API endpoints
    endpoints = [
        endpoint["path"].replace("/", "")
        for endpoint in config["api"]["endpoints"]
    ]

    # UI pages
    pages = config["ui"]["pages"]

    # Auth roles
    auth_roles = config["auth"]["roles"]

    # -------------------------
    # API ↔ Database Validation
    # -------------------------
    for endpoint in endpoints:

        if endpoint not in tables:
            errors.append(
                f"Missing table for endpoint {endpoint}"
            )

    # -------------------------
    # Database Validation
    # -------------------------
    if len(tables) == 0:
        errors.append(
            "No database tables defined"
        )

    # -------------------------
    # API Validation
    # -------------------------
    if len(endpoints) == 0:
        errors.append(
            "No API endpoints defined"
        )

    # -------------------------
    # UI Validation
    # -------------------------
    if len(pages) == 0:
        errors.append(
            "UI pages missing"
        )

    # -------------------------
    # Auth Validation
    # -------------------------
    if not auth_roles:
        errors.append(
            "Auth roles missing"
        )

    # -------------------------
    # Final Result
    # -------------------------
    return {
        "valid": len(errors) == 0,
        "errors": errors
    }