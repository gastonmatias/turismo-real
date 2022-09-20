from django.contrib import admin

# para poder borrar users qe tengan token valido activo (https://stackoverflow.com/questions/40604877/how-to-delete-a-django-jwt-token)
#class OutstandingTokenAdmin(token_blacklist.admin.OutstandingTokenAdmin):
#    def has_delete_permission(self, *args, **kwargs):
#        return True # or whatever logic you want
#
#admin.site.unregister(token_blacklist.models.OutstandingToken)
#admin.site.register(token_blacklist.models.OutstandingToken, OutstandingTokenAdmin)   