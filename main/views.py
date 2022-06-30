from flask import Blueprint, render_template, request

from functions import get_by_word

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page():
    search_word = request.args.get('s')
    posts = get_by_word(search_word)
    return render_template('post_list.html', word=search_word, posts=posts)

