from rest_framework import permissions

from product.permissions import IsStaffEditorPermission

class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]


class UserQuerySetMixin():
    user_field = 'user'
    allow_staff_view = False 
    def get_queryset(self, *args, **kwargs):
        lookup_data = {}
        lookup_data[self.user_field] = self.request.user
        print('this...........',self.request.user)
        qs = super().get_queryset(*args, **kwargs)
        user = self.request.user
        if self.allow_staff_view and user.is_staff:# this decide if the staff user is to all the query including those that dont belong to him
            return qs
        return qs.filter(**lookup_data)