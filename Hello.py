# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import replicate
REPLICATE_API_TOKEN='r8_9iriilvAwoY8Eat4IKWjbTNM3Gx9fNG2I2iFD'
LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )
    
    st.write("# Welcome to MusicGen👋")
    st.markdown(
        """
        Please describe the music in natural language.
    """
    )
    st.sidebar.success("Select a demo above.")
    
    if prompt := st.chat_input():
        st.chat_message("user").write(prompt)
        output = replicate.run(
        "nateraw/musicgen-songstarter-v0.2:020ac56a613f4494065e2e5544c7377788a8abcfbe645ecb8146634de0bc383e",
        input={
            "top_k": 250,
            "top_p": 0,
            "prompt": prompt,
            "duration": 10,
            "input_audio": "https://ting8.yymp3.com/new27/ybe/1.mp3",
            "temperature": 1,
            "continuation": False,
            "output_format": "wav",
            "continuation_start": 0,
            "normalization_strategy": "loudness",
            "classifier_free_guidance": 3
        })
        st.audio(output[0])
        st.audio(output[1])
        st.audio(output[2])

   
   
   
if __name__ == "__main__":

#   print(output)
  run()
