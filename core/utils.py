from crum import get_current_user   # third party package

# to save currently logged in user by model itself
def auto_save_current_user(obj):
    user = get_current_user()
    if user and not user.pk:    # security check
        user = None
    if not obj.pk:
        obj.user = user