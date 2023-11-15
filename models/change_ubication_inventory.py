# -*- coding: utf-8 -*-
from odoo import models, fields, api



class ChangeUbicationInventory(models.Model):
    _inherit = 'sale.order'

    

    #agregamos el onchange por ubicacion de tipo de venta
    @api.onchange('type_id')
    def onchange_sale_type(self):
        # Si el tipo de venta es Liquidación
        if self.type_id.name == 'Liquidacion':
            # Obtener el almacén de liquidación
            warehouse = self.env['stock.warehouse'].search([('name', '=', 'Almacén Liquidación')], limit=1)
            # Si existe el almacén
            if warehouse:
                # Asignar el almacén de liquidación al pedido de venta
                self.warehouse_id = warehouse.id
            # Si no existe el almacén
            else:
                # Mostrar un mensaje de error
                return {'warning': {
                    'title': 'Error',
                    'message': 'No se encontró el "Almacén Liquidación". Por favor, crealoantes de seleccionar este tipo de venta.'
                }}