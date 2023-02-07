from odoo import api, fields, models
from datetime import date
from odoo.exceptions import ValidationError

class SchoolStudent(models.Model):
    _name = "school.student"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Estudiante escolar'

    name = fields.Char(string='Estudiante', required=True, tracking=True)
    birth_date = fields.Date(string='Fecha de nacimiento', required=True, tracking=True)
    age = fields.Integer(string='Edad', compute='calculate_age', tracking=True, readonly=True)
    final_exam_grade = fields.Float(string='Calificación del examen final', required=True, tracking=True)
    subject_ids = fields.Many2many('school.subject',
                                   'school_student_subject_rel',
                                   'student_id',
                                   'subject_id',
                                   string='Asignaturas', required=True, on_delete='cascade')

    # Extra fields
    gender = fields.Selection([('male', 'M'), ('female', 'F')], string='Género', tracking=True)
    address = fields.Char(string='Dirección', tracking=True)

    @api.onchange('birth_date')
    def calculate_age(self):
        for student in self:
            if student.birth_date:
                born = student.birth_date
                today = date.today()
                student.age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    @api.constrains('final_exam_grade', 'age')
    def verify_final_exam_grade_and_age(self):
        for student in self:
            if student.final_exam_grade < 0 or student.final_exam_grade > 10:
                raise ValidationError("La calificación del examen final debe estar entre 0 y 10.")

            if student.age < 0:
                raise ValidationError("La edad no puede ser menor a 0.")
