# from odoo import models, fields, api


# class duplicate_guard(models.Model):
#     _name = 'duplicate_guard.duplicate_guard'
#     _description = 'duplicate_guard.duplicate_guard'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

