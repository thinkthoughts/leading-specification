
from .figures import plot_construction_sequence, plot_engineering_grammar
from .paths import RepoPaths
from .validation import validate_context

def initialize_notebook_context(context, start=None):
    validate_context(context)
    paths=RepoPaths.discover(start)
    manifest=context.save(paths.results/"00_engineering_context.json")
    grammar=plot_engineering_grammar(context, paths.figures/"00_engineering_grammar.png")
    construction=plot_construction_sequence(context, paths.figures/"00_construction_sequence.png")
    return {"manifest":manifest,"engineering_grammar":grammar,"construction_sequence":construction}
