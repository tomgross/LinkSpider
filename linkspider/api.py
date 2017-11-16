from guillotina import configure
from guillotina.interfaces import IResourceSerializeToJson
from linkspider.content import IURL
from guillotina.component import get_multi_adapter



@configure.service(method='GET', name='@urls',
                   permission='guillotina.Public',
                   allow_access=True)
async def url_list(context, request):
    urls = []
    async for ident, url in context.async_items(suppress_events=True):
        if IURL.providedBy(url):
            urls.append([await get_multi_adapter((url, request), IResourceSerializeToJson)(), url.status])

    return {
        'urls': urls,
        'num': len(urls),
        'codes': [[200], [404], [500]],
        'code': 200,
        'name': 'Link Spider V1.0'
    }


from guillotina.interfaces import IContainer
from guillotina.interfaces import IRequest
from guillotina.interfaces import IResource
from guillotina.traversal import TraversalRouter
from guillotina.traversal import traverse
from guillotina.content import Resource
from zope.interface import alsoProvides
from zope.interface import implementer
from linkspider.interfaces import ILichesLayer
from linkspider.interfaces import ILMSLayer


@configure.contenttype(type_name="LichesRouteSegment")
@implementer(ILichesLayer)
class LichesRouteSegment(Resource):

    type_name = 'LichesRouteSegment'

    def __init__(self, name, parent):
        super().__init__()
        self.__name__ = self.id = name
        self.__parent__ = parent


@configure.contenttype(type_name="LMSRouteSegment")
class LMSRouteSegment(LichesRouteSegment):

    type_name = 'LMSRouteSegment'


class LinkCheckerRouter(TraversalRouter):
    async def traverse(self, request: IRequest) -> IResource:
        '''custom traversal here...'''
        resource, tail = await super().traverse(request)
        if len(tail) > 0 and tail[0] in ('liches', 'lms') and IContainer.providedBy(resource):
            segment = LichesRouteSegment(tail[0], resource)
            if tail[0] == 'liches':
                alsoProvides(request, ILichesLayer)
            elif tail[0] == 'lms':
                #segment = LMSRouteSegment(tail[0], resource)
                alsoProvides(request, ILMSLayer)
            if len(tail) > 1:
                # finish traversal from here
                return await traverse(request, segment, tail[1:])
            else:
                resource = segment
                tail = tail[1:]
        return resource, tail


@configure.service(method='GET', name='home',
                   permission='guillotina.Public',
                   context=ILichesLayer,
                   allow_access=True)
async def url_list(context, request):
    urls = context.__parent__
    result = await urls.async_len()
    logged_in = True
    return {'result': result, 'project': 'liches', 'loggedin': logged_in}
