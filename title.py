import streamlit as st
import pandas as pd
st.set_page_config(page_title="Zakaria Mostafa",layout='wide',initial_sidebar_state='expanded')

st.title("welcome To My Page :heart_eyes:")


st.sidebar.title("[ZAKARIA MOSTAFA MOHAMED ](https://www.linkedin.com/in/zakaria-mostafa/)")
st.sidebar.subheader("DATA SCIENCE & ANALYTICS  :bar_chart:")


st.sidebar.image('sidebar.jpg')



st.sidebar.write("")

st.sidebar.subheader("MY RECENT WORK ") 


bu = st.sidebar.button("Submit")

if bu:
    st.sidebar.write("Dasboard  (https://tip-dashboard.streamlit.app/)")
    st.sidebar.write("Dasboard Kiva (https://kivagy.streamlit.app/)")




st.sidebar.subheader('Addres :house: Abu Dhabi ')



st.subheader('CV')
st.subheader('ـــــــــــــــــــــــــ')

st.image('cv-Zakaria.jpg')



  
st.subheader("CERTIFICATES")
st.subheader('ــــــــــــــــــــــــــــــــ')

a1,a2 = st.columns(2)

#cert
a1.image("power bi.jpg")
a1.image("power bi2.jpg")
a1.image("Analysis.jpg")

a2.image("oracle.jpg")
a2.image("zakaria.png")
a2.image("database_sql_python.jpg")
bt1 = st.sidebar.button("About")



if bt1:
    st.subheader(' Meet Zakaria Mustafa')
    st.text('''
        In the fast-paced world of data analytics, professionals who possess a diverse skill set
        and a passion for uncovering insights are in high demand. One such individual who has 
        risen to prominence in the field is Zakaria Mustafa. As a seasoned data analyst, Zakaria 
        combines his expertise in Excel, Power BI, SQL, and Python to turn raw data into 
        actionable insights that drive strategic decision-making.
        ''')
    st.subheader('Excel: The Foundation of Data Analysis')
    st.text(''' 
Zakaria's journey as a data analyst began with Microsoft Excel, a widely-used 
spreadsheet software that remains a fundamental tool in the world of data analysis.
With a meticulous attention to detail and an analytical mindset,Zakaria mastered Excel
numerous functions and features, enabling him to efficiently manage, clean, and analyze 
data. He soon became adept at creating data models, pivot tables, and visualizations 
that brought clarity to complex datasets.
''')
    st.subheader('Power BI: Transforming Data into Interactive Visualizations')
    st.text('''
Realizing the need for more advanced data visualization tools, Zakaria ventured into 
Power BI, Microsoft's powerful business intelligence platform. Power BI allowed him to 
take his data analysis to the next level by creating interactive dashboards and reports
Zakaria's proficiency in Power BI allowed him to transform data into compelling 
visualizations that not only conveyed insights but also made data-driven storytelling 
accessible to a wider audience within organizations.                    
 ''')
    st.subheader('SQL: Unearthing Data from Relational Databases')
    st.text(''' 
SQL, the language for managing and querying relational databases, became a crucial 
part of Zakaria's toolkit. With SQL, he could efficiently retrieve, manipulate, and 
aggregate data from various sources. This skill opened the door to working with large 
and complex datasets, a necessity in today's data-driven world. Zakaria's command of 
SQL allows him to navigate databases with ease, enabling him to extract the precise 
information needed for analysis.
''')
    st.subheader('Python: Automating and Enhancing Data Analysis')
    st.text(''' 
The world of data analytics is dynamic and ever-evolving, and Zakaria Mustafa 
recognized the importance of learning a versatile programming language like Python
Python is not only a powerful tool for data analysis but also for automation and data 
processing. Zakaria harnessed Python's capabilities to create custom scripts and 
programs that streamlined his analytical workflows. This proficiency expanded his
horizons to tackle more complex data challenges, from machine learning to data science 
projects.
Zakaria's journey from mastering Excel to embracing Power BI, SQL, and Python
showcases his commitment to evolving in the data analytics field continually. His 
proficiency in these four key tools makes him a valuable asset for any organization 
seeking data-driven insights and strategic decision-making. His ability to clean, analyze
visualize, and automate data processes positions him as a true data analysis maestro
Zakaria Mustafa's story is a testament to the ever-increasing importance of data 
analytics in the business world and the adaptability and continuous learning required in 
the field. As the world generates more data than ever before, professionals like Zakaria 
play a pivotal role in harnessing that data's potential and transforming it into actionable
intelligence. In the era of big data, the skills and expertise he brings to the table are 
more critical than ever, making him an exemplar of the modern data analyst.
''')
st.sidebar.subheader('We are happy to serve you :heart_eyes:')
# button certificates
c1,c2,= st.columns(2)
c1.subheader('More Certificates :point_right:')
st.subheader('ــــــــــــــــــــــــــــــــ')

with c2:
    b_c = st.button("Submit Certi..")

#more certificates

c1,c2 = st.columns(2)

if b_c:

    c1.image('more3.jpg')
    c2.image('mor4.jpg')
    c1.image('mor5.jpg')
    c2.image('mor6.jpg')
    c1.image('more1.jpg')
    c2.image('more2.jpg')
    c1.image('mor7.jpg')
    c2.image('men1.jpg')
    c1.image('men11.jpg')
    c2.image('men12.jpg')
    c1.image('men13.jpg')
    c2.image('men14.jpg')
    c1.image('men1.jpg')
    c2.image('men2.jpg')
    c1.image('men3.jpg')
    c2.image('men4.jpg')
    c1.image('men5.jpg')
    c2.image('men6.jpg')
    c1.image('men7.jpg')
    c2.image('men8.jpg')
    c1.image('men9.jpg')
    c2.image('men10.jpg')











