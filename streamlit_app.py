# #Without stop
# # import streamlit as st
# # import pandas as pd
# # import subprocess
# # import warnings

# # # Suppress specific warnings
# # warnings.filterwarnings('ignore')

# # # Function to load data
# # def load_data(file_path):
# #     return pd.read_csv(file_path)

# # # Function to save selected rows to user_feedback.csv
# # def save_selected_rows(df):
# #     selected_df = df[df['Select'] == True]
# #     selected_df.drop(columns=['Select'], inplace=True)
# #     selected_df.to_csv('C:/Users/A7765/AI/user_feedback.csv', index=False)

# # # Function to delete selected rows
# # def delete_selected_rows(df):
# #     df = df[df['Select'] == False]
# #     return df

# # # Load firewall logs data
# # def get_firewall_logs():
# #     firewall_logs = load_data('C:/Users/A7765/AI/firewall_logs.csv')
# #     firewall_logs['Select'] = False
# #     return firewall_logs

# # # Load rules data
# # def get_rules_data():
# #     return load_data('C:/Users/A7765/AI/rules.csv')

# # # Load user feedback data
# # def get_feedback_data():
# #     return load_data('C:/Users/A7765/AI/user_feedback.csv')

# # # Initialize session state
# # if 'df' not in st.session_state:
# #     st.session_state.df = get_firewall_logs()

# # if 'rules_df' not in st.session_state:
# #     st.session_state.rules_df = get_rules_data()

# # if 'feedback_df' not in st.session_state:
# #     st.session_state.feedback_df = get_feedback_data()

# # # Title of the app
# # st.title('Firewall Logs Table')

# # # Layout for the top buttons
# # col1, col2 = st.columns([1, 1])
# # with col1:
# #     if st.button('Traffic'):
# #         try:
# #             # Run overwrite.py using the Python executable from the virtual environment
# #             result = subprocess.run(['C:/Users/A7765/AI/myenv/Scripts/python.exe', 'C:/Users/A7765/AI/overwrite.py'], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
# #             st.success('overwrite.py script ran successfully.')
# #             st.text(f"Output:\n{result.stdout.decode('utf-8')}")
            
# #             # Then run the firewall.py script
# #             subprocess.Popen(['C:/Users/A7765/AI/myenv/Scripts/python.exe', 'C:/Users/A7765/AI/firewall.py'])
# #             st.success('firewall.py script is running in the background.')
# #         except subprocess.CalledProcessError as e:
# #             st.error(f"Failed to run traffic script: {e}")
# #             st.error(f"Error output: {e.stderr.decode('utf-8')}")

# # with col2:
# #     if st.button('Refresh'):
# #         st.session_state.df = get_firewall_logs()

# # # Display the table with checkboxes for each row
# # edited_df = st.data_editor(st.session_state.df, key='data_editor')

# # # Layout for the bottom buttons
# # col3, col4, col5 = st.columns([1, 1, 1])
# # with col3:
# #     if st.button('Save rule'):
# #         if edited_df['Select'].any():
# #             save_selected_rows(edited_df)
# #             st.session_state.feedback_df = get_feedback_data()  # Refresh feedback table
# #             st.success('Selected rows have been saved to user_feedback.csv')
# #         else:
# #             st.warning('No rows selected')

# # with col4:
# #     if st.button('Delete rule'):
# #         if edited_df['Select'].any():
# #             st.session_state.df = delete_selected_rows(edited_df)
# #             st.success('Selected rows have been deleted')
# #         else:
# #             st.warning('No rows selected')

# # with col5:
# #     if st.button('Run Model'):
# #         try:
# #             # Run ml_model.py using the Python executable from the virtual environment
# #             result = subprocess.run(['C:/Users/A7765/AI/myenv/Scripts/python.exe', 'C:/Users/A7765/AI/ml_model.py'], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
# #             st.success('Model script has run successfully.')
# #             st.text(f"Output:\n{result.stdout.decode('utf-8')}")
# #         except subprocess.CalledProcessError as e:
# #             st.error(f"Failed to run model script: {e}")
# #             st.error(f"Error output: {e.stderr.decode('utf-8')}")


# # # Display feedback.csv file as a table in between
# # st.subheader('Feedback Rule Table')

# # if st.button('Refresh Feedback Table'):
# #     st.session_state.feedback_df = get_feedback_data()

# # st.write(st.session_state.feedback_df)

# # # Display rules.csv file at the bottom
# # st.subheader('Rules Table')

# # if st.button('Refresh Rules Table'):
# #     st.session_state.rules_df = get_rules_data()

# # st.write(st.session_state.rules_df)


# #with stop button
# # import streamlit as st
# # import pandas as pd
# # import subprocess
# # import warnings
# # import os
# # import signal

# # # Suppress specific warnings
# # warnings.filterwarnings('ignore')

# # # Function to load data
# # def load_data(file_path):
# #     return pd.read_csv(file_path)

# # # Function to save selected rows to user_feedback.csv
# # def save_selected_rows(df):
# #     selected_df = df[df['Select'] == True]
# #     selected_df.drop(columns=['Select'], inplace=True)
# #     selected_df.to_csv('C:/Users/A7765/AI/user_feedback.csv', index=False)

# # # Function to delete selected rows
# # def delete_selected_rows(df):
# #     df = df[df['Select'] == False]
# #     return df

# # # Load firewall logs data
# # def get_firewall_logs():
# #     firewall_logs = load_data('C:/Users/A7765/AI/firewall_logs.csv')
# #     firewall_logs['Select'] = False
# #     return firewall_logs

# # # Load rules data
# # def get_rules_data():
# #     return load_data('C:/Users/A7765/AI/rules.csv')

# # # Load user feedback data
# # def get_feedback_data():
# #     return load_data('C:/Users/A7765/AI/user_feedback.csv')

# # # Initialize session state
# # if 'df' not in st.session_state:
# #     st.session_state.df = get_firewall_logs()

# # if 'rules_df' not in st.session_state:
# #     st.session_state.rules_df = get_rules_data()

# # if 'feedback_df' not in st.session_state:
# #     st.session_state.feedback_df = get_feedback_data()

# # # Keep track of the firewall.py process
# # if 'firewall_process' not in st.session_state:
# #     st.session_state.firewall_process = None

# # # Title of the app
# # st.title('Firewall Logs Table')

# # # Layout for the top buttons
# # col1, col2, col3 = st.columns([1, 1, 1])

# # # Traffic button
# # with col1:
# #     if st.button('Traffic'):
# #         if st.session_state.firewall_process is None:
# #             try:
# #                 # Run overwrite.py using the Python executable from the virtual environment
# #                 result = subprocess.run(['C:/Users/A7765/AI/myenv/Scripts/python.exe', 'C:/Users/A7765/AI/overwrite.py'], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
# #                 st.success('overwrite.py script ran successfully.')
# #                 st.text(f"Output:\n{result.stdout.decode('utf-8')}")
                
# #                 # Then run the firewall.py script
# #                 process = subprocess.Popen(['C:/Users/A7765/AI/myenv/Scripts/python.exe', 'C:/Users/A7765/AI/firewall.py'])
# #                 st.session_state.firewall_process = process
# #                 st.success('firewall.py script is running in the background.')
# #             except subprocess.CalledProcessError as e:
# #                 st.error(f"Failed to run traffic script: {e}")
# #                 st.error(f"Error output: {e.stderr.decode('utf-8')}")
# #         else:
# #             st.warning("firewall.py is already running.")

# # # Stop button
# # with col2:
# #     if st.button('Stop Traffic'):
# #         if st.session_state.firewall_process is not None:
# #             st.session_state.firewall_process.terminate()
# #             st.session_state.firewall_process = None
# #             st.success('firewall.py script has been stopped.')
# #         else:
# #             st.warning("No firewall.py process is currently running.")

# # # Refresh button
# # with col3:
# #     if st.button('Refresh'):
# #         st.session_state.df = get_firewall_logs()

# # # Display the table with checkboxes for each row
# # edited_df = st.data_editor(st.session_state.df, key='data_editor')

# # # Layout for the bottom buttons
# # col4, col5, col6 = st.columns([1, 1, 1])

# # # Save rule button
# # with col4:
# #     if st.button('Save rule'):
# #         if edited_df['Select'].any():
# #             save_selected_rows(edited_df)
# #             st.session_state.feedback_df = get_feedback_data()  # Refresh feedback table
# #             st.success('Selected rows have been saved to user_feedback.csv')
# #         else:
# #             st.warning('No rows selected')

# # # Delete rule button
# # with col5:
# #     if st.button('Delete rule'):
# #         if edited_df['Select'].any():
# #             st.session_state.df = delete_selected_rows(edited_df)
# #             st.success('Selected rows have been deleted')
# #         else:
# #             st.warning('No rows selected')

# # # Run model button
# # with col6:
# #     if st.button('Run Model'):
# #         try:
# #             # Run ml_model.py using the Python executable from the virtual environment
# #             result = subprocess.run(['C:/Users/A7765/AI/myenv/Scripts/python.exe', 'C:/Users/A7765/AI/ml_model.py'], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
# #             st.success('Model script has run successfully.')
# #             st.text(f"Output:\n{result.stdout.decode('utf-8')}")
# #         except subprocess.CalledProcessError as e:
# #             st.error(f"Failed to run model script: {e}")
# #             st.error(f"Error output: {e.stderr.decode('utf-8')}")

# # # Display feedback.csv file as a table in between
# # st.subheader('Feedback Rule Table')

# # if st.button('Refresh Feedback Table'):
# #     st.session_state.feedback_df = get_feedback_data()

# # st.write(st.session_state.feedback_df)

# # # Display rules.csv file at the bottom
# # st.subheader('Rules Table')

# # if st.button('Refresh Rules Table'):
# #     st.session_state.rules_df = get_rules_data()

# # st.write(st.session_state.rules_df)

# #GenAI

# # import streamlit as st
# # import pandas as pd
# # import subprocess
# # import warnings
# # import os
# # import signal
# # import google.generativeai as genai

# # # Suppress specific warnings
# # warnings.filterwarnings('ignore')

# # # Function to load data
# # def load_data(file_path):
# #     return pd.read_csv(file_path)

# # # Function to save selected rows to user_feedback.csv
# # def save_selected_rows(df):
# #     selected_df = df[df['Select'] == True]
# #     selected_df.drop(columns=['Select'], inplace=True)
# #     selected_df.to_csv('C:/Users/A7765/AI/user_feedback.csv', index=False)

# # # Function to delete selected rows
# # def delete_selected_rows(df):
# #     df = df[df['Select'] == False]
# #     return df

# # # Load firewall logs data
# # def get_firewall_logs():
# #     firewall_logs = load_data('C:/Users/A7765/AI/firewall_logs.csv')
# #     firewall_logs['Select'] = False
# #     return firewall_logs

# # # Load rules data
# # def get_rules_data():
# #     return load_data('C:/Users/A7765/AI/rules.csv')

# # # Load user feedback data
# # def get_feedback_data():
# #     return load_data('C:/Users/A7765/AI/user_feedback.csv')

# # # Initialize session state
# # if 'df' not in st.session_state:
# #     st.session_state.df = get_firewall_logs()

# # if 'rules_df' not in st.session_state:
# #     st.session_state.rules_df = get_rules_data()

# # if 'feedback_df' not in st.session_state:
# #     st.session_state.feedback_df = get_feedback_data()

# # # Keep track of the firewall.py process
# # if 'firewall_process' not in st.session_state:
# #     st.session_state.firewall_process = None

# # # Title of the app
# # st.title('Firewall Logs Table')

# # # Layout for the top buttons
# # col1, col2, col3 = st.columns([1, 1, 1])

# # # Traffic button
# # with col1:
# #     if st.button('Traffic'):
# #         if st.session_state.firewall_process is None:
# #             try:
# #                 # Run overwrite.py using the Python executable from the virtual environment
# #                 result = subprocess.run(['C:/Users/A7765/AI/myenv/Scripts/python.exe', 'C:/Users/A7765/AI/overwrite.py'], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
# #                 st.success('overwrite.py script ran successfully.')
# #                 st.text(f"Output:\n{result.stdout.decode('utf-8')}")
                
# #                 # Then run the firewall.py script
# #                 process = subprocess.Popen(['C:/Users/A7765/AI/myenv/Scripts/python.exe', 'C:/Users/A7765/AI/firewall.py'])
# #                 st.session_state.firewall_process = process
# #                 st.success('firewall.py script is running in the background.')
# #             except subprocess.CalledProcessError as e:
# #                 st.error(f"Failed to run traffic script: {e}")
# #                 st.error(f"Error output: {e.stderr.decode('utf-8')}")
# #         else:
# #             st.warning("firewall.py is already running.")

# # # Stop button
# # with col2:
# #     if st.button('Stop Traffic'):
# #         if st.session_state.firewall_process is not None:
# #             st.session_state.firewall_process.terminate()
# #             st.session_state.firewall_process = None
# #             st.success('firewall.py script has been stopped.')
# #         else:
# #             st.warning("No firewall.py process is currently running.")

# # # Refresh button
# # with col3:
# #     if st.button('Refresh'):
# #         st.session_state.df = get_firewall_logs()

# # # Display the table with checkboxes for each row
# # edited_df = st.data_editor(st.session_state.df, key='data_editor')

# # # Layout for the bottom buttons
# # col4, col5, col6 = st.columns([1, 1, 1])

# # # Save rule button
# # with col4:
# #     if st.button('Save rule'):
# #         if edited_df['Select'].any():
# #             save_selected_rows(edited_df)
# #             st.session_state.feedback_df = get_feedback_data()  # Refresh feedback table
# #             st.success('Selected rows have been saved to user_feedback.csv')
# #         else:
# #             st.warning('No rows selected')

# # # Delete rule button
# # with col5:
# #     if st.button('Delete rule'):
# #         if edited_df['Select'].any():
# #             st.session_state.df = delete_selected_rows(edited_df)
# #             st.success('Selected rows have been deleted')
# #         else:
# #             st.warning('No rows selected')

# # # Run model button
# # with col6:
# #     if st.button('Run Model'):
# #         try:
# #             # Run ml_model.py using the Python executable from the virtual environment
# #             result = subprocess.run(['C:/Users/A7765/AI/myenv/Scripts/python.exe', 'C:/Users/A7765/AI/ml_model.py'], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
# #             st.success('Model script has run successfully.')
# #             st.text(f"Output:\n{result.stdout.decode('utf-8')}")
# #         except subprocess.CalledProcessError as e:
# #             st.error(f"Failed to run model script: {e}")
# #             st.error(f"Error output: {e.stderr.decode('utf-8')}")

# # # Display feedback.csv file as a table in between
# # st.subheader('Feedback Rule Table')

# # if st.button('Refresh Feedback Table'):
# #     st.session_state.feedback_df = get_feedback_data()

# # st.write(st.session_state.feedback_df)

# # # Display rules.csv file at the bottom
# # st.subheader('Rules Table')

# # if st.button('Refresh Rules Table'):
# #     st.session_state.rules_df = get_rules_data()

# # st.write(st.session_state.rules_df)

# # # GenAI conversation section
# # st.subheader('Ask AI-Guard')

# # user_input = st.text_input('Enter your question for AI-Guard:', '')
# # if st.button('Submit to AI-Guard'):
# #     try:
# #         genai.configure(api_key="AIzaSyDnWLKJfJvEP0CQqFspQEij0iK-iVnxqww")

# #         # Set up the model
# #         generation_config = {
# #             "temperature": 0.9,
# #             "top_p": 1,
# #             "top_k": 1,
# #             "max_output_tokens": 2048,
# #         }

# #         safety_settings = [
# #             {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
# #             {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
# #             {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
# #             {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
# #         ]

# #         model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config, safety_settings=safety_settings)
# #         convo = model.start_chat(history=[])
# #         convo.send_message(user_input)
# #         response = convo.last.text
# #         st.text_area('GenAI Response:', value=response, height=300)
# #     except Exception as e:
# #         st.error(f'Failed to connect to GenAI: {str(e)}')


# import streamlit as st
# import pandas as pd
# import subprocess
# import warnings
# import os
# import signal
# import google.generativeai as genai

# # Suppress specific warnings
# warnings.filterwarnings('ignore')

# # Function to load data
# def load_data(file_path):
#     return pd.read_csv(file_path)

# # Function to save selected rows to user_feedback.csv
# def save_selected_rows(df):
#     selected_df = df[df['Select'] == True]
#     selected_df.drop(columns=['Select'], inplace=True)
#     selected_df.to_csv('C:/Users/A7765/AI/user_feedback.csv', index=False)

# # Function to delete selected rows
# def delete_selected_rows(df):
#     df = df[df['Select'] == False]
#     return df

# # Load firewall logs data
# def get_firewall_logs():
#     firewall_logs = load_data('C:/Users/A7765/AI/firewall_logs.csv')
#     firewall_logs['Select'] = False
#     return firewall_logs

# # Load rules data
# def get_rules_data():
#     return load_data('C:/Users/A7765/AI/rules.csv')

# # Load user feedback data
# def get_feedback_data():
#     return load_data('C:/Users/A7765/AI/user_feedback.csv')

# # Initialize session state
# if 'df' not in st.session_state:
#     st.session_state.df = get_firewall_logs()

# if 'rules_df' not in st.session_state:
#     st.session_state.rules_df = get_rules_data()

# if 'feedback_df' not in st.session_state:
#     st.session_state.feedback_df = get_feedback_data()

# # Keep track of the firewall.py process
# if 'firewall_process' not in st.session_state:
#     st.session_state.firewall_process = None

# # Title of the app
# st.title('Firewall Logs Table')

# # Layout for the top buttons
# col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

# # Traffic button
# with col1:
#     if st.button('Traffic'):
#         if st.session_state.firewall_process is None:
#             try:
#                 # Run overwrite.py using the Python executable from the virtual environment
#                 result = subprocess.run(['C:/Users/A7765/AI/myenv/Scripts/python.exe', 'C:/Users/A7765/AI/overwrite.py'], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
#                 st.success('overwrite.py script ran successfully.')
#                 st.text(f"Output:\n{result.stdout.decode('utf-8')}")
                
#                 # Then run the firewall.py script
#                 process = subprocess.Popen(['C:/Users/A7765/AI/myenv/Scripts/python.exe', 'C:/Users/A7765/AI/firewall.py'])
#                 st.session_state.firewall_process = process
#                 st.success('firewall.py script is running in the background.')
#             except subprocess.CalledProcessError as e:
#                 st.error(f"Failed to run traffic script: {e}")
#                 st.error(f"Error output: {e.stderr.decode('utf-8')}")
#         else:
#             st.warning("firewall.py is already running.")

# # Stop button
# with col2:
#     if st.button('Stop Traffic'):
#         if st.session_state.firewall_process is not None:
#             st.session_state.firewall_process.terminate()
#             st.session_state.firewall_process = None
#             st.success('firewall.py script has been stopped.')
#         else:
#             st.warning("No firewall.py process is currently running.")

# # Refresh button
# with col3:
#     if st.button('Refresh'):
#         st.session_state.df = get_firewall_logs()

# # Breach button
# with col4:
#     if st.button('Breach'):
#         try:
#             # Run Breach.py and capture the output
#             result = subprocess.run(['C:/Users/A7765/AI/myenv/Scripts/python.exe', 'C:/Users/A7765/AI/Breach.py'], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
#             st.success('Breach.py script ran successfully.')
#             st.text_area('Breach Result:', value=result.stdout.decode('utf-8'), height=300)
#         except subprocess.CalledProcessError as e:
#             st.error(f"Failed to run Breach script: {e}")
#             st.error(f"Error output: {e.stderr.decode('utf-8')}")

# # Display the table with checkboxes for each row
# edited_df = st.data_editor(st.session_state.df, key='data_editor')

# # Layout for the bottom buttons
# col4, col5, col6 = st.columns([1, 1, 1])

# # Save rule button
# with col4:
#     if st.button('Save rule'):
#         if edited_df['Select'].any():
#             save_selected_rows(edited_df)
#             st.session_state.feedback_df = get_feedback_data()  # Refresh feedback table
#             st.success('Selected rows have been saved to user_feedback.csv')
#         else:
#             st.warning('No rows selected')

# # Delete rule button
# with col5:
#     if st.button('Delete rule'):
#         if edited_df['Select'].any():
#             st.session_state.df = delete_selected_rows(edited_df)
#             st.success('Selected rows have been deleted')
#         else:
#             st.warning('No rows selected')

# # Run model button
# with col6:
#     if st.button('Run Model'):
#         try:
#             # Run ml_model.py using the Python executable from the virtual environment
#             result = subprocess.run(['C:/Users/A7765/AI/myenv/Scripts/python.exe', 'C:/Users/A7765/AI/ml_model.py'], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
#             st.success('Model script has run successfully.')
#             st.text(f"Output:\n{result.stdout.decode('utf-8')}")
#         except subprocess.CalledProcessError as e:
#             st.error(f"Failed to run model script: {e}")
#             st.error(f"Error output: {e.stderr.decode('utf-8')}")

# # Display feedback.csv file as a table in between
# st.subheader('Feedback Rule Table')

# if st.button('Refresh Feedback Table'):
#     st.session_state.feedback_df = get_feedback_data()

# st.write(st.session_state.feedback_df)

# # Display rules.csv file at the bottom
# st.subheader('Rules Table')

# if st.button('Refresh Rules Table'):
#     st.session_state.rules_df = get_rules_data()

# st.write(st.session_state.rules_df)

# # GenAI conversation section
# st.subheader('Ask AI-Guard')

# user_input = st.text_input('Enter your question for AI-Guard:', '')
# if st.button('Submit to AI-Guard'):
#     try:
#         genai.configure(api_key="AIzaSyDnWLKJfJvEP0CQqFspQEij0iK-iVnxqww")

#         # Set up the model
#         generation_config = {
#             "temperature": 0.9,
#             "top_p": 1,
#             "top_k": 1,
#             "max_output_tokens": 2048,
#         }

#         safety_settings = [
#             {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
#             {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
#             {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
#             {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
#         ]

#         model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config, safety_settings=safety_settings)
#         convo = model.start_chat(history=[])
#         convo.send_message(user_input)
#         response = convo.last.text
#         st.text_area('GenAI Response:', value=response, height=300)
#     except Exception as e:
#         st.error(f'Failed to connect to GenAI: {str(e)}')

# import streamlit as st
# import pandas as pd
# import subprocess
# import warnings
# import google.generativeai as genai

# csv_file = 'C:/Users/A7765/AI/firewall_logs.csv'
# df = pd.read_csv(csv_file)
# print(df)

# # Suppress specific warnings
# warnings.filterwarnings('ignore')

# # Function to load data
# def load_data(file_path):
#     return pd.read_csv(file_path)

# # Load firewall logs data
# def get_firewall_logs():
#     firewall_logs = load_data('C:/Users/A7765/AI/firewall_logs.csv')
#     firewall_logs['Select'] = False
#     return firewall_logs

# # Load feedback and rules data
# def get_feedback_data():
#     return load_data('C:/Users/A7765/AI/user_feedback.csv')

# def get_rules_data():
#     return load_data('C:/Users/A7765/AI/rules.csv')

# # Initialize session state for firewall process and logs data
# if 'firewall_process' not in st.session_state:
#     st.session_state.firewall_process = None

# if 'df' not in st.session_state:
#     st.session_state.df = get_firewall_logs()

# if 'rules_df' not in st.session_state:
#     st.session_state.rules_df = get_rules_data()

# if 'feedback_df' not in st.session_state:
#     st.session_state.feedback_df = get_feedback_data()

# # Create tabs for the UI
# tab1, tab2 = st.tabs(["🚦 Network Traffic & AI-Guard", "🔐 Breach Detection"])

# # First Tab: Traffic & AI-Guard
# with tab1:
#     st.header("🚦 Network Traffic Control & AI-Guard")

#     # Layout for the traffic control buttons
#     col1, col2, col3 = st.columns([1, 1, 1])

#     # Traffic button
#     with col1:
#         if st.button('Start Traffic'):
#             if st.session_state.firewall_process is None:
#                 try:
#                     # Run overwrite.py using the Python executable from the virtual environment
#                     result = subprocess.run(['C:/Users/A7765/AI/myenv/Scripts/python.exe', 'C:/Users/A7765/AI/overwrite.py'], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
#                     st.success('Traffic started successfully.')
#                     st.text(f"Output:\n{result.stdout.decode('utf-8')}")

#                     # Then run the firewall.py script
#                     process = subprocess.Popen(['C:/Users/A7765/AI/myenv/Scripts/python.exe', 'C:/Users/A7765/AI/firewall.py'])
#                     st.session_state.firewall_process = process
#                     st.success('firewall.py is running in the background.')
#                 except subprocess.CalledProcessError as e:
#                     st.error(f"Failed to start traffic: {e}")
#                     st.error(f"Error output: {e.stderr.decode('utf-8')}")
#             else:
#                 st.warning("Traffic is already running.")

#     # Stop Traffic button
#     with col2:
#         if st.button('Stop Traffic'):
#             if st.session_state.firewall_process is not None:
#                 st.session_state.firewall_process.terminate()
#                 st.session_state.firewall_process = None
#                 st.success('Traffic stopped successfully.')
#             else:
#                 st.warning("No traffic process is currently running.")

#     # Refresh button
#     with col3:
#         if st.button('Refresh Logs'):
#             st.session_state.df = get_firewall_logs()
#             st.success('Logs refreshed.')

#     # Divider for spacing and separation
#     st.markdown("---")

#     # Display the logs table with checkboxes for each row
#     st.subheader("Firewall Logs Table")
#     edited_df = st.data_editor(st.session_state.df, key='data_editor')

#     # Bottom row buttons for managing rules
#     col4, col5, col6 = st.columns([1, 1, 1])

#     # Save rule button
#     with col4:
#         if st.button('Save Rule'):
#             if edited_df['Select'].any():
#                 selected_df = edited_df[edited_df['Select'] == True]
#                 selected_df.drop(columns=['Select'], inplace=True)
#                 selected_df.to_csv('C:/Users/A7765/AI/user_feedback.csv', index=False)
#                 st.session_state.feedback_df = get_feedback_data()
#                 st.success('Selected rows saved to user_feedback.csv')
#             else:
#                 st.warning('No rows selected')

#     # Delete rule button
#     with col5:
#         if st.button('Delete Rule'):
#             if edited_df['Select'].any():
#                 st.session_state.df = edited_df[edited_df['Select'] == False]
#                 st.success('Selected rows have been deleted')
#             else:
#                 st.warning('No rows selected')

#     # Run model button
#     with col6:
#         if st.button('Run Model'):
#             try:
#                 # Run ml_model.py using the Python executable from the virtual environment
#                 result = subprocess.run(['C:/Users/A7765/AI/myenv/Scripts/python.exe', 'C:/Users/A7765/AI/ml_model.py'], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
#                 st.success('Model script ran successfully.')
#                 st.text(f"Output:\n{result.stdout.decode('utf-8')}")
#             except subprocess.CalledProcessError as e:
#                 st.error(f"Failed to run model script: {e}")
#                 st.error(f"Error output: {e.stderr.decode('utf-8')}")

#     # Divider for spacing and separation
#     st.markdown("---")

#     # Display feedback.csv file as a table
#     st.subheader('Feedback Rule Table')
#     if st.button('Refresh Feedback Table'):
#         st.session_state.feedback_df = get_feedback_data()

#     st.write(st.session_state.feedback_df)

#     # Divider for spacing and separation
#     st.markdown("---")

#     # Display rules.csv file as a table
#     st.subheader('Rules Table')
#     if st.button('Refresh Rules Table'):
#         st.session_state.rules_df = get_rules_data()

#     st.write(st.session_state.rules_df)



# # Second Tab: Breach Detection
# with tab2:
#     st.header("🔐 Breach Detection")

#     if st.button('Run Breach Detection'):
#         try:
#             # Run Breach.py and capture the output
#             result = subprocess.run(['C:/Users/A7765/AI/myenv/Scripts/python.exe', 'C:/Users/A7765/AI/Breach.py'], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
#             st.success('Breach detection completed successfully.')
#             st.text_area('Breach Detection Result:', value=result.stdout.decode('utf-8'), height=300)
#         except subprocess.CalledProcessError as e:
#             st.error(f"Failed to run Breach Detection: {e}")
#             st.error(f"Error output: {e.stderr.decode('utf-8')}")
    

#         # Divider for spacing and separation
#     st.markdown("---")

#     # # GenAI conversation section
#     # st.subheader("🤖 Ask AI-Guard")

#     # user_input = st.text_input('Ask a question to AI-Guard:')
#     # print(user_input)
#     # print(csv_file)
#     # if st.button('Submit to AI-Guard'):
#     #     try:
#     #         genai.configure(api_key="AIzaSyDnWLKJfJvEP0CQqFspQEij0iK-iVnxqww")

#     #         # Set up the model
#     #         generation_config = {
#     #             "temperature": 0.9,
#     #             "top_p": 1,
#     #             "top_k": 1,
#     #             "max_output_tokens": 2048,
#     #         }

#     #         safety_settings = [
#     #             {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
#     #             {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
#     #             {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
#     #             {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
#     #         ]

#     #         model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config, safety_settings=safety_settings)
#     #         convo = model.start_chat(history=[])
#     #         convo.send_message(user_input)
#     #         response = convo.last.text
#     #         st.text_area('AI-Guard Response:', value=response, height=300)
#     #     except Exception as e:
#     #         st.error(f"Failed to connect to AI-Guard: {str(e)}")
#     # GenAI conversation section
#     st.subheader("🤖 Ask AI-Guard")

#     # Get the user input for the question
#     user_input = st.text_input('Ask a question to AI-Guard:')

#     # Convert the DataFrame to CSV format to pass it along with the question
#     df_csv = df.to_csv(index=False)

#     # Prepare the prompt to send to AI-Guard, combining the user's question and the DataFrame data
#     prompt = f"Question: {user_input}\n\nHere is the data in CSV format:\n{df_csv}"

#     # Display the prompt for debugging or user visibility (optional)
#     st.text_area("Prompt sent to AI-Guard:", value=prompt, height=200)

#     # When the user clicks the submit button, send the question and DataFrame to AI-Guard
#     if st.button('Submit to AI-Guard'):
#         try:
#             # Configure GenAI with your API key
#             genai.configure(api_key="AIzaSyDnWLKJfJvEP0CQqFspQEij0iK-iVnxqww")

#             # Set up the model
#             generation_config = {
#                 "temperature": 0.9,
#                 "top_p": 1,
#                 "top_k": 1,
#                 "max_output_tokens": 2048,
#             }

#             safety_settings = [
#                 {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
#                 {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
#                 {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
#                 {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
#             ]

#             # Initialize the model and start a chat
#             model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config, safety_settings=safety_settings)
#             convo = model.start_chat(history=[])
            
#             # Send the prompt containing the question and DataFrame data to AI-Guard
#             convo.send_message(prompt)
#             response = convo.last.text
            
#             # Display the AI's response
#             st.text_area('AI-Guard Response:', value=response, height=300)
        
#         except Exception as e:
#             st.error(f"Failed to connect to AI-Guard: {str(e)}")



import streamlit as st
import pandas as pd
import subprocess
import warnings
import google.generativeai as genai

csv_file = 'C:/Users/A7765/AI/firewall_logs.csv'
df = pd.read_csv(csv_file)
print(df)

# Suppress specific warnings
warnings.filterwarnings('ignore')

# Function to load data
def load_data(file_path):
    return pd.read_csv(file_path)

# Load firewall logs data
def get_firewall_logs():
    firewall_logs = load_data('C:/Users/A7765/AI/firewall_logs.csv')
    firewall_logs['Select'] = False
    return firewall_logs

# Load feedback and rules data
def get_feedback_data():
    return load_data('C:/Users/A7765/AI/user_feedback.csv')

def get_rules_data():
    return load_data('C:/Users/A7765/AI/rules.csv')

# Initialize session state for firewall process and logs data
if 'firewall_process' not in st.session_state:
    st.session_state.firewall_process = None

if 'df' not in st.session_state:
    st.session_state.df = get_firewall_logs()

if 'rules_df' not in st.session_state:
    st.session_state.rules_df = get_rules_data()

if 'feedback_df' not in st.session_state:
    st.session_state.feedback_df = get_feedback_data()

# Create tabs for the UI
tab1, tab2 = st.tabs(["🚦 Network Traffic & AI-Guard", "🔐 Breach Detection"])

# First Tab: Traffic & AI-Guard
with tab1:
    st.header("🚦 Network Traffic Control & AI-Guard")

    # Layout for the traffic control buttons
    col1, col2, col3 = st.columns([1, 1, 1])

    # Traffic button
    with col1:
        if st.button('Start Traffic'):
            if st.session_state.firewall_process is None:
                try:
                    # Run overwrite.py using the Python executable from the virtual environment
                    result = subprocess.run(['C:/Users/A7765/AI/myenv/Scripts/python.exe', 'C:/Users/A7765/AI/overwrite.py'], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                    st.success('Traffic started successfully.')
                    st.text(f"Output:\n{result.stdout.decode('utf-8')}")

                    # Then run the firewall.py script
                    process = subprocess.Popen(['C:/Users/A7765/AI/myenv/Scripts/python.exe', 'C:/Users/A7765/AI/firewall.py'])
                    st.session_state.firewall_process = process
                    st.success('firewall.py is running in the background.')
                except subprocess.CalledProcessError as e:
                    st.error(f"Failed to start traffic: {e}")
                    st.error(f"Error output: {e.stderr.decode('utf-8')}")
            else:
                st.warning("Traffic is already running.")

    # Stop Traffic button
    with col2:
        if st.button('Stop Traffic'):
            if st.session_state.firewall_process is not None:
                st.session_state.firewall_process.terminate()
                st.session_state.firewall_process = None
                st.success('Traffic stopped successfully.')
            else:
                st.warning("No traffic process is currently running.")

    # Refresh button
    with col3:
        if st.button('Refresh Logs'):
            st.session_state.df = get_firewall_logs()
            st.success('Logs refreshed.')

    # Divider for spacing and separation
    st.markdown("---")

    # Display the logs table with checkboxes for each row
    st.subheader("Firewall Logs Table")
    edited_df = st.data_editor(st.session_state.df, key='data_editor')

    # Bottom row buttons for managing rules
    col4, col5, col6 = st.columns([1, 1, 1])

    # Save rule button
    with col4:
        if st.button('Save Rule'):
            if edited_df['Select'].any():
                selected_df = edited_df[edited_df['Select'] == True]
                selected_df.drop(columns=['Select'], inplace=True)
                selected_df.to_csv('C:/Users/A7765/AI/user_feedback.csv', index=False)
                st.session_state.feedback_df = get_feedback_data()
                st.success('Selected rows saved to user_feedback.csv')
            else:
                st.warning('No rows selected')

    # Delete rule button
    with col5:
        if st.button('Delete Rule'):
            if edited_df['Select'].any():
                st.session_state.df = edited_df[edited_df['Select'] == False]
                st.success('Selected rows have been deleted')
            else:
                st.warning('No rows selected')

    # Run model button
    with col6:
        if st.button('Run Model'):
            try:
                # Run ml_model.py using the Python executable from the virtual environment
                result = subprocess.run(['C:/Users/A7765/AI/myenv/Scripts/python.exe', 'C:/Users/A7765/AI/ml_model.py'], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                st.success('Model script ran successfully.')
                st.text(f"Output:\n{result.stdout.decode('utf-8')}")
            except subprocess.CalledProcessError as e:
                st.error(f"Failed to run model script: {e}")
                st.error(f"Error output: {e.stderr.decode('utf-8')}")

    # Divider for spacing and separation
    st.markdown("---")

    # Display feedback.csv file as a table
    st.subheader('Feedback Rule Table')
    if st.button('Refresh Feedback Table'):
        st.session_state.feedback_df = get_feedback_data()

    st.write(st.session_state.feedback_df)

    # Divider for spacing and separation
    st.markdown("---")

    # Display rules.csv file as a table
    st.subheader('Rules Table')
    if st.button('Refresh Rules Table'):
        st.session_state.rules_df = get_rules_data()

    st.write(st.session_state.rules_df)
# Second Tab: Breach Detection
with tab2:
    st.header("🔐 Breach Detection")

    # Run Breach Detection button
    if st.button('Run Breach Detection'):
        try:
            # Run Breach.py and capture the output
            result = subprocess.run(['C:/Users/A7765/AI/myenv/Scripts/python.exe', 'C:/Users/A7765/AI/Breach.py'], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            st.success('Breach detection completed successfully.')
            st.text_area('Breach Detection Result:', value=result.stdout.decode('utf-8'), height=300)
        except subprocess.CalledProcessError as e:
            st.error(f"Failed to run Breach Detection: {e}")
            st.error(f"Error output: {e.stderr.decode('utf-8')}")

    # Divider for spacing and separation
    st.markdown("---")

    # Run Anomaly Detection button
    if st.button('Run Anomalies Detection'):
        try:
            # Run Anomaly.py and capture the output
            result = subprocess.run(['C:/Users/A7765/AI/myenv/Scripts/python.exe', 'C:/Users/A7765/AI/anomoly.py'], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            st.success('Anomaly detection completed successfully.')
            st.text_area('Anomaly Detection Result:', value=result.stdout.decode('utf-8'), height=300)
        except subprocess.CalledProcessError as e:
            st.error(f"Failed to run Anomaly Detection: {e}")
            st.error(f"Error output: {e.stderr.decode('utf-8')}")

    # Divider for spacing and separation
    st.markdown("---")

    # GenAI conversation section
    st.subheader("🤖 Ask AI-Guard")

    # Get the user input for the question
    user_input = st.text_input('Ask a question to AI-Guard:')

    # Convert the DataFrame to CSV format to pass it along with the question
    df_csv = df.to_csv(index=False)

    # Prepare the prompt to send to AI-Guard, combining the user's question and the DataFrame data
    prompt = f"Question: {user_input}\n\nHere is the data in CSV format:\n{df_csv}"

    # Display the prompt for debugging or user visibility (optional)
    st.text_area("Prompt sent to AI-Guard:", value=prompt, height=200)

    # When the user clicks the submit button, send the question and DataFrame to AI-Guard
    if st.button('Submit to AI-Guard'):
        try:
            # Configure GenAI with your API key
            genai.configure(api_key="AIzaSyDnWLKJfJvEP0CQqFspQEij0iK-iVnxqww")

            # Set up the model
            generation_config = {
                "temperature": 0.9,
                "top_p": 1,
                "top_k": 1,
                "max_output_tokens": 2048,
            }

            safety_settings = [
                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            ]

            # Initialize the model and start a chat
            model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config, safety_settings=safety_settings)
            convo = model.start_chat(history=[])
            
            # Send the prompt containing the question and DataFrame data to AI-Guard
            convo.send_message(prompt)
            response = convo.last.text
            
            # Display the AI's response
            st.text_area('AI-Guard Response:', value=response, height=300)
        
        except Exception as e:
            st.error(f"Failed to connect to AI-Guard: {str(e)}")
