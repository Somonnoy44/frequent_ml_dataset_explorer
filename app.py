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

		<h1> Hello </h1>

	"""
	st.markdown(html_variable, unsafe_allow_html = True)

if __name__ == '__main__':
	main()