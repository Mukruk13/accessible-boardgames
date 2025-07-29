# screens/settings/accessibility_section.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.clock import Clock

from logic.commands.update_config import update_config_item
from logic.commands.set_voice_speed import set_voice_speed
from logic.commands.set_voice_volume import set_voice_volume


class AccessibilitySection(BoxLayout):
    def __init__(self, screen, **kwargs):
        super().__init__(orientation="vertical", spacing=10, size_hint_y=None, **kwargs)
        self.bind(minimum_height=self.setter("height"))
        self.screen = screen
        self.config = screen.config

        self.accessibility_label = Label(markup=True, size_hint_y=None, height=30)

        self.voice_speed_label = Label(size_hint_y=None, height=30)
        self.voice_speed_slider_label = Label(size_hint_y=None, height=30)
        self.voice_speed_slider = Slider(min=100, max=300, value=100, step=5, size_hint=(1, None), height=50)
        self.voice_speed_slider.bind(value=self.on_voice_speed_change)

        self.voice_volume_label = Label(size_hint_y=None, height=30)
        self.voice_volume_slider_label = Label(size_hint_y=None, height=30)
        self.voice_volume_slider = Slider(min=0, max=100, value=100, step=1, size_hint=(1, None), height=50)
        self.voice_volume_slider.bind(value=self.on_voice_volume_change)

        self.contrast_label = Label(size_hint_y=None, height=30)
        self.tts_toggle_button = Button(size_hint=(1, None), height=50)
        self.tts_toggle_button.bind(on_release=self.toggle_tts)

        self.add_widget(self.accessibility_label)
        self.add_widget(self.voice_speed_label)
        self.add_widget(self.voice_speed_slider_label)
        self.add_widget(self.voice_speed_slider)
        self.add_widget(self.voice_volume_label)
        self.add_widget(self.voice_volume_slider_label)
        self.add_widget(self.voice_volume_slider)
        self.add_widget(self.contrast_label)
        self.add_widget(self.tts_toggle_button)

    def update_texts(self):
        self.screen.set_text_from_key(
            self.accessibility_label, "settings.accessibility", markup=True, bold=True
        )
        self.screen.set_text_from_key(self.voice_speed_label, "settings.voice_speed")
        self.screen.set_text_from_key(self.voice_volume_label, "settings.voice_volume")
        self.screen.set_text_from_key(self.contrast_label, "settings.contrast")
        self.update_tts_button_label()

        # Prevent triggering callbacks on initial setup
        rate = max(100, min(300, self.config.get("voice_rate_percent", 100)))
        self.voice_speed_slider.unbind(value=self.on_voice_speed_change)
        self.voice_speed_slider.value = rate
        self.voice_speed_slider.bind(value=self.on_voice_speed_change)
        self.voice_speed_slider_label.text = f"{rate}%"

        volume = max(0, min(100, self.config.get("voice_volume_percent", 100)))
        self.voice_volume_slider.unbind(value=self.on_voice_volume_change)
        self.voice_volume_slider.value = volume
        self.voice_volume_slider.bind(value=self.on_voice_volume_change)
        self.voice_volume_slider_label.text = f"{volume}%"

    def toggle_tts(self, instance):
        state = not self.config.get("tts_enabled", True)
        update_config_item("tts_enabled", state)
        self.update_tts_button_label()
        key = "meta.tts_turned_on" if state else "meta.tts_turned_off"
        Clock.schedule_once(lambda dt: self.screen.speak_key(key, force=True), 0.1)

    def update_tts_button_label(self):
        key = "settings.tts_on" if self.config.get("tts_enabled", True) else "settings.tts_off"
        self.screen.set_text_from_key(self.tts_toggle_button, key)

    def on_voice_speed_change(self, slider, value):
        percent = int(value)
        self.voice_speed_slider_label.text = f"{percent}%"
        update_config_item("voice_rate_percent", percent)
        set_voice_speed(percent)
        Clock.schedule_once(lambda dt: self.screen.speak_key("meta.speed_changed", value=percent), 0.1)

    def on_voice_volume_change(self, slider, value):
        percent = int(value)
        self.voice_volume_slider_label.text = f"{percent}%"
        update_config_item("voice_volume_percent", percent)
        set_voice_volume(percent)
        Clock.schedule_once(lambda dt: self.screen.speak_key("meta.volume_changed", value=percent), 0.1)

