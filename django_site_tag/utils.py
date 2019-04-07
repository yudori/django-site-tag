from django.conf import settings


def InvalidPositionException(ValueError):
    pass


def get_setting(name, default=None):
    """Get django setting if set, else return default

    Arguments:
        name {string} -- The name of the setting attribute to be gotten

    Keyword Arguments:
        default {?} -- The default value to be returned if attribute isn't found (default: {None})

    Returns:
        ? -- Setting value or default
    """

    if hasattr(settings, name):
        return getattr(settings, name)
    return default


def find_and_append_text(text, search_string, extra_text):
    """Finds a substring in a string and appends extra text in located position.
    
    Arguments:
        text {string} -- Full text to search for substring
        search_string {string} -- keyword to search for
        extra_text {string} -- text to append after search_string is found
    """

    index = text.find(search_string)
    index = index + len(search_string)
    result_text = text

    if index >= 0:
        result_text = text[:index] + extra_text + text[index:]
    
    return result_text


def get_default_tag_text():
    """Get tag text to be displayed when not explicitly supplied by user
    
    Returns:
        string -- The default tag text
    """

    tag_text = ''
    if get_setting('DEBUG'):
        tag_text = 'DEV'
    return tag_text


def get_css_position(position_string):
    """Get the position of a tag element as css
    
    Arguments:
        position_string {string} -- A string containing 4 values separated by a space denoting
            the top, right, bottom and left position magnitudes respectively
    
    Raises:
        InvalidPositionException -- Raised when the positional arguments are less than or
            greater than 4
    
    Returns:
        string -- built css style attributes and values
    """

    position_list = position_string.split()
    if not len(position_list) == 4:
        raise InvalidPositionException('Invalid number of position arguments, must be 4')
    return 'position: absolute; top:{}; right:{}; bottom:{}; left:{}'.format(
        position_list[0], position_list[1], position_list[2], position_list[3]
    )


def get_site_tag():
    """Get html representation of site tag
    
    Returns:
        string -- The image/text site tag in html
    """
    tag_position = get_css_position(get_setting('SITE_TAG_POSITION') or '15px 0px 0px 15px')
    image_url = get_setting('SITE_TAG_IMAGE')
    if image_url:
        html_content = '<div>   \
                            <img style="height: 100%; width: auto" src="{}"></img>  \
                        </div>'.format(image_url)
    else:
        tag_text = get_setting('SITE_TAG_TEXT') or get_default_tag_text()
        tag_text_style = get_setting('SITE_TAG_TEXT_STYLE') or 'padding: 10px;'
        tag_text_border_style = get_setting('SITE_TAG_TEXT_BORDER_STYLE') or '2px dashed #ff0000;'
        html_content = '<span style="border: {} opacity: 0.5; filter: alpha(opacity=50);"><span style="{}">{}</span></span>' \
                       .format(tag_text_border_style, tag_text_style, tag_text)
    return '<div style="{}">{}</div>'.format(tag_position, html_content)
