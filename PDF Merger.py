from PyPDF2 import PdfWriter
import streamlit as st
merger = PdfWriter()


def merge_pd(files):
    for pdf in files:
        merger.append(pdf)

    merger.write("Joint.pdf")
    merger.close()


merge_fun = merge_pd(['dummy.pdf','sample.pdf'])


