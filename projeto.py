from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient

endpoint = "https://<your-resource>.cognitiveservices.azure.com/"
key = "<your-key>"

client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

with open("document.pdf", "rb") as f:
    poller = client.begin_analyze_document("prebuilt-document", document=f)
result = poller.result()

# extrair texto e tabelas
for page in result.pages:
    print("Página:", page.page_number)
    for line in page.lines:
        print(line.content)

for table in result.tables:
    for r, row in enumerate(table.cells):
        # use row.column_index / row.row_index / row.content
        pass
