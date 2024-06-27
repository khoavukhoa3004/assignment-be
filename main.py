from file_mngt import extract_document, extract_paragraph_text, recovery_document, extract_pptx

TARGET_FOLDER = "output"

### QUESTION 1
extract_document("pdf_mock_file.pdf", f"{TARGET_FOLDER}/q1/pdf_mock_folder")

extract_document("docx_mock_file.docx", f"{TARGET_FOLDER}/q1/docx_mock_folder")

### QUESTION 2
extract_paragraph_text("pdf_mock_file.pdf", f"{TARGET_FOLDER}/q2/pdf_mock_folder")

extract_paragraph_text("docx_mock_file.docx", f"{TARGET_FOLDER}/q2/docx_mock_folder")

### QUESTION 3
recovery_document(f"{TARGET_FOLDER}/q2/pdf_mock_folder/text.json", f"{TARGET_FOLDER}/q3/pdf_mock_folder")

recovery_document(f"{TARGET_FOLDER}/q2/docx_mock_folder/text.json", f"{TARGET_FOLDER}/q3/docx_mock_folder")

### QUESTION 4
# extract_pptx("Networking.pptx", f"{TARGET_FOLDER}/q4/pptx_mock_folder")