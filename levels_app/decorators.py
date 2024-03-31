from django.http import HttpResponseForbidden

from levels_app.models import Level


def level_up_ownership_required(func):
    def decorated(request, *args, **kwargs):
        level = Level.objects.get(pk=kwargs['pk'])
        if not level.user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated