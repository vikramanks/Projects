import pytesseract
import utlil
from pdf2image import convert_from_path
from parser_prescription import PrescriptionPraser
from parser_patient_details import PatientDetailsParser

Poppler_path = r'C:\poppler-22.04.0\Library\bin'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract(file_path, file_format):
    # step1 extracting text from pdf
    pages = convert_from_path(file_path, poppler_path=Poppler_path)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    document_text = ''
    if len(pages) > 0:
        page = pages[0]
        processed_image = utlil.preprcess_image(page)
        text = pytesseract.image_to_string(processed_image, lang='eng')
        document_text = '\n' + text

    # step2 fields from text
    if file_format == 'prescription':
        extracted_data = PrescriptionPraser(document_text).parse()
    elif file_format == 'patient_details':
        extracted_data = PatientDetailsParser(document_text).parse()
    else:
        raise Exception("Invalid Document Format")

    return extracted_data


if __name__ == "__main__":
    data = extract(r'F:\Vikraman\Code_Basics_Course\my_project_medical\Backend\notebook\docs\prescription\pre_2.pdf',
                   'prescription')
    print(data)
