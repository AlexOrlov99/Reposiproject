from . import get_env_variable

SECRET_KEY = get_env_variable('SECRET_KEY')
ADMIN_SITE_URL = get_env_variable('ADMIN_SITE_URL')
AUTH_USER_MODEL = get_env_variable('AUTH_USER_MODEL')

# ---------------------------------------------------------
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]
DEBUG_TOOLBAR_PATCH_SETTINGS = False

# ---------------------------------------------------------
SHELL_PLUS_PRE_IMPORTS = [
    ('django.db', ('connection', 'reset_queries', 'connections')),
    ('datetime', ('datetime', 'timedelta', 'date')),
    ('json', ('loads', 'dumps')),
]

SHELL_PLUS_MODEL_ALIASES = {
    'auths':{
        'CustomUser':'U',
    },
    'firstapp': {
        'Student': 'S',
        'File': 'F',
        'Homework': 'H',
        'Group': 'G',
        'Professor': 'P',
    },
}
SHELL_PLUS = 'Ipython'
SHELL_PLUS_PRINT_SQL = True
SHELL_PLUS_PRINT_SQL_TRUNCATE = 1000
# ---------------------------------------------------------