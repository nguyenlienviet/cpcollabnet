class CpCollabNetRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'collabs':
            if model._meta.model_name == 'pubsubmission':
                return 'default'
            return 'cpcollabnet'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'collabs':
            if model._meta.model_name == 'pubsubmission':
                return 'default'
            return 'cpcollabnet'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'cpcollabnet':
            return False
        return None
