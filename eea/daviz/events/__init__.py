""" Daviz/events init module with DavizEnabledEvent class
"""
from zope.interface import implements
from eea.daviz.events.interfaces import IDavizRelationsChangedEvent
from eea.daviz.events.interfaces import IDavizSpreadSheetChanged

#BBB
from eea.app.visualization.events import \
     VisualizationEnabledEvent as DavizEnabledEvent
from eea.app.visualization.events import \
     VisualizationFacetDeletedEvent as DavizFacetDeletedEvent

class DavizRelationsChanged(object):
    """ Sent if relations for a Daviz Visualization were changed
    """
    implements(IDavizRelationsChangedEvent)

    def __init__(self, context, **kwargs):
        self.object = context
        self.relatedItems = kwargs.get('relatedItems', [])

class DavizSpreadSheetChanged(object):
    """ Sent if spreadsheet for a Daviz Visualization was changed
    """
    implements(IDavizSpreadSheetChanged)

    def __init__(self, context, **kwargs):
        self.object = context
        self.spreadsheet = kwargs.get('spreadsheet', '')

__all__ = (
    DavizEnabledEvent.__name__,
    DavizFacetDeletedEvent.__name__,
    DavizRelationsChanged.__name__,
    DavizSpreadSheetChanged.__name__,
)
