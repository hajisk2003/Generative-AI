from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader=DirectoryLoader(
    path='books',
    globs='*.pdf',
    loader_cls=PyPDFLoader
)

docs=loader.load()
docs[1].page_content
docs[326].page_content

print(len(docs))