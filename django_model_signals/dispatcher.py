class ModelSignalDispatcher:

    @staticmethod
    def pre_init(sender, **kwargs):
        kwargs['instance'].pre_init(**kwargs)

    @staticmethod
    def post_init(sender, **kwargs):
        kwargs['instance'].post_init(**kwargs)

    @staticmethod
    def pre_save(sender, **kwargs):
        kwargs['instance'].pre_save(**kwargs)

    @staticmethod
    def post_save(sender, **kwargs):
        kwargs['instance'].post_save(**kwargs)

    @staticmethod
    def pre_delete(sender, **kwargs):
        kwargs['instance'].pre_delete(**kwargs)

    @staticmethod
    def post_delete(sender, **kwargs):
        kwargs['instance'].post_delete(**kwargs)

    @staticmethod
    def m2m_changed(sender, **kwargs):
        kwargs['instance'].m2m_changed(**kwargs)
