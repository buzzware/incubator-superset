from superset.embeddable.CustomSecurityManager import CustomSecurityManager

CUSTOM_SECURITY_MANAGER = CustomSecurityManager     # specify our CustomSecurityManager in order to implement these extensions

PUBLIC_ROLE_LIKE_GAMMA = True   # standard superset option - public users have some access (or none)

DEFEAT_ALL_SECURITY = True      # !!!WARNING!!! literally no security if True - This is as bad as it sounds
