import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd

st.set_page_config(page_title= "Analisis Pasar AI dan IoT dalam Bidang Perikanan di Indonesia", page_icon='icon.jpg',layout="wide")
st.sidebar.subheader('Analisis Pasar AI dan IoT dalam Bidang Perikanan di Indonesia')
st.sidebar.markdown(f"""
                   Analisis dilakukan berdasarkan data pada **[Statistik Kementerian Kelautan dan Perikanan (KKP)](https://statistik.kkp.go.id/)** dan **[Badan Pusat Statistik (BPS)](https://www.bps.go.id/)**.
                   \ndibuat dengan menggunakan Tableau, Excel dan Python""")
st.sidebar.markdown('**[Adi Nugraha, 2022](https://id.linkedin.com/in/adinugraha790)**')

st.title('Analisis Kompetitif dan Rekomendasi')
st.subheader("Analisis Kompetitif")

st.markdown('Berikut ini adalah hasil observasi situs web resmi sekitar 15 startup perikanan Indonesia, dan data pembandingnya dari Statistik KKP untuk tahun 2020.')
st.markdown('_Impact Metrics_ adalah seberapa besar pengaruh _startup_ tersebut terhadap perikanan Indonesia dan Daerah adalah ruang lingkup pengaruhnya, dan data pembandingnya adalah data dari Statistik KKP 2020. Disini dapat dilihat bahwa **masih sangat besar gap antara pengaruhnya dan keseluruhan populasi**, sehingga dapat dikatakan **masih sangat luas ruang untuk ekspansi pasar dan menambahkan _marketshare_**.')
df = pd.read_excel('Startup Impact.xlsx')
st.table(df)

# df1 = pd.read_excel('Comparation.xlsx')
# st.table(df1)

st.markdown('Berikut ini adalah bagaimana startup-startup tersebut berkontribusi terhadap perikanan Indoneia. 15 _startup_ perikanan yang besar di Indonesia hanya mendominasi 3 bidang penerapan, yaitu monitoring kualitas air, rantai pasok, serta manajemen dan pembiayaan budidaya. ')
df2 = pd.read_excel('Potensi AI dan IoT serta Startup.xlsx')
st.table(df2)
st.markdown('Dapat dilihat bahwa terdapat banyak sekali baris aplikasi IoT dan AI pada perikanan tangkap dan budidaya yang kosong, menandakan bahwa terdapatnya banyak peluang untuk startup lainnya untuk melengkapi dan berkontribusi.')

st.subheader("Rekomendasi")
st.markdown('Berikut ini adalah rangkuman rekomendasi dari penjelasan yang telah disampaikan:')
df3 = pd.read_excel('Rekomendasi.xlsx')
st.table(df3)