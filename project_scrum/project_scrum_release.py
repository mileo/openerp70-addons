# -*- coding: utf-8 -*-
from osv import fields, osv
from tools.translate import _

class projectScrumRelease(osv.osv):
    _name = 'project.scrum.release'
    
    _columns = {
        'name': fields.char("Name", size=128, required=True),
        'goal': fields.text("Goal"),
        'note': fields.text("Note"),
        'project_id': fields.many2one('project.project', "Project", domain=[('is_scrum', '=', True)], required=True),
        'date_start': fields.date('Starting Date'),
        'date_stop': fields.date('Ending Date'),
        'delivery_date_estimated': fields.date("Estimated date of delivery"),
        'delivery_date_effective': fields.date("Effective date of delivery"),
    }

class projectProjectInehrit(osv.osv):
    _inherit = 'project.project'
    _columns = {
        'release_ids': fields.one2many('project.scrum.release', 'project_id', "Releases", readonly=True),
    }

