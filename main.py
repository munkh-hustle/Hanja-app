from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
import csv

# Load dictionary from CSV file with UTF-8 encoding
def load_dictionary():
    dictionary = {}
    with open('test_data_100.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            korean, hanja, mongolian = row
            dictionary[hanja] = {'표제어': korean, '몽골어 대역어': mongolian}
    return dictionary

# Load data at app start
dictionary_data = load_dictionary()

def get_entry(hanja_character):
    return dictionary_data.get(hanja_character, None)

class DictionaryApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        # Text input for searching
        self.search_input = TextInput(hint_text="Enter Hanja Character", size_hint=(1, 0.1))
        self.layout.add_widget(self.search_input)
        
        # Button to trigger search
        search_button = Button(text="Search", size_hint=(1, 0.1))
        search_button.bind(on_press=self.search_hanja)
        self.layout.add_widget(search_button)
        
        # Labels for displaying results using different fonts
        self.result_label_hanja = Label(text="Hanja Result",
                                        font_name='NotoSansCJK-Regular.ttf',  # Font for Hanja/Korean
                                        font_size='20sp', size_hint=(1, 0.3))
        self.layout.add_widget(self.result_label_hanja)
        
        self.result_label_mongolian = Label(text="Mongolian Result",
                                            font_name='NotoSans-Regular.ttf',  # Font for Mongolian
                                            font_size='20sp', size_hint=(1, 0.3))
        self.layout.add_widget(self.result_label_mongolian)
        
        return self.layout
    
    def search_hanja(self, instance):
        hanja = self.search_input.text
        entry = get_entry(hanja)
        if entry:
            self.result_label_hanja.text = f"Hanja: {hanja}\nKorean: {entry['표제어']}"
            self.result_label_mongolian.text = f"Mongolian: {entry['몽골어 대역어']}"
        else:
            self.result_label_hanja.text = "Hanja character not found."
            self.result_label_mongolian.text = "Mongolian translation not found."

if __name__ == '__main__':
    DictionaryApp().run()
