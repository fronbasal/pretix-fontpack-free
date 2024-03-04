from django.apps import AppConfig
from . import __version__


class PluginApp(AppConfig):
    name = 'pretix_fontpackfree'
    verbose_name = 'Fontpack: Free fonts'

    class PretixPluginMeta:
        name = 'Fontpack: Free fonts (+ Inconsolata)'
        author = 'Raphael Michel & Daniel Malik'
        description = 'Pack of free fonts for pretix + Inconsolata'
        visible = False
        version = __version__
        compatibility = "pretix>=4.16.0"

    def ready(self):
        from . import signals  # NOQA

