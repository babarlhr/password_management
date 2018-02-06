# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from datetime import datetime
import string

class SitesType(models.Model): 
    _name = "sites.type"
    _description = "Sites type"
    name = fields.Char('Name')

class Users(models.Model):
    _inherit = "res.users"
    _description = "Inherit this model in order to make the group selected by default for the newly created users."
    
    def _default_groups(self):
        default_groups = super(Users, self)._default_groups()
        print(str(default_groups))
        groups = ['|',('name','=','Website User'),'|',('name','=','Server User'),'|',('name','=','Database User'),'|',('name','=','Attachment User'),'|',('name','=','Socialmedia User'),('name','=','User')]
        return default_groups + self.env['res.groups'].search(groups)

    groups_id = fields.Many2many('res.groups', 'res_groups_users_rel', 'uid', 'gid', string='Groups', default=_default_groups)

    
class LoginPasswordCredentials(models.Model):
    _name = "login.password.credentials"
    _inherit = ['mail.thread']
    _description = "Manage Login Password Credentials"
    _rec_name = 'project_id'
    
#     name = fields.Char(string='Site Name')
    project_id = fields.Many2one('project.project', string='Project')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('waiting_approval', 'Waiting Approval'),
        ('updated', 'Approved'),], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')
    department_id = fields.Many2one('hr.department',string='Project For')
    website_line_ids = fields.One2many('login.password.website', 'line_id', 'Password Line')
    server_line_ids = fields.One2many('login.password.server', 'line_id', 'Server Line')
    department_ids = fields.Many2many('hr.department', 'department_type_rel', 'department_id', 'type_id', string='Visibile For deparments')
    database_line_ids = fields.One2many('login.password.database', 'line_id', 'Database Line')
    socialmedia_line_ids = fields.One2many('login.password.socialmedia', 'line_id', 'Social Media Line')
    extrainfo_line_ids = fields.One2many('login.password.extrainfo', 'line_id', 'Extra Info Line')
    attachment_line_ids = fields.One2many('login.password.attachment', 'line_id', 'Attachment Line')
    color = fields.Integer(string='Color Index')
    new_attachment = fields.Many2many('ir.attachment', string="Attachment")
    user_ids = fields.Many2many('res.users', string="Visible for users")

    @api.multi
    def update(self):
        self.write({'state': 'updated'})
    
    @api.multi
    def edit(self):
        self.write({'state': 'draft'}) 
     
    @api.multi
    def send_to_approval(self):
        self.write({'state': 'waiting_approval'})   
        
class LoginPasswordWebsite(models.Model): 
    _name = "login.password.website"
    _description = "Login Line Web Items"
    
    line_id = fields.Many2one('login.password.credentials', 'lineItem')
    name = fields.Char(string='Title')
    site_url = fields.Char(string='Url')
    user_name = fields.Char('Username')
    password = fields.Char('Password')
    site_type_id = fields.Many2one('sites.type',string="Site Type")
    date = fields.Date('Password Since')
    notes = fields.Char('Notes',size=64)
    
class LoginPasswordServer(models.Model): 
    _name = "login.password.server"
    _description = "Login Line Web Items"
    
    line_id = fields.Many2one('login.password.credentials', 'lineItem')
    name = fields.Char(string='Server')
    ip_address = fields.Char(string='IP Address')
    user_name = fields.Char('Username')
    password = fields.Char('Password or SSH Key') 
    site_type_id = fields.Many2one('sites.type',string="Site Type")
    date = fields.Date('Password Since')
    
class LoginPasswordDatabase(models.Model): 
    _name = "login.password.database"
    _description = "Login Line Web Items"
    
    line_id = fields.Many2one('login.password.credentials', 'lineItem')
    name = fields.Char(string='Server/DB for')
    ip_address = fields.Char(string='IP Address')
    db_name = fields.Char(string='DB Name')
    user_name = fields.Char('DB Username')
    password = fields.Char('DB Password') 
    site_type_id = fields.Many2one('sites.type',string="Site Type")
    date = fields.Date('Password Since')

class SocialMediaSites(models.Model): 
    _name = "social.media.sites"
    _description = "Social Media Sites"
    
    name = fields.Char('Name')    
    
class LoginPasswordSocialmedia(models.Model): 
    _name = "login.password.socialmedia"
    _description = "Login social media sites"
    
    line_id = fields.Many2one('login.password.credentials', 'lineItem')
    login = fields.Many2one('social.media.sites', 'Login For')
    page_url = fields.Char(string='Page URL')
    phone_number = fields.Char(string='Phone Number Associated')
    user_name = fields.Char('Username')
    password = fields.Char('Password')  
    site_type_id = fields.Many2one('sites.type',string="Site Type")
    date = fields.Date('Password Since')
    
class LoginPasswordExtrainfo(models.Model): 
    _name = "login.password.extrainfo"
    _description = "Login Extra Info"
    
    line_id = fields.Many2one('login.password.credentials', 'lineItem')
    name = fields.Text('Extra Info')
   
class LoginPasswordAttachment(models.Model):
    _name = "login.password.attachment"
    _description = "Attachment Line"

    line_id = fields.Many2one('login.password.credentials', 'lineItem')
    name = fields.Char('File Name')
    doc_name = fields.Char('File Name')
    attachment = fields.Binary('Attachment')   
    site_type_id = fields.Many2one('sites.type',string="Site Type")
