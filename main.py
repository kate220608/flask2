from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/training/<prof>')
def index(prof):
    img1 = url_for('static', filename='img/spaceship_1.jpg')
    img2 = url_for('static', filename='img/spaceship_2.png')
    css = url_for('static', filename='css/style.css')
    return render_template('training.html',  prof=prof, img1=img1, img2=img2, css=css)


@app.route('/list_prof/<type_of_list>')
def print_list(type_of_list):
    css = url_for('static', filename='css/style.css')
    return render_template('list.html', css=css, type_of_list=type_of_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')