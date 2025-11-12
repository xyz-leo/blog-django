from site_setup.models import SiteSetup


def site_setup(request):
    """
    Context processor to add site setup information to the context.
    """
    setup = SiteSetup.objects.order_by('-id').first()

    return {
        'site_setup': setup,
    }
