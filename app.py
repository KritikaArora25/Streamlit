import streamlit as st

st.title('Title -> GeeksforGeeks')
st.header('Header -> GeeksforGeeks')
st.subheader('Subheader -> GeeksforGeeks')
st.text('text -> GeeksforGeeks')


st.markdown('# Hi')
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('#### Hi')
st.markdown('##### Hi')
st.markdown('Hi')

st.success('Success!')
st.info('Information!')
st.warning('Warning!')
st.error('Error!')

exp=ZeroDivisionError('Division is not possible with Zero')
st.exception(exp)

st.help(ZeroDivisionError)  #Takes us to the documentation

st.write('range(1,10)')
st.write(range(1,10))
st.write(1+2+3)
st.write("1+2+3")

st.code('x=10\n'
        'for i in range(x):\n'
        '\tprint(i)')

st.checkbox('Male')   # 2 checkboxes cannot be of same name
st.checkbox('Female')
if(st.checkbox('Adult')):     #checkbox with validation
    st.write('You are an adult!')

radioButton = st.radio('Select : ',('Male','Female','Other'))
if(radioButton == 'Male'):
    st.write('You are a Male')
elif(radioButton == 'Female'):
    st.write('You are a Female')
elif(radioButton == 'Other'):
    st.write('You are an Other gender')


st.subheader('Select Box')
selectBox = st.selectbox("Data Science : ", ['Data Analysis','Web Scrapping',
                                 'Machine Learning','Deep Learning',
                                 'Natural Language Processing',
                                 'Computer Vision','Image Processing'])
st.write("You've Selected : ",selectBox)


st.subheader('MultiSelect Box')
multiSelBox = st.multiselect("Data Science : ", ['Data Analysis','Web Scrapping',
                                 'Machine Learning','Deep Learning',
                                 'Natural Language Processing',
                                 'Computer Vision','Image Processing'])
st.write("You've Selected : ",len(multiSelBox) , 'courses')


st.subheader('Button')
if(st.button('Click me!')):
    st.write('Thanks for Clicking me!')

st.subheader('Slider')
vol = st.slider('Select the Volume',1,100,step = 1)
st.write("The Volume is : ",vol)

st.subheader('Text Input')
name = st.text_input("Name : ")
if(name):
    st.write("Hi, ",name)
username = st.text_input("Username : ")
password= st.text_input("Password : ", type = 'password')

st.subheader('Text Area')
textArea=st.text_area("Write something interesting about yourself in 20 words")
st.write(textArea)

st.subheader("Input Number")
st.number_input('Select your age : ',18,110)

st.subheader("Input Date")
st.date_input('Enter your DOB : ')

st.subheader("Input Time")
st.time_input('Time : ')







