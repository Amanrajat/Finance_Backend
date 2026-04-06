from rest_framework.throttling import ScopedRateThrottle

class RecordThrottle(ScopedRateThrottle):
    scope = 'records'

class RecordWriteThrottle(ScopedRateThrottle):
    scope = 'records_write'