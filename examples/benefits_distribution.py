
from leading_specification import EngineeringContext, LeadingSpecification

CONTEXT = EngineeringContext(
    repository="benefits-distribution",
    specification=LeadingSpecification(
        engineering_statement="Benefit Distribution Specifies Sustainable Development",
        constraint="deployment constraints",
        connected_lanes=("deployment policy", "telemetry", "benefit distribution", "development indicators"),
        engineering_objects=("policy", "telemetry", "distribution state", "indicator"),
        state_variables=("pi_t", "T_t", "d_t", "I_t"),
        observations=("deployment telemetry",),
        construction_sequence=("00 context", "07 telemetry", "13 estimation", "17 distribution", "23 dynamics", "29 optimization", "37 controllers", "43 benchmarks"),
        trailing_indicators=("sustainable-development indicators",),
    ),
    next_notebook="07_telemetry.ipynb",
    source="Google DeepMind: The Case for Globally Beneficial Technology",
)
