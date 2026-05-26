import sqlite3

def simulate_runtime(schema):

    conn = sqlite3.connect(":memory:")

    cursor = conn.cursor()

    created_tables = []

    for table in schema.database:

        fields_sql = []

        for field in table.fields:

            sql_type = "TEXT"

            if field.type == "integer":
                sql_type = "INTEGER"

            fields_sql.append(
                f"{field.name} {sql_type}"
            )

        query = f"""
        CREATE TABLE {table.name} (
            {",".join(fields_sql)}
        )
        """

        cursor.execute(query)

        created_tables.append(table.name)

    return {
        "status":"success",
        "tables_created": created_tables
    }