from flask import Flask, render_template, flash, request
import applog.list_jobs as jobs


app = Flask(__name__)


@app.route('/')
def homepage():
    flash('flash test')
    return render_template('main.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/search-results/', methods=['GET'])
def results():
    search_query = request.args.get('q')
    search_location = request.args.get('l')
    search_string = 'jobs?q=' + search_query + '&l=' + search_location
    search_url = 'https://www.indeed.com/' + search_string
    df = jobs.get_all_parameters_for_all_listings(search_url)
    del df['Link']
    TABLE = df.to_html(classes='table table-hover', index=False, escape=False)
    flash(len(df))
    flash(TABLE)

    import sys
    flash(sys.path)
    return render_template('results.html', TABLE=TABLE)


if __name__ == '__main__':
    app.run(debug=True)
