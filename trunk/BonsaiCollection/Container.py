# -*- coding: utf-8 -*-
#
# File: Container.py
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
        name='shape',
        widget=StringWidget(
            label='Shape',
            label_msgid='BonsaiCollection_label_shape',
            i18n_domain='BonsaiCollection',
        )
    ),

    StringField(
        name='color',
        widget=StringWidget(
            label='Color',
            label_msgid='BonsaiCollection_label_color',
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

    StringField(
        name='size',
        widget=StringWidget(
            label='Size',
            label_msgid='BonsaiCollection_label_size',
            i18n_domain='BonsaiCollection',
        )
    ),

    IntegerField(
        name='cost',
        widget=IntegerField._properties['widget'](
            label='Cost',
            label_msgid='BonsaiCollection_label_cost',
            i18n_domain='BonsaiCollection',
        )
    ),

    DateTimeField(
        name='acquiredDate',
        widget=CalendarWidget(
            show_hm=False,
            label='Acquireddate',
            label_msgid='BonsaiCollection_label_acquiredDate',
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

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Container_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Container(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Pot'

    meta_type = 'Container'
    portal_type = 'Container'
    allowed_content_types = []
    filter_content_types = 1
    global_allow = 0
    content_icon = 'stone.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Pot"
    typeDescMsgId = 'description_edit_container'


    actions =  (


       {'action': "string:${object_url}/container_view",
        'category': "object",
        'id': 'view',
        'name': 'View',
        'permissions': ("View",),
        'condition': 'python:1'
       },


    )

    _at_rename_after_creation = True

    schema = Container_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(Container, PROJECTNAME)
# end of class Container

##code-section module-footer #fill in your manual code here
##/code-section module-footer



