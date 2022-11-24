from django.contrib import admin
from .models import Review


class ReviewEvaluationFilter(admin.SimpleListFilter):

    title = "Filter reviews by Rating"

    parameter_name = "evaluation_status"

    def lookups(self, request, model_admin):
        return [("good", "Good"), ("bad", "Bad")]

    def queryset(self, request, reviews):
        status = self.value()
        if status:
            if status == "good":
                return reviews.filter(rating__gte=3)
            else:
                return reviews.filter(rating__lte=2)
        else:
            return reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )

    list_filter = (ReviewEvaluationFilter,)
