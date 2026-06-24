import streamlit as st

from pipeline.intent import extract_intent
from pipeline.design import design_system
from pipeline.schema_generator import generate_schemas
from pipeline.validator import validate
from pipeline.repair import repair
from runtime.simulator import simulate

st.set_page_config(
    page_title="AI App Compiler",
    layout="wide"
)

st.title("AI App Compiler")

user_prompt = st.text_area(
    "Enter your app idea",
    placeholder="Build a CRM with login, contacts, payments and admin dashboard"
)

if st.button("Generate"):

    try:

        # Stage 1
        intent = extract_intent(user_prompt)

        st.subheader("1. Intent Extraction")
        st.json(intent)

        # Stage 2
        design = design_system(intent)

        st.subheader("2. System Design")
        st.json(design)

        # Stage 3
        schemas = generate_schemas(design)

        st.subheader("3. Generated Schemas")
        st.json(schemas)

        # Stage 4
        validation = validate(schemas)

        st.subheader("4. Validation")
        st.json(validation)

        # Stage 5
        if not validation["valid"]:

            schemas = repair(
                schemas,
                validation["errors"]
            )

            st.subheader("5. Repair Output")
            st.json(schemas)

        # Stage 6
        execution = simulate(schemas)

        st.subheader("6. Execution Simulation")
        st.json(execution)

    except Exception as e:

        st.error(str(e))