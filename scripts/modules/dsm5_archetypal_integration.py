# PROJECT-168 CLINICAL INTEGRATION MODULE
# Timestamp: 2025-08-27T06:27:48-07:00 (Updated)
# Module: DSM-5 Archetypal Framing Engine
# File: /modules/dsm5_archetypal_integration.py

project_168:
  clinical_integration:
    module_name: "DSM-5 Archetypal Framing Engine"
    objective: "Bridge clinical diagnosis with archetypal symbolism through non-clinical, poetic framing"
    core_principle: "Hendoku Iyaku (毒を薬に) - Transform diagnostic 'poison' into symbolic 'medicine'"
    disclaimer: "This module does NOT provide medical diagnosis, treatment, or advice. It offers archetypal perspectives for contemplation only."

    input_handling:
      dsm5_input:
        method: "User-self-reported diagnostic code or condition name"
        examples: 
          - "F41.1 (Generalized Anxiety Disorder)"
          - "F43.23 (Adjustment Disorder with Mixed Anxiety and Depressed Mood)"
          - "PTSD"
          - "Bipolar II"
        validation: "Regex match against known DSM-5 codes OR NLP matching against common condition names"
        file: "/clinical/input_validation.py"

      soft_input_protocol:
        rule: "All clinical input is treated as 'soft' user-self-reported data. The system makes NO clinical validation."
        purpose: "To provide a framework for the user to contextualize their experience, not to define it."
        file: "/clinical/soft_input_handler.py"

    processing_engine:
      framework: "Archetypal Reframing"
      process_flow:
        1. "Acknowledge: System acknowledges the input without judgment."
        2. "Contextualize: Maps the diagnosis to its general archetypal 'challenge' (Poison)."
        3. "Reframe: Offers the archetypal 'potential' or 'medicine' inherent in the challenge."
        4. "Symbolize: Returns a symbol set for contemplation and integration."
      file: "/clinical/archetypal_reframer.py"

    output_framing:
      structure: "Poetic, non-clinical, and archetypal"
      example:
        user_input: "F41.1 (Generalized Anxiety Disorder)"
        system_response:
          archetypal_challenge: "The Hyper-Vigilant Guardian. The mind's constant scanning of the horizon for threats, born from a deep commitment to safety."
          archetypal_potential: "The Profound Discerner. The ability to perceive subtle patterns, nuances, and potential outcomes that others miss. The energy of preparation can be alchemized into the energy of profound presence."
          symbol_set: 
            - primary: "♍︎" (Virgo) # For analysis and discernment
            - secondary: "⛰" (Mountain) # For grounding and perspective
            - tertiary: "🛡" (Shield) # For conscious protection
          actionable_contemplation: "How can the energy of constant scanning be redirected from identifying threats to perceiving beauty and opportunity? What is the difference between vigilance and presence?"
      file: "/clinical/output_generator.py"

    symbol_mapping:
      data_source: "/data/core/psl27_matrices.csv"
      algorithm: "Fuzzy match between DSM5 condition keywords and archetypal matrices"
      custom_symbols: "User can propose new mappings via Baligon Protocol"
      file: "/clinical/dsm5_symbol_mapper.py"

    ethical_guardrails:
      mandatory_warnings:
        - "This is not a medical tool. Please consult a healthcare professional for diagnosis and treatment."
        - "Your lived experience is more complex than any diagnostic code."
        - "This framing is a perspective for exploration, not a definition of your being."
      access_control: "Module only available to users aged 18+"
      crisis_protocol: "If input indicates severe risk (e.g., suicidal ideation), display crisis resources and encourage professional help."
      file: "/clinical/ethical_guardrails.py"

    integration_with_core:
      link_to_verbosity: 
        default: "Returns the archetypal challenge/potential and symbol set."
        minimal: "Returns only the symbol set."
        detailed: "Returns extended analysis, including planetary and qabalistic correspondences related to the challenge."
      impact_calculation: "A user's engagement with this module contributes to 'global_group_impact' for mental health-related archetypes."
      file: "/clinical/core_integration.py"

# END OF CLINICAL INTEGRATION MODULE SPECIFICATION
