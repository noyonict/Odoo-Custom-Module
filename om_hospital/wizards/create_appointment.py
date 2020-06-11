from odoo import models, fields, api, _


class CreatAppointment(models.TransientModel):
    _name = 'create.appointment'
    _description = 'Create Appointment'

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    appointment_date = fields.Date(string='Appointment Date')
    note = fields.Text('Notes', default='Created form the wizard.')

    def create_appointment(self):
        vals = {
            'patient_id': self.patient_id.id,
            'appointment_date': self.appointment_date,
        }
        self.env['hospital.appointment'].create(vals)

