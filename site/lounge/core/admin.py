from django.contrib import admin
from models import Lounge, Topic, Comment, Tag

class LoungeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Lounge, LoungeAdmin)

class TopicAdmin(admin.ModelAdmin):
    pass
admin.site.register(Topic, TopicAdmin)

class CommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Comment, CommentAdmin)

class TagAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tag, TagAdmin)