from project.settings import INSTALLED_APPS, ALLOWED_HOSTS, BASE_DIR
import os

INSTALLED_APPS.append( 'webpack_loader',)
INSTALLED_APPS.append( 'app',)

ALLOWED_HOSTS.append('*',)

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, 'static',)
    os.path.join(BASE_DIR, 'app', 'vueapp','dist', 'static')
]

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'static/vueapp/',
        'STATS_FILE': os.path.join(BASE_DIR, 'app', 'vueapp', 'webpack-stats.json')
    }
}

INTERNAL_IPS = (
    '0.0.0.0',
    '127.0.0.1',
)