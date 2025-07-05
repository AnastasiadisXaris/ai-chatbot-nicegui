import os
from nicegui import ui
from chatbot import get_bot_response

chat_history = []

def send():
    message = input_box.value.strip()
    if not message:
        return
    ui.chat_message(message, name='Εσύ', avatar='👤')
    response = get_bot_response(message)
    ui.chat_message(response, name='AI Bot', avatar='🤖')
    input_box.value = ''

ui.label('🤖 AI Chatbot με NiceGUI και Hugging Face (υποστηρίζει Ελληνικά)')
input_box = ui.input(placeholder='Γράψε το μήνυμά σου εδώ...').on('keydown.enter', send)
ui.button('Αποστολή', on_click=send)

ui.run(host='0.0.0.0', port=int(os.getenv('PORT', 8080)))
