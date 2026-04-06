from rest_framework.throttling import ScopedRateThrottle


class DashboardThrottle(ScopedRateThrottle):
    scope = 'dashboard'