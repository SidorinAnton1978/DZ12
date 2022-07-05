from flask import Blueprint, render_template, request

from functions import save_picture, add_post

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='./templates')


@loader_blueprint.route('/post')
def post_page():
    return render_template('post_form.html')


@loader_blueprint.post('/post')
def add_post_page():
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:
        return 'Нет картинки или текста'

    picture_path = '/' + save_picture(picture)
    post = add_post({'pic': picture_path, 'content': content})
    return render_template('post_uploaded.html', post=post)

