from django.contrib import admin

from .models import Question

class PollsAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'choice_one', 'choice_two', 'choice_three', 'votes_one', 'votes_two', 'votes_three')
admin.site.register(Question, PollsAdmin)

#admin.site.register(Question)