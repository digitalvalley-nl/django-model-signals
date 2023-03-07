class ModelSignalsTransceiver:

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

    @classmethod
    def pre_bulk_save(cls, **kwargs):
      pass

    @classmethod
    def post_bulk_save(cls, **kwargs):
      pass

    class ModelSignalsMeta:
        signals = []
