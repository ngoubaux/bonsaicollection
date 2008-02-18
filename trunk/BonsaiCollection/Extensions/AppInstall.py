from Products.ATVocabularyManager.config import TOOL_NAME as ATVOCABULARYTOOL
from Products.CMFCore.utils import getToolByName
from Products.ATVocabularyManager.utils.vocabs import createSimpleVocabs
   
def install(self):

    vocabs = {}

    vocabs['SpecieLevel'] = (
           ('hard', u'Difficile'),
           ('middle', u'Moyen'),
           ('norm', u'Normal'),
           ('easy', u'Facile'),
           ('imm', u'Immortel'),
       )
   
    vocabs['TreeClass'] = (
           ('pinopsida', u'Pinopsida'),
       ) 
       
    vocabs['TreeFamilly'] = (
           ('salicaceae', u'Salicaceae'),
           ('taxaceae', u'Taxaceae'),
           ('podocarpaceae', u'Podocarpaceae'),
       )   
       
    vocabs['BonsaiWorkType'] = (
          ('pincing', u'Pincement'),
          ('defoliation', u'Defoliation'),
          ('wiring', u'Ligature'),
          ('greffe', u'Greffe'),
          ('layer', u'Marcottage'),
          ('repotting', u'Rempotage'),
          ('structcutting', u'Taille de structure'),
          ('carecutting', u'Taille d entretien'),
          ('feeding', u'Fertilisation'),
          ('jin', u'Jin - Shari'),
       )    
    vocabs['BonsaiOrigin'] = (
          ('seed', u'Semi'),
          ('taking', u'Prelevement'),
          ('prof', u'Professionel bonsai'),
          ('div', u'Division'),
          ('raw', u'Jardinerie'),
       )
    vocabs['TreeType'] = (
          ('conifer', u'Conifer'),
          ('feuillu', u'Feuillu'),
       )
       
    vocabs['SpecieGrowth'] = (
           ('vfast', u'Tres rapide'),
           ('fast', u'Rapide'),
           ('norm', u'Normale'),
           ('slow', u'Lente'),
           ('vslow', u'Tres lente'),
       )   
       
    vocabs['BlightSeverity'] = (
          ('minor', u'Mineur'),
          ('important', u'Important'),
          ('major', u'Majeur'),
          ('death', u'Mortelle'),
       )
    
    vocabs['BlightGroup'] = (
          ('fungi', 'Champignon'),
          ('bacteria', 'Virus'),
          ('Bug', 'Insecte'),
          ('nutrient', 'Carence'),
          ('excess', 'Exces'),
       )
       
    vocabs['EncycloProductType'] = (
          ('chimic', 'Chimique'),
          ('animal', 'Animal'),
          ('bio', 'bio'),
          ('boisson', 'Boisson'),
       )
    
    vocabs['BonsaiTreatment'] = (
         ('prevent' ,'Preventif'),
         ('curative', 'Curatif'),
       )
  
    portal=getToolByName(self,'portal_url').getPortalObject()
    atvm = getToolByName(portal, ATVOCABULARYTOOL)
    createSimpleVocabs(atvm, vocabs)
