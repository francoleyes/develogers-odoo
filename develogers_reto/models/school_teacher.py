from odoo import api, fields, models

class SchoolTeacher(models.Model):
    _name = "school.teacher"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Maestro escolar'

    name = fields.Char(string='Maestro', required=True, tracking=True)
    profile = fields.Text(string='Perfil', required=True, tracking=True)
    subject_ids = fields.One2many('school.subject', 'teacher_id',
                               string='Asignaturas')

    # Extra fields
    average_student_grade = fields.Float(string='Calificación promedio de los estudiantes',
                                         compute='calculate_average_student_grade', readonly=True)

    def calculate_average_student_grade(self):
        for teacher in self:
            if teacher.subject_ids:
                subject_ids = teacher.subject_ids
                student_grades = []
                for subject in subject_ids:
                    for student in subject.student_ids:
                        student_grades.append(student.final_exam_grade)
                if student_grades:
                    teacher.average_student_grade = sum(student_grades) / len(student_grades)
                else:
                    teacher.average_student_grade = 0
            else:
                teacher.average_student_grade = 0
