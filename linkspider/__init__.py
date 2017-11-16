from guillotina import configure
from linkspider.api import LinkCheckerRouter

app_settings = {
    # provide custom application settings here...

    'commands': {
        'runner': 'linkspider.command.Runner'
    },

    'router': LinkCheckerRouter

}


def includeme(root):
    """
    custom application initialization here
    """
    configure.scan('linkspider.api')
    configure.scan('linkspider.install')
    configure.scan('linkspider.content')
