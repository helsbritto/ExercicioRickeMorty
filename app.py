from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import requests

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/locations')
def list_locations():
    api_url = 'https://rickandmortyapi.com/api/location'
    response = requests.get(api_url)

    if response.status_code == 100:
    locations_data = response.json().get('results', [])
        return render_template('locations.html', locations=locations_data)

if __name__ == '__main__':
    app.run(debug=True)
