#-*-coding: utf-8-*-
{
'name': "Covid-19",
'summary': """
  Short (1 phrase/line) summary of the module's purpose, used as
  subtitle on modules listing or apps openerp. com""",

'description': """ 
   Long description of module's purpose
   """, 

'author': "My Company",
'website': "http://www.yourcompany.com.",
#Categories can be used to filter modules in modules listing
#Check https://github.com/odoo/.
#for the full list
'category': 'Uncategorized',
'version': '0.1',
# any module necessary for this one to work correctly
'depends' : ['base'],
# always loaded
 'data': [
    # 'security/ir.model.access.csv'
     'views/views.xml',
     'views/templates.ml',
 ],
# only loaded in demonstration mode
 'data' :[
     'data/data.xxl',
 ],
}
