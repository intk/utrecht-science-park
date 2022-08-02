# get a preview image
from plone.namedfile.scaling import ImageScaling


class FallbackImageScale(ImageScaling):
    def __init__(self, context, request):
        # identifies the proper @@images view for the content item used as fallback

        # import pdb
        #
        # pdb.set_trace()
        obj = None
        for child in context.contentValues():
            if getattr(child, "preview_image", None):  # TODO: handle permissions
                obj = child

        print("Using", obj)
        self.context = obj or context
        self.request = request
        ImageScaling.__init__(self, self.context, self.request)
