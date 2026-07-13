
import pytest
from leading_specification import ContextValidationError, EngineeringContext, LeadingSpecification, validate_context

def test_valid_context():
    c=EngineeringContext("example",LeadingSpecification("A Specifies B","constraint",("lane",),("object",),("x_t",),("y_t",),("00","07")),"07.ipynb")
    validate_context(c)

def test_empty_repository_rejected():
    c=EngineeringContext("",LeadingSpecification("A Specifies B","constraint",("lane",),("object",),("x_t",),("y_t",),("00",)),"07.ipynb")
    with pytest.raises(ContextValidationError): validate_context(c)
