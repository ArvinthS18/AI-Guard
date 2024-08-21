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
# #     selected_df.to_csv('C:/Users/Aravindan/aigs/user_feedback.csv', index=False)

# # # Function to delete selected rows
# # def delete_selected_rows(df):
# #     df = df[df['Select'] == False]
# #     return df

# # # Load firewall logs data
# # def get_firewall_logs():
# #     firewall_logs = load_data('C:/Users/Aravindan/aigs/firewall_logs.csv')
# #     firewall_logs['Select'] = False
# #     return firewall_logs

# # # Load rules data
# # def get_rules_data():
# #     return load_data('C:/Users/Aravindan/aigs/rules.csv')

# # # Load user feedback data
# # def get_feedback_data():
# #     return load_data('C:/Users/Aravindan/aigs/user_feedback.csv')

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
# #             # First run the overwrite.py script
# #             subprocess.run(['python', 'C:/Users/Aravindan/aigs/overwrite.py'], check=True)
# #             # Then run the firewall.py script
# #             subprocess.Popen(['python', 'C:/Users/Aravindan/aigs/firewall.py'])
# #             st.success('Traffic script is running in the background.')
# #         except subprocess.CalledProcessError as e:
# #             st.error(f"Failed to run traffic script: {e}")

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
# #             subprocess.run(['python', 'C:/Users/Aravindan/aigs/ml_model.py'], check=True)
# #             st.success('Model script has run successfully.')
# #         except subprocess.CalledProcessError as e:
# #             st.error(f"Failed to run model script: {e}")

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


# import streamlit as st
# import pandas as pd
# import subprocess
# import warnings
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
#     selected_df.to_csv('C:/Users/Aravindan/aigs/user_feedback.csv', index=False)

# # Function to delete selected rows
# def delete_selected_rows(df):
#     df = df[df['Select'] == False]
#     return df

# # Load firewall logs data
# def get_firewall_logs():
#     firewall_logs = load_data('C:/Users/Aravindan/aigs/firewall_logs.csv')
#     firewall_logs['Select'] = False
#     return firewall_logs

# # Load rules data
# def get_rules_data():
#     return load_data('C:/Users/Aravindan/aigs/rules.csv')

# # Load user feedback data
# def get_feedback_data():
#     return load_data('C:/Users/Aravindan/aigs/user_feedback.csv')

# # Initialize session state
# if 'df' not in st.session_state:
#     st.session_state.df = get_firewall_logs()

# if 'rules_df' not in st.session_state:
#     st.session_state.rules_df = get_rules_data()

# if 'feedback_df' not in st.session_state:
#     st.session_state.feedback_df = get_feedback_data()

# if 'process' not in st.session_state:
#     st.session_state.process = None

# # Title of the app
# st.title('Firewall Logs Table')

# # Layout for the top buttons
# col1, col2, col3 = st.columns([1, 1, 1])
# with col1:
#     # if st.button('Traffic'):
#     #     try:
#     #         if st.session_state.process is None or st.session_state.process.poll() is not None:
#     #             # Only start if no process is running
#     #             st.session_state.process = subprocess.Popen(['python', 'C:/Users/Aravindan/aigs/firewall.py'])
#     #             st.success('Traffic script is running in the background.')
#     #         else:
#     #             st.error('A script is already running.')
#     #     except Exception as e:
#     #         st.error(f"Failed to run traffic script: {e}")
#     if st.button('Traffic'):
#         try:
#             # First run the overwrite.py script
#             subprocess.run(['python', 'C:/Users/Aravindan/aigs/overwrite.py'], check=True)
#             # Then run the firewall.py script
#             subprocess.Popen(['python', 'C:/Users/Aravindan/aigs/firewall.py'])
#             st.success('Traffic script is running in the background.')
#         except subprocess.CalledProcessError as e:
#             st.error(f"Failed to run traffic script: {e}")

# with col2:
#     if st.button('Stop Traffic'):
#         if st.session_state.process is not None:
#             st.session_state.process.terminate()
#             st.success('Traffic script has been stopped.')
#         else:
#             st.error('No script is running.')

# with col3:
#     if st.button('Refresh'):
#         st.session_state.df = get_firewall_logs()

# # Display the table with checkboxes for each row
# edited_df = st.data_editor(st.session_state.df, key='data_editor')

# # Layout for the bottom buttons
# col4, col5, col6 = st.columns([1, 1, 1])
# with col4:
#     if st.button('Save rule'):
#         if edited_df['Select'].any():
#             save_selected_rows(edited_df)
#             st.session_state.feedback_df = get_feedback_data()  # Refresh feedback table
#             st.success('Selected rows have been saved to user_feedback.csv')
#         else:
#             st.warning('No rows selected')

# with col5:
#     if st.button('Delete rule'):
#         if edited_df['Select'].any():
#             st.session_state.df = delete_selected_rows(edited_df)
#             st.success('Selected rows have been deleted')
#         else:
#             st.warning('No rows selected')

# with col6:
#     if st.button('Run Model'):
#         try:
#             subprocess.run(['python', 'C:/Users/Aravindan/aigs/ml_model.py'], check=True)
#             st.success('Model script has run successfully.')
#         except subprocess.CalledProcessError as e:
#             st.error(f"Failed to run model script: {e}")

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
# st.subheader('Ask GenAI')

# user_input = st.text_input('Enter your question for GenAI:', '')
# if st.button('Submit to GenAI'):
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



# # # import streamlit as st
# # # import pandas as pd
# # # import subprocess
# # # import warnings
# # # import google.generativeai as genai

# # # # Suppress specific warnings
# # # warnings.filterwarnings('ignore')

# # # # Configure the Google Generative AI
# # # api_key = "AIzaSyDnWLKJfJvEP0CQqFspQEij0iK-iVnxqww"  # Use the actual API key
# # # genai.configure(api_key=api_key)

# # # # Define the model configuration
# # # generation_config = {
# # #     "temperature": 0.9,
# # #     "top_p": 1,
# # #     "top_k": 1,
# # #     "max_output_tokens": 2048
# # # }

# # # safety_settings = [
# # #     {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
# # #     {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
# # #     {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
# # #     {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"}
# # # ]

# # # model = genai.GenerativeModel(model_name="gemini-1.0-pro",
# # #                               generation_config=generation_config,
# # #                               safety_settings=safety_settings)

# # # # Function to get model response
# # # def get_model_response(input_text):
# # #     convo = model.start_chat(history=[{"role": "user", "parts": [input_text]}])
# # #     convo.send_message(input_text)
# # #     return convo.last.text

# # # # Load data function
# # # def load_data(file_path):
# # #     return pd.read_csv(file_path)

# # # # Function to save selected rows to user_feedback.csv
# # # def save_selected_rows(df):
# # #     selected_df = df[df['Select'] == True]
# # #     selected_df.drop(columns=['Select'], inplace=True)
# # #     selected_df.to_csv('C:/Users/Aravindan/aigs/user_feedback.csv', index=False)

# # # # Function to delete selected rows
# # # def delete_selected_rows(df):
# # #     df = df[df['Select'] == False]
# # #     return df

# # # # Initialize session state
# # # if 'df' not in st.session_state:
# # #     st.session_state.df = load_data('C:/Users/Aravindan/aigs/firewall_logs.csv')

# # # if 'rules_df' not in st.session_state:
# # #     st.session_state.rules_df = load_data('C:/Users/Aravindan/aigs/rules.csv')

# # # if 'feedback_df' not in st.session_state:
# # #     st.session_state.feedback_df = load_data('C:/Users/Aravindan/aigs/user_feedback.csv')

# # # if 'process' not in st.session_state:
# # #     st.session_state.process = None

# # # # App title
# # # st.title('Firewall Logs Management and AI Interaction System')

# # # # User input for AI model query
# # # st.sidebar.title("AI Query Panel")
# # # user_input = st.sidebar.text_input("Enter your query:", "")
# # # if st.sidebar.button('Get AI Response'):
# # #     if user_input:
# # #         try:
# # #             response = get_model_response(user_input)
# # #             st.sidebar.text_area("AI Response:", value=response, height=300)
# # #         except Exception as e:
# # #             st.sidebar.error(f"Error while getting response from AI: {str(e)}")
# # #     else:
# # #         st.sidebar.error("Please enter a query to get a response.")

# # # # Layout for the top buttons
# # # col1, col2, col3 = st.columns([1, 1, 1])
# # # with col1:
# # #     if st.button('Traffic'):
# # #         try:
# # #             if st.session_state.process is None or st.session_state.process.poll() is not None:
# # #                 st.session_state.process = subprocess.Popen(['python', 'C:/Users/Aravindan/aigs/firewall.py'])
# # #                 st.success('Traffic script is running in the background.')
# # #             else:
# # #                 st.error('A script is already running.')
# # #         except Exception as e:
# # #             st.error(f"Failed to run traffic script: {e}")

# # # with col2:
# # #     if st.button('Stop Traffic'):
# # #         if st.session_state.process is not None:
# # #             st.session_state.process.terminate()
# # #             st.success('Traffic script has been stopped.')
# # #         else:
# # #             st.error('No script is running.')

# # # with col3:
# # #     if st.button('Refresh'):
# # #         st.session_state.df = load_data('C:/Users/Aravindan/aigs/firewall_logs.csv')

# # # # Display the table with checkboxes for each row
# # # edited_df = st.data_editor(st.session_state.df, key='data_editor')

# # # # Layout for the bottom buttons
# # # col4, col5, col6 = st.columns([1, 1, 1])
# # # with col4:
# # #     if st.button('Save rule'):
# # #         if edited_df['Select'].any():
# # #             save_selected_rows(edited_df)
# # #             st.session_state.feedback_df = load_data('C:/Users/Aravindan/aigs/user_feedback.csv')
# # #             st.success('Selected rows have been saved to user_feedback.csv')
# # #         else:
# # #             st.warning('No rows selected')

# # # with col5:
# # #     if st.button('Delete rule'):
# # #         if edited_df['Select'].any():
# # #             st.session_state.df = delete_selected_rows(edited_df)
# # #             st.success('Selected rows have been deleted')
# # #         else:
# # #             st.warning('No rows selected')

# # # with col6:
# # #     if st.button('Run Model'):
# # #         try:
# # #             subprocess.run(['python', 'C:/Users/Aravindan/aigs/ml_model.py'], check=True)
# # #             st.success('Model script has run successfully.')
# # #         except subprocess.CalledProcessError as e:
# # #             st.error(f"Failed to run model script: {e}")

# # # # Display feedback.csv file as a table in between
# # # st.subheader('Feedback Rule Table')
# # # if st.button('Refresh Feedback Table'):
# # #     st.session_state.feedback_df = load_data('C:/Users/Aravindan/aigs/user_feedback.csv')
# # # st.write(st.session_state.feedback_df)

# # # # Display rules.csv file at the bottom
# # # st.subheader('Rules Table')
# # # if st.button('Refresh Rules Table'):
# # #     st.session_state.rules_df = load_data('C:/Users/Aravindan/aigs/rules.csv')
# # # st.write(st.session_state.rules_df)



import streamlit as st
import pandas as pd
import subprocess
import warnings
import google.generativeai as genai

# Suppress specific warnings
warnings.filterwarnings('ignore')

# Function to load data
def load_data(file_path):
    return pd.read_csv(file_path)

# Function to save selected rows to user_feedback.csv
def save_selected_rows(df):
    selected_df = df[df['Select'] == True]
    selected_df.drop(columns=['Select'], inplace=True)
    selected_df.to_csv('C:/Users/A7765/AI-Guard/user_feedback.csv', index=False)
    

# Function to delete selected rows
def delete_selected_rows(df):
    df = df[df['Select'] == False]
    return df

# Load firewall logs data
def get_firewall_logs():
    firewall_logs = load_data('C:/Users/A7765/AI-Guard/firewall_logs.csv')
    firewall_logs['Select'] = False
    return firewall_logs

# Load rules data
def get_rules_data():
    return load_data('C:/Users/A7765/AI-Guard/rules.csv')
    

# Load user feedback data
def get_feedback_data():
    return load_data('C:/Users/A7765/AI-Guard/user_feedback.csv')

# Initialize session state
if 'df' not in st.session_state:
    st.session_state.df = get_firewall_logs()

if 'rules_df' not in st.session_state:
    st.session_state.rules_df = get_rules_data()

if 'feedback_df' not in st.session_state:
    st.session_state.feedback_df = get_feedback_data()

if 'process' not in st.session_state:
    st.session_state.process = None

# Title of the app
st.title('Firewall Logs Table')

# Layout for the top buttons
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button('Traffic'):
        try:
            # First run the overwrite.py script
            # subprocess.run(['python', 'C:/Users/A7765/AI-Guard/overwrite.py'], check=True)
            
            # Then run the firewall.py script if not already running
            if st.session_state.process is None or st.session_state.process.poll() is not None:
                st.session_state.process = subprocess.Popen(['python', 'C:/Users/A7765/AI-Guard/firewall.py'])
                st.success('Traffic script is running in the background.')
            else:
                st.error('A script is already running.')
        except subprocess.CalledProcessError as e:
            st.error(f"Failed to run traffic script: {e}")

with col2:
    if st.button('Stop Traffic'):
        if st.session_state.process is not None:
            st.session_state.process.terminate()
            st.session_state.process = None  # Reset process state
            st.success('Traffic script has been stopped.')
        else:
            st.error('No script is running.')

with col3:
    if st.button('Refresh'):
        st.session_state.df = get_firewall_logs()

# Display the table with checkboxes for each row
edited_df = st.data_editor(st.session_state.df, key='data_editor')

# Layout for the bottom buttons
col4, col5, col6 = st.columns([1, 1, 1])

with col4:
    if st.button('Save rule'):
        if edited_df['Select'].any():
            save_selected_rows(edited_df)
            st.session_state.feedback_df = get_feedback_data()  # Refresh feedback table
            st.success('Selected rows have been saved to user_feedback.csv')
        else:
            st.warning('No rows selected')

with col5:
    if st.button('Delete rule'):
        if edited_df['Select'].any():
            st.session_state.df = delete_selected_rows(edited_df)
            st.success('Selected rows have been deleted')
        else:
            st.warning('No rows selected')

with col6:
    if st.button('Run Model'):
        try:
            subprocess.run(['python', 'C:/Users/A7765/AI-Guard/ml_model.py'], check=True)
            st.success('Model script has run successfully.')
        except subprocess.CalledProcessError as e:
            st.error(f"Failed to run model script: {e}")

# Display feedback.csv file as a table in between
st.subheader('Feedback Rule Table')

if st.button('Refresh Feedback Table'):
    st.session_state.feedback_df = get_feedback_data()

st.write(st.session_state.feedback_df)

# Display rules.csv file at the bottom
st.subheader('Rules Table')

if st.button('Refresh Rules Table'):
    st.session_state.rules_df = get_rules_data()

st.write(st.session_state.rules_df)

# GenAI conversation section
st.subheader('Ask GenAI')

user_input = st.text_input('Enter your question for GenAI:', '')
if st.button('Submit to GenAI'):
    try:
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

        model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config, safety_settings=safety_settings)
        convo = model.start_chat(history=[])
        convo.send_message(user_input)
        response = convo.last.text
        st.text_area('GenAI Response:', value=response, height=300)
    except Exception as e:
        st.error(f'Failed to connect to GenAI: {str(e)}')
