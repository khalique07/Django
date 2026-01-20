from django.contrib import admin
from .models import Form

class FormAdmin(admin.ModelAdmin):
    """
    Customized admin interface for Form model
    """
    # Display these fields in the list view
    list_display = ("first_name", "last_name", "email")
    
    # Add search functionality
    search_fields = ("first_name", "email")
    
    # Add filter sidebar
    list_filter = ("date", "occupation")
    
    # Default ordering (use - for descending)
    ordering = ("first_name",)
    
    # Make specific fields read-only
    readonly_fields = ("occupation",)

# Register model with custom admin class
admin.site.register(Form, FormAdmin)
