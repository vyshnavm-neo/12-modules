# -*- coding: utf-8 -*-

from odoo import models, fields


class Mobilemodel(models.Model):
    _name = 'custom.model'
    _rec_name = 'name'

    height = fields.Char(string="Height")
    weight = fields.Char(string="weight")
    blood_group = fields.Char(string="Blood Group")
    name = fields.Many2one("res.partner", string="Name")
    age = fields.Char(string="Age")
    # image_256 = fields.Binary(string="Profile Photo")
    email = fields.Char(string="Email")
    mobile = fields.Char(string="Mobile")








