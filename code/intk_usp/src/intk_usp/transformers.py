import urllib

from plone.app.linkintegrity.interfaces import IRetriever
from plone.app.linkintegrity.retriever import DXGeneral
from plone.restapi.behaviors import IBlocks
from plone.restapi.deserializer.blocks import iterate_children
from zope.component import adapter, subscribers
from zope.globalrequest import getRequest
from zope.interface import implementer
from zope.publisher.interfaces.browser import IBrowserRequest

# from plone.restapi.interfaces import IBlockFieldLinkIntegrityRetriever
# def get_blocks(obj):
#     """ get_blocks """
#
#     blocks_layout = getattr(obj, 'blocks_layout', {})
#
#     if isinstance(blocks_layout, str):
#         blocks_layout = json.loads(blocks_layout)
#         obj.blocks_layout = blocks_layout
#         obj._p_changed = True
#         logger.info('Converted str blocks_layout for % s',
#                     obj.absolute_url())
#
#     order = blocks_layout.get('items', [])
#
#     blocks = getattr(obj, 'blocks', {})
#
#     if isinstance(blocks, str):
#         blocks = json.loads(blocks)
#         obj.blocks = blocks
#         obj._p_changed = True
#         logger.info('Converted str blocks for % s', obj.absolute_url())
#
#     out = []
#     for _id in order:
#         if _id not in blocks:
#             obj.blocks_layout['items'] = [b for b in order if b in blocks]
#             obj._p_changed = True
#             logger.info("Object with incomplete blocks %s", obj.absolute_url())
#             continue
#         out.append((_id, blocks[_id]))
#
#     return out
#
#
# class BlocksTraverser(object):
#     """ BlocksTraverser """
#
#     def __init__(self, context):
#         self.context = context
#
#     def __call__(self, visitor):
#
#         for (_, block_value) in get_blocks(self.context):
#
#             if visitor(block_value):
#                 self.context._p_changed = True
#
#             self.handle_subblocks(block_value, visitor)
#
#     def handle_subblocks(self, block_value, visitor):
#         """ handle_subblocks """
#
#         if "data" in block_value and isinstance(block_value["data"], dict) \
#                 and "blocks" in block_value["data"]:
#             for block in block_value["data"]["blocks"].values():
#                 if visitor(block):
#                     self.context._p_changed = True
#
#                 self.handle_subblocks(block, visitor)
#
#         if "blocks" in block_value:
#             for block in block_value['blocks'].values():
#                 if visitor(block):
#                     self.context._p_changed = True
#
#                 self.handle_subblocks(block, visitor)
#
#         # if block_value.get('@type') in chart_block_types:
#         #     visitor(block_value.get('chartData', {}))
#
#
# class ResolveUIDDeserializerBase(object):
#     """The "url" smart block field.
#     This is a generic handler. In all blocks, it converts any "url"
#     field from using resolveuid to an "absolute" URL
#     """
#
#     order = 1
#     block_type = None
#     fields = ["url", "href"]        #, "provider_url"
#
#     def __init__(self, context):
#         self.context = context
#
#     def __call__(self, block):
#         dirty = False
#         # Convert absolute links to resolveuid
#         for field in self.fields:
#             link = block.get(field, "")
#             if link and isinstance(link, str):
#                 if 'resolveuid' not in link:
#                     block[field] = path2uid(context=self.context,
#                                             link=clean_url(link))
#                     logger.info("fixed block field:'%s' in %s (%s) => (%s)",
#                                 field, self.context.absolute_url(), link,
#                                 block[field])
#             elif link and isinstance(link, list):
#                 # Detect if it has an object inside with an
#                 # "@id" key (object_widget)
#                 if link and isinstance(link[0], dict) \
#                         and "@id" in link[0]:
#                     for item in link:
#                         if 'resolveuid' not in item['@id']:
#                             old = item['@id']
#                             item["@id"] = path2uid(
#                                 context=self.context,
#                                 link=clean_url(item["@id"])
#                             )
#                             dirty = True
#                             logger.info(
#                                 "fixed block field:'%s' in %s (%s) => (%s)",
#                                 field, self.context.absolute_url(), old,
#                                 item['@id'])
#                 elif link and isinstance(link[0], str):
#                     dirty = any(
#                         ['resolveuid' not in bit for bit in link]) or dirty
#                     block[field] = [
#                         path2uid(context=self.context, link=clean_url(bit))
#                         for bit in link
#                     ]
#
#         return dirty


# @implementer(IBlockFieldDeserializationTransformer)

def fix(url):
    if 'http' in url and 'utrecht' in url:
        return urllib.parse.urlparse(url).path
    else:
        return url


@adapter(IBlocks, IBrowserRequest)
class ActionLinksTransformers(object):
    order = 100
    block_type = 'actionLinks'

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self, value):
        actions = value.get('actions', None)
        if actions:
            for action in actions:
                if action.get('href', None):
                    action['href'] = fix(action['href'])
                if action.get('linkHref'):
                    for link in action['linkHref']:
                        link['@id'] = fix(link['@id'])

        return value
