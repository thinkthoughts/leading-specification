
from leading_specification import EngineeringContext, LeadingSpecification

def test_round_trip(tmp_path):
    c=EngineeringContext("example",LeadingSpecification("A Specifies B","constraint",("lane",),("object",),("x_t",),("y_t",),("00","07")),"07.ipynb")
    assert EngineeringContext.load(c.save(tmp_path/"context.json")) == c
