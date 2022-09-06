from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests
from random import randint
import uuid

Builder.load_file('frontend.kv')


class FirstScreen(Screen):
    def get_image_link(self):
        # Get the text from the Text Widget
        query = self.manager.current_screen.ids.user_query.text

        # Search on wikipedia
        page = wikipedia.page(query, auto_suggest=False)

        # Catch a random image link
        image_link = page.images[randint(0, (len(page.images)-1))]
        return image_link

    def download_image(self):
        # Download the image
        headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
        }
        response = requests.get(self.get_image_link(), headers=headers)

        # Save it
        image_path = f"images/image_{uuid.uuid4()}.jpg"
        with open(image_path, "wb") as file:
            file.write(response.content)
        return image_path

    def search_image(self):
        # Show it
        self.manager.current_screen.ids.img.source = self.download_image()


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()