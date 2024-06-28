from constant import INPUT_FOLDER, MOCK_FILE_DOCX, MOCK_FILE_PDF, MOCK_FOLDER_DOCX, MOCK_FOLDER_PDF, TARGET_FOLDER
from file_mngt import extract_document, extract_paragraph_text, recovery_document, extract_pptx



### QUESTION 1
extract_document(f"/app/input/{MOCK_FILE_PDF}", f"{TARGET_FOLDER}/q1/{MOCK_FOLDER_PDF}")

extract_document(f"/app/input/{MOCK_FILE_DOCX}", f"{TARGET_FOLDER}/q1/{MOCK_FOLDER_DOCX}")

### QUESTION 2
extract_paragraph_text(MOCK_FILE_PDF, f"{INPUT_FOLDER}/{MOCK_FILE_PDF}", f"{TARGET_FOLDER}/q2/{MOCK_FILE_PDF}")

extract_paragraph_text(MOCK_FILE_DOCX, f"{INPUT_FOLDER}/{MOCK_FILE_DOCX}", f"{TARGET_FOLDER}/q2/{MOCK_FILE_DOCX}")

### QUESTION 3
recovery_document(f"{TARGET_FOLDER}/q2/{MOCK_FOLDER_PDF}/text.json", f"{TARGET_FOLDER}/q3/{MOCK_FOLDER_PDF}")

recovery_document(f"{TARGET_FOLDER}/q2/{MOCK_FOLDER_DOCX}/text.json", f"{TARGET_FOLDER}/q3/{MOCK_FOLDER_DOCX}")

### QUESTION 4
# extract_pptx("Networking.pptx", f"{TARGET_FOLDER}/q4/pptx_mock_folder")