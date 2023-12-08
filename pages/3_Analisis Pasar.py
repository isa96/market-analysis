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

st.title('Analisis Potensi Pasar')
st.subheader("Volume Produksi berdasarkan Komoditas Perikanan")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Budidaya")
    html_temp="""<div class='tableauPlaceholder' id='viz1661273336354' style='position: relative'><noscript><a href='#'><img alt='VolProdKomd ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;4_&#47;4_2_1VolumeProduksiBudidayaberdasarkanKomoditas&#47;VolProdKomd&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='4_2_1VolumeProduksiBudidayaberdasarkanKomoditas&#47;VolProdKomd' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;4_&#47;4_2_1VolumeProduksiBudidayaberdasarkanKomoditas&#47;VolProdKomd&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1661273336354');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1155px';vizElement.style.height='559px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1155px';vizElement.style.height='559px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(html_temp, width=638, height=338)

with col2:
    st.subheader("Tangkap")
    html_temp="""<div class='tableauPlaceholder' id='viz1661281426501' style='position: relative'><noscript><a href='#'><img alt='VolProdKomd ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;4_&#47;4_2_2VolumeProduksiTangkapLautberdasarkanKomoditas&#47;VolProdKomd&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='4_2_2VolumeProduksiTangkapLautberdasarkanKomoditas&#47;VolProdKomd' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;4_&#47;4_2_2VolumeProduksiTangkapLautberdasarkanKomoditas&#47;VolProdKomd&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1661281426501');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1155px';vizElement.style.height='559px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1155px';vizElement.style.height='559px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(html_temp, width=638, height=338)
    html_temp="""<div class='tableauPlaceholder' id='viz1661281482728' style='position: relative'><noscript><a href='#'><img alt='VolProdKomd ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;4_&#47;4_2_3VolumeProduksiTangkapPUDberdasarkanKomoditas&#47;VolProdKomd&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='4_2_3VolumeProduksiTangkapPUDberdasarkanKomoditas&#47;VolProdKomd' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;4_&#47;4_2_3VolumeProduksiTangkapPUDberdasarkanKomoditas&#47;VolProdKomd&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1661281482728');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1155px';vizElement.style.height='559px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1155px';vizElement.style.height='559px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(html_temp, width=638, height=338)

with st.container():
    st.markdown("""**Asumsi**""")
    st.image('Volume.png')

with st.expander("Asumsi: ketika produksi meningkat, maka akan semakin banyak aktivitas perikanannya dan semakin banyak IoT dan layanan AI yang akan dipakai.", expanded=True):
    st.markdown("""**Wawasan penting**""")
    lst = ['Rumput laut adalah komoditas budidaya dengan produksi terbesar dibandingkan dengan komoditas lain dan jenis usaha lainnya, bahkan menyusun hingga lebih dari 50% total volume produksi', 
        'Komoditas dengan volume produksi total terbanyak jenis usaha budidaya setelah rumput laut adalah ikan nila, lele, udang, bandeng',
        'Komoditas dengan volume produksi total terbanyak jenis usaha tangkap laut adalah tongkol, layang, cakalang, kembung',
        'Komoditas dengan volume produksi total terbanyak jenis usaha tangkap PUD (Perairan Umum Daratan) adalah gabus, nila, dan patin.']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

st.markdown('Komoditas dengan volume produksi terbesar total di semua jenis usaha adalah rumput laut, yang produksinya hingga mencapai 11.05 juta ton pada tahun 2016. Volumenya sangat besar bahkan dapat mencapai lebih dari 50% total volume produksi. Selain rumput laut, yang memiliki volume produksi terbesar pada jenis usaha budidaya adalah ikan nila (1.172.616 ton), ikan lele (993.749 ton), udang (881.581 ton), dan ikan bandeng (811.870 ton), ikan mas (560.651 ton), dan ikan patin (327.129 ton).')
st.markdown('Komoditas yang memiliki volume produksi total terbanyak pada jenis usaha tangkap laut adalah ikan tongkol (581.057 ton), ikan layang (548.645 ton), ikan cakalang (468.258 ton), ikan tuna (300.791 ton) dan ikan kakap (292.531 ton).')
st.markdown('Komoditas yang memiliki volume produksi total terbanyak pada jenis usaha tangkap perairan umum daratan (PUD) adalah ikan nila (57.849 ton), ikan patin (53.088 ton), dan ikan gabus (59.510 ton).')

st.subheader("Volume Produksi dan Nilai Produksi per Volume berdasarkan Komoditas Perikanan dan Provinsi")

html_temp = """<div class='tableauPlaceholder' id='viz1661754624566' style='position: relative'><noscript><a href='#'><img alt='Dashboard 2 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;2_&#47;2_4VolumeProduksidanNilaiperVolumenya&#47;Dashboard2&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='2_4VolumeProduksidanNilaiperVolumenya&#47;Dashboard2' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;2_&#47;2_4VolumeProduksidanNilaiperVolumenya&#47;Dashboard2&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1661754624566');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='935px';vizElement.style.height='527px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='935px';vizElement.style.height='527px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=935, height=500)

st.caption('')

with st.expander('Volume Produksi berdasarkan Provinsi dan Komoditas', expanded=False):
    html_temp = """<div class='tableauPlaceholder' id='viz1659568823662' style='position: relative'><noscript><a href='#'><img alt='VolProdKom2020 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;3_&#47;3_1VolumeProduksiKomditasberdasarkanProvinsi&#47;VolProdKom2020_1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='3_1VolumeProduksiKomditasberdasarkanProvinsi&#47;VolProdKom2020_1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;3_&#47;3_1VolumeProduksiKomditasberdasarkanProvinsi&#47;VolProdKom2020_1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1659568823662');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(html_temp, width=1200, height=900)

# with st.expander("Lihat wawasan penting", expanded=True):
#     st.markdown("""**Wawasan penting**""")
#     lst = ['Komoditas yang diproduksi terbanyak dengan usaha budidaya adalah ikan nila, mas, dan lele.', 
#         'Nilai produksi cenderung sebanding dengan total produksinya untuk kebanyakan spesies']

#     s = ''

#     for i in lst:
#         s += "- " + i + "\n"

#     st.markdown(s)


# st.subheader("Nilai Produksi berdasarkan Komoditas Perikanan dan Provinsi")

# html_temp="""<div class='tableauPlaceholder' id='viz1661274109504' style='position: relative'><noscript><a href='#'><img alt='Dashboard 2 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;2_&#47;2_3_1NilaiProduksiBudidayabdsKomoditasProvinsi&#47;Dashboard2&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='2_3_1NilaiProduksiBudidayabdsKomoditasProvinsi&#47;Dashboard2' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;2_&#47;2_3_1NilaiProduksiBudidayabdsKomoditasProvinsi&#47;Dashboard2&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1661274109504');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1130px';vizElement.style.height='559px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1130px';vizElement.style.height='559px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
# components.html(html_temp, width=1200, height=582)
with st.container():
    st.markdown("""**Asumsi**""")
    st.image('Nilai per Volume.png')

with st.expander("Asumsi: ketika nilai per volume komoditas tinggi dan produksinya tinggi, maka akan semakin mungkin dan mampu untuk memakai jasa AI dan membeli IoT.", expanded=True):
    st.markdown("""**Wawasan penting**""")
    lst = ['Komoditas yang diproduksi terbanyak namun dengan nilai produksi kecil adalah rumput laut', 
        'Udang, bandeng, mas, nila dan lele adalah komoditas yang nilainya cenderung besar meskipun diproduksi tidak sebanyak rumput laut',
        'Ikan kerapu, kakap, bawal, dan lobster adalah komoditas bernilai per volume tinggi']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)
st.subheader("Pertumbuhan Tahunan Produksi Perikanan")

col1, col2 = st.columns(2)
with col1:
    html_temp="""<div class='tableauPlaceholder' id='viz1661755832440' style='position: relative'><noscript><a href='#'><img alt='AnnualGwthD ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;4_&#47;4_1_1AnnualGrowthBudidayabyPulau&#47;AnnualGwthD&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='4_1_1AnnualGrowthBudidayabyPulau&#47;AnnualGwthD' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;4_&#47;4_1_1AnnualGrowthBudidayabyPulau&#47;AnnualGwthD&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1661755832440');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='550px';vizElement.style.height='659px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='550px';vizElement.style.height='659px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(html_temp, width=550, height=720)
with col2:
    html_temp="""<div class='tableauPlaceholder' id='viz1661285836493' style='position: relative'><noscript><a href='#'><img alt='Dashboard 2 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;4_&#47;4_1_2AnnualGrowthTangkapbyPulau&#47;Dashboard2&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='4_1_2AnnualGrowthTangkapbyPulau&#47;Dashboard2' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;4_&#47;4_1_2AnnualGrowthTangkapbyPulau&#47;Dashboard2&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1661285836493');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='600px';vizElement.style.height='587px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='600px';vizElement.style.height='587px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(html_temp, width=550, height=720)

st.caption('')
with st.container():
    st.markdown("""**Asumsi**""")
    st.image('Annual Growth.png')

with st.expander("Asumsi: semakin stabil atau menaiknya produksi, maka akan semakin tumbuh pula kuantitas jasa AI dan IoT yang dibeli.", expanded=True):
    st.markdown("""**Wawasan penting**""")
    lst = ['Pulau yang stabil pertumbuhan total produksi perikanan budidayanya adalah Pulau Jawa, Kalimantan dan Sulawesi',
    'Pulau yang stabil pertumbuhan total produksi perikanan tangkapnya adalah Pulau Jawa, Kalimantan dan Sulawesi',
    'Pulau/kepulauan dengan pertumbuhan total produksi perikanan budidaya tertinggi adalah Kepulauan Maluku dengan pertumbuhan tertinggi sebesar 2.509%.', 
        'Kepulauan Nusa Tenggara dan Pulau Papua adalah yang tertinggi pertumbuhan total produksi perikanan budidayanya setelah Kepulauan Maluku.']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

st.markdown('Kepulauan Maluku memiliki pertumbuhan yang sangat besar pada tahun 2002 dan 2004 seperti yang sudah disebutkan di atas. Meskipun sempat menurun tajam, Kepulauan Maluku juga mengalami kenaikan yang tinggi sebesar 331% pada tahun 2007, 484% pada tahun 2010, dan 108% pada tahun 2011. Walaupun begitu, fluktuasi meningkat dan menurun terjadi pada tahun setelahnya dan pada tahun 2020 mengalami penurunan sebesar 60%.')
st.markdown('Kepulauan Nusa Tenggara juga mengalami kenaikan total produksi perikanan budidaya yang pesat pada tahun 2004 (885%), 2005 (75%), dan 2006 (50%). Setelah tahun tersebut umumnya terjadi fluktuasi, dengan pengecualian pada tahun 2013 (147%). Sedangkan di Pulau Papua umumnya mengalami fluktuasi total produksi perikanan budidaya pada rentang 2001-2020, dengan kenaikan cukup hebat terjadi pada tahun 2002 (96%), 2005 (118%), dan 2008 (186%).')
st.markdown('Pertumbuhan di pulau-pulau lainnya tidak menyimpang dari 100%, Seperti di Pulau Jawa misalnya, pertumbuhan total produksi perikanan budidaya ada pada tahun 2002 (54%) dan 2010 (40%). Selain tahun tersebut, fluktuasi pertumbuhan total produksi perikanan budidaya berada di kisaran -24% hingga 33%. Pada pertumbuhan total produksi perikanan budidaya di Pulau Kalimantan, umumnya hanya terjadi kenaikan total produksi perikanan budidaya, kenaikan tertinggi ada pada tahun 2007 (85%). Sementara itu, penurunan total produksi perikanan budidaya (atau persentase negatif) terjadi pada tahun 2006 (-30%), dan 2019 (-13%).')
st.markdown('Selain pulau dan kepulauan yang telah disebutkan, ada Pulau Sulawesi dan Sumatera. Pertumbuhan total produksi perikanan budidaya di Pulau Sulawesi cenderung positif atau terjadi kenaikan atau stagnasi total produksi perikanan budidaya pada rentang tahun 2001-2017. Pertumbuhan tertinggi ada pada tahun 2004 (70%) dan 2005 (79%). Sementara itu, pertumbuhan total produksi perikanan budidaya di Pulau Sumatera cenderung positif, dengan penurunan terjadi pada tahun 2004 (-24%) dan 2020 (-12%). Pertumbuhan maksimal total produksi perikanan budidaya ada pada tahun 2002 (89%).')

# st.subheader("Jumlah Populasi Pembudidaya")

# html_temp="""<div class='tableauPlaceholder' id='viz1661275640302' style='position: relative'><noscript><a href='#'><img alt='N&amp;PBD ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5_&#47;5_2_2JumlahPembudidayabdsProvinsi&#47;NPBD&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='5_2_2JumlahPembudidayabdsProvinsi&#47;NPBD' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5_&#47;5_2_2JumlahPembudidayabdsProvinsi&#47;NPBD&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1661275640302');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1155px';vizElement.style.height='659px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1155px';vizElement.style.height='659px';} else { vizElement.style.width='100%';vizElement.style.height='777px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
# components.html(html_temp, width=1165, height=638)
# st.caption('')
# with st.expander("Lihat wawasan penting", expanded=True):
#     st.markdown("""**Wawasan penting**""")
#     lst = ['Populasi tertinggi cenderung ada pada Provinsi Jawa Barat, Jawa Tengah dan Jawa Timur, serta beberapa bagian Pulau Sumatera', 
#         'Pembudidaya populasinya cenderung menurun dan dapat berfluktuasi tajam']

#     s = ''

#     for i in lst:
#         s += "- " + i + "\n"

#     st.markdown(s)

# st.markdown('Dalam fluktuasi populasi pembudidaya, populasi terbanyak cenderung ada pada 3 provinsi yaitu Jawa Barat, Jawa Tengah, dan Jawa Timur, lalu diikuti dengan Pulau Sumatera. ')
# st.markdown('Fluktuasi populasi ini diikuti penurunan ketika mendekati tahun 2020.')
# st.markdown('Pada kebanyakan provinsi, pembudidaya cenderung lebih banyak daripada nelayan laut dan nelayan PUD. Namun, jumlah pembudidaya di setiap provinsi dapat fluktuasi dengan cukup tajam. Ini terdapat kemungkinan bahwa terjadinya usaha pembudidaya baru untuk melakukan kegiatan budidaya, namun karena terjadinya kerugian ataupun modal yang tidak cukup sehingga usaha dihentikan. Pola terjadinya fluktuasi tersebut berbeda-beda tiap provinsi. ')
# st.markdown('Kenaikan yang tajam ini terjadi contohnya pada provinsi Jawa Barat dan Jawa Tengah, pada tahun 2012, pembudidaya pada Provinsi Jawa Barat sangat tinggi, namun ketika tahun 2015 menjadi sangat kecil. Kenaikan yang tajam ini juga terjadi pada tahun 2018, dengan penurunan kembali pada tahun selanjutnya. Menariknya bersamaan dengan kenaikan tersebut, pembudidaya di provinsi lain cenderung turun.')

st.subheader("Jumlah Rumah Tangga Perikanan (RTP)")

html_temp="""<div class='tableauPlaceholder' id='viz1661756085291' style='position: relative'><noscript><a href='#'><img alt='JRTP ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5_&#47;5_3JumlahRumahTanggaPerikananbdsProvinsi&#47;JRTP&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='5_3JumlahRumahTanggaPerikananbdsProvinsi&#47;JRTP' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5_&#47;5_3JumlahRumahTanggaPerikananbdsProvinsi&#47;JRTP&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1661756085291');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1135px';vizElement.style.height='665px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1135px';vizElement.style.height='665px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=1165, height=638)

html_temp="""<div class='tableauPlaceholder' id='viz1661756182382' style='position: relative'><noscript><a href='#'><img alt='JRTP Tangkap ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5_&#47;5_3_2JRTPTangkap&#47;JRTPTangkap&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='5_3_2JRTPTangkap&#47;JRTPTangkap' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5_&#47;5_3_2JRTPTangkap&#47;JRTPTangkap&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1661756182382');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1150px';vizElement.style.height='609px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1150px';vizElement.style.height='609px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=1165, height=638)

with st.container():
    st.markdown("""**Asumsi**""")
    st.image('JRTP.png')

st.caption('')
with st.expander("Asumsi: semakin banyak RTPnya (unit usaha), maka akan semakin banyak jasa AI dan IoT yang dibeli.", expanded=True):
    st.markdown("""**Wawasan penting**""")
    lst = ['Jumlah RTP Budidaya Darat (air tawar dan payau) mengalami peningkatan, dengan provinsi yang mendominasi adalah Jawa Tengah, Jawa Barat, dan Jawa Timur', 
        'Jumlah RTP Budidaya Laut cenderung naik, dengan provinsi yang JRTPnya tinggi adalah Sulawesi Selatan, Nusa Tenggara Barat, dan Sulawesi Tenggara yang mendominasi',
        'Jumlah RTP Tangkap Laut cenderung berfluktuasi, provinsi yang JRTPnya tinggi adalah Jawa Tengah, Kalimantan Selatan, dan Maluku',
        'Jumlah RTP Tangkap PUD cenderung berfluktuasi, provinsi yang JRTPnya tinggi adalah Sulawesi Selatan, Jawa Tengah, dan Kalimantan Timur']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

st.markdown('Definisi Rumah Tangga Perikanan menurut Badan Pusat Statistik adalah unit usaha yang melakukan kegiatan penangkapan/budidaya ikan/binatang air lainnya/tanaman air dengan tujuan sebagian/seluruh hasilnya untuk dijual.')
st.markdown('Jumlah Rumah Tangga Perikanan (JRTP) Budidaya Darat pada tahun 2000, yang mendominasi adalah Banten, Jawa Barat, dan Yogyakarta. Namun mulai dari tahun 2004 hingga seterusnya yang mendominasi adalah Jawa Barat, Jawa Tengah, dan Jawa Timur. Untuk kebanyakan provinsi, JRTP Budidaya Darat ini cenderung naik dibandingkan dengan tahun 2000.')
st.markdown('JRTP Budidaya Laut sangat rendah pada tahun 2000, namun seiring waktu berjalan kebanyakan provinsi cenderung naik JRTP Budidaya Lautnya. Provinsi yang mempunyai JRTP Budidaya Laut tinggi pada tahun 2014 adalah Sulawesi Tengah, Tenggara dan Selatan, Nusa Tenggara Barat, dan Jateng. Setelah itu, pada tahun 2016 pulau Sulawesi, Jawa Barat, Jawa Tengah, dan Jawa Timur serta Nusa Tenggara Barat merupakan daerah yang mendominasi.')


st.subheader("Luas Usaha Budidaya")

html_temp="""<div class='tableauPlaceholder' id='viz1661277170234' style='position: relative'><noscript><a href='#'><img alt='LUB&amp;ProdBD ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5_&#47;5_4LuasUsahadanProduksiBudidayabdsJenisnya&#47;LUBProdBD&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='5_4LuasUsahadanProduksiBudidayabdsJenisnya&#47;LUBProdBD' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5_&#47;5_4LuasUsahadanProduksiBudidayabdsJenisnya&#47;LUBProdBD&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1661277170234');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1155px';vizElement.style.height='659px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1155px';vizElement.style.height='659px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=1165, height=638)
with st.container():
    st.markdown("""**Asumsi**""")
    st.image('Luas Usaha.png')

st.caption('')
with st.expander("Asumsi: semakin luas usaha dan produksi budidayanya, maka akan semakin berpotensinya jasa AI dan IoT yang akan dipakai.", expanded=True):
    st.markdown("""**Wawasan penting**""")
    lst = ['Budidaya Laut memiliki produksi dan luas usaha tertinggi, setelah itu kolam dan tambak',
        'Luas usaha kolam dan sawah cenderung berfluktuasi dan trennya tidak begitu meningkat, namun produksinya yang meningkat', 
        'Luas usaha keramba, tambak, dan budidaya laut cenderung mengalami tren meningkat, dan produksinya pun cenderung meningkat',
        'Luas usaha budidaya jaring apung dan jaring tancap bertambah,namun terdapat penurunan pada produksi budidaya jaring apung (2016) dan produksi budidaya jaring tancap (2015)']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

st.markdown('Luas usaha kolam dan sawah cenderung berfluktuasi dan trennya tidak begitu meningkat, namun produksinya yang meningkat. Ini dapat terjadi karena penggunaan sistem budidaya yang lebih baik, seperti biofloc dibanding budidaya konvensional, atau intensifikasi terjadi misalnya dengan penggunaan metode recirculating aquaculture system (RAS) atau dengan penggunaan nanobubble.')
st.markdown('Luas usaha keramba, tambak, dan budidaya laut cenderung mengalami tren meningkat, dan produksinya pun cenderung meningkat. Ini terjadi karena perluasan usaha budidaya laut cenderung sebanding dengan peningkatan produksinya.')
st.markdown('Luas usaha budidaya jaring apung dan jaring tancap memiliki anomali, karena ketika luas usaha bertambah, terdapat penurunan pada produksi budidaya jaring apung (2016) dan produksi budidaya jaring tancap (2015). Ini dapat terjadi karena kualitas air yang buruk karena mengandalkan perairan terbuka untuk usaha budidayanya, atau terdapat penyakit dan atau mikroorganisme yang menyebabkan kematian massal dan menurunnya produksi komoditas di kedua jenis usaha tersebut.')


st.subheader("Luas Usaha berdasarkan Subsektor Budidaya")

html_temp="""<div class='tableauPlaceholder' id='viz1661281108026' style='position: relative'><noscript><a href='#'><img alt='Luas Usaha ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;6_&#47;6_1LuasUsahaBudidayabdsSubsektor&#47;LuasUsaha&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='6_1LuasUsahaBudidayabdsSubsektor&#47;LuasUsaha' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;6_&#47;6_1LuasUsahaBudidayabdsSubsektor&#47;LuasUsaha&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1661281108026');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1124px';vizElement.style.height='659px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1124px';vizElement.style.height='659px';} else { vizElement.style.width='100%';vizElement.style.height='827px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=1165, height=638)
st.caption('')
with st.expander("Grafik ini digunakan untuk memetakan setiap subsektor budidaya dalam provinsi. Klik pada subsektor budidaya untuk distribusi spesifik luas usaha masing-masing subsektor.", expanded=True):
    st.markdown("""**Wawasan penting**""")
    lst = ['Secara konsisten, luas usaha budidaya tambak paling luas dibandingkan dengan subsektor budidaya lainnya, diikuti oleh budidaya laut, dan kolam',         'Provinsi dengan luas usaha tambak tertinggi adalah Sulawesi Selatan, Kalimantan Timur, dan Jawa Barat',
        'Provinsi dengan luas usaha budidaya laut tertinggi adalah  Jawa Timur, Sulawesi Selatan, dan Sulawesi Tengah',
        'Provinsi dengan luas usaha kolam tertinggi adalah Jawa Barat, Sumatera Selatan, dan Jawa Timur',
        'Pada tahun 2010, terdapat penyusutan luas kolamsecara drastis di Kalimantan Barat dan Kepulauan Riau',
        'Pada tahun 2013, terdapat kenaikan drastis luas budidaya laut di Jawa Timur']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

st.markdown('Luas usaha budidaya umumnya akan sebanding dengan jumlah individu benih hewan yang disebar, volume produksi panen, dan seberapa banyak perangkat IoT yang dibutuhkan. Luas usaha budidaya subsektor tambak, budidaya laut, dan kolam adalah yang paling luas. Dengan luas tambak tertinggi ada pada provinsi Kalimantan Timur, Sulawesi Selatan, Jawa Barat, Jawa Tengah, dan Jawa Timur. Provinsi yang memiliki luas usaha budidaya laut tertinggi adalah Jawa Timur, Pulau Sulawesi, dan Nusa Tenggara. Subsektor budidaya kolam memiliki luas tertinggi pada Provinsi Jawa Barat, Jawa Timur, Sumatera Barat, Sumatera Selatan dan Sumatera Utara. Sementara itu, subsektor dengan luas tertinggi keempat adalah sawah/minapadi yang mempunyai luas tertinggi di Jawa Barat dan Jawa Timur. Subsektor keramba memiliki luas tertinggi di Kalimantan Tengah dan Lampung. Subsektor jaring apung memiliki luas tertinggi di Jawa Barat, Lampung, dan Jawa Timur.')

# st.subheader("Produksi dan Nilai Produksi berdasarkan Subsektor Budidaya")

# html_temp="""<div class='tableauPlaceholder' id='viz1661281145013' style='position: relative'><noscript><a href='#'><img alt='Produksi &amp; Nilai ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;6_&#47;6_2ProduksidanNilaiBudidayaberdasarkanSubsektor&#47;ProduksiNilai&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='6_2ProduksidanNilaiBudidayaberdasarkanSubsektor&#47;ProduksiNilai' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;6_&#47;6_2ProduksidanNilaiBudidayaberdasarkanSubsektor&#47;ProduksiNilai&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1661281145013');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1149px';vizElement.style.height='659px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1149px';vizElement.style.height='659px';} else { vizElement.style.width='100%';vizElement.style.height='777px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
# components.html(html_temp, width=1165, height=638)
# st.caption('')
# with st.expander("Asumsi: semakin tinggi nilai per volume, semakin _favorable_ suatu subsektor untuk suatu jasa AI dan IoT.", expanded=True):
#     st.markdown("""**Wawasan penting**""")
#     lst = ['Tambak semi-intensif, kolam air tenang, tambak sederhana dan jaring apung laut mempunyai perbandingan antara nilai:volume dan produksi yang tinggi dibandingkan dengan jenis budidaya lainnya', 
#         'Rumput laut mempunyai perbandingan nilai:volume yang rendah meskipun produksinya tinggi',
#         'Tambak intensif memiliki produksi tertinggi di Jawa Timur, dan terdapat produksi di Aceh, Jawa Barat, Jawa Tengah, Sulawesi Barat dan Sulawesi Selatan']

#     s = ''

#     for i in lst:
#         s += "- " + i + "\n"

#     st.markdown(s)

# st.markdown('Perbandingan diantara nilai dan volume produksinya memberikan gambaran seberapa bernilainya komoditas-komoditas yang dihasilkan oleh subsektor perikanan budidaya tersebut. Diharapkan informasi ini membantu dalam prioritisasi pembuatan produk dan pemasaran.')
# st.markdown('Ketika dibandingkan secara kualitatif pada grafik, tambak semi-intensif, kolam air tenang, tambak sederhana dan jaring apung laut mempunyai perbandingan antara nilai:volume dan produksi yang tinggi dibandingkan dengan jenis budidaya lainnya. Tambak semi-intensif produksinya banyak di Jawa Barat, Jawa Timur, NTB, dan Sulawesi Tenggara. Jenis budidaya dengan kolam air tenang memiliki produksi terbanyak di Jawa Barat, Jawa Timur, Sumatera Selatan, dan Jawa Tengah. Tambak sederhana memiliki produksi terbanyak di Sulawesi Selatan dan Jawa Timur. Jaring apung laut memiliki produksi terbanyak di Kepulauan Riau, Sumatera Utara dan Maluku. Sementara itu, rumput laut mempunyai perbandingan nilai:volume yang rendah meskipun produksinya tinggi. Tambak intensif yang mewajibkan pembudidaya memiliki modal yang besar sangat jarang adanya, tercatat di Indonesia hanya ada pada 7 provinsi saja, dengan produksi terbanyak ada di Jawa Timur.')



st.subheader("Produksi berdasarkan Jenis Kegiatan Budidaya")

html_temp="""<div class='tableauPlaceholder' id='viz1661281028495' style='position: relative'><noscript><a href='#'><img alt='Jenis Kegiatan ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;6_&#47;6_3ProduksiberdasarkanJenisKegiatan&#47;JenisKegiatan&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='6_3ProduksiberdasarkanJenisKegiatan&#47;JenisKegiatan' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;6_&#47;6_3ProduksiberdasarkanJenisKegiatan&#47;JenisKegiatan&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1661281028495');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1150px';vizElement.style.height='927px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1150px';vizElement.style.height='927px';} else { vizElement.style.width='100%';vizElement.style.height='1127px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=1165, height=600)
with st.container():
    st.markdown("""**Asumsi**""")
    st.image('Jenis Kegiatan.png')

st.caption('')
with st.expander("Asumsi: semakin besar produksi kegiatan budidaya, maka akan semakin banyak dibutuhkan jasa AI dan IoTnya.", expanded=True):
    st.markdown("""**Wawasan penting**""")
    lst = ['Usaha Pembesaran memiliki konsentrasi tertinggi di Sulawesi Selatan yang komoditas tertingginya rumput laut', 
        'Provinsi dengan usaha pembesaran tertinggi setelah Sulawesi Selatan adalah Nusa Tenggara Barat, Nusa Tenggara Timur, Jawa Barat, Jawa Timur, Sulawesi Tengah dan Sulawesi Tenggara',
        'Provinsi dengan usaha pembenihan tertinggi yang konsisten pada tahun 2017-2019 adalah Jawa Barat, Sumatera Utara, dan Jawa Timur']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

st.markdown('')
st.markdown('')

st.subheader("Jumlah Kapal Tangkap dan Produksinya")

html_temp="""<div class='tableauPlaceholder' id='viz1661284980653' style='position: relative'><noscript><a href='#'><img alt='KPLPRODT ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5_&#47;5_6JumlahKapalTangkapIkandanProduksinya&#47;KPLPRODT&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='5_6JumlahKapalTangkapIkandanProduksinya&#47;KPLPRODT' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5_&#47;5_6JumlahKapalTangkapIkandanProduksinya&#47;KPLPRODT&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1661284980653');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1149px';vizElement.style.height='559px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1149px';vizElement.style.height='559px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=1150, height=532)

with st.container():
    st.markdown("""**Asumsi**""")
    st.image('Jumlah Kapal dan Produksinya.png')

html_temp="<div class='tableauPlaceholder' id='viz1661758122505' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;7_&#47;7_1JumlahKapalTangkap&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='7_1JumlahKapalTangkap&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;7_&#47;7_1JumlahKapalTangkap&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1661758122505');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
components.html(html_temp, width=700, height=482)

with st.container():
    st.markdown("""**Asumsi**""")
    st.image('Jumlah Kapal.png')

with st.expander("Asumsi: semakin banyak unit kapalnya pada suatu jenis usaha dan provinsi, semakin dibutuhkan jasa AI dan IoTnya.", expanded=True):
    st.markdown("""**Wawasan penting**""")
    lst = ['Jumlah perahu perikanan tangkap laut cenderung menurun, namun produksi perikanan tangkapnya naik', 
        'Jumlah perahu untuk perikanan tangkap darat juga berfluktuasi cenderung stabil, namun untuk produksi perikanan tangkap daratnya cenderung naik',
        'Jawa Barat, Jawa Timur, dan Sumatera Utara adalah provinsi dengan kapal motor terbanyak',
        'Jawa Timur, Kalimantan Timur, dan Sulawesi Tenggara adalah provinsi dengan jenis kapal motor tempel terbanyak',
        'Maluku, Sumatera Selatan, dan Nusa Tenggara Timur adalah provinsi dengan jenis kapal tanpa motor terbanyak']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

st.markdown('Jumlah perahu untuk perikanan tangkap laut berfluktuasi cenderung menurun, namun produksi perikanan tangkapnya naik. Jumlah perahu untuk perikanan tangkap darat juga berfluktuasi cenderung stabil, namun untuk produksi perikanan tangkap daratnya cenderung naik. Kedua tren ini dapat terjadi karena manajemen dan monitor WPP yang baik, atau karena total produksinya belum memenuhi Maximum Sustainable Yield, ataupun meningkatnya kualitas manajemen penangkapan ikan.')
st.markdown('Dilihat dari _value_nya, perahu motor memiliki lebih _value_ dibandingkan dengan perahu motor tempel, dan perahu motor tempel memiliki _value_ yang lebih tinggi dibandingkan perahu tanpa motor. Karena itu, dapat dilihat bahwa akan lebih baik untuk mentargetkan konsumen di kapal motor terlebih dahulu lalu kapal motor tempel, dengan anggapan bahwa unit usaha yang memiliki kapal motor lebih mampu untuk membeli jasa AI dan IoT.')

st.subheader("Wilayah Pengelolaan Perikanan dan Tingkat Pemanfaatannya")

st.image('wpp.png')

html_temp="""<div class='tableauPlaceholder' id='viz1661285123760' style='position: relative'><noscript><a href='#'><img alt='TPKomoditas ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;4_&#47;4_4TingkatPemanfaatanKomoditasdiWPP&#47;TPKomoditas_1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='4_4TingkatPemanfaatanKomoditasdiWPP&#47;TPKomoditas_1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;4_&#47;4_4TingkatPemanfaatanKomoditasdiWPP&#47;TPKomoditas_1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1661285123760');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='750px';vizElement.style.height='1102px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='750px';vizElement.style.height='1102px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=1200, height=500)

with st.container():
    st.markdown("""**Asumsi**""")
    st.image('WPPi.png')

with st.expander("Asumsi: semakin banyak komoditas yang overfishing statusnya dan di bawah fully exploited, maka akan semakin banyak dibutuhkan jasa AI dan IoT untuk pengawasan dan optimisasinya.", expanded=True):
    st.markdown("""**Wawasan penting**""")
    lst = ['WPP 571, 572, dan 714 mengalami penambahan komoditas yang statusnya _over-exploited_', 
        'WPP 573, 711, 712, 713, 715, 716, dan 717 mengalami penurunan komoditas yang statusnya _over-exploited_',
        'Ikan karang dan lobster pada WPP 573 mempunyai status pemanfaatan yang sangat _over-exploited_']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

st.markdown('Wilayah Pengelolaan Perikanan Negara Republik Indonesia adalah wilayah pengelolaan perikanan untuk penangkapan ikan, pembudidayaan ikan, konservasi, penelitian, dan pengembangan perikanan yang meliputi perairan pedalaman, perairan kepulauan, laut territorial, zona tambahan, dan zona ekonomi eksklusif, dikutip dari Peraturan Menteri Kelautan dan Perikanan RI No. 18/2014. Pada grafik adalah Tingkat Pemanfaatan Komoditas Ikan berdasarkan Keputusan Menteri Kelautan dan Perikanan No. 50/2017 dan No. 19/2022.')
st.markdown('Tingkat pemanfaatan adalah suatu indikator yang menunjukkan tingkat termanfaatkannya suatu komoditas di Wilayah Pengelolaan Perikanan (WPP) di Indonesia. Ketika tingkat pemanfaatannya kurang dari 0.5, maka penangkapannya boleh ditambah. Mengutip keputusan Menteri di atas, ketika tingkat pemanfaatannya antara 0.5 dan 1, maka komoditas tersebut sudah _fully exploited_ dan penangkapannya perlu dimonitor ketat. Sedangkan ketika tingkat pemanfaatannya lebih dari 1, berarti komoditas tersebut _over-exploited_ dan upaya penangkapan harus dikurangi.')
st.markdown('Pada WPP 571, WPP572, dan WPP714 terdapat masing-masing 5, 5, 3 komoditas yang statusnya _over-exploited_ berdasarkan Kepmen KP No.19/2022, bertambah dari masing-masing 2, 1, 2 komoditas pada Kepmen KP No.50/2017. Berbeda dengan WPP yang baru saja disebutkan, WPP573, 711, 712, 713, 715, 716, dan 717 mengalami penurunan jumlah komoditas yang mempunyai status _over-exploited_ dari Kepmen KP No.50/2017 ke Kepmen KP No.19/2022. Namun perlu diingat bahwa WPP 573 dan WPP 711 mempunyai komoditas dengan tingkat pemanfaatan mendekati dan melebihi 2. Untuk WPP 573 adalah ikan karang (2), dan lobster (2.5), sedangkan untuk WPP 711 adalah kepiting (1.9).')
