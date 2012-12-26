from flask import Flask, render_template
app = Flask(__name__)

from flask.ext.bootstrap import Bootstrap

Bootstrap(app)

app.config['BOOTSTRAP_USE_MINIFIED'] = True
app.config['BOOTSTRAP_USE_CDN'] = True
app.config['BOOTSTRAP_FONTAWESOME'] = True

@app.route('/')
def index():
    return render_template('base.html') 

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/bullet')
def bullet():
    return render_template('bullet.html')

@app.route('/stacked')
def stacked():
    return render_template('stacked.html')

@app.route('/stacked2')
def stacked2():
    return render_template('stacked2.html')

@app.route('/bar')
def bar():
    return render_template('bar.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80,debug=True)
