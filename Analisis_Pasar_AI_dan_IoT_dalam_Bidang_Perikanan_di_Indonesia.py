import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd

st.set_page_config(page_title= "Analisis Pasar AI dan IoT dalam Bidang Perikanan di Indonesia", page_icon='icon.jpg',layout="wide")
st.sidebar.subheader('Analisis Pasar AI dan IoT dalam Bidang Perikanan di Indonesia')
st.sidebar.markdown(f"""
                   Analisis dilakukan berdasarkan data pada **[Statistik Kementerian Kelautan dan Perikanan (KKP)](https://statistik.kkp.go.id/)** dan **[Badan Pusat Statistik (BPS)](https://www.bps.go.id/)**.
                   \ndibuat dengan menggunakan Tableau, Excel, dan Python""")
st.sidebar.markdown('**[Adi Nugraha, 2022](https://id.linkedin.com/in/adinugraha790)**')

st.title('AI, IoT, dan Pemanfaatannya di Perikanan')
st.subheader('Kecerdasan Buatan (_Artificial Intelligence_/AI)')

st.markdown("Sistem AI (Artificial Intelligence) atau sistem kecerdasan buatan adalah ‘perangkat lunak yang dikembangkan dengan satu atau lebih teknik dan pendekatan yang tercantum dalam Lampiran I dan dapat, untuk serangkaian tujuan yang ditentukan manusia, menghasilkan **keluaran seperti konten, prediksi, rekomendasi, atau keputusan** yang mempengaruhi lingkungan tempat mereka berinteraksi’ (Proposal AIA (AI Act)).")

st.markdown("Pendekatan yang tercantum pada Lampiran I tersebut dapat digambarkan sebagai berikut:")
st.image("AI-AIA-classification.png", width=700, caption='(Fernandes-Salvador et al. 2022)')
st.caption("")
st.caption("")
st.subheader('_Internet of Things_ (IoT)')
st.markdown("IoT atau _Internet of Things_ adalah perangkat yang memiliki kemampuan untuk mentransfer data melalui jaringan dengan sangat sedikit campur tangan manusia. Terdapat tiga bagian dari IoT yaitu _things_ yang mengambil data dan mengirimnya, _things_ yang menerima data dan melakukan sesuatu dengannya, dan _things_ yang melakukan keduanya. IoT ini menghubungkan beberapa perangkat dengan internet, dan membantu interaksi antara mesin dan mesin, serta mesin dan manusia. Komponen IoT adalah sensor/perangkat, pemrosesan data, konektivitas, dan antarmuka pengguna.")

st.subheader('Pemanfaatan AI dan IoT dalam Perikanan')
st.markdown("Data dari lingkungan akan di _capture_ oleh IoT yang selanjutnya akan diakusisi dan kurasi. Setelah itu, dialirkan datanya ke sistem AI untuk diproduksi konten, rekomendasi, maupun keputusan.")

P_AO = pd.read_excel('Potensi AI dan IoT.xlsx')
st.image("Pemanfaatan.jpg", width=700)
tab1, tab2 = st.tabs(["Budidaya", "Tangkap"])

with tab1:
    st.markdown("Pemanfaatan AI dan IoT dalam Perikanan Budidaya, disarikan dari **Vo et al. (2021)**.")
    P_AO_B = P_AO[P_AO['Perikanan'] == 'Budidaya']
    P_AO_B = P_AO_B.drop('Perikanan', axis=1)
    P_AO_B.index = np.arange(1, len(P_AO_B)+1)
    st.table(P_AO_B)

with tab2:
    st.markdown("Pemanfaatan AI dan IoT dalam Perikanan Tangkap, disarikan dari **Fernandes-Salvador et al. (2022)**.")
    P_AO_T = P_AO[P_AO['Perikanan'] == 'Tangkap']
    P_AO_T = P_AO_T.drop('Perikanan', axis=1)
    P_AO_T.index = np.arange(1, len(P_AO_T)+1)
    st.table(P_AO_T)

# Akhir page
with st.expander("Referensi", expanded=True):
    st.markdown("**Literatur:**")
    lst = ['Fernandes-Salvador, J.A., Oanta, G.A., Olivert-Amado, A., Goienetxea, I., Ibaibarriaga, L., Aranda, M., Cuende, E., Foti, G., Olabarrieta, I., Murua, J., Prellezo, R., Iñarra, B., Quincoces, I., Caballero, A., SobrinoHeredia, J. M, 2022, Research for PECH Committee – _Artificial Intelligence and the fisheries sector_, European Parliament, Policy Department for Structural and Cohesion Policies, Brussels.', 
        'Vo, T.T.E., Ko, H., Huh, J.-H., Kim, Y. Overview of Smart Aquaculture System: Focusing on Applications of Machine Learning and Computer Vision. _Electronics_ 2021, 10, 2882.  https://doi.org/10.3390/electronics10222882']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)
