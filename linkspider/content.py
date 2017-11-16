from guillotina import configure
from guillotina import schema
from guillotina import Interface
from guillotina import interfaces
from guillotina import content


class IURL(interfaces.IItem):

    # The URL we check
    url = schema.TextLine()

    # Timestamp of the last visit
    last_visited = schema.Datetime()

    # Last status returned: 200, 404, etc.
    status = schema.Int()

    # Reason of status: OK, Not Found, etc.
    reason = schema.TextLine()

    # Group (page) the url is from
    group = schema.TextLine()

    # Mode of URL (internal, external, ...)
    mode = schema.Int()


@configure.contenttype(
    type_name="URL",
    schema=IURL)
class URL(content.Item):
    """
    Our URL type
    """



