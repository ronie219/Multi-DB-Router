app_list = ['product2', 'product3', 'product4', 'product5']


class ProductRouter:

    def db_for_read(self, model, **hints):

        if model._meta.app_label in app_list:
            return str(model._meta.app_label)
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in app_list:
            return model._meta.app_label
        return None

    def allow_relation(self, obj1, obj2, **hints):

        if obj1._meta.app_label in app_list or \
                obj2._meta.app_label in app_list:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in app_list:
            return db in app_list
        return None
