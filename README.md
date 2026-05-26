# ForgeFlow 🚀

ForgeFlow is a compiler-style AI application generation system that transforms natural language prompts into structured, validated, and execution-aware application configurations.

Instead of relying on a single prompt, ForgeFlow uses a deterministic multi-stage pipeline inspired by traditional compiler architectures.

---

# ✨ Features

- Multi-stage AI generation pipeline
- Intent extraction layer
- System architecture generation
- Schema generation engine
- Validation + repair engine
- Cross-layer consistency checks
- Runtime simulation
- Deterministic structured outputs
- Metrics dashboard
- Edge-case evaluation framework

---

# 🧠 Compiler-Style Architecture

ForgeFlow follows a staged pipeline:

```text
User Prompt
    ↓
Intent Extraction
    ↓
System Architecture Layer
    ↓
Schema Generation
    ↓
Validation Engine
    ↓
Repair Engine
    ↓
Runtime Simulation
```

---

# ⚙️ Pipeline Stages

## 1. Intent Extraction

The user prompt is parsed into a structured intermediate representation.

Extracted:
- entities
- features
- roles
- modules

Example:

```json
{
  "features": ["login", "dashboard"],
  "entities": ["users", "contacts"],
  "roles": ["admin", "user"]
}
```

---

## 2. System Architecture Layer

ForgeFlow converts extracted intent into:
- application modules
- database entities
- authentication flows
- role relationships

This stage behaves similarly to semantic analysis in a compiler.

---

## 3. Schema Generation

ForgeFlow generates:

### UI Schema
- pages
- layouts
- components

### API Schema
- endpoints
- methods
- validation

### Database Schema
- tables
- fields
- relationships

### Auth Rules
- permissions
- role-based access control

---

## 4. Validation Engine

The validation layer ensures:
- valid JSON
- required fields present
- schema consistency
- API ↔ DB matching
- UI ↔ API consistency

Detected failures:
- missing fields
- hallucinated properties
- invalid structures
- logical inconsistencies

---

## 5. Repair Engine

Instead of retrying the entire generation blindly, ForgeFlow repairs only failed sections.

Repair strategies:
- partial regeneration
- default value insertion
- schema normalization
- consistency correction

This significantly improves reliability and latency.

---

## 6. Runtime Simulation

ForgeFlow simulates execution by:
- validating generated schemas
- simulating table creation
- verifying runtime compatibility

This ensures outputs are execution-aware.

---

# 📊 Evaluation Framework

ForgeFlow includes:
- 10 normal product prompts
- 10 edge-case prompts

Edge cases include:
- vague prompts
- conflicting requirements
- incomplete instructions
- logical contradictions

Tracked metrics:
- success rate
- latency
- repair frequency
- schema accuracy

Dataset file:

```text
backend/evaluation_dataset.json
```

---

# 🖥️ Tech Stack

## Frontend
- Next.js
- Tailwind CSS
- Framer Motion
- Axios

## Backend
- FastAPI
- Python
- Gemini API

---

# 🚀 Running Locally

## 1. Clone Repository

```bash
git clone YOUR_REPO_URL
```

---

## 2. Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

## 3. Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```text
http://localhost:3000
```

---

# 🔥 Example Prompt

```text
Build a CRM with login, contacts, analytics dashboard, role-based access, and premium subscription payments.
```

---

# 🎯 Design Goals

ForgeFlow was designed around:
- reliability
- deterministic behavior
- modular generation
- execution awareness
- repairability
- schema consistency

---

# 📌 Future Improvements

- Real code generation runtime
- Live deployment generation
- Database migration engine
- Multi-model orchestration
- Visual workflow editor
- Fine-grained permission compiler

---

# 🏆 Why ForgeFlow?

Traditional prompt-based generation systems are brittle.

ForgeFlow approaches AI generation as a compiler problem:
- structured stages
- deterministic outputs
- validation layers
- repair systems
- execution awareness

This makes the system significantly more reliable for production-oriented application generation.

---

# 👨‍💻 Author

Built with ❤️ using compiler-inspired AI system design.