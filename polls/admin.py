from django.contrib import admin

from .models import Question, Choice


# Instead of calling the Choice model in the register() call, we can add a new class to make the page easier to read when more choice fields are needed
class ChoiceInline(admin.TabularInline):
    model = Choice
    # Dictates the number of question choices that can be added at a time
    extra = 2


# Sets the order of the questions on the admin site
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        # The None element essentially skips adding a header
        (None,               {'fields': ['question_text']}),
        # The Date information element adds a page element that acts as a "title" for the question
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    # Sets the table column order of the admin panel
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # Filters the rows in the Questions panel by Published Date
    # Since pub_date is a DateTime, Django auto-populates a filtering modal with appropriate choices
    list_filter = ['pub_date']
    # Adds a search bar
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
