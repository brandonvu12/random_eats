from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
from flask import render_template, redirect, request

from forms import SearchForm
from api import get_data
import urllib.parse

@app.route('/', methods = ['GET', 'POST'])
@app.route('/search', methods = ['POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        location = request.form.get('location')
        term = request.form.get('search')
        return redirect('/results/{}/{}'.format(location, term))
    return render_template('search.html', form = form)

@app.route('/results/<location>/')
@app.route('/results/<location>/<term>')
def results(location, term = ''):
    business = get_data(location, term)
    if business == None:
        return redirect('/no-results')
    name = business['name']
    image = business['image_url']
    rating = business['rating']
    address = ' '.join(business['location']['display_address'])
    maps = 'https://www.google.com/maps/search/?api=1&query=' + urllib.parse.quote_plus(name + ' ' + business['location']['display_address'][-1])

    return render_template('results.html', name=name, image=image,
    rating=rating, address=address, maps = maps)

@app.route('/no-results')
def no_results():
    return render_template('no-results.html')
if __name__ == '__main__':
    app.run()

