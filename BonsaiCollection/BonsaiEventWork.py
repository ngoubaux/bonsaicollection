# -*- coding: utf-8 -*-
#
# File: BonsaiEventWork.py
#
# Copyright (c) 2008 by []
# Generator: ArchGenXML Version 1.5.2
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.BonsaiCollection.BonsaiEvent import BonsaiEvent
from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.BonsaiCollection.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='workType',
        widget=SelectionWidget(
            label='Worktype',
            label_msgid='BonsaiCollection_label_workType',
            i18n_domain='BonsaiCollection',
        ),
        vocabulary=NamedVocabulary("""BonsaiWorkType""")
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BonsaiEventWork_schema = BaseSchema.copy() + \
    getattr(BonsaiEvent, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BonsaiEventWork(BaseContent, BonsaiEvent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),) + (getattr(BonsaiEvent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Travail'

    meta_type = 'BonsaiEventWork'
    portal_type = 'BonsaiEventWork'
    allowed_content_types = [] + list(getattr(BonsaiEvent, 'allowed_content_types', []))
    filter_content_types = 0
    global_allow = 0
    content_icon = 'date.png'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Travail"
    typeDescMsgId = 'description_edit_bonsaieventwork'

    _at_rename_after_creation = True

    schema = BonsaiEventWork_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(BonsaiEventWork, PROJECTNAME)
# end of class BonsaiEventWork

##code-section module-footer #fill in your manual code here
##/code-section module-footer



