from odoo import api, fields, models, _


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _rec_name = 'patient_name'
    _description = 'Patient Record'

    patient_name = fields.Char(string='Name', required=True)
    name_seq = fields.Char(string='Patient ID', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], default='male', setring='Gender')
    patient_age = fields.Char('Age')
    notes = fields.Text(string='Notes')
    image = fields.Binary(string='Image')

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        result = super(HospitalPatient, self).create(vals)
        return result
