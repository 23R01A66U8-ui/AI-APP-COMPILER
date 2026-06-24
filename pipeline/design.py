def design_system(intent):

    features = intent.get("features", [])
    roles = intent.get("roles", [])

    entities = ["User"]
    pages = ["Dashboard"]
    workflows = []

    if "login" in features:
        pages.append("Login")
        workflows.append("User Login")

    if "contact management" in features:
        entities.append("Contact")
        pages.append("Contacts")
        workflows.append("Manage Contacts")

    if "payment processing" in features:
        entities.append("Payment")
        pages.append("Payments")
        workflows.append("Process Payments")

    if "role based access" in features:
        entities.append("Role")
        workflows.append("Manage Permissions")

    if "admin dashboard" in features:
        entities.append("Analytics")
        pages.append("Admin Dashboard")
        workflows.append("View Analytics")

    return {
        "entities": entities,
        "pages": pages,
        "roles": roles,
        "workflows": workflows
    }