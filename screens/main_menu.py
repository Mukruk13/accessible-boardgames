from screens.base_screen import BaseScreen

class MainMenuScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.spoken = False
        layout = BoxLayout(orientation='vertical', spacing=20, padding=50)

        btn_select = Button(text='Wybierz grę')
        btn_add = Button(text='Dodaj nową grę')
        btn_settings = Button(text='Ustawienia')

        btn_select.bind(on_release=lambda x: self.navigate_to('select_game'))
        btn_add.bind(on_release=lambda x: self.navigate_to('add_game'))
        btn_settings.bind(on_release=lambda x: self.navigate_to('settings'))

        layout.add_widget(btn_select)
        layout.add_widget(btn_add)
        layout.add_widget(btn_settings)

        self.add_widget(layout)

    def on_enter(self):
        if not self.spoken:
            self.speak("Witaj! Wybierz grę, dodaj nową lub przejdź do ustawień.")
            self.spoken = True
