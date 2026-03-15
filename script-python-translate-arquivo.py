def translate_document(path):
    document = Document(path)
    full_text = []
    for paragraph in document.paragraphs:
        translated_text = translator_text(paragraph.text, language_destination)
        full_text.append(translated_text)

    translated_doc = Document()
    for line in full_text:
        print(line)
        translated_doc.add_paragraph(line)
    path_translated = path.replace(".docx", f"_{language_destination}.docx")
    translated_doc.save(path_translated)
    return path_translated

input_file = "/content/MUSICA.docx"
translate_document(input_file)
