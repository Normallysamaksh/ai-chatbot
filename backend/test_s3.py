from backend.aws.s3 import list_pdfs, download_pdf

pdfs = list_pdfs()
print(pdfs)

if pdfs:
    download_pdf(pdfs[0], f"backend/uploads/{pdfs[0]}")
    print("Downloaded:", pdfs[0])
