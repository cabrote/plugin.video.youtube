__author__ = 'bromix'

from . import DirectoryItem
from .. import constants


class SearchHistoryItem(DirectoryItem):
    def __init__(self, context, query, image=None, fanart=None):
        if image is None:
            image = context.create_resource_path('media/search.png')
            pass

        DirectoryItem.__init__(self, query, context.create_uri([constants.paths.SEARCH, 'query'], {'q': query}),
                               image=image)
        if fanart:
            self.set_fanart(fanart)
            pass
        else:
            self.set_fanart(context.get_fanart())
            pass

        context_menu = [(context.localize(constants.localize.SEARCH_REMOVE),
                         'RunPlugin(%s)' % context.create_uri([constants.paths.SEARCH, 'remove'], params={'q': query}))]
        self.set_context_menu(context_menu)
        pass

    pass
