from guillotina import configure
from linkspider.api import ILichesLayer


@configure.service(method='GET', name='home',
                   permission='guillotina.Public',
                   context=ILichesLayer,
                   allow_access=True)
async def url_list(context, request):
    result = len(context.async_items(suppress_events=True))
    logged_in = True
    return {'result': result, 'project': 'liches', 'loggedin': logged_in}
