from app_communication import *
import streamlit as st
import json

# get_episode_audio_url('aa893d1970fb47ceb1d728dfdb2c6585')

st.title('Podcast Summarizer')
episode_id = st.sidebar.text_input('Enter episode ID: ', 'aa893d1970fb47ceb1d728dfdb2c6585')
st.sidebar.button('Get Podcast Summary', on_click=save_transcript, args=(episode_id,))

def get_clean_time(start_ms):
    seconds = int((start_ms / 1000) % 60)
    minutes = int((start_ms / (1000 * 60)) % 60)
    hours = int((start_ms / (1000 * 60 * 60)) % 24)
    if hours > 0:
        start_t = f'{hours:02d}:{minutes:02d}:{seconds:02d}'
    else:
        start_t = f'{minutes:02d}:{seconds:02d}'
        
    return start_t

filename = episode_id + '_chapters.json'
print(filename)

with open(filename, 'r') as f:
    data = json.load(f)
    
    chapters = data['chapters']
    podcast_title = data['podcast_title']
    episode_title = data['episode_title']
    thumbnail = data['thumbnail']

st.header(f'{podcast_title} - {episode_title}')
st.image(thumbnail)

for chap in chapters:
    with st.expander(chap['gist'] + ' ( ' + get_clean_time(chap['start']) + ' )'):
        chap['summary']
    
    # st.subheader(chap['title'])
    # st.write(chap['text'])
    # st.write('')

# save_transcript('aa893d1970fb47ceb1d728dfdb2c6585')

