# -*- coding: utf-8 -*-
from dateutil.tz import tzlocal
from guillotina.commands import Command
from guillotina.component import get_utility
from guillotina.interfaces import IApplication
from guillotina.interfaces import IDatabase

import aiohttp
import datetime


async def download_url(url):
    async with aiohttp.ClientSession() as session:
        resp = await session.get(url.url)
        url.last_visited = datetime.datetime.now(tz=tzlocal())
        url.status = resp.status
        url.reason = url.reason


class Runner(Command):

    def get_parser(self):
        parser = super(Runner, self).get_parser()
        # add command arguments here...
        return parser

    async def check_links(self, db):
        tm = self.request._tm = db.get_transaction_manager()
        self.request._db_id = db.id
        tm = db.get_transaction_manager()
        tm.request = self.request
        self.request._txn = txn = await tm.begin(self.request)
        container = await db.async_get(self.arguments.container)

        async for id_, url in container.async_items(suppress_events=True):
            if url.last_visited + datetime.timedelta(days=1) <= datetime.datetime.now(tz=tzlocal()):
                await download_url(url)
                await tm.commit(txn=txn)
            else:
                print('Skipping {0}'.format(url.url))

    async def run(self, arguments, settings, app):
        arguments.container = 'urls'
        root = get_utility(IApplication, name='root')
        for _id, db in root:
            if IDatabase.providedBy(db):
                await self.check_links(db)
