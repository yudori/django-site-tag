from django_site_tag.utils import find_and_append_text, get_site_tag


class SiteTagMiddleware:

    BODY_TAG = '<body>'
    DEFAULT_CHARSET = 'utf-8'

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        charset = response.charset or self.DEFAULT_CHARSET
        # get response content and insert the site tag in <body> tag
        response.content = find_and_append_text(response.content,
                                                self.BODY_TAG.encode(charset),
                                                get_site_tag().encode(charset))
        return response

