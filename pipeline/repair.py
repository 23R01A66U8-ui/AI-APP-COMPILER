def repair(config, errors):

    for error in errors:

        # Fix missing auth roles
        if error == "Auth roles missing":

            config["auth"]["roles"] = {
                "admin": [
                    "view",
                    "create",
                    "update",
                    "delete"
                ],
                "user": [
                    "view"
                ]
            }

        # Fix missing UI
        elif error == "UI pages missing":

            config["ui"]["pages"] = [
                {
                    "name": "Dashboard",
                    "components": [
                        "table",
                        "form"
                    ]
                }
            ]

        # Fix missing DB
        elif error == "No database tables defined":

            config["database"]["tables"] = [
                {
                    "name": "users",
                    "fields": [
                        "id",
                        "name"
                    ]
                }
            ]

        # Fix missing API
        elif error == "No API endpoints defined":

            config["api"]["endpoints"] = [
                {
                    "path": "/users",
                    "method": "GET"
                }
            ]

        # Fix endpoint-table mismatch
        elif "Missing table for endpoint" in error:

            table_name = error.replace(
                "Missing table for endpoint ",
                ""
            )

            config["database"]["tables"].append({
                "name": table_name,
                "fields": [
                    "id",
                    "name"
                ]
            })

    return config