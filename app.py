import os
import streamlit as st

# EDA Libraries
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('Agg')

import seaborn as sns

def main():
	""" Frequent ML Dataset Explorer """
	st.title("Frequent ML Dataset Explorer")
	st.subheader("Dataset Explorer using Streamlit")

	html_variable = """

		<div style = "background-color: red;"> <p style = "color: white; font-size: 22px;">Made by Somonnoy Banerjee</p>

	"""
	st.markdown(html_variable, unsafe_allow_html = True)

	def file_selector(folder_path = '.'):
		filenames = os.listdir(folder_path)
		selected_filename = st.selectbox("Please select a file", filenames)
		return os.path.join(folder_path, selected_filename)

	filename = file_selector()


if __name__ == '__main__':
	main()