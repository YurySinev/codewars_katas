def generate_hashtag(s):
    if len(s)==0:
        return False
    temp = '#' + s.title()
    hashtag = temp.replace(" ", "")
    return hashtag if len(hashtag) < 141 else False


print(generate_hashtag("Hello there thanks for trying my Kata"))
