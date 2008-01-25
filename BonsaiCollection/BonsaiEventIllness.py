# -*- coding: utf-8 -*-
#
# File: BonsaiEventIllness.py
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
from Products.BonsaiCollection.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    ReferenceField(
        name='blights',
        widget=ReferenceWidget(
            label='Blights',
            label_msgid='BonsaiCollection_label_blights',
            i18n_domain='BonsaiCollection',
        ),
        allowed_types=('Blight',),
        multiValued=0,
        relationship='Illness type'
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BonsaiEventIllness_schema = BaseSchema.copy() + \
    getattr(BonsaiEvent, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BonsaiEventIllness(BaseContent, BonsaiEvent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),) + (getattr(BonsaiEvent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Maladie'

    meta_type = 'BonsaiEventIllness'
    portal_type = 'BonsaiEventIllness'
    allowed_content_types = [] + list(getattr(BonsaiEvent, 'allowed_content_types', []))
    filter_content_types = 0
    global_allow = 0
    content_icon = 'bug_error.png'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Maladie"
    typeDescMsgId = 'description_edit_bonsaieventillness'

    _at_rename_after_creation = True

    schema = BonsaiEventIllness_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(BonsaiEventIllness, PROJECTNAME)
# end of class BonsaiEventIllness

##code-section module-footer #fill in your manual code here
##/code-section module-footer



