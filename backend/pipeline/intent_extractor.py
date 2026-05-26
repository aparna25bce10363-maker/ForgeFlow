def extract_intent(user_prompt):

    prompt = user_prompt.lower()

    features = []
    entities = []
    roles = []

    # Features

    if "login" in prompt:
        features.append("login")

    if "dashboard" in prompt:
        features.append("dashboard")

    if "payment" in prompt:
        features.append("payments")

    if "analytics" in prompt:
        features.append("analytics")

    # Entities

    if "crm" in prompt:
        entities.extend([
            "users",
            "contacts"
        ])

    if "ecommerce" in prompt:
        entities.extend([
            "products",
            "orders"
        ])

    # Roles

    if "admin" in prompt:
        roles.append("admin")

    roles.append("user")

    return {

        "app_name":"ForgeFlow Generated App",

        "features": features,

        "entities": entities,

        "roles": roles
    }