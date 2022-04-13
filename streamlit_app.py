import streamlit as st
import streamlit_book as stb
# import streamlit as st
import numpy as np
import pandas as pd
import pyarrow as pa
import seaborn as sns
# from apps.praproses import preprocessing2
import os
from dateutil import parser
import joblib
from sklearn.feature_selection import mutual_info_classif
from sklearn.feature_selection import SelectKBest
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import StackingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

# Set wide display
st.set_page_config(layout="wide")

# Set shared sidebar
st.sidebar.markdown("## Shared Sidebar")
split_size = st.sidebar.slider('Rasio Pembagian Data (% Untuk Data Latih)', 10, 90, 80, 5)
st.session_state.split_size = split_size
jumlah_fitur = st.sidebar.slider('jumlah pilihan fitur (Untuk Data Latih)', 5, 47, 20, 5)
st.session_state.jumlah_fitur = jumlah_fitur
parameter_n_estimators = st.sidebar.slider('Number of estimators (n_estimators)', 10, 100, 50, 10)
st.session_state.parameter_n_estimators = parameter_n_estimators
tetangga = st.sidebar.slider('Jumlah K (KNN)', 11, 101, 55, 11)
st.session_state.tetangga = tetangga
# Set multipage
save_answers = False
stb.set_chapter_config(path="pages/",
                       save_answers=save_answers,
                       )
