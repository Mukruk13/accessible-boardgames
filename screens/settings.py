#screens/settings.py

from screens.base_screen import BaseScreen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.clock import Clock
from kivy.uix.button import Button

from services.voice_reader import speak, set_voice_for_language

from utils.translations import translations, language_display_map, reverse_language_display_map
from utils.config import save_config, load_config


class SettingsScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        config = load_config()
        self.selected_language = config.get("language", "en")
        self.lang_data = translations.get(self.selected_language, translations["en"])

        self.main_layout = BoxLayout(orientation='vertical', padding=20, spacing=30)
        self.build_ui()
        self.add_widget(self.main_layout)

    def on_enter(self):
        Clock.schedule_once(lambda dt: self.speak(self.lang_data["settings_title"]), 0.1)

    def build_ui(self):
        self.main_layout.clear_widgets()

        # Navigation & UI Section
        nav_ui_section = BoxLayout(orientation='vertical', spacing=10)
        nav_ui_section.add_widget(Label(text=f"[b]{self.lang_data['nav_ui']}[/b]", markup=True))
        nav_ui_section.add_widget(Label(text=self.lang_data["back_style"]))
        nav_ui_section.add_widget(Label(text=self.lang_data["font_size"]))

        # Accessibility Settings
        accessibility_section = BoxLayout(orientation='vertical', spacing=10)
        accessibility_section.add_widget(Label(text=f"[b]{self.lang_data['accessibility']}[/b]", markup=True))
        accessibility_section.add_widget(Label(text=self.lang_data["voice_speed"]))
        accessibility_section.add_widget(Label(text=self.lang_data["contrast"]))

        # Language Section
        language_section = BoxLayout(orientation='vertical', spacing=10)
        language_section.add_widget(Label(text=f"[b]{self.lang_data['language']}[/b]", markup=True))

        display_name = reverse_language_display_map.get(self.selected_language, "English")

        self.language_spinner = Spinner(
            text=display_name,
            values=list(language_display_map.keys()),
            size_hint=(1, None),
            height=50
        )

        self.language_spinner.bind(text=self.set_language)
        language_section.add_widget(self.language_spinner)

        # Back button Section:
        back_button_section = BoxLayout(orientation='vertical', spacing=10)
        back_button = Button(text=self.lang_data['back_to_main_menu'], size_hint=(1, None), height=50)
        back_button.bind(
            on_release=lambda instance: self.navigate_to('main_menu'))
        back_button_section.add_widget(back_button)

        self.main_layout.add_widget(nav_ui_section)
        self.main_layout.add_widget(accessibility_section)
        self.main_layout.add_widget(language_section)
        self.main_layout.add_widget(back_button_section)

    def set_language(self, spinner, language_name):
        lang_code = language_display_map.get(language_name)
        if not lang_code:
            print(f"Unsupported language: {language_name}")
            return

        self.selected_language = lang_code
        self.lang_data = translations[lang_code]

        set_voice_for_language(lang_code)

        # Save to config
        save_config({"language": lang_code})

        # Update other screens if needed
        if self.manager:
            try:
                main_menu = self.manager.get_screen('main_menu')
                main_menu.set_language(lang_code)
            except Exception as e:
                print(f"Main menu screen not found or error: {e}")

        # self.speak(f"Language set to {language_name}")
        print("Language change")
        # speak(self.lang_data.get("language_changed"))
        Clock.schedule_once(lambda dt: self.speak(self.lang_data['language_changed']), 0.1)


        self.build_ui()

