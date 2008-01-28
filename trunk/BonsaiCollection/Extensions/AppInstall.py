from Products.ATVocabularyManager.config import TOOL_NAME as ATVOCABULARYTOOL
from Products.CMFCore.utils import getToolByName
from Products.ATVocabularyManager.utils.vocabs import createSimpleVocabs
   
def install(self):

    vocabs = {}

    vocabs['SpecieLevel'] = (
           ('hard', 'Hard'),
           ('middle', u'Middle'),
           ('norm', u'Normal'),
           ('easy', u'easy'),
           ('imm', u'Immortal'),
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
          ('prof', u'Professionel'),
          ('div', u'division'),
       )
    vocabs['TreeType'] = (
          ('conifer', u'Conifer'),
          ('feuillu', u'Feuillu'),
       )
       
    vocabs['SpecieGrowth'] = (
           ('vfast', u'Very fast'),
           ('fast', u'Fast'),
           ('norm', u'Normal'),
           ('slow', u'Slow'),
           ('vslow', u'Very slow'),
       )   
       
    vocabs['BlightSeverity'] = (
          ('minor', u'Minor'),
          ('important', u'Important'),
          ('major', u'Major'),
          ('death', u'Death'),
       )
    
    vocabs['BlightGroup'] = (
          ('fungi', 'Fungi'),
          ('bacteria', 'Bacteria'),
          ('viruses', 'Viruses'),
          ('nutrient', 'Nutrient deficiency'),
          ('excess', 'Excess'),
       )
  
    portal=getToolByName(self,'portal_url').getPortalObject()
    atvm = getToolByName(portal, ATVOCABULARYTOOL)
    createSimpleVocabs(atvm, vocabs)