import os
import streamlit as st

# EDA Libraries
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('Agg')

import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

def main():



	""" Frequent ML Dataset Explorer """
	st.title("Frequent ML Dataset Explorer")
	st.subheader("Dataset Explorer using Streamlit")

	html_variable = """

		<div style = "background-color: red;"> <p style = "color: white; font-size: 22px;">Made by Somonnoy Banerjee</p>
		</style>
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
		

	"""
	st.markdown(html_variable, unsafe_allow_html = True)

	def file_selector(folder_path = './datasets'):
		filenames = os.listdir(folder_path)
		selected_filename = st.selectbox("Please select a file", filenames)
		return os.path.join(folder_path, selected_filename)

	filename = file_selector()

	#st.write('You selected {}'.format(filename))

	st.info('You selected {}'.format(filename))

	# Read the Dataset

	df = pd.read_csv(filename)

	# Show the Dataset

	if st.checkbox("Show Dataset"):
		number = st.number_input('Select number of rows for preview',  min_value = 1, max_value = 20, value = 5, step=1)
		st.dataframe(df.head(number))

	# Display Column Names

	if st.button('Display Column Names'):
		st.write(df.columns)

	# Show Shape

	if st.checkbox('Display Shape of Dataset'):
		#st.write(df.shape)
		data_dim = st.radio("Show Dimension by ", ('rows', 'columns', 'complete shape'))
		if data_dim == 'columns':
			st.text('Number of Columns')
			st.write(df.shape[1])
		elif data_dim == 'rows':
			st.text('Number of Rows')
			st.write(df.shape[0])
		else:
			st.text('Shape of the Dataset')
			st.write(df.shape)


	# Select Columns

	if st.checkbox("Select columns to be displayed"):
		all_cols = df.columns.tolist()
		selected_cols = st.multiselect("Select", all_cols)
		df_new = df[selected_cols]
		st.dataframe(df_new)

	# Show Values

	# if st.button('Display Value Count'):
	# 	st.text("Value Count of the Target Class")
	# 	st.write(df.iloc[:, -1].value_counts())

	# Show Data Types

	# if st.button('Display Data Types'):
	# 	st.write(df.dtypes)

	# Show Summary

	if st.button('Display Summary of Dataset'):
		st.write(df.describe())

	# Data Visualization

	st.subheader('Data Visualization')

	# Correlation



	# Seaborn

	if st.checkbox("Correlation Plot [Seaborn]"):
		st.write(sns.heatmap(df.corr(),annot=True))
		st.pyplot()

	# Count Plot

	if st.checkbox("Plot of Value Counts"):
		st.text("Value Counts By Target")
		all_columns_names = df.columns.tolist()
		primary_col = st.selectbox("Primary Columm to GroupBy",all_columns_names)
		selected_columns_names = st.multiselect("Select Columns",all_columns_names)
		if st.button("Plot"):
			st.text("Generate Plot")
			if selected_columns_names:
				vc_plot = df.groupby(primary_col)[selected_columns_names].count()
			else:
				vc_plot = df.iloc[:,-1].value_counts()
			st.write(vc_plot.plot(kind="bar"))
			st.pyplot()


	# Pie Chart

	if st.checkbox("Pie Plot"):
		all_col_names = df.columns.tolist()
		st.success("Generating a Pie Plot")
		st.write(df.iloc[:, -1].value_counts().plot.pie(autopct = "%1.1f%%"))
		st.pyplot()



	# Customizable Plot

	st.subheader('Customizable Plot')
	all_col_names = df.columns.tolist()
	type_of_plot = st.selectbox("Select Type of Plot", ["area", "bar", "line", "hist", "box", "kde"])
	selected_col_names = st.multiselect("Select Columns to Plot", all_col_names)

	if st.button("Generate Plot"):
		st.success("Generating Customizable Plot of {} for {} ".format(type_of_plot, selected_col_names))

		# Plot using Streamlit

		if type_of_plot == 'area':
			custom_data = df[selected_col_names]
			st.area_chart(custom_data)

		elif type_of_plot == 'bar':
			custom_data = df[selected_col_names]
			st.bar_chart(custom_data)

		elif type_of_plot == 'line':
			custom_data = df[selected_col_names]
			st.line_chart(custom_data)

		elif type_of_plot:
			custom_plot = df[selected_col_names].plot(kind = type_of_plot)
			st.write(custom_plot)
			st.pyplot()

if __name__ == '__main__':
	main()