from django.dispatch import receiver
from pretix.plugins.ticketoutputpdf.signals import register_fonts


@receiver(register_fonts, dispatch_uid="fontpack_free_fonts")
def fontpack_free(sender, **kwargs):
    basepath = "pretix_fontpackfree"

    return {
        "Inconsolata": {
            "regular": {
                "woff2": basepath + "/Inconsolata-Regular.woff2",
                "truetype": basepath + "/Inconsolata-Regular.ttf",
            },
            "bold": {
                "woff2": basepath + "/Inconsolata-Bold.woff2",
                "truetype": basepath + "/Inconsolata-Bold.ttf",
            },
        },
    }
