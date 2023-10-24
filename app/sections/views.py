from app.sections import section_blueprint


def all_sections():
    return '<h2> section osama page all_section</h2>'


@section_blueprint.route('hello', endpoint='section_hello')
def hello_section():
    return '<h2> ok page hello </h2>'
