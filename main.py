from gettext import translation
import deep_translator

translator = deep_translator.GoogleTranslator(source='ru', target='en')
print(translator.translate('корова'))