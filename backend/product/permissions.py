from rest_framework import permissions

'''
    what we did here is to overite the method in the class we inherite from

    not the framework grant permission bass on the return value of this method.
    it look like the method has_permission grant the user permission in general 
    and the has_permission grant the use object permission's
'''

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
    # def has_permission(self, request, view):
    #     if not request.user.is_staff:
    #         return False
    #     return super().has_permission(request, view)
        
'''
    now to solve the problem of custom permission is simple to 
    argument this perms_map which we have access to since we inherite 
    from the djangomodelpemissions 
    perms_map = {
        'GET': [],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
    that is simple as that

'''

    
    # def has_permission(self, request, view):
    #     user = request.user
    #     print(user.get_all_permissions()) 
    #     if request.user.is_staff:
    #         if user.has_perm('product.add_product'):
    #             '''
    #                 this is the standard format <app_name>.<action>_<productNameInLoweCase>
    #                 when making use of the methode has_perm()
                    
    #             '''
    #             return True

    #         if user.has_perm('product.change_product'):
    #             return True
            
    #         if user.has_perm('product.delete_product'):
    #             return True
            
    #         if user.has_perm("product.view_product"):
    #             return True

    #         print('didnt work')
    #         return False
    #     return False
'''
 not if after setting this and the permission refuse to complie 
 chack the syntac in the has_perm() method in the user,
 in other to view the correct synthax print(user.get_all_permissions()) 
 this will return the all the permission of the user in there correct syntax
 set in the admin's

 not the proble with this is that it not doing the permission correctyl
 the user is only given the view_product but instead on the browser session
 he can perform update.

 the reason fro this is that the view is inheriting from a class that 
 have meany views (mixin) with default permission's for each inherent view

 and also for any permission condission chack it return true, but what we want
 is a specific action to be carried out
 '''


    # def has_object_permission(self, request, view, obj):
    #     return obj.owner == request.user