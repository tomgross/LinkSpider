from guillotina import configure


app_settings = {
    # provide custom application settings here...

    "commands": {
        "runner": "guillotina_linkchecker.command.Runner"
    }

}


def includeme(root):
    """
    custom application initialization here
    """
    configure.scan('guillotina_linkchecker.api')
    configure.scan('guillotina_linkchecker.install')
    configure.scan('guillotina_linkchecker.content')
