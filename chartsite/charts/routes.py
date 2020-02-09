from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from chartsite import db
from chartsite.models import Chart
from chartsite.charts.forms import ChartForm

charts = Blueprint('charts', __name__)


def chart_list():
    all_charts = Chart.query.all()
    id_list = []
    for i in all_charts:
        id_list = id_list.append(i)
    return id_list


@charts.route("/chart/new", methods=['GET', 'POST'])
def new_chart():
    form = ChartForm()
    if form.validate_on_submit():
        chart = Chart(name=form.name.data,
                      embed_text=form.embed_text.data)
        db.session.add(chart)
        db.session.commit()
        flash('Chart created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_chart.html',
                           name='New chart',
                           form=form)


@charts.route("/chartloop")
def chartloop():
    # Still figuring out logic here...
    # Basically want to loop through all charts on a timer
    all_charts = Chart.query.all()
    return render_template('home.html',
                           name='New chart')


@charts.route("/chart/<int:chart_id>")
def chart(chart_id):
    chart = Chart.query.get_or_404(chart_id)
    return render_template('chart.html', chart=chart)


@charts.route("/chart/<int:chart_id>/update", methods=['GET', 'POST'])
def update_chart(chart_id):
    chart = Chart.query.get_or_404(chart_id)
    form = ChartForm()
    if form.validate_on_submit():
        chart.name = form.name.data
        chart.embed_text = form.embed_text.data
        db.session.commit()
        flash("Chart updated!", 'success')
        return redirect(url_for('charts.chart', chart_id=chart.id))
    elif request.method == 'GET':
        form.name.data = chart.name
        form.embed_text.data = chart.embed_text
    return render_template('create_chart.html', title="Update chart",
                           form=form)


@charts.route("/chart/<int:charts_id>/delete", methods=["POST"])
def delete_chart(chart_id):
    # Can't actually access this yet...
    chart = Chart.query.get_or_404(chart_id)
    db.session.delete(chart)
    db.session.commit()
    flash('Your chart has been deleted!', 'success')
    return redirect(url_for('main.home'))
