from odoo import api, fields, models
from odoo.exceptions import ValidationError

class SchoolSubject(models.Model):
    _name = "school.subject"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Asignatura escolar'

    name = fields.Char(string='Asignatura', required=True, tracking=True)
    credits = fields.Integer(string='Créditos', required=True, tracking=True)
    max_students = fields.Integer(string='Número máximo de estudiantes', required=True, tracking=True)
    active = fields.Boolean(string='Activo', default=True, tracking=True)
    student_ids = fields.Many2many('school.student',
                                    'school_student_subject_rel',
                                    'subject_id',
                                    'student_id',
                                    string='Estudiantes')
    teacher_id = fields.Many2one('school.teacher', string='Maestro', required=True, on_delete='cascade')

    # Extra fields
    enrollment = fields.Integer(string='Cantidad de estudiantes matriculados', compute='calculate_student_enrollment', readonly=True, default=0)

    def calculate_student_enrollment(self):
        for subject in self:
            if subject.student_ids:
                subject.enrollment = len(subject.student_ids)
                print(len(subject.student_ids))
            else:
                subject.enrollment = 0

    @api.constrains('credits', 'max_students')
    def verify_credits_and_max_students(self):
        for subject in self:
            if subject.credits <= 0:
                raise ValidationError("Los créditos deben ser mayores a 0.")

            if subject.max_students <= 0:
                raise ValidationError("El número máximo de estudiantes debe ser mayor a 0.")