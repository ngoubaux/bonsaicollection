# -*- coding: utf-8 -*-
#
# File: ProductVolume.py
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

ProductVolume_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class ProductVolume(BaseFolder):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseFolder,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Volume produits'

    meta_type = 'ProductVolume'
    portal_type = 'ProductVolume'
    allowed_content_types = ['EncycloProduct']
    filter_content_types = 1
    global_allow = 0
    content_icon = 'book_blue.png'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Volume produits"
    typeDescMsgId = 'description_edit_productvolume'

    _at_rename_after_creation = True

    schema = ProductVolume_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(ProductVolume, PROJECTNAME)
# end of class ProductVolume

##code-section module-footer #fill in your manual code here
##/code-section module-footer



