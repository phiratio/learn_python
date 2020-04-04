# Code Listing #9

"""

SSTI - Server Side Template Injection example - using Flask

"""

# 09-ssti-example.py
from flask import Flask
from flask import request, render_template_string, render_template

app = Flask(__name__)


@app.route('/hello-ssti')
def hello_ssti():
    person = {'name': "world", 'secret': 'jo5gmvlligcZ5YZGenWnGcol8JnwhWZd2lJZYo=='}
    if request.args.get('name'):
        person['name'] = request.args.get('name')

    #template = '''<h2>Hello %s!</h2>''' % person['name']
    template = f'''<h2>Hello {person['name']}!</h2>'''
    return render_template_string(template, person=person)


if __name__ == "__main__":
    app.run(debug=True)

    # in browser add querystring, no slash at the end of url
    # ?name=hi {{person.secret}}