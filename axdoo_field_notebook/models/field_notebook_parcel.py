# Copyright 2020 Manuel Calero <manuelcalero@xtendoo.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from datetime import date
from odoo import fields, models


class FieldNotebookParcel(models.Model):
    _name = "field.notebook.parcel"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Field Notebook Parcel"

    name = fields.Char(
        string="Parcel Name",
        required=True,
        index=True,
        tracking=True,
    )
    year_harvest = fields.Integer(
        string="Year of harvest",
        required=True,
        default=date.today().year
    )
    technical_ids = fields.Many2one(
        comodel_name='field.notebook.technical',
        inverse_name='parcel_ids',
        string='Technical',
        copy=True,
        auto_join=True,
    )

class FieldNotebookParcelTechnical(models.Model):
    _name = 'field.notebook.parcel.technical'
    _description = 'Parcel Technical'

    technical_id = fields.Many2one(
        comodel_name='field.notebook.technical',
        string='Technical',
        required=True,
        delegate=True,
    )
    parcel_id = fields.Many2one(
        comodel_name='field.notebook.parcel',
        string='Parcel',
        required=True,
        index=True,
        copy=False,
    )

    # _sql_constraints = [
    #     (
    #         "parcel_uniq",
    #         "unique(technical_id, parcel_id)",
    #         _("This parcel already exists in this exploitation !"),
    #     )
    # ]
