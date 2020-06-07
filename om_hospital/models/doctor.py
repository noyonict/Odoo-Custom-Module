from odoo import api, fields, models, _


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Doctor Name', required=True)
    phone = fields.Char('Doctor Phone')
    email = fields.Char('Doctor Email')
    notes = fields.Char('Notes')
    active = fields.Boolean(default=True)
    user_id = fields.Many2one('res.user', 'Related User',
                              help='Current user of the doctor')

