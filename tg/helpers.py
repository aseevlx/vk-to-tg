def get_repost_text(post):
    """
    Generate text from reposted text
    :param post: TgPost object
    :return: str
    """
    if not post.reposted_from:
        return ''

    repost_text = f'Репост {post.reposted_from}\n\n{post.reposted_text}'

    return repost_text
