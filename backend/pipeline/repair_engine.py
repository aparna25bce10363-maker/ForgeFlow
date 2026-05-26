from models.app_schema import Field, AuthRule

def repair_schema(schema, errors):

    repaired_items = []

    for error in errors:

        # Missing DB field repair

        if "missing DB field" in error:

            missing_field = error.split(": ")[1]

            schema.database[0].fields.append(

                Field(
                    name=missing_field,
                    type="string",
                    required=False
                )
            )

            repaired_items.append(
                f"Added missing DB field: {missing_field}"
            )

        # Missing auth repair

        if "No authentication rules defined" in error:

            schema.auth_rules.append(

                AuthRule(
                    role="user",
                    permissions=["read"]
                )

            )

            repaired_items.append(
                "Added default auth rule"
            )

    return {
        "schema": schema,
        "repairs": repaired_items
    }