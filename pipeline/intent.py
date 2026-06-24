def extract_intent(user_prompt):

    user_prompt = user_prompt.lower()

    features = []

    if "login" in user_prompt:
        features.append("login")

    if "contact" in user_prompt:
        features.append("contact management")

    if "payment" in user_prompt:
        features.append("payment processing")

    if "dashboard" in user_prompt:
        features.append("admin dashboard")

    if "role" in user_prompt:
        features.append("role based access")

    roles = []

    if "admin" in user_prompt:
        roles.append("admin")

    roles.append("user")

    return {
        "app_type": "CRM",
        "features": features,
        "roles": roles
    }