import json


def load_json():
    with open('posts.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def get_by_word(word):
    result = []
    for post in load_json():
        if word.lower() in post['content'].lower():
            result.append(post)
    return result


def save_picture(picture):
    filename = picture.filename
    path = f'uploads/images/{filename}'
    picture.save(path)
    return path


def add_post(post):
    posts = load_json()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file)
    return posts
