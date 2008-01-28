# -*- coding: utf-8 -*-
#
# File: Blight.py
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

    TextField(
        name='care',
        widget=TextAreaWidget(
            label='Care',
            label_msgid='BonsaiCollection_label_care',
            i18n_domain='BonsaiCollection',
        )
    ),

    TextField(
        name='symptoms',
        widget=TextAreaWidget(
            label='Symptoms',
            label_msgid='BonsaiCollection_label_symptoms',
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
        name='severity',
        widget=SelectionWidget(
            label='Severity',
            label_msgid='BonsaiCollection_label_severity',
            i18n_domain='BonsaiCollection',
        ),
        vocabulary=NamedVocabulary("""BlightSeverity""")
    ),

    StringField(
        name='kind',
        widget=SelectionWidget(
            label='Kind',
            label_msgid='BonsaiCollection_label_kind',
            i18n_domain='BonsaiCollection',
        ),
        content_icon="bug.png",
        vocabulary=NamedVocabulary("""BlightGroup""")
    ),

    TextField(
        name='consequence',
        widget=TextAreaWidget(
            label='Consequence',
            label_msgid='BonsaiCollection_label_consequence',
            i18n_domain='BonsaiCollection',
        )
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Blight_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Blight(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Maladie'

    meta_type = 'Blight'
    portal_type = 'Blight'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 0
    content_icon = 'bug.png'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Maladie"
    typeDescMsgId = 'description_edit_blight'


    actions =  (


       {'action': "string:${object_url}/blight_view",
        'category': "object",
        'id': 'view',
        'name': 'View',
        'permissions': ("View",),
        'condition': 'python:1'
       },


    )

    _at_rename_after_creation = True

    schema = Blight_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(Blight, PROJECTNAME)
# end of class Blight

##code-section module-footer #fill in your manual code here
##/code-section module-footer



