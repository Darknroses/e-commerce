# Copyright 2017 Tecnativa - David Vidal
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models
from odoo.http import request


class Website(models.Model):
    _inherit = "website"

    website_hide_price = fields.Boolean(
        string="Hide prices on website",
        copy=False,
        help="Hide price at website level",
    )
    website_show_price = fields.Boolean(compute="_compute_website_show_price")
    website_hide_price_default_message = fields.Char(
        string="Default Hidden price message",
        help="When the price is hidden on the website because of product "
        "configuration we can give the customer some tips on how to find it "
        "out.",
        translate=True,
    )

    def _compute_website_show_price(self):
        for rec in self:
            rec.website_show_price = (
                not rec.website_hide_price
                and request.env.user.partner_id.website_show_price
            )
