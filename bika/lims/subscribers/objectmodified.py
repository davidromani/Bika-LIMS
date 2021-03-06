from Products.CMFCore.utils import getToolByName
from bika.lims import bikaMessageFactory as _
from bika.lims import logger
import transaction

def ObjectModifiedEventHandler(obj, event):
    """ Various types need automation on edit.
    """
    if not hasattr(obj, 'portal_type'):
        return

    if obj.portal_type == 'Calculation':
        # Update historyaware back-references
        backrefs = obj.getBackReferences('AnalysisServiceCalculation')
        for i,service in enumerate(backrefs):
            print "%s points to %s (version %s)" % (service.Title(), obj.Title(), obj.version_id+1)
            service['reference_versions'][obj.UID()] = obj.version_id+1
