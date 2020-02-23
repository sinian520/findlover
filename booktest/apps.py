from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class BooktestConfig(AppConfig):
    name = 'booktest'
class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'