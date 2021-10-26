from django.test import TestCase
from .models import Category, Medicine, MedicineForm


class MedicineModelTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):

        Medicine.objects.create(
            medicineName = 'septrine',
            # category= categ,
            genericName= 'septrinae',
            # form= form,
            discount= 0,
            sideEffect= '',
            slug= '',
            image= '',
        )
    
    def test_string_method(self):
        medicine = Medicine.objects.get(medicineId=1)
        expected_string= medicine.medicineName
        self.assertEqual(str(medicine), expected_string)