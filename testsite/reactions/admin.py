from django.contrib import admin

from .models import ImageReaction, TweetReaction


class ReactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'reacted_to', 'deleted')
    list_filter = ('deleted', )

    actions = ['delete_selected', 'undelete_selected']

    def undelete_selected(self, request, objs):
        objs.update(deleted=False)

    def delete_selected(self, request, objs):
        objs.update(deleted=True)

    delete_selected.short_description = "Delete selected Reactions"
    undelete_selected.short_description = "Undelete selected Reactions"


admin.site.register(ImageReaction, ReactionAdmin)
admin.site.register(TweetReaction, ReactionAdmin)
