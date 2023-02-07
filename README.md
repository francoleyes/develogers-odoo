# Módulo School en Odoo
Este módulo de Odoo permite la gestión de estudiantes y maestros en un sistema escolar. Para poder utilizar este módulo de manera óptima, es necesario que el usuario que lo instala pertenezca al grupo de administrador de la categoría 'Develogers - Reto' en Odoo. De esta manera, tendrá los permisos necesarios para realizar las operaciones read-write-create-delete en el sistema.

## Documentación

class SchoolStudent
    Esta clase representa un estudiante escolar en el sistema. Hereda de `mail.thread` y `mail.activity.mixin` para tener
    capacidades de seguimiento y actividades en el sistema.

    Atributos:
        - name (Char): El nombre del estudiante. Es un campo requerido y con seguimiento.
        - birth_date (Date): La fecha de nacimiento del estudiante. Es un campo requerido y con seguimiento.
        - age (Integer): La edad del estudiante. Es un campo calculado y con seguimiento.
        - final_exam_grade (Float): La calificación obtenida en el examen final. Es un campo requerido y con seguimiento.
        - subject_ids (Many2many): Las asignaturas matriculadas por el estudiante. Es un campo requerido y con seguimiento.
        - gender (Selection): El género del estudiante. Es un campo con seguimiento.
        - address (Char): La dirección del estudiante. Es un campo con seguimiento.

    Métodos:
        - calculate_age (onchange): Este método es llamado automáticamente cuando se cambia el valor de `birth_date`.
          Calcula la edad del estudiante en base a su fecha de nacimiento.
        - verify_final_exam_grade_and_age (constrains): Este método es llamado automáticamente cuando se guarda un
          registro de estudiante. Verifica que la calificación obtenida en el examen final esté entre 0 y 10 y que la
          edad sea mayor a 0. Si alguna de estas condiciones no se cumple, se lanza una excepción de validación.
          
          
       

class SchoolSubject:
    Esta clase representa una asignatura escolar en el sistema. Hereda de `mail.thread` y `mail.activity.mixin` para tener
    capacidades de seguimiento y actividades en el sistema.

    Atributos:
        - name (Char): El nombre de la asignatura. Es un campo requerido y con seguimiento.
        - credits (Integer): La cantidad de créditos de la asignatura. Es un campo requerido y con seguimiento.
        - max_students (Integer): El número máximo de estudiantes que pueden matricularse en la asignatura. Es un campo requerido y con seguimiento.
        - active (Boolean): Indica si la asignatura está activa o no. Es un campo con seguimiento.
        - student_ids (Many2many): Los estudiantes matriculados en la asignatura. Es un campo con seguimiento.
        - teacher_id (Many2one): El maestro responsable de la asignatura. Es un campo requerido y con seguimiento.
        - enrollment (Integer): La cantidad de estudiantes matriculados en la asignatura. Es un campo calculado y con seguimiento.

    Métodos:
        - calculate_student_enrollment (compute): Este método es llamado automáticamente cuando se accede al campo `enrollment`.
          Calcula la cantidad de estudiantes matriculados en la asignatura.
        - verify_credits_and_max_students (constrains): Este método es llamado automáticamente cuando se guarda un registro de asignatura.
          Verifica que la cantidad de créditos sea mayor a 0 y que el número máximo de estudiantes sea mayor a 0. Si alguna de estas
          condiciones no se cumple, se lanza una excepción de validación.
          
          
          
          
class SchoolTeacher(models.Model):
    Esta clase representa a un maestro escolar en el sistema. Hereda de `mail.thread` y `mail.activity.mixin` para tener
    capacidades de seguimiento y actividades en el sistema.

    Atributos:
        - name (Char): El nombre del maestro. Es un campo requerido y con seguimiento.
        - profile (Text): El perfil del maestro. Es un campo requerido y con seguimiento.
        - subject_ids (One2many): Las asignaturas impartidas por el maestro. Es un campo requerido y con seguimiento.
        - average_student_grade (Float): La calificación promedio de los estudiantes en las asignaturas impartidas
          por el maestro. Es un campo calculado y de solo lectura.

    Métodos:
        - calculate_average_student_grade (compute): Este método es llamado automáticamente cuando se accede al valor
          de `average_student_grade`. Calcula la calificación promedio de los estudiantes en las asignaturas impartidas
          por el maestro.
