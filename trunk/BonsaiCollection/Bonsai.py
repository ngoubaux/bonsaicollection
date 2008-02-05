# -*- coding: utf-8 -*-
#
# File: Bonsai.py
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

# additional imports from tagged value 'import'
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
from random import choice

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='origin',
        widget=SelectionWidget(
            label='Origin',
            label_msgid='BonsaiCollection_label_origin',
            i18n_domain='BonsaiCollection',
        ),
        vocabulary=NamedVocabulary("""BonsaiOrigin""")
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

    ImageField(
        name='project',
        widget=ImageWidget(
            label='Project',
            label_msgid='BonsaiCollection_label_project',
            i18n_domain='BonsaiCollection',
        ),
        storage=AttributeStorage(),
        sizes={'thumb':(80,80), 'normal' : (200,200)}
    ),

    TextField(
        name='remark',
        widget=TextAreaWidget(
            label='Remark',
            label_msgid='BonsaiCollection_label_remark',
            i18n_domain='BonsaiCollection',
        )
    ),

    ReferenceField(
        name='container',
        allowed_content_types="Container",
        widget=ReferenceBrowserWidget(
            startup_directory="../",
            label='Container',
            label_msgid='BonsaiCollection_label_container',
            i18n_domain='BonsaiCollection',
        ),
        allowed_types=('Container',),
        multiValued=0,
        relationship='in container'
    ),

    ReferenceField(
        name='treestyles',
        widget=ReferenceWidget(
            label='Treestyles',
            label_msgid='BonsaiCollection_label_treestyles',
            i18n_domain='BonsaiCollection',
        ),
        allowed_types=('TreeStyle',),
        multiValued=0,
        relationship='as style'
    ),

    ReferenceField(
        name='species',
        widget=ReferenceWidget(
            label='Species',
            label_msgid='BonsaiCollection_label_species',
            i18n_domain='BonsaiCollection',
        ),
        allowed_types=('Specie',),
        multiValued=0,
        relationship='is specie'
    ),

    ReferenceField(
        name='CurrentView',
        allowed_content_types="ATPhoto",
        widget=ReferenceBrowserWidget(
            startup_directory=".",
            label='Currentview',
            label_msgid='BonsaiCollection_label_CurrentView',
            i18n_domain='BonsaiCollection',
        ),
        allowed_types=('ATPhoto',),
        multiValued=0,
        relationship='looks like'
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Bonsai_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Bonsai(BaseFolder):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseFolder,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Bonsaï'

    meta_type = 'Bonsai'
    portal_type = 'Bonsai'
    allowed_content_types = ['ATPhotoAlbum', 'BonsaiDimension', 'BonsaiEventIllness', 'BonsaiEventWork']
    filter_content_types = 1
    global_allow = 0
    content_icon = 'bonsai.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Bonsaï"
    typeDescMsgId = 'description_edit_bonsai'


    actions =  (


       {'action': "string:${object_url}/bonsai_view",
        'category': "object",
        'id': 'view',
        'name': 'View',
        'permissions': ("View",),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/works_view",
        'category': "object",
        'id': 'works_view',
        'name': 'travaux',
        'permissions': ("View",),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/illnesses_view",
        'category': "object",
        'id': 'illnesses_view',
        'name': 'maladies',
        'permissions': ("View",),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/gallery_view",
        'category': "object",
        'id': 'gallery_view',
        'name': 'Photo albums',
        'permissions': ("View",),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/evolution_view",
        'category': "object",
        'id': 'evolution_view',
        'name': 'Evolution',
        'permissions': ("View",),
        'condition': 'python:1'
       },


    )

    _at_rename_after_creation = True

    schema = Bonsai_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('getPicture')
    def getPicture(self):
        """
        return the referenced photo or try to get one
        """
        refs = self.getReferenceImpl(relationship='looks like');
        if len(refs) > 0 :
          return refs[0].getTargetObject()
        else:
          results = self.portal_catalog.searchResults(portal_type='ATPhoto',         																	  path='/'.join(self.getPhysicalPath()))
          if len(results) > 0:
            return choice(results).getObject()
     	pass


registerType(Bonsai, PROJECTNAME)
# end of class Bonsai

##code-section module-footer #fill in your manual code here
##/code-section module-footer



