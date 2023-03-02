class ModelSignalTransceiver:

    def pre_init(self, **kwargs):
        pass

    def post_init(self, **kwargs):
        pass

    def pre_save(self, **kwargs):
        pass

    def post_save(self, **kwargs):
        pass

    def pre_delete(self, **kwargs):
        pass

    def post_delete(self, **kwargs):
        pass

    def m2m_changed(self, **kwargs):
        pass

    class ModelSignalMeta:
        signals = []
