# -*- coding: utf-8 -*-
#
# File: BonsaiCollection.py
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

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BonsaiCollection_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BonsaiCollection(BaseFolder):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseFolder,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Bonsaï Collection'

    meta_type = 'BonsaiCollection'
    portal_type = 'BonsaiCollection'
    allowed_content_types = ['Bonsai', 'Containers']
    filter_content_types = 1
    global_allow = 1
    content_icon = 'folder_bonsai.png'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Bonsaï Collection"
    typeDescMsgId = 'description_edit_bonsaicollection'


    actions =  (


       {'action': "string:${object_url}/bonsaicollection_view",
        'category': "object",
        'id': 'view',
        'name': 'View',
        'permissions': ("View",),
        'condition': 'python:1'
       },


    )

    _at_rename_after_creation = True

    schema = BonsaiCollection_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(BonsaiCollection, PROJECTNAME)
# end of class BonsaiCollection

##code-section module-footer #fill in your manual code here
##/code-section module-footer



