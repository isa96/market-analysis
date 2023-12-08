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

st.title('Mengapa Analisis Pasar Perikanan Indonesia?')
st.subheader('Produksi Perikanan Indonesia di Mata Dunia')
st.markdown("Indonesia merupakan negara produsen komoditas perikanan utama dunia. Dikutip dari FAO (2022), pada tahun 2020, Indonesia merupakan produsen terbesar kedua dunia untuk budidaya alga (rumput laut, dll), ketiga untuk budidaya hewan akuatik (total volume produksi 5 juta ton), dan produsen perikanan tangkap terbesar kedua dunia dengan total volume produksi 6.43 juta ton.")

col1, col2, col3 = st.columns(3)
col1.metric("Budidaya Alga", "ke-2", "27.42%")
col2.metric("Budidaya Hewan Akuatik", "ke-3", "5 juta ton")
col3.metric("Produksi Tangkapan", "ke-2", "6.43 juta ton")

st.subheader('Peranan _Startup_ Perikanan Sangat Besar dalam Mendukung Produktivitas Perikanan Budidaya Indonesia')
st.caption('~ Direktorat Jenderal Perikanan Budidaya, Kementerian Kelautan dan Perikanan')
st.markdown('Berdasarkan data yang dihimpun oleh jaringan start up bidang perikanan yang tergabung dalam Digifish Network, disebutkan setidaknya terdapat lebih dari **700 _start-up_** bidang perikanan tersebar di Indonesia.')
st.markdown('**Analisis pasar** untuk AI dan IoT dalam bidang perikanan di Indonesia perlu dilakukan untuk **mengurangi resiko bisnis**, **mengetahui ukuran dan struktur pasar**, **mengertinya tentang konsumen**, **meningkatkan efektivitas promosi**, **mengoptimalkan harga**, dan **segmentasi pasar**.')
# st.subheader('Angka Konsumsi Ikan Indonesia dan Dunia')

# st.image('AKI Dunia.png', caption='Angka Konsumsi Ikan Dunia (FAO, 2022)', width=800)

# with st.expander("Lihat wawasan penting", expanded=True):
#     st.markdown("""**Wawasan penting**""")
#     lst = ['Konsumsi Makanan Akuatik per kapita dunia cenderung meningkat tiap tahunnya.', 
#         'Konsumsi Makanan Akuatik negara-negara di benua Asia sangat tinggi dibandingkan benua lainnya.']

#     s = ''

#     for i in lst:
#         s += "- " + i + "\n"

#     st.markdown(s)

# html_temp = """<div class='tableauPlaceholder' id='viz1661221022441' style='position: relative'><noscript><a href='#'><img alt='Angka Konsumsi Ikan Indonesia, 2010-2021 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;6_&#47;6_5AngkaKonsumsiIkanIndonesiaTahunan&#47;AKITahunan&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='6_5AngkaKonsumsiIkanIndonesiaTahunan&#47;AKITahunan' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;6_&#47;6_5AngkaKonsumsiIkanIndonesiaTahunan&#47;AKITahunan&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1661221022441');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
# components.html(html_temp, width=800, height=600)

# with st.expander("Angka Konsumsi Ikan berdasarkan Provinsi", expanded=False):
#     html_temp = "<div class='tableauPlaceholder' id='viz1661221374783' style='position: relative'><noscript><a href='#'><img alt='AKI ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5_&#47;5_5AngkaKonsumsiIkanbdsProvinsi&#47;AKI&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='5_5AngkaKonsumsiIkanbdsProvinsi&#47;AKI' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5_&#47;5_5AngkaKonsumsiIkanbdsProvinsi&#47;AKI&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1661221374783');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1155px';vizElement.style.height='727px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1155px';vizElement.style.height='727px';} else { vizElement.style.width='100%';vizElement.style.height='777px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
#     components.html(html_temp, width=1155, height=700)

# with st.expander("Lihat wawasan penting", expanded=True):
#     st.markdown("""**Wawasan penting**""")
#     lst = ['Angka Konsumsi Ikan (AKI) untuk kebanyakan provinsi di Indonesia cenderung naik setiap tahunnya', 'AKI tertinggi ada pada Provinsi Maluku',
#     'Pertumbuhan AKI terkecil ada pada tahun 2019-2020.']

#     s = ''

#     for i in lst:
#         s += "- " + i + "\n"

#     st.markdown(s)

# with st.container():
#     st.markdown("""Konsumsi Makanan Akuatik cenderung naik pada semua periode. Kenaikan tersebut ada dari sekitar 7.5 kg per tahun pada tahun 1961 ke sekitar 21 kg per tahun pada tahun 2020. Konsumsi Makanan Akuatik terbesar ada pada benua Asia dan Eropa. Untuk masyarakat Indonesia, Angka Konsumsi Ikan (AKI) adalah jumlah kilogram ikan yang dikonsumsi masyarakat Indonesia selama satu tahun dalam bentuk konversi setara konsumsi ikan utuh segar . Angka Konsumsi Ikan (AKI) untuk kebanyakan provinsi di Indonesia cenderung naik setiap tahunnya, dengan konsumsi tertinggi ada hampir secara konsisten ada pada Provinsi Maluku. Sementara itu, pulau atau kepulauan yang mempunyai AKI tinggi adalah Pulau Maluku, Pulau Kalimantan, dan Pulau Sulawesi.""")
