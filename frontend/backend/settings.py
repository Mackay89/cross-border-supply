NSTALLED_APPS = [
            ...
                'rest_framework',
                    'api',
                    ]

REST_FRAMEWORK = {
            'DEFAULT_AUTHENTICATION_CLASSES': [
                        'rest_framework_simplejwt.authentication.JWTAuthentication',
                            ],
            }

# Add necessary CORS settings
CORS_ALLOW_ALL_ORIGINS = True

