# MBSE_AAS_OCL

This repository contains all models, files, and scripts developed as part of the research work described in the paper:
“Asset Administration Shell-Based Object Constraint Language Validation Framework for Model-Based System Engineering”

The study presents a complete workflow for applying semantic OCL constraints to information models using the Asset Administration Shell (AAS) as a central integration layer. The approach demonstrates how constraints can be validated over model instances and how the results can be integrated into AASs for interoperability, transparency, and machine processing.

# Methodology Summary
The workflow integrates model-driven engineering concepts with AAS technology through the following steps:

1. Fetch and transform AML models into EMF-compatible .ecore and .xmi formats.
2. Apply OCL constraints to model instances.
3. Generate validation result logs.
4. Serialize results into JSON or XML.
5. Store all related files inside AAS submodels for interoperability and machine processing.

The process is supported by a dedicated OCL Validation Component (OVC), currently under development.

# Dependencies
1. AutomationML
2. Eclipse Modeling Framework (EMF)
3. Eclipse OCL Plugin
4. Python 3.11+
5. Eclipse BaSyx (for AAS handling)


# How to Reproduce
1. Clone the repository.
2. Open .aml files using AML editor to see meta and instance information of the example.
3. Open the .ecore (OCLinEcore) and .xmi files using Eclipse Modeling Framework (EMF).
4. Apply OCL constraints (using EMF OCL Plugin).
5. Run ResultSerializationJSON.py to convert validation logs (generated in EMF Validity View) to JSON format.
6. Explore AAS integration structure using Eclipse BaSyx or any AAS-compatible platform.

