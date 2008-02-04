# -*- coding: utf-8 -*-
#
# File: EncycloProduct.py
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
from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.BonsaiCollection.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='type',
        widget=SelectionWidget(
            label='Type',
            label_msgid='BonsaiCollection_label_type',
            i18n_domain='BonsaiCollection',
        ),
        vocabulary=NamedVocabulary("""EncycloProductType""")
    ),

    StringField(
        name='whereToFind',
        widget=StringWidget(
            label='Wheretofind',
            label_msgid='BonsaiCollection_label_whereToFind',
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

    ImageField(
        name='picture',
        widget=ImageWidget(
            label='Picture',
            label_msgid='BonsaiCollection_label_picture',
            i18n_domain='BonsaiCollection',
        ),
        storage=AttributeStorage(),
        sizes={'thumb':(80,80), 'normal' : (200,200)}
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

EncycloProduct_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class EncycloProduct(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Produit'

    meta_type = 'EncycloProduct'
    portal_type = 'EncycloProduct'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 0
    content_icon = 'potion_blue.png'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Produit"
    typeDescMsgId = 'description_edit_encycloproduct'


    actions =  (


       {'action': "string:${object_url}/encycloproduct_view",
        'category': "object",
        'id': 'view',
        'name': 'View',
        'permissions': ("View",),
        'condition': 'python:1'
       },


    )

    _at_rename_after_creation = True

    schema = EncycloProduct_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(EncycloProduct, PROJECTNAME)
# end of class EncycloProduct

##code-section module-footer #fill in your manual code here
##/code-section module-footer



