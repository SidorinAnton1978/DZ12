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

