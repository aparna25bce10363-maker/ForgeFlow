def create_architecture(intent):

    architecture = {
        "entities": [],
        "roles": [],
        "modules": [],
        "database_tables": []
    }

    architecture["roles"] = intent.get("roles", [])

    features = intent.get("features", [])

    entities = intent.get("entities", [])

    for entity in entities:

        architecture["entities"].append(entity)

        architecture["database_tables"].append(
            entity.lower()
        )

    if "payments" in features:
        architecture["modules"].append("Stripe")

    if "dashboard" in features:
        architecture["modules"].append("Analytics")

    if "login" in features:
        architecture["modules"].append("Authentication")

    return architecture