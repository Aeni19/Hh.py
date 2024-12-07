from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from plyer import notification
from datetime import datetime, timedelta
from threading import Timer

class NotifyHubApp(App):
    def build(self):
        # Main layout
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Title input
        self.title_input = TextInput(hint_text='Enter notification title', multiline=False)
        self.layout.add_widget(self.title_input)

        # Message input
        self.message_input = TextInput(hint_text='Enter notification message', multiline=False)
        self.layout.add_widget(self.message_input)

        # Time delay input (in seconds)
        self.time_input = TextInput(hint_text='Enter delay in seconds', multiline=False, input_filter='int')
        self.layout.add_widget(self.time_input)

        # Submit button
        self.submit_button = Button(text='Set Notification', on_press=self.set_notification)
        self.layout.add_widget(self.submit_button)

        # Status label
        self.status_label = Label(text='')
        self.layout.add_widget(self.status_label)

        return self.layout

    def set_notification(self, instance):
        try:
            title = self.title_input.text
            message = self.message_input.text
            delay = int(self.time_input.text)

            if not title or not message or delay <= 0:
                self.status_label.text = 'All fields must be valid!'
                return

            # Schedule notification
            self.status_label.text = f'Notification set for {delay} seconds from now.'
            Timer(delay, self.send_notification, args=(title, message)).start()
        except ValueError:
            self.status_label.text = 'Invalid input for delay!'

    def send_notification(self, title, message):
        notification.notify(
            title=title,
            message=message,
            app_name='NotifyHub'
        )
        self.status_label.text = 'Notification sent!'

if __name__ == '__main__':
    NotifyHubApp().run()
