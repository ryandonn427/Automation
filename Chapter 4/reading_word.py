import docx

doc = docx.Document('document-1.docx')

print(doc.core_properties.keywords)
print(doc.core_properties.title)
print(doc.core_properties.modified)
