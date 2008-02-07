# -*- coding: utf-8 -*-
#
# File: TreeStyle.py
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

    StringField(
        name='japaneseName',
        filter_content_types="1",
        widget=StringWidget(
            label='Japanesename',
            label_msgid='BonsaiCollection_label_japaneseName',
            i18n_domain='BonsaiCollection',
        )
    ),

    ImageField(
        name='image',
        widget=ImageWidget(
            label='Image',
            label_msgid='BonsaiCollection_label_image',
            i18n_domain='BonsaiCollection',
        ),
        storage=AttributeStorage(),
        sizes={'thumb':(80,80), 'normal' : (200,200)}
    ),

    TextField(
        name='description',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label='Description',
            label_msgid='BonsaiCollection_label_description',
            i18n_domain='BonsaiCollection',
        ),
        default_output_type='text/html'
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

TreeStyle_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class TreeStyle(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Style arbre'

    meta_type = 'TreeStyle'
    portal_type = 'TreeStyle'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 0
    content_icon = 'paintbrush.png'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Style arbre"
    typeDescMsgId = 'description_edit_treestyle'


    actions =  (


       {'action': "string:${object_url}/treestyle_view",
        'category': "object",
        'id': 'view',
        'name': 'View',
        'permissions': ("View",),
        'condition': 'python:1'
       },


    )

    _at_rename_after_creation = True

    schema = TreeStyle_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(TreeStyle, PROJECTNAME)
# end of class TreeStyle

##code-section module-footer #fill in your manual code here
##/code-section module-footer



