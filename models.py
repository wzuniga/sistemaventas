# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Cliente(models.Model):
    _name = 'ventas.cliente'
    _rec_name = 'nombre_cl'
    
    nombre_cl = fields.Char(string='Nombre de cliente',
                            size=40,
                            required=True,
                            help='Nombre del cliente')

    apellido_cl = fields.Char(string='Apellido de cliente',
                              size=40,
                              required=True,
                              help='Apellido del cliente')

    ventas_ids = fields.One2many('ventas.venta',
                                 'cliente_id',
                                 string='Compras')


class Producto(models.Model):
    _name = 'ventas.producto'
    _rec_name = 'nombre_pr'

    nombre_pr = fields.Char(string='Nombre del producto',
                            size=40,
                            required=True,
                            help='Nombre del producto')


class Temporada(models.Model):
    _name = 'ventas.temporada'
    _rec_name = 'numero'

    numero = fields.Integer(string='Numero Temporada',
                            size=2,
                            required=True,
                            help='Numero de la temporada')
    
    anno = fields.Integer(string='Año',
                          size=4,
                          required=True,
                          help='Año de la temporada')

    ventas_ids = fields.One2many('ventas.venta','temporada_id',string='Detalle temporada')

    #constrainnnn  sql


class Venta(models.Model):
    _name = 'ventas.venta'
    _rec_name = 'name'

    cancelado = fields.Boolean(string='Cancelado',
                               default=False,
                               compute='_compute_debt',
                               store=True)
    
    fecha_pedido = fields.Date(required=True)

    cliente_id = fields.Many2one('ventas.cliente','Cliente',required=True)

    pago_ids = fields.One2many('ventas.pago','ventas_id',string='Pagos',required=True)

    relacion_ids = fields.One2many('ventas.producto.precio.temporada',
    							   'ventas_id',
    							   string='Detalle venta',
                                   required=True)

    temporada_id = fields.Many2one('ventas.temporada','Temporada',required=True)

    name = fields.Char(string='Nombre a quien se vendio',
                       compute='_make_name',
                       store =True)

    deuda = fields.Float(string="Deuda",
    					 digits=(6,2),
    					 compute="_compute_debt",
    					 store=True,
    					 help="Deuda vigente")

    @api.multi
    @api.depends('cliente_id','temporada_id')
    def _make_name(self):
    	nombre = str(self.cliente_id.nombre_cl if self.cliente_id.nombre_cl else " ******* ")
    	anno = " - A" + str(self.temporada_id.anno if self.temporada_id.anno else "0000")
    	numero = " - T" + str(self.temporada_id.numero if self.temporada_id.numero else "0")

        self.name = nombre + anno + numero 
        			 

    @api.multi
    @api.depends('pago_ids','relacion_ids')
    def _compute_debt(self):
    	total = 0
    	pagado = 0

    	for pago in self.pago_ids:
    		pagado+=pago.cantidad

    	for articulo in self.relacion_ids:
    		total+=articulo.precio_id.venta

    	self.deuda = total - pagado

    	self.cancelado = (True if self.deuda <= 0 else False)


class Precio(models.Model):
    _name = 'ventas.precio'
    _rec_name = 'venta'

    compra = fields.Float(string='Precio de compra',
                          digits=(6,2),
                          required=True,
                          help='Precio del producto cuando se compro')

    venta = fields.Float(string='Precio de venta',
                         digits=(6,2),
                         required=True,
                         help='Precio del producto de venta')

class Pago(models.Model):
    _name = 'ventas.pago'
    _rec_name = 'cantidad'

    cantidad = fields.Float(string='Pagado',
                            digits=(6,2),
                            required=True,
                            help='Pagos a cuenta')

    fecha_pago = fields.Date(required=True)

    ventas_id = fields.Many2one('ventas.venta','Ventas',required=True)
    

class Producto_precio_temporada(models.Model):
    _name = 'ventas.producto.precio.temporada'

    producto_id = fields.Many2one('ventas.producto','Producto')

    precio_id = fields.Many2one('ventas.precio','Precio')

    ventas_id = fields.Many2one('ventas.venta','Ventas')