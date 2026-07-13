
from .context import EngineeringContext

class ContextValidationError(ValueError):
    pass

def validate_context(context: EngineeringContext) -> None:
    if not context.repository.strip():
        raise ContextValidationError("repository must be non-empty")
    if not context.next_notebook.strip():
        raise ContextValidationError("next_notebook must be non-empty")
    spec = context.specification
    if not spec.engineering_statement.strip():
        raise ContextValidationError("engineering_statement must be non-empty")
    if not spec.constraint.strip():
        raise ContextValidationError("constraint must be non-empty")
    for name in ("connected_lanes", "engineering_objects", "state_variables", "observations", "construction_sequence"):
        values = getattr(spec, name)
        if not values or any(not str(item).strip() for item in values):
            raise ContextValidationError(f"{name} must contain non-empty items")
