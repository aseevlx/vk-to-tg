def get_post_text(post):
    text = post.text
    if post.reposted_from:
        # TODO: check for length, e.g.: 1024 for photo.caption, 4096 for message.text
        reposted_text = f'Репост из {post.reposted_from}\n{post.reposted_text}'
    if text:
        text = f'{reposted_text}\n{text}'
    else:
        text = reposted_text

    return text