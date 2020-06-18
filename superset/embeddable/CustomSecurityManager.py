from .CustomAuthDBView import CustomAuthDBView
from .. import SupersetSecurityManager

class CustomSecurityManager(SupersetSecurityManager):
    
    # authdbview = CustomAuthDBView     # disabled for now

    def can_access(self, permission_name: str, view_name: str) -> bool:
        if self.appbuilder.app.config.get('DEFEAT_ALL_SECURITY'):
            return True
        return super().can_access(permission_name,view_name)
        
    def has_access(self, permission_name, view_name):
        if self.appbuilder.app.config.get('DEFEAT_ALL_SECURITY'):
            return True
        return super().has_access(permission_name,view_name)
