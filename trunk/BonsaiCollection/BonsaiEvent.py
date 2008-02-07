# -*- coding: utf-8 -*-
#
# File: BonsaiEvent.py
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
        widget=CalendarWidget(
            label='When',
            label_msgid='BonsaiCollection_label_when',
            i18n_domain='BonsaiCollection',
        )
    ),

    TextField(
        name='remark',
        widget=TextAreaWidget(
            label='Remark',
            label_msgid='BonsaiCollection_label_remark',
            i18n_domain='BonsaiCollection',
        )
    ),

    StringField(
        name='where',
        widget=StringWidget(
            label='Where',
            label_msgid='BonsaiCollection_label_where',
            i18n_domain='BonsaiCollection',
        )
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BonsaiEvent_schema = schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BonsaiEvent(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    allowed_content_types = []
    _at_rename_after_creation = True

    schema = BonsaiEvent_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

# end of class BonsaiEvent

##code-section module-footer #fill in your manual code here
##/code-section module-footer



