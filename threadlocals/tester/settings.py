# Stripped-down Django settings for testrunner

DEBUG = True

SECRET_KEY = 'NOT_SO_SECRET'

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'threadlocals.middleware.ThreadLocalMiddleware'
]

TEST_RUNNER = 'testrunner.NoDbTestRunner'
ROOT_URLCONF = 'threadlocals.tester.urls'
INSTALLED_APPS = [
    'threadlocals.tester',
]
