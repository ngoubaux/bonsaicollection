# -*- coding: utf-8 -*-
#
# File: Specie.py
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
        name='commonName',
        widget=StringWidget(
            label='Commonname',
            label_msgid='BonsaiCollection_label_commonName',
            i18n_domain='BonsaiCollection',
        ),
        schemata="Botany"
    ),

    StringField(
        name='family',
        widget=StringWidget(
            description="(Podocarpaceae, Pinaceae, Rosaceae, Aquifoliaceae, ..)",
            label='Family',
            label_msgid='BonsaiCollection_label_family',
            description_msgid='BonsaiCollection_help_family',
            i18n_domain='BonsaiCollection',
        ),
        schemata="Botany"
    ),

    StringField(
        name='cultivar',
        widget=StringWidget(
            label='Cultivar',
            label_msgid='BonsaiCollection_label_cultivar',
            i18n_domain='BonsaiCollection',
        ),
        schemata="Botany"
    ),

    StringField(
        name='genus',
        widget=StringWidget(
            description="(Taxus,Malus, Ilex, ...)",
            label='Genus',
            label_msgid='BonsaiCollection_label_genus',
            description_msgid='BonsaiCollection_help_genus',
            i18n_domain='BonsaiCollection',
        ),
        schemata="Botany"
    ),

    StringField(
        name='growth',
        widget=SelectionWidget(
            label='Growth',
            label_msgid='BonsaiCollection_label_growth',
            i18n_domain='BonsaiCollection',
        ),
        schemata="Culture",
        vocabulary=NamedVocabulary("""SpecieGrowth""")
    ),

    TextField(
        name='description',
        widget=TextAreaWidget(
            label='Description',
            label_msgid='BonsaiCollection_label_description',
            i18n_domain='BonsaiCollection',
        ),
        schemata="Presentation"
    ),

    ImageField(
        name='generalPicture',
        schemata="Presentation",
        widget=ImageWidget(
            label='Generalpicture',
            label_msgid='BonsaiCollection_label_generalPicture',
            i18n_domain='BonsaiCollection',
        ),
        storage=AttributeStorage(),
        sizes={'thumb':(80,80), 'normal' : (200,200)}
    ),

    ImageField(
        name='leafPicture',
        schemata="Presentation",
        widget=ImageWidget(
            label='Leafpicture',
            label_msgid='BonsaiCollection_label_leafPicture',
            i18n_domain='BonsaiCollection',
        ),
        storage=AttributeStorage(),
        sizes={'thumb':(80,80), 'normal' : (200,200)}
    ),

    ImageField(
        name='fruitPicture',
        schemata="Presentation",
        widget=ImageWidget(
            label='Fruitpicture',
            label_msgid='BonsaiCollection_label_fruitPicture',
            i18n_domain='BonsaiCollection',
        ),
        storage=AttributeStorage(),
        sizes={'thumb':(80,80), 'normal' : (200,200)}
    ),

    ImageField(
        name='flowerPicture',
        schemata="Presentation",
        widget=ImageWidget(
            label='Flowerpicture',
            label_msgid='BonsaiCollection_label_flowerPicture',
            i18n_domain='BonsaiCollection',
        ),
        storage=AttributeStorage(),
        sizes={'thumb':(80,80), 'normal' : (200,200)}
    ),

    StringField(
        name='variety',
        widget=StringWidget(
            description="(baccata, sylvestris, aquifolium)",
            label='Variety',
            label_msgid='BonsaiCollection_label_variety',
            description_msgid='BonsaiCollection_help_variety',
            i18n_domain='BonsaiCollection',
        ),
        schemata="Botany"
    ),

    StringField(
        name='location',
        widget=StringWidget(
            label='Location',
            label_msgid='BonsaiCollection_label_location',
            i18n_domain='BonsaiCollection',
        ),
        schemata="Botany"
    ),

    TextField(
        name='seed',
        widget=TextAreaWidget(
            label='Seed',
            label_msgid='BonsaiCollection_label_seed',
            i18n_domain='BonsaiCollection',
        ),
        schemata="Getting"
    ),

    TextField(
        name='cutting',
        widget=TextAreaWidget(
            label='Cutting',
            label_msgid='BonsaiCollection_label_cutting',
            i18n_domain='BonsaiCollection',
        ),
        schemata="Getting"
    ),

    TextField(
        name='layer',
        widget=TextAreaWidget(
            label='Layer',
            label_msgid='BonsaiCollection_label_layer',
            i18n_domain='BonsaiCollection',
        ),
        schemata="Getting"
    ),

    TextField(
        name='budding',
        widget=TextAreaWidget(
            label='Budding',
            label_msgid='BonsaiCollection_label_budding',
            i18n_domain='BonsaiCollection',
        ),
        schemata="Getting"
    ),

    TextField(
        name='care',
        widget=TextAreaWidget(
            label='Care',
            label_msgid='BonsaiCollection_label_care',
            i18n_domain='BonsaiCollection',
        ),
        schemata="Culture"
    ),

    StringField(
        name='level',
        schemata="Culture",
        widget=SelectionWidget(
            label='Level',
            label_msgid='BonsaiCollection_label_level',
            i18n_domain='BonsaiCollection',
        ),
        vocabulary=NamedVocabulary("""SpecieLevel""")
    ),

    TextField(
        name='light',
        widget=TextAreaWidget(
            label='Light',
            label_msgid='BonsaiCollection_label_light',
            i18n_domain='BonsaiCollection',
        ),
        schemata="Culture"
    ),

    TextField(
        name='hygrometry',
        widget=TextAreaWidget(
            label='Hygrometry',
            label_msgid='BonsaiCollection_label_hygrometry',
            i18n_domain='BonsaiCollection',
        ),
        schemata="Culture"
    ),

    StringField(
        name='temperature',
        widget=StringWidget(
            label='Temperature',
            label_msgid='BonsaiCollection_label_temperature',
            i18n_domain='BonsaiCollection',
        ),
        schemata="Culture"
    ),

    TextField(
        name='fertilisation',
        widget=TextAreaWidget(
            label='Fertilisation',
            label_msgid='BonsaiCollection_label_fertilisation',
            i18n_domain='BonsaiCollection',
        ),
        schemata="Culture"
    ),

    TextField(
        name='watering',
        widget=TextAreaWidget(
            label='Watering',
            label_msgid='BonsaiCollection_label_watering',
            i18n_domain='BonsaiCollection',
        ),
        schemata="Culture"
    ),

    TextField(
        name='transplanting',
        widget=TextAreaWidget(
            label='Transplanting',
            label_msgid='BonsaiCollection_label_transplanting',
            i18n_domain='BonsaiCollection',
        ),
        schemata="Culture"
    ),

    TextField(
        name='soilMixture',
        widget=TextAreaWidget(
            label='Soilmixture',
            label_msgid='BonsaiCollection_label_soilMixture',
            i18n_domain='BonsaiCollection',
        ),
        schemata="Culture"
    ),

    TextField(
        name='wiring',
        widget=TextAreaWidget(
            label='Wiring',
            label_msgid='BonsaiCollection_label_wiring',
            i18n_domain='BonsaiCollection',
        ),
        schemata="Aesthetic"
    ),

    TextField(
        name='potStyle',
        widget=TextAreaWidget(
            label='Potstyle',
            label_msgid='BonsaiCollection_label_potStyle',
            i18n_domain='BonsaiCollection',
        ),
        schemata="Aesthetic"
    ),

    StringField(
        name='TreeType',
        widget=SelectionWidget(
            label='Treetype',
            label_msgid='BonsaiCollection_label_TreeType',
            i18n_domain='BonsaiCollection',
        ),
        schemata="Botany",
        vocabulary=NamedVocabulary("""TreeType""")
    ),

    ReferenceField(
        name='Common style',
        widget=ReferenceWidget(
            label='Common style',
            label_msgid='BonsaiCollection_label_Common style',
            i18n_domain='BonsaiCollection',
        ),
        allowed_types=('TreeStyle',),
        schemata="Aesthetic",
        multiValued=1,
        relationship='specie_common style'
    ),

    ReferenceField(
        name='Common illness',
        widget=ReferenceWidget(
            label='Common illness',
            label_msgid='BonsaiCollection_label_Common illness',
            i18n_domain='BonsaiCollection',
        ),
        allowed_types=('Blight',),
        schemata="Culture",
        multiValued=1,
        relationship='specie_common illness'
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Specie_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
Specie_schema['id'].schemata='Botany'

Specie_schema['title'].widget.label='Nom botanique'
Specie_schema['title'].schemata='Botany'
Specie_schema['title'].widget.description='Nom botanique de l\'arbre'
##/code-section after-schema

class Specie(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Specie'

    meta_type = 'Specie'
    portal_type = 'Specie'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 0
    content_icon = 'tree.png'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Specie"
    typeDescMsgId = 'description_edit_specie'


    actions =  (


       {'action': "string:${object_url}/specie_view",
        'category': "object",
        'id': 'view',
        'name': 'View',
        'permissions': ("View",),
        'condition': 'python:1'
       },


    )

    _at_rename_after_creation = True

    schema = Specie_schema

    ##code-section class-header #fill in your manual code here
    #schema.moveField('someFieldICreated', after='text')
    #schema.moveField('someOtherFieldICreated', pos='top')
    ##/code-section class-header

    # Methods


registerType(Specie, PROJECTNAME)
# end of class Specie

##code-section module-footer #fill in your manual code here
##/code-section module-footer



