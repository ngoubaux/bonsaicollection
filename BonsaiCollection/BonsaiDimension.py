# -*- coding: utf-8 -*-
#
# File: BonsaiDimension.py
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
from Products.BonsaiCollection.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    DateTimeField(
        name='when',
        index="DateIndex",
        widget=CalendarWidget(
            show_hm=False,
            label='When',
            label_msgid='BonsaiCollection_label_when',
            i18n_domain='BonsaiCollection',
        )
    ),

    IntegerField(
        name='trunkSize',
        widget=IntegerField._properties['widget'](
            label='Trunksize',
            label_msgid='BonsaiCollection_label_trunkSize',
            i18n_domain='BonsaiCollection',
        ),
        description="en cm"
    ),

    IntegerField(
        name='height',
        widget=IntegerField._properties['widget'](
            label='Height',
            label_msgid='BonsaiCollection_label_height',
            i18n_domain='BonsaiCollection',
        ),
        description="en cm"
    ),

    IntegerField(
        name='width',
        widget=IntegerField._properties['widget'](
            label='Width',
            label_msgid='BonsaiCollection_label_width',
            i18n_domain='BonsaiCollection',
        ),
        description="en cm"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BonsaiDimension_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BonsaiDimension(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Prise de dimension'

    meta_type = 'BonsaiDimension'
    portal_type = 'BonsaiDimension'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 0
    #content_icon = 'BonsaiDimension.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Prise de dimension"
    typeDescMsgId = 'description_edit_bonsaidimension'

    _at_rename_after_creation = True

    schema = BonsaiDimension_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(BonsaiDimension, PROJECTNAME)
# end of class BonsaiDimension

##code-section module-footer #fill in your manual code here
##/code-section module-footer



