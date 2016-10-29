
def get_avatar(backend, strategy, details, response, user=None, *args, **kwargs):
    url = None
    if backend.name == 'facebook':
        url = "http://graph.facebook.com/%s/picture?type=small"%response['id']
    if url:
        user.avatar = url
        user.save()
