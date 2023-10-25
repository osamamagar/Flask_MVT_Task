from flask import render_template, request, redirect, url_for
from app.sections import section_blueprint
from app.models import Section, db


@section_blueprint.route('/',endpoint='sections_home' )
def sections_home():
    sections = Section.query.all()
    return render_template('sections/sections_home.html', sections=sections)




@section_blueprint.route('/create_section', methods=['GET', 'POST'], endpoint='create_section')
def create_section():
    if request.method == 'POST':
        name = request.form['name']
        section = Section(name=name)
        db.session.add(section)
        db.session.commit()
        return redirect(url_for('sections.sections_home'))

    return render_template('sections/create_section.html')


