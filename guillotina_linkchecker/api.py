from guillotina import configure



@configure.service(method='POST', name='@runner',
                   permission='guillotina.AccessContent')
async def linkchecker_runner(context, request):


    urls = []
    async for ident, member in context.async_items(suppress_events=True):
             urls.append(str(member))

    return {
        'running': urls,
    }



# async def hello_many():
#     while True:
#         number = random.randint(0, 3)
#         await asyncio.sleep(number)
#         print('Hello {}'.format(number))
#
#
# event_loop = asyncio.get_event_loop()
# task = asyncio.Task(hello_many())
# print('task running now...')
# event_loop.run_until_complete(asyncio.sleep(10))
# print('we waited 10 seconds')
# task.cancel()
# print('task cancelled')
#
# async def download_url(url):
#     async with aiohttp.ClientSession() as session:
#         resp = await session.get(url)
#         text = await resp.text()
#         print(f'Downloaded {url}, size {len(text)}')
#
#
# event_loop = asyncio.get_event_loop()
# event_loop.run_until_complete(asyncio.gather(
#     download_url('https://www.google.com'),
#     download_url('https://www.facebook.com'),
#     download_url('https://www.twitter.com'),
#     download_url('https://www.stackoverflow.com')
# ))

