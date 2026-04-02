import xml.etree.ElementTree as ET
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from faculty.models import Subject, Teacher
from .models import TimeTable

class XMLTimetableImporter:
    """
    Handles importing of XML timetable files.
    Expected format is a general school XML or Untis-style exports.
    """
    
    def __init__(self, xml_file):
        self.tree = ET.parse(xml_file)
        self.root = self.tree.getroot()
        self.results = {
            'success': False,
            'imported_count': 0,
            'errors': [],
            'warnings': []
        }

    def run(self):
        # We look for <lesson> tags or <entry> tags
        lessons = self.root.findall('.//lesson') or self.root.findall('.//entry')
        
        if not lessons:
            self.results['errors'].append("Aucun élément <lesson> ou <entry> trouvé dans le fichier XML.")
            return self.results

        # To avoid duplicates if we re-import the same file
        # Optional: Decide if we want to clear existing or just append
        
        day_map = {
            '1': 'Monday', '2': 'Tuesday', '3': 'Wednesday', '4': 'Thursday', '5': 'Friday', '6': 'Saturday',
            'MON': 'Monday', 'TUE': 'Tuesday', 'WED': 'Wednesday', 'THU': 'Thursday', 'FRI': 'Friday', 'SAT': 'Saturday',
            'LUNDI': 'Monday', 'MARDI': 'Tuesday', 'MERCREDI': 'Wednesday', 'JEUDI': 'Thursday', 'VENDREDI': 'Friday', 'SAMEDI': 'Saturday'
        }

        for lesson_node in lessons:
            try:
                # Basic mapping (Untis XML style or generic)
                subject_code = self._get_node_text(lesson_node, 'subject', 'sub')
                teacher_code = self._get_node_text(lesson_node, 'teacher', 'tea')
                klass_name = self._get_node_text(lesson_node, 'klass', 'class')
                room_no = self._get_node_text(lesson_node, 'room', 'roo', default='TBA')
                day_val = self._get_node_text(lesson_node, 'day', 'd')
                start_time_str = self._get_node_text(lesson_node, 'start_time', 'start', 'start_t')
                end_time_str = self._get_node_text(lesson_node, 'end_time', 'end', 'end_t')

                if not all([subject_code, teacher_code, klass_name, day_val, start_time_str, end_time_str]):
                    self.results['warnings'].append(f"Élément ignoré : Données incomplètes (Sujet: {subject_code}, Classe: {klass_name})")
                    continue

                # Normalize Day
                day = day_map.get(day_val.upper(), day_val.capitalize())
                if day not in dict(TimeTable._meta.get_field('day_of_week').choices):
                     self.results['warnings'].append(f"Jour inconnu '{day_val}' pour {subject_code}")
                     continue

                # Get Subject and Teacher objects
                try:
                    # Look by ID or name
                    subject = Subject.objects.filter(subject_id=subject_code).first() or Subject.objects.filter(name__icontains=subject_code).first()
                    teacher = Teacher.objects.filter(teacher_id=teacher_code).first() or Teacher.objects.filter(last_name__icontains=teacher_code).first()
                    
                    if not subject:
                        self.results['warnings'].append(f"Sujet '{subject_code}' non trouvé dans la base de données.")
                        continue
                    if not teacher:
                        self.results['warnings'].append(f"Professeur '{teacher_code}' non trouvé.")
                        continue

                    # Create TimeTable entry
                    TimeTable.objects.create(
                        class_name=klass_name,
                        section='A', # Default
                        subject=subject,
                        teacher=teacher,
                        day_of_week=day,
                        start_time=self._parse_time(start_time_str),
                        end_time=self._parse_time(end_time_str),
                        room_no=room_no
                    )
                    self.results['imported_count'] += 1

                except Exception as e:
                    self.results['errors'].append(f"Erreur lors de la création pour {subject_code}: {str(e)}")

            except Exception as e:
                self.results['errors'].append(f"Erreur de lecture d'un nœud XML: {str(e)}")

        self.results['success'] = self.results['imported_count'] > 0
        return self.results

    def _get_node_text(self, parent, *tag_names, default=None):
        for tag in tag_names:
            node = parent.find(tag)
            if node is not None and node.text:
                return node.text.strip()
        return default

    def _parse_time(self, time_str):
        # Handle formats like HH:MM, HHMM, or H:MM
        time_str = time_str.replace(':', '')
        if len(time_str) == 3: time_str = '0' + time_str
        if len(time_str) == 4:
            return datetime.strptime(time_str, '%H%M').time()
        return datetime.strptime(time_str, '%H:%M').time()
