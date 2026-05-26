from models.app_schema import *

def generate_schema(architecture):

    database = []

    for entity in architecture["entities"]:

        database.append(

            Table(
                name=entity.lower(),

                fields=[

                    Field(
                        name="id",
                        type="integer",
                        required=True
                    ),

                    Field(
                        name="name",
                        type="string",
                        required=True
                    )
                ]
            )
        )

    apis = []

    for entity in architecture["entities"]:

        apis.append(

            APIEndpoint(
                path=f"/{entity.lower()}",
                method="GET",
                request_fields=[],
                response_fields=[
                    "id",
                    "name"
                ]
            )
        )

    pages = [

        Page(
            name="Dashboard",
            components=[
                "Sidebar",
                "Charts",
                "Stats"
            ]
        )
    ]

    auth_rules = []

    for role in architecture["roles"]:

        auth_rules.append(

            AuthRule(
                role=role,
                permissions=["read","write"]
            )
        )

    return AppSchema(

        app_name="ForgeFlow Generated App",

        database=database,

        apis=apis,

        pages=pages,

        auth_rules=auth_rules
    )