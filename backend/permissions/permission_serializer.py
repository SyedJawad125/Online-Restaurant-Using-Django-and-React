from .models import Role, Permission
from rest_framework.serializers import ModelSerializer
from user_auth.user_serializer import UserListingSerializer

class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields='__all__'

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['role_added_by_user'] = UserListingSerializer(instance.role_added_by_user).data if instance.role_added_by_user else None
    #     data['role_updated_by_user'] = UserListingSerializer(instance.role_updated_by_user).data if instance.role_updated_by_user else None
    #     return data
    
class PermissionSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields='__all__'

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['per_added_by_user'] = UserListingSerializer(instance.per_added_by_user).data if instance.per_added_by_user else None
    #     data['per_updated_by_user'] = UserListingSerializer(instance.per_updated_by_user).data if instance.per_updated_by_user else None
    #     return data
