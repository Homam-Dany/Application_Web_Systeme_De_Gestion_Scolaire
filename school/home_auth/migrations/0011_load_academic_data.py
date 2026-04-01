from django.db import migrations
import datetime

def load_data(apps, schema_editor):
    data = [
    {'model': 'student.Exam', 'fields': {
        'id': 2,
        'name': 'Analyse 1',
        'subject_id': 197,
        'date': datetime.date(2026, 3, 21),
        'start_time': datetime.time(16, 12),
        'end_time': datetime.time(16, 15),
        'total_marks': 20
    }},
    {'model': 'student.Exam', 'fields': {
        'id': 3,
        'name': 'Analyse 4',
        'subject_id': 143,
        'date': datetime.date(2026, 3, 21),
        'start_time': datetime.time(16, 49),
        'end_time': datetime.time(16, 51),
        'total_marks': 20
    }},
    {'model': 'student.Exam', 'fields': {
        'id': 4,
        'name': 'Algebre 1',
        'subject_id': 174,
        'date': datetime.date(2026, 3, 22),
        'start_time': datetime.time(16, 50),
        'end_time': datetime.time(16, 53),
        'total_marks': 20
    }},
    {'model': 'student.Exam', 'fields': {
        'id': 5,
        'name': 'Electricite',
        'subject_id': 200,
        'date': datetime.date(2026, 3, 21),
        'start_time': datetime.time(20, 46),
        'end_time': datetime.time(20, 47),
        'total_marks': 20
    }},
    {'model': 'student.Exam', 'fields': {
        'id': 6,
        'name': 'Analyse 4',
        'subject_id': 143,
        'date': datetime.date(2026, 3, 21),
        'start_time': datetime.time(22, 39),
        'end_time': datetime.time(22, 41),
        'total_marks': 20
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 1,
        'exam_id': 2,
        'student_id': 396,
        'marks_obtained': Decimal('15.50'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 2,
        'exam_id': 2,
        'student_id': 398,
        'marks_obtained': Decimal('20.00'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 3,
        'exam_id': 2,
        'student_id': 397,
        'marks_obtained': Decimal('12.75'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 4,
        'exam_id': 2,
        'student_id': 401,
        'marks_obtained': Decimal('18.75'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 5,
        'exam_id': 2,
        'student_id': 400,
        'marks_obtained': Decimal('10.25'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 6,
        'exam_id': 2,
        'student_id': 399,
        'marks_obtained': Decimal('4.00'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 7,
        'exam_id': 2,
        'student_id': 402,
        'marks_obtained': Decimal('9.00'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 8,
        'exam_id': 2,
        'student_id': 403,
        'marks_obtained': Decimal('12.00'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 9,
        'exam_id': 3,
        'student_id': 330,
        'marks_obtained': Decimal('12.00'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 10,
        'exam_id': 3,
        'student_id': 329,
        'marks_obtained': Decimal('11.00'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 11,
        'exam_id': 3,
        'student_id': 325,
        'marks_obtained': Decimal('15.00'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 12,
        'exam_id': 3,
        'student_id': 327,
        'marks_obtained': Decimal('17.00'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 13,
        'exam_id': 3,
        'student_id': 326,
        'marks_obtained': Decimal('10.00'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 14,
        'exam_id': 3,
        'student_id': 324,
        'marks_obtained': Decimal('9.00'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 15,
        'exam_id': 3,
        'student_id': 328,
        'marks_obtained': Decimal('7.00'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 16,
        'exam_id': 3,
        'student_id': 331,
        'marks_obtained': Decimal('4.50'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 17,
        'exam_id': 5,
        'student_id': 396,
        'marks_obtained': Decimal('7.50'),
        'proposed_marks': None,
        'rattrapage_marks': Decimal('9.50'),
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 18,
        'exam_id': 5,
        'student_id': 398,
        'marks_obtained': Decimal('20.00'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 19,
        'exam_id': 5,
        'student_id': 397,
        'marks_obtained': Decimal('7.00'),
        'proposed_marks': None,
        'rattrapage_marks': Decimal('13.50'),
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 20,
        'exam_id': 5,
        'student_id': 401,
        'marks_obtained': Decimal('9.00'),
        'proposed_marks': None,
        'rattrapage_marks': Decimal('10.00'),
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 21,
        'exam_id': 5,
        'student_id': 400,
        'marks_obtained': Decimal('6.50'),
        'proposed_marks': None,
        'rattrapage_marks': Decimal('15.00'),
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 22,
        'exam_id': 5,
        'student_id': 399,
        'marks_obtained': Decimal('11.00'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 23,
        'exam_id': 5,
        'student_id': 402,
        'marks_obtained': Decimal('12.00'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 24,
        'exam_id': 5,
        'student_id': 403,
        'marks_obtained': Decimal('11.00'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 25,
        'exam_id': 6,
        'student_id': 330,
        'marks_obtained': Decimal('20.00'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 26,
        'exam_id': 6,
        'student_id': 329,
        'marks_obtained': Decimal('11.00'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 27,
        'exam_id': 6,
        'student_id': 461,
        'marks_obtained': Decimal('12.00'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 28,
        'exam_id': 6,
        'student_id': 325,
        'marks_obtained': Decimal('7.00'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 29,
        'exam_id': 6,
        'student_id': 327,
        'marks_obtained': Decimal('5.00'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 30,
        'exam_id': 6,
        'student_id': 326,
        'marks_obtained': Decimal('13.00'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 31,
        'exam_id': 6,
        'student_id': 324,
        'marks_obtained': Decimal('8.00'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 32,
        'exam_id': 6,
        'student_id': 328,
        'marks_obtained': Decimal('1.00'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.ExamResult', 'fields': {
        'id': 33,
        'exam_id': 6,
        'student_id': 331,
        'marks_obtained': Decimal('11.00'),
        'proposed_marks': None,
        'rattrapage_marks': None,
        'grade': 'N/A',
        'is_published': True
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 92,
        'class_name': 'MIP',
        'section': 'S1',
        'subject_id': 125,
        'teacher_id': 50,
        'day_of_week': 'LUNDI',
        'start_time': datetime.time(16, 0),
        'end_time': datetime.time(17, 30),
        'room_no': 'Amphi 3 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 93,
        'class_name': 'MIP',
        'section': 'S1',
        'subject_id': 125,
        'teacher_id': 50,
        'day_of_week': 'JEUDI',
        'start_time': datetime.time(12, 30),
        'end_time': datetime.time(14, 0),
        'room_no': 'E19 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 94,
        'class_name': 'MIP',
        'section': 'S1',
        'subject_id': 125,
        'teacher_id': 50,
        'day_of_week': 'MARDI',
        'start_time': datetime.time(14, 15),
        'end_time': datetime.time(15, 45),
        'room_no': 'C12 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 95,
        'class_name': 'MIP',
        'section': 'S1',
        'subject_id': 126,
        'teacher_id': 44,
        'day_of_week': 'VENDREDI',
        'start_time': datetime.time(16, 0),
        'end_time': datetime.time(17, 30),
        'room_no': 'Amphi 6 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 96,
        'class_name': 'MIP',
        'section': 'S1',
        'subject_id': 126,
        'teacher_id': 44,
        'day_of_week': 'JEUDI',
        'start_time': datetime.time(16, 0),
        'end_time': datetime.time(17, 30),
        'room_no': 'B18 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 97,
        'class_name': 'MIP',
        'section': 'S1',
        'subject_id': 126,
        'teacher_id': 44,
        'day_of_week': 'VENDREDI',
        'start_time': datetime.time(14, 15),
        'end_time': datetime.time(15, 45),
        'room_no': 'E18 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 98,
        'class_name': 'MIP',
        'section': 'S1',
        'subject_id': 127,
        'teacher_id': 59,
        'day_of_week': 'SAMEDI',
        'start_time': datetime.time(16, 0),
        'end_time': datetime.time(17, 30),
        'room_no': 'Amphi 7 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 99,
        'class_name': 'MIP',
        'section': 'S1',
        'subject_id': 127,
        'teacher_id': 59,
        'day_of_week': 'SAMEDI',
        'start_time': datetime.time(9, 0),
        'end_time': datetime.time(10, 30),
        'room_no': 'E2 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 100,
        'class_name': 'MIP',
        'section': 'S1',
        'subject_id': 127,
        'teacher_id': 59,
        'day_of_week': 'SAMEDI',
        'start_time': datetime.time(12, 30),
        'end_time': datetime.time(14, 0),
        'room_no': 'B6 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 101,
        'class_name': 'MIP',
        'section': 'S1',
        'subject_id': 128,
        'teacher_id': 69,
        'day_of_week': 'LUNDI',
        'start_time': datetime.time(9, 0),
        'end_time': datetime.time(10, 30),
        'room_no': 'Amphi 1 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 102,
        'class_name': 'MIP',
        'section': 'S1',
        'subject_id': 128,
        'teacher_id': 69,
        'day_of_week': 'SAMEDI',
        'start_time': datetime.time(14, 15),
        'end_time': datetime.time(15, 45),
        'room_no': 'C21 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 103,
        'class_name': 'MIP',
        'section': 'S1',
        'subject_id': 128,
        'teacher_id': 69,
        'day_of_week': 'VENDREDI',
        'start_time': datetime.time(10, 45),
        'end_time': datetime.time(12, 15),
        'room_no': 'E5 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 104,
        'class_name': 'MIP',
        'section': 'S1',
        'subject_id': 129,
        'teacher_id': 63,
        'day_of_week': 'MARDI',
        'start_time': datetime.time(9, 0),
        'end_time': datetime.time(10, 30),
        'room_no': 'Amphi 3 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 105,
        'class_name': 'MIP',
        'section': 'S1',
        'subject_id': 129,
        'teacher_id': 63,
        'day_of_week': 'MERCREDI',
        'start_time': datetime.time(16, 0),
        'end_time': datetime.time(17, 30),
        'room_no': 'B18 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 106,
        'class_name': 'MIP',
        'section': 'S1',
        'subject_id': 129,
        'teacher_id': 63,
        'day_of_week': 'SAMEDI',
        'start_time': datetime.time(10, 45),
        'end_time': datetime.time(12, 15),
        'room_no': 'E2 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 107,
        'class_name': 'MIP',
        'section': 'S1',
        'subject_id': 130,
        'teacher_id': 76,
        'day_of_week': 'MARDI',
        'start_time': datetime.time(10, 45),
        'end_time': datetime.time(12, 15),
        'room_no': 'Amphi 7 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 108,
        'class_name': 'MIP',
        'section': 'S1',
        'subject_id': 130,
        'teacher_id': 76,
        'day_of_week': 'MERCREDI',
        'start_time': datetime.time(9, 0),
        'end_time': datetime.time(10, 30),
        'room_no': 'D14 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 109,
        'class_name': 'MIP',
        'section': 'S1',
        'subject_id': 130,
        'teacher_id': 76,
        'day_of_week': 'LUNDI',
        'start_time': datetime.time(10, 45),
        'end_time': datetime.time(12, 15),
        'room_no': 'A17 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 110,
        'class_name': 'MIPC_1',
        'section': 'S1',
        'subject_id': 149,
        'teacher_id': 44,
        'day_of_week': 'JEUDI',
        'start_time': datetime.time(14, 15),
        'end_time': datetime.time(15, 45),
        'room_no': 'Amphi 4 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 111,
        'class_name': 'MIPC_1',
        'section': 'S1',
        'subject_id': 149,
        'teacher_id': 44,
        'day_of_week': 'MARDI',
        'start_time': datetime.time(10, 45),
        'end_time': datetime.time(12, 15),
        'room_no': 'C20 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 112,
        'class_name': 'MIPC_1',
        'section': 'S1',
        'subject_id': 149,
        'teacher_id': 44,
        'day_of_week': 'MERCREDI',
        'start_time': datetime.time(14, 15),
        'end_time': datetime.time(15, 45),
        'room_no': 'B25 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 113,
        'class_name': 'MIPC_1',
        'section': 'S1',
        'subject_id': 150,
        'teacher_id': 61,
        'day_of_week': 'VENDREDI',
        'start_time': datetime.time(12, 30),
        'end_time': datetime.time(14, 0),
        'room_no': 'Amphi 7 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 114,
        'class_name': 'MIPC_1',
        'section': 'S1',
        'subject_id': 150,
        'teacher_id': 61,
        'day_of_week': 'MERCREDI',
        'start_time': datetime.time(16, 0),
        'end_time': datetime.time(17, 30),
        'room_no': 'D12 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 115,
        'class_name': 'MIPC_1',
        'section': 'S1',
        'subject_id': 150,
        'teacher_id': 61,
        'day_of_week': 'JEUDI',
        'start_time': datetime.time(12, 30),
        'end_time': datetime.time(14, 0),
        'room_no': 'B21 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 116,
        'class_name': 'MIPC_1',
        'section': 'S1',
        'subject_id': 151,
        'teacher_id': 78,
        'day_of_week': 'LUNDI',
        'start_time': datetime.time(16, 0),
        'end_time': datetime.time(17, 30),
        'room_no': 'Amphi 3 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 117,
        'class_name': 'MIPC_1',
        'section': 'S1',
        'subject_id': 151,
        'teacher_id': 78,
        'day_of_week': 'MARDI',
        'start_time': datetime.time(12, 30),
        'end_time': datetime.time(14, 0),
        'room_no': 'C4 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 118,
        'class_name': 'MIPC_1',
        'section': 'S1',
        'subject_id': 151,
        'teacher_id': 78,
        'day_of_week': 'JEUDI',
        'start_time': datetime.time(16, 0),
        'end_time': datetime.time(17, 30),
        'room_no': 'A19 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 119,
        'class_name': 'MIPC_1',
        'section': 'S1',
        'subject_id': 152,
        'teacher_id': 69,
        'day_of_week': 'JEUDI',
        'start_time': datetime.time(10, 45),
        'end_time': datetime.time(12, 15),
        'room_no': 'Amphi 6 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 120,
        'class_name': 'MIPC_1',
        'section': 'S1',
        'subject_id': 152,
        'teacher_id': 69,
        'day_of_week': 'SAMEDI',
        'start_time': datetime.time(9, 0),
        'end_time': datetime.time(10, 30),
        'room_no': 'D11 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 121,
        'class_name': 'MIPC_1',
        'section': 'S1',
        'subject_id': 152,
        'teacher_id': 69,
        'day_of_week': 'SAMEDI',
        'start_time': datetime.time(14, 15),
        'end_time': datetime.time(15, 45),
        'room_no': 'C23 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 122,
        'class_name': 'MIPC_1',
        'section': 'S1',
        'subject_id': 153,
        'teacher_id': 63,
        'day_of_week': 'MERCREDI',
        'start_time': datetime.time(9, 0),
        'end_time': datetime.time(10, 30),
        'room_no': 'Amphi 6 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 123,
        'class_name': 'MIPC_1',
        'section': 'S1',
        'subject_id': 153,
        'teacher_id': 63,
        'day_of_week': 'LUNDI',
        'start_time': datetime.time(14, 15),
        'end_time': datetime.time(15, 45),
        'room_no': 'A21 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 124,
        'class_name': 'MIPC_1',
        'section': 'S1',
        'subject_id': 153,
        'teacher_id': 63,
        'day_of_week': 'VENDREDI',
        'start_time': datetime.time(9, 0),
        'end_time': datetime.time(10, 30),
        'room_no': 'B2 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 125,
        'class_name': 'MIPC_1',
        'section': 'S1',
        'subject_id': 154,
        'teacher_id': 58,
        'day_of_week': 'LUNDI',
        'start_time': datetime.time(10, 45),
        'end_time': datetime.time(12, 15),
        'room_no': 'Amphi 1 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 126,
        'class_name': 'MIPC_1',
        'section': 'S1',
        'subject_id': 154,
        'teacher_id': 58,
        'day_of_week': 'VENDREDI',
        'start_time': datetime.time(10, 45),
        'end_time': datetime.time(12, 15),
        'room_no': 'B9 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 127,
        'class_name': 'MIPC_1',
        'section': 'S1',
        'subject_id': 154,
        'teacher_id': 58,
        'day_of_week': 'VENDREDI',
        'start_time': datetime.time(16, 0),
        'end_time': datetime.time(17, 30),
        'room_no': 'D13 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 128,
        'class_name': 'MIPC_2',
        'section': 'S1',
        'subject_id': 173,
        'teacher_id': 71,
        'day_of_week': 'SAMEDI',
        'start_time': datetime.time(16, 0),
        'end_time': datetime.time(17, 30),
        'room_no': 'Amphi 5 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 129,
        'class_name': 'MIPC_2',
        'section': 'S1',
        'subject_id': 173,
        'teacher_id': 71,
        'day_of_week': 'SAMEDI',
        'start_time': datetime.time(10, 45),
        'end_time': datetime.time(12, 15),
        'room_no': 'E14 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 130,
        'class_name': 'MIPC_2',
        'section': 'S1',
        'subject_id': 173,
        'teacher_id': 71,
        'day_of_week': 'MARDI',
        'start_time': datetime.time(12, 30),
        'end_time': datetime.time(14, 0),
        'room_no': 'B19 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 131,
        'class_name': 'MIPC_2',
        'section': 'S1',
        'subject_id': 174,
        'teacher_id': 60,
        'day_of_week': 'MERCREDI',
        'start_time': datetime.time(12, 30),
        'end_time': datetime.time(14, 0),
        'room_no': 'Amphi 3 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 132,
        'class_name': 'MIPC_2',
        'section': 'S1',
        'subject_id': 174,
        'teacher_id': 60,
        'day_of_week': 'VENDREDI',
        'start_time': datetime.time(9, 0),
        'end_time': datetime.time(10, 30),
        'room_no': 'B15 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 133,
        'class_name': 'MIPC_2',
        'section': 'S1',
        'subject_id': 174,
        'teacher_id': 60,
        'day_of_week': 'JEUDI',
        'start_time': datetime.time(14, 15),
        'end_time': datetime.time(15, 45),
        'room_no': 'B16 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 134,
        'class_name': 'MIPC_2',
        'section': 'S1',
        'subject_id': 175,
        'teacher_id': 75,
        'day_of_week': 'MARDI',
        'start_time': datetime.time(10, 45),
        'end_time': datetime.time(12, 15),
        'room_no': 'Amphi 8 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 135,
        'class_name': 'MIPC_2',
        'section': 'S1',
        'subject_id': 175,
        'teacher_id': 75,
        'day_of_week': 'LUNDI',
        'start_time': datetime.time(9, 0),
        'end_time': datetime.time(10, 30),
        'room_no': 'F25 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 136,
        'class_name': 'MIPC_2',
        'section': 'S1',
        'subject_id': 175,
        'teacher_id': 75,
        'day_of_week': 'LUNDI',
        'start_time': datetime.time(14, 15),
        'end_time': datetime.time(15, 45),
        'room_no': 'C18 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 137,
        'class_name': 'MIPC_2',
        'section': 'S1',
        'subject_id': 176,
        'teacher_id': 59,
        'day_of_week': 'SAMEDI',
        'start_time': datetime.time(14, 15),
        'end_time': datetime.time(15, 45),
        'room_no': 'Amphi 3 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 138,
        'class_name': 'MIPC_2',
        'section': 'S1',
        'subject_id': 176,
        'teacher_id': 59,
        'day_of_week': 'LUNDI',
        'start_time': datetime.time(10, 45),
        'end_time': datetime.time(12, 15),
        'room_no': 'B21 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 139,
        'class_name': 'MIPC_2',
        'section': 'S1',
        'subject_id': 176,
        'teacher_id': 59,
        'day_of_week': 'MARDI',
        'start_time': datetime.time(9, 0),
        'end_time': datetime.time(10, 30),
        'room_no': 'B10 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 140,
        'class_name': 'MIPC_2',
        'section': 'S1',
        'subject_id': 177,
        'teacher_id': 54,
        'day_of_week': 'MERCREDI',
        'start_time': datetime.time(9, 0),
        'end_time': datetime.time(10, 30),
        'room_no': 'Amphi 6 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 141,
        'class_name': 'MIPC_2',
        'section': 'S1',
        'subject_id': 177,
        'teacher_id': 54,
        'day_of_week': 'JEUDI',
        'start_time': datetime.time(9, 0),
        'end_time': datetime.time(10, 30),
        'room_no': 'C16 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 142,
        'class_name': 'MIPC_2',
        'section': 'S1',
        'subject_id': 177,
        'teacher_id': 54,
        'day_of_week': 'MARDI',
        'start_time': datetime.time(14, 15),
        'end_time': datetime.time(15, 45),
        'room_no': 'C5 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 143,
        'class_name': 'MIPC_2',
        'section': 'S1',
        'subject_id': 178,
        'teacher_id': 76,
        'day_of_week': 'MARDI',
        'start_time': datetime.time(16, 0),
        'end_time': datetime.time(17, 30),
        'room_no': 'Amphi 4 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 144,
        'class_name': 'MIPC_2',
        'section': 'S1',
        'subject_id': 178,
        'teacher_id': 76,
        'day_of_week': 'VENDREDI',
        'start_time': datetime.time(10, 45),
        'end_time': datetime.time(12, 15),
        'room_no': 'C5 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 145,
        'class_name': 'MIPC_2',
        'section': 'S1',
        'subject_id': 178,
        'teacher_id': 76,
        'day_of_week': 'LUNDI',
        'start_time': datetime.time(12, 30),
        'end_time': datetime.time(14, 0),
        'room_no': 'E8 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 146,
        'class_name': 'BCG',
        'section': 'S1',
        'subject_id': 197,
        'teacher_id': 71,
        'day_of_week': 'MARDI',
        'start_time': datetime.time(12, 30),
        'end_time': datetime.time(14, 0),
        'room_no': 'Amphi 4 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 147,
        'class_name': 'BCG',
        'section': 'S1',
        'subject_id': 197,
        'teacher_id': 71,
        'day_of_week': 'MARDI',
        'start_time': datetime.time(14, 15),
        'end_time': datetime.time(15, 45),
        'room_no': 'A5 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 148,
        'class_name': 'BCG',
        'section': 'S1',
        'subject_id': 197,
        'teacher_id': 71,
        'day_of_week': 'LUNDI',
        'start_time': datetime.time(9, 0),
        'end_time': datetime.time(10, 30),
        'room_no': 'D13 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 149,
        'class_name': 'BCG',
        'section': 'S1',
        'subject_id': 198,
        'teacher_id': 73,
        'day_of_week': 'MARDI',
        'start_time': datetime.time(9, 0),
        'end_time': datetime.time(10, 30),
        'room_no': 'Amphi 4 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 150,
        'class_name': 'BCG',
        'section': 'S1',
        'subject_id': 198,
        'teacher_id': 73,
        'day_of_week': 'VENDREDI',
        'start_time': datetime.time(12, 30),
        'end_time': datetime.time(14, 0),
        'room_no': 'A4 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 151,
        'class_name': 'BCG',
        'section': 'S1',
        'subject_id': 198,
        'teacher_id': 73,
        'day_of_week': 'SAMEDI',
        'start_time': datetime.time(10, 45),
        'end_time': datetime.time(12, 15),
        'room_no': 'C20 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 152,
        'class_name': 'BCG',
        'section': 'S1',
        'subject_id': 199,
        'teacher_id': 75,
        'day_of_week': 'LUNDI',
        'start_time': datetime.time(12, 30),
        'end_time': datetime.time(14, 0),
        'room_no': 'Amphi 5 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 153,
        'class_name': 'BCG',
        'section': 'S1',
        'subject_id': 199,
        'teacher_id': 75,
        'day_of_week': 'MERCREDI',
        'start_time': datetime.time(14, 15),
        'end_time': datetime.time(15, 45),
        'room_no': 'F6 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 154,
        'class_name': 'BCG',
        'section': 'S1',
        'subject_id': 199,
        'teacher_id': 75,
        'day_of_week': 'JEUDI',
        'start_time': datetime.time(9, 0),
        'end_time': datetime.time(10, 30),
        'room_no': 'D21 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 155,
        'class_name': 'BCG',
        'section': 'S1',
        'subject_id': 200,
        'teacher_id': 75,
        'day_of_week': 'MERCREDI',
        'start_time': datetime.time(10, 45),
        'end_time': datetime.time(12, 15),
        'room_no': 'Amphi 8 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 156,
        'class_name': 'BCG',
        'section': 'S1',
        'subject_id': 200,
        'teacher_id': 75,
        'day_of_week': 'SAMEDI',
        'start_time': datetime.time(9, 0),
        'end_time': datetime.time(10, 30),
        'room_no': 'D14 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 157,
        'class_name': 'BCG',
        'section': 'S1',
        'subject_id': 200,
        'teacher_id': 75,
        'day_of_week': 'VENDREDI',
        'start_time': datetime.time(14, 15),
        'end_time': datetime.time(15, 45),
        'room_no': 'A14 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 158,
        'class_name': 'BCG',
        'section': 'S1',
        'subject_id': 201,
        'teacher_id': 63,
        'day_of_week': 'LUNDI',
        'start_time': datetime.time(16, 0),
        'end_time': datetime.time(17, 30),
        'room_no': 'Amphi 7 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 159,
        'class_name': 'BCG',
        'section': 'S1',
        'subject_id': 201,
        'teacher_id': 63,
        'day_of_week': 'MARDI',
        'start_time': datetime.time(10, 45),
        'end_time': datetime.time(12, 15),
        'room_no': 'A8 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 160,
        'class_name': 'BCG',
        'section': 'S1',
        'subject_id': 201,
        'teacher_id': 63,
        'day_of_week': 'LUNDI',
        'start_time': datetime.time(10, 45),
        'end_time': datetime.time(12, 15),
        'room_no': 'D4 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 161,
        'class_name': 'BCG',
        'section': 'S1',
        'subject_id': 202,
        'teacher_id': 64,
        'day_of_week': 'VENDREDI',
        'start_time': datetime.time(10, 45),
        'end_time': datetime.time(12, 15),
        'room_no': 'Amphi 6 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 162,
        'class_name': 'BCG',
        'section': 'S1',
        'subject_id': 202,
        'teacher_id': 64,
        'day_of_week': 'SAMEDI',
        'start_time': datetime.time(14, 15),
        'end_time': datetime.time(15, 45),
        'room_no': 'C21 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 163,
        'class_name': 'BCG',
        'section': 'S1',
        'subject_id': 202,
        'teacher_id': 64,
        'day_of_week': 'JEUDI',
        'start_time': datetime.time(12, 30),
        'end_time': datetime.time(14, 0),
        'room_no': 'F11 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 164,
        'class_name': 'GEGM',
        'section': 'S1',
        'subject_id': 221,
        'teacher_id': 60,
        'day_of_week': 'LUNDI',
        'start_time': datetime.time(10, 45),
        'end_time': datetime.time(12, 15),
        'room_no': 'Amphi 7 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 165,
        'class_name': 'GEGM',
        'section': 'S1',
        'subject_id': 221,
        'teacher_id': 60,
        'day_of_week': 'MERCREDI',
        'start_time': datetime.time(9, 0),
        'end_time': datetime.time(10, 30),
        'room_no': 'B15 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 166,
        'class_name': 'GEGM',
        'section': 'S1',
        'subject_id': 221,
        'teacher_id': 60,
        'day_of_week': 'JEUDI',
        'start_time': datetime.time(16, 0),
        'end_time': datetime.time(17, 30),
        'room_no': 'F25 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 167,
        'class_name': 'GEGM',
        'section': 'S1',
        'subject_id': 222,
        'teacher_id': 44,
        'day_of_week': 'MARDI',
        'start_time': datetime.time(16, 0),
        'end_time': datetime.time(17, 30),
        'room_no': 'Amphi 3 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 168,
        'class_name': 'GEGM',
        'section': 'S1',
        'subject_id': 222,
        'teacher_id': 44,
        'day_of_week': 'SAMEDI',
        'start_time': datetime.time(10, 45),
        'end_time': datetime.time(12, 15),
        'room_no': 'D23 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 169,
        'class_name': 'GEGM',
        'section': 'S1',
        'subject_id': 222,
        'teacher_id': 44,
        'day_of_week': 'MERCREDI',
        'start_time': datetime.time(10, 45),
        'end_time': datetime.time(12, 15),
        'room_no': 'F18 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 170,
        'class_name': 'GEGM',
        'section': 'S1',
        'subject_id': 223,
        'teacher_id': 78,
        'day_of_week': 'MERCREDI',
        'start_time': datetime.time(16, 0),
        'end_time': datetime.time(17, 30),
        'room_no': 'Amphi 8 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 171,
        'class_name': 'GEGM',
        'section': 'S1',
        'subject_id': 223,
        'teacher_id': 78,
        'day_of_week': 'SAMEDI',
        'start_time': datetime.time(9, 0),
        'end_time': datetime.time(10, 30),
        'room_no': 'F17 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 172,
        'class_name': 'GEGM',
        'section': 'S1',
        'subject_id': 223,
        'teacher_id': 78,
        'day_of_week': 'SAMEDI',
        'start_time': datetime.time(16, 0),
        'end_time': datetime.time(17, 30),
        'room_no': 'A16 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 173,
        'class_name': 'GEGM',
        'section': 'S1',
        'subject_id': 224,
        'teacher_id': 78,
        'day_of_week': 'JEUDI',
        'start_time': datetime.time(14, 15),
        'end_time': datetime.time(15, 45),
        'room_no': 'Amphi 5 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 174,
        'class_name': 'GEGM',
        'section': 'S1',
        'subject_id': 224,
        'teacher_id': 78,
        'day_of_week': 'VENDREDI',
        'start_time': datetime.time(16, 0),
        'end_time': datetime.time(17, 30),
        'room_no': 'D3 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 175,
        'class_name': 'GEGM',
        'section': 'S1',
        'subject_id': 224,
        'teacher_id': 78,
        'day_of_week': 'MERCREDI',
        'start_time': datetime.time(14, 15),
        'end_time': datetime.time(15, 45),
        'room_no': 'E4 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 176,
        'class_name': 'GEGM',
        'section': 'S1',
        'subject_id': 225,
        'teacher_id': 56,
        'day_of_week': 'JEUDI',
        'start_time': datetime.time(12, 30),
        'end_time': datetime.time(14, 0),
        'room_no': 'Amphi 5 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 177,
        'class_name': 'GEGM',
        'section': 'S1',
        'subject_id': 225,
        'teacher_id': 56,
        'day_of_week': 'SAMEDI',
        'start_time': datetime.time(12, 30),
        'end_time': datetime.time(14, 0),
        'room_no': 'A8 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 178,
        'class_name': 'GEGM',
        'section': 'S1',
        'subject_id': 225,
        'teacher_id': 56,
        'day_of_week': 'VENDREDI',
        'start_time': datetime.time(9, 0),
        'end_time': datetime.time(10, 30),
        'room_no': 'E8 (TP)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 179,
        'class_name': 'GEGM',
        'section': 'S1',
        'subject_id': 226,
        'teacher_id': 58,
        'day_of_week': 'VENDREDI',
        'start_time': datetime.time(14, 15),
        'end_time': datetime.time(15, 45),
        'room_no': 'Amphi 4 (Cours)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 180,
        'class_name': 'GEGM',
        'section': 'S1',
        'subject_id': 226,
        'teacher_id': 58,
        'day_of_week': 'VENDREDI',
        'start_time': datetime.time(10, 45),
        'end_time': datetime.time(12, 15),
        'room_no': 'D23 (TD)'
    }},
    {'model': 'student.TimeTable', 'fields': {
        'id': 181,
        'class_name': 'GEGM',
        'section': 'S1',
        'subject_id': 226,
        'teacher_id': 58,
        'day_of_week': 'LUNDI',
        'start_time': datetime.time(14, 15),
        'end_time': datetime.time(15, 45),
        'room_no': 'E17 (TP)'
    }},
    {'model': 'student.Holiday', 'fields': {
        'id': 3,
        'holiday_id': 'HOL-2026-01',
        'name': 'Nouvel An',
        'holiday_type': 'Civil',
        'start_date': datetime.date(2026, 1, 1),
        'end_date': datetime.date(2026, 1, 1)
    }},
    {'model': 'student.Holiday', 'fields': {
        'id': 4,
        'holiday_id': 'HOL-2026-02',
        'name': "Manifeste de l'Indépendance",
        'holiday_type': 'Civil',
        'start_date': datetime.date(2026, 1, 11),
        'end_date': datetime.date(2026, 1, 11)
    }},
    {'model': 'student.Holiday', 'fields': {
        'id': 5,
        'holiday_id': 'HOL-2026-03',
        'name': 'Nouvel An Amazigh',
        'holiday_type': 'Civil',
        'start_date': datetime.date(2026, 1, 14),
        'end_date': datetime.date(2026, 1, 14)
    }},
    {'model': 'student.Holiday', 'fields': {
        'id': 6,
        'holiday_id': 'HOL-2026-04',
        'name': 'Fête du Travail',
        'holiday_type': 'Civil',
        'start_date': datetime.date(2026, 5, 1),
        'end_date': datetime.date(2026, 5, 1)
    }},
    {'model': 'student.Holiday', 'fields': {
        'id': 7,
        'holiday_id': 'HOL-2026-05',
        'name': 'Fête du Trône',
        'holiday_type': 'Civil',
        'start_date': datetime.date(2026, 7, 30),
        'end_date': datetime.date(2026, 7, 30)
    }},
    {'model': 'student.Holiday', 'fields': {
        'id': 8,
        'holiday_id': 'HOL-2026-06',
        'name': 'Récupération de Oued Eddahab',
        'holiday_type': 'Civil',
        'start_date': datetime.date(2026, 8, 14),
        'end_date': datetime.date(2026, 8, 14)
    }},
    {'model': 'student.Holiday', 'fields': {
        'id': 9,
        'holiday_id': 'HOL-2026-07',
        'name': 'Révolution du Roi et du Peuple',
        'holiday_type': 'Civil',
        'start_date': datetime.date(2026, 8, 20),
        'end_date': datetime.date(2026, 8, 20)
    }},
    {'model': 'student.Holiday', 'fields': {
        'id': 10,
        'holiday_id': 'HOL-2026-08',
        'name': 'Fête de la Jeunesse',
        'holiday_type': 'Civil',
        'start_date': datetime.date(2026, 8, 21),
        'end_date': datetime.date(2026, 8, 21)
    }},
    {'model': 'student.Holiday', 'fields': {
        'id': 11,
        'holiday_id': 'HOL-2026-09',
        'name': "Fête de l'Unité",
        'holiday_type': 'Civil',
        'start_date': datetime.date(2026, 10, 31),
        'end_date': datetime.date(2026, 10, 31)
    }},
    {'model': 'student.Holiday', 'fields': {
        'id': 12,
        'holiday_id': 'HOL-2026-10',
        'name': 'Anniversaire de la Marche Verte',
        'holiday_type': 'Civil',
        'start_date': datetime.date(2026, 11, 6),
        'end_date': datetime.date(2026, 11, 6)
    }},
    {'model': 'student.Holiday', 'fields': {
        'id': 13,
        'holiday_id': 'HOL-2026-11',
        'name': "Fête de l'Indépendance",
        'holiday_type': 'Civil',
        'start_date': datetime.date(2026, 11, 18),
        'end_date': datetime.date(2026, 11, 18)
    }},
    {'model': 'student.GradeNegotiationHistory', 'fields': {
        'id': 1,
        'result_id': 5,
        'teacher_id': 61,
        'action': 'Accepté',
        'original_mark': Decimal('10.00'),
        'proposed_mark': Decimal('10.25'),
        'date_decided': datetime.datetime(2026, 3, 21, 17, 32, 16)
    }},
    {'model': 'student.GradeNegotiationHistory', 'fields': {
        'id': 2,
        'result_id': 10,
        'teacher_id': 61,
        'action': 'Refusé',
        'original_mark': Decimal('11.00'),
        'proposed_mark': Decimal('11.25'),
        'date_decided': datetime.datetime(2026, 3, 21, 20, 43, 52)
    }},
    {'model': 'student.GradeNegotiationHistory', 'fields': {
        'id': 3,
        'result_id': 18,
        'teacher_id': 78,
        'action': 'Accepté',
        'original_mark': Decimal('11.00'),
        'proposed_mark': Decimal('20.00'),
        'date_decided': datetime.datetime(2026, 3, 25, 10, 44, 46)
    }},
    {'model': 'student.StudentCardRequest', 'fields': {
        'id': 1,
        'student_id': 396,
        'photo': 'student_cards/photos/unnamed_1.jpg',
        'blood_type': None,
        'status': 'Générée',
        'issued_card': 'student_cards/generated/card_ETU_BCG_S1_01.png',
        'request_date': datetime.datetime(2026, 3, 21, 18, 11, 28),
        'admin_notes': None
    }},
    {'model': 'student.StudentCardRequest', 'fields': {
        'id': 2,
        'student_id': 461,
        'photo': 'student_cards/photos/WhatsApp_Image_2025-12-09_at_15.50.04.jpeg',
        'blood_type': None,
        'status': 'Générée',
        'issued_card': 'student_cards/generated/card_STU-537.png',
        'request_date': datetime.datetime(2026, 3, 21, 22, 44, 22),
        'admin_notes': None
    }},
    {'model': 'student.CertificateRequest', 'fields': {
        'id': 2,
        'student_id': 461,
        'certificate_type': 'Attestation de Scolarité',
        'status': 'Approved',
        'date_requested': datetime.datetime(2026, 3, 21, 22, 45, 23)
    }},
    {'model': 'student.CertificateRequest', 'fields': {
        'id': 3,
        'student_id': 461,
        'certificate_type': 'Relevé de Notes (Transcript)',
        'status': 'Approved',
        'date_requested': datetime.datetime(2026, 3, 21, 22, 51, 4)
    }},
    {'model': 'student.CertificateRequest', 'fields': {
        'id': 4,
        'student_id': 461,
        'certificate_type': 'Certificat de Réussite',
        'status': 'Approved',
        'date_requested': datetime.datetime(2026, 3, 21, 22, 51, 7)
    }},
    {'model': 'student.CertificateRequest', 'fields': {
        'id': 5,
        'student_id': 461,
        'certificate_type': 'Attestation de Scolarité',
        'status': 'Approved',
        'date_requested': datetime.datetime(2026, 3, 25, 10, 31, 32)
    }},
    {'model': 'student.CertificateRequest', 'fields': {
        'id': 6,
        'student_id': 396,
        'certificate_type': 'Attestation de Scolarité',
        'status': 'Pending',
        'date_requested': datetime.datetime(2026, 3, 27, 14, 33, 24)
    }}
    ]
    
    print(f"\n[Data Migration] Loading {len(data)} entries for 0011_load_academic_data...")
    for item in data:
        app_label, model_name = item['model'].split('.')
        Model = apps.get_model(app_label, model_name)
        fields = item['fields']
        # update_or_create to ensure no duplicates
        pk_val = fields.pop('id', None)
        if pk_val:
            Model.objects.update_or_create(id=pk_val, defaults=fields)
        else:
            Model.objects.create(**fields)

class Migration(migrations.Migration):
    dependencies = [
        ('home_auth', '0010_load_student_data'),
    ]
    operations = [
        migrations.RunPython(load_data),
    ]
