import streamlit
import pandas
streamlit.title(" My Parents New Healthy divers")
streamlit.header(' 🥣 Breakfast Menu')
streamlit.text('🍊 Orange 3 & Bluberry Oatmeal')
streamlit.text('🥬  kale ,Spinach & Rockett Smoothie')
streamlit.text(' 🥚Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 Avocado Toast')
streamlit.header('🍌🥭Build Your own Fruit Smoothie ')
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruit_selected=streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado'])
fruits_to_show = my_fruit_list.loc[fruit_selected]
# display the table on the page

streamlit.dataframe(fruits_to_show)
