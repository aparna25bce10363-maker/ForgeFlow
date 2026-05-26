from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pipeline.intent_extractor import extract_intent
from pipeline.architecture_planner import create_architecture
from pipeline.schema_generator import generate_schema
from pipeline.validator import validate_schema
from pipeline.repair_engine import repair_schema
from pipeline.runtime_simulator import simulate_runtime

app = FastAPI()

# CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():

    return {
        "message":"ForgeFlow Backend Running"
    }

@app.post("/generate")
def generate(payload: dict):

    try:

        prompt = payload["prompt"]

        # Stage 1
        intent = extract_intent(prompt)

        # Stage 2
        architecture = create_architecture(intent)

        # Stage 3
        schema = generate_schema(architecture)

        # Stage 4
        validation_errors = validate_schema(schema)

        repair_log = []

        # Stage 5
        if validation_errors:

            repaired = repair_schema(
                schema,
                validation_errors
            )

            schema = repaired["schema"]

            repair_log = repaired["repairs"]

        # Stage 6
        runtime = simulate_runtime(schema)

        return {

            "intent": intent,

            "architecture": architecture,

            "schema": schema.dict(),

            "validation_errors": validation_errors,

            "repair_log": repair_log,

            "runtime": runtime
        }

    except Exception as e:

        return {
            "error": str(e)
        }