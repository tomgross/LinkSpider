from guillotina import configure
from guillotina import schema
from guillotina import Interface
from guillotina import interfaces
from guillotina import content


class IURL(interfaces.IItem):
    url = schema.TextLine()
    last_visited = schema.Datetime()
    status = schema.Int()
    reason = schema.TextLine()


@configure.contenttype(
    type_name="Url",
    schema=IURL)
class URL(content.Item):
    """
    Our URL type
    """



