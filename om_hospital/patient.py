from odoo import api, fields, models, _


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    patient_name = fields.Char(string='Patient Name')


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _rec_name = 'patient_name'
    _description = 'Patient Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    @api.depends('patient_age')
    def set_age_group(self):
        for s in self:
            if int(s.patient_age) < 18:
                s.age_group = 'minor'
            else:
                s.age_group = 'major'

    patient_name = fields.Char(string='Name', required=True, track_visibility='always')
    name_seq = fields.Char(string='Patient ID', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], default='male', setring='Gender')
    patient_age = fields.Integer('Age', track_visibility='always')
    age_group = fields.Selection([
        ('major', 'Major'),
        ('minor', 'Minor')
    ], setring='Age Group', default='major', compute='set_age_group')
    notes = fields.Text(string='Notes')
    image = fields.Binary(string='Image')

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        result = super(HospitalPatient, self).create(vals)
        return result
