class CpCollabNetRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'collabs':
            return 'cpcollabnet'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'collabs':
            return 'cpcollabnet'
        return 'default'
