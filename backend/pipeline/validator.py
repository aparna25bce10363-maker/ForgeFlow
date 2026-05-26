def validate_schema(schema):

    errors = []

    db_fields = []

    # Collect all DB fields

    for table in schema.database:

        for field in table.fields:

            db_fields.append(field.name)

    # Validate APIs against DB

    for api in schema.apis:

        for field in api.response_fields:

            if field not in db_fields:

                errors.append(
                    f"API references missing DB field: {field}"
                )

    # Validate auth roles

    if len(schema.auth_rules) == 0:

        errors.append(
            "No authentication rules defined"
        )

    return errors