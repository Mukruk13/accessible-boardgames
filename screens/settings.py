# screens/settings.py

from typing import Any

from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView

from screens.base_screen import BaseScreen

from logic.commands.update_config import update_config_item
from logic.commands.set_voice_speed import set_voice_speed
from logic.commands.set_voice_volume import set_voice_volume
from logic.queries.get_translations import get_language_names


class SettingsScreen(BaseScreen):
    """
    Screen for adjusting application settings including language, voice, and accessibility options.
    """

    speak_on_enter_key: str = "settings.settings_title"

    def __init__(self, **kwargs: Any) -> None:
        """
        Initializes the settings screen and builds its UI layout.
        """
        super().__init__(**kwargs)
        self.build_ui()

    def build_ui(self) -> None:
        """
        Constructs the layout and components for the settings interface.

        Bonus tip:
        Wrapping the main layout inside a ScrollView allows scrolling
        if the content is too long for the screen.
        """
        # Create the main vertical BoxLayout with padding and spacing
        self.main_layout = BoxLayout(orientation="vertical", padding=20, spacing=30, size_hint_y=None)
        # Set minimum height to allow scrolling properly
        self.main_layout.bind(minimum_height=self.main_layout.setter("height"))

        # Navigation & UI Section
        self.nav_ui_label = Label(markup=True, size_hint_y=None, height=30)
        self.back_style_label = Label(size_hint_y=None, height=30)
        self.font_size_label = Label(size_hint_y=None, height=30)
        nav_ui_section = BoxLayout(orientation="vertical", spacing=10, size_hint_y=None)
        nav_ui_section.bind(minimum_height=nav_ui_section.setter("height"))
        nav_ui_section.add_widget(self.nav_ui_label)
        nav_ui_section.add_widget(self.back_style_label)
        nav_ui_section.add_widget(self.font_size_label)

        # Accessibility Section
        self.accessibility_label = Label(markup=True, size_hint_y=None, height=30)
        self.voice_speed_label = Label(size_hint_y=None, height=30)
        self.voice_speed_slider_label = Label(size_hint_y=None, height=30)
        self.voice_speed_slider = Slider(
            min=100,
            max=300,
            value=100,
            step=5,
            size_hint=(1, None),
            height=50
        )
        self.voice_speed_slider.bind(value=self.on_voice_speed_change)
        self.voice_volume_label = Label(size_hint_y=None, height=30)
        self.voice_volume_slider_label = Label(size_hint_y=None, height=30)
        self.voice_volume_slider = Slider(
            min=0,
            max=100,
            value=100,
            step=1,
            size_hint=(1, None),
            height=50
        )
        self.voice_volume_slider.bind(value=self.on_voice_volume_change)

        self.contrast_label = Label(size_hint_y=None, height=30)
        self.tts_toggle_button = Button(size_hint=(1, None), height=50)
        self.tts_toggle_button.bind(on_release=self.toggle_tts)

        accessibility_section = BoxLayout(orientation="vertical", spacing=10, size_hint_y=None)
        accessibility_section.bind(minimum_height=accessibility_section.setter("height"))
        accessibility_section.add_widget(self.accessibility_label)
        accessibility_section.add_widget(self.voice_speed_label)
        accessibility_section.add_widget(self.voice_speed_slider_label)
        accessibility_section.add_widget(self.voice_speed_slider)
        accessibility_section.add_widget(self.voice_volume_label)
        accessibility_section.add_widget(self.voice_volume_slider_label)
        accessibility_section.add_widget(self.voice_volume_slider)
        accessibility_section.add_widget(self.contrast_label)
        accessibility_section.add_widget(self.tts_toggle_button)

        # Language Section
        self.language_label = Label(markup=True, size_hint_y=None, height=30)
        self.language_spinner = Spinner(size_hint=(1, None), height=50)
        self.language_spinner.bind(text=self.set_language)
        language_section = BoxLayout(orientation="vertical", spacing=10, size_hint_y=None)
        language_section.bind(minimum_height=language_section.setter("height"))
        language_section.add_widget(self.language_label)
        language_section.add_widget(self.language_spinner)

        # Back Button
        self.back_button = Button(size_hint=(1, None), height=50)
        self.back_button.bind(on_release=lambda instance: self.navigate_to("main_menu"))
        back_section = BoxLayout(orientation="vertical", spacing=10, size_hint_y=None)
        back_section.bind(minimum_height=back_section.setter("height"))
        back_section.add_widget(self.back_button)

        # Add sections to main_layout
        self.main_layout.add_widget(nav_ui_section)
        self.main_layout.add_widget(accessibility_section)
        self.main_layout.add_widget(language_section)
        self.main_layout.add_widget(back_section)

        # Wrap main_layout in a ScrollView
        scroll_view = ScrollView(size_hint=(1, 1))
        scroll_view.add_widget(self.main_layout)

        # Add ScrollView to the screen instead of main_layout directly
        self.add_widget(scroll_view)

    def update_texts(self) -> None:
        """
        Refreshes all text elements on the screen to reflect the current language.
        """
        self._update_navigation_labels()
        self._update_accessibility_labels()
        self._update_language_spinner()
        self.set_text_from_key(self.back_button, "settings.back_to_main_menu")

    def _update_navigation_labels(self) -> None:
        self.set_text_from_key(
            self.nav_ui_label, "settings.nav_ui", markup=True, bold=True
        )
        self.set_text_from_key(self.back_style_label, "settings.back_style")
        self.set_text_from_key(self.font_size_label, "settings.font_size")

    def _update_accessibility_labels(self) -> None:
        self.set_text_from_key(
            self.accessibility_label,
            "settings.accessibility",
            markup=True,
            bold=True
        )
        self.set_text_from_key(self.voice_speed_label, "settings.voice_speed")
        self.set_text_from_key(self.voice_volume_label, "settings.voice_volume")
        self.set_text_from_key(self.contrast_label, "settings.contrast")
        self.update_tts_button_label()

        # Update voice speed slider and label
        voice_rate_percent = self.config.get("voice_rate_percent", 100)
        voice_rate_percent = max(100, min(300, voice_rate_percent))
        self.voice_speed_slider.value = voice_rate_percent
        self.voice_speed_slider_label.text = f"{voice_rate_percent}%"

        # Update voice volume slider and label
        voice_volume_percent = self.config.get("voice_volume_percent", 100)
        voice_volume_percent = max(0, min(100, voice_volume_percent))
        self.voice_volume_slider.value = voice_volume_percent
        self.voice_volume_slider_label.text = f"{voice_volume_percent}%"

    def _update_language_spinner(self) -> None:
        self.set_text_from_key(
            self.language_label, "settings.language", markup=True, bold=True
        )
        config_lang = self.config.get("language", "en")
        localized_names = get_language_names(config_lang)

        available_languages = {
            code: name for code, name in localized_names.items()
            if code != self.config["language"]
        }

        self.language_spinner.values = list(available_languages.values())
        self.language_spinner.text = localized_names.get(self.config["language"], "English")

    def set_language(self, spinner: Spinner, language_display_name: str) -> None:
        """
        Sets the application's language based on the user's selection.

        Args:
            spinner (Spinner): The spinner instance triggering the event.
            language_display_name (str): The display name of the selected language.
        """
        current_lang = self.config.get("language", "en")
        display_map = get_language_names(current_lang)
        reverse_map = {v: k for k, v in display_map.items()}

        lang_code = reverse_map.get(language_display_name)
        if not lang_code or lang_code == self.config["language"]:
            return

        update_config_item("language", lang_code)
        Clock.schedule_once(lambda dt: self.speak_key("meta.language_changed"), 0.1)

    def toggle_tts(self, instance: Any) -> None:
        """
        Toggles text-to-speech (TTS) on or off and announces the new state.

        Args:
            instance (Any): The widget instance that triggered the toggle.
        """
        current_state = self.config.get("tts_enabled", True)
        new_state = not current_state

        update_config_item("tts_enabled", new_state)
        self.update_tts_button_label()

        status_key = "meta.tts_turned_on" if new_state else "meta.tts_turned_off"
        Clock.schedule_once(lambda dt: self.speak_key(status_key, force=True), 0.1)

    def update_tts_button_label(self) -> None:
        """
        Updates the TTS toggle button label to reflect the current state.
        """
        is_enabled = self.config.get("tts_enabled", True)
        label_key = "settings.tts_on" if is_enabled else "settings.tts_off"
        self.set_text_from_key(self.tts_toggle_button, label_key)

    def on_voice_speed_change(self, slider: Slider, value: float) -> None:
        """
        Called when the voice speed slider is adjusted.

        Args:
            slider (Slider): The slider instance.
            value (float): The new value.
        """
        percent = int(value)
        self.voice_speed_slider_label.text = f"{percent}%"

        update_config_item("voice_rate_percent", percent)
        set_voice_speed(percent)

    def on_voice_volume_change(self, slider: Slider, value: float) -> None:
        percent = int(value)
        self.voice_volume_slider_label.text = f"{percent}%"
        update_config_item("voice_volume_percent", percent)
        set_voice_volume(percent)