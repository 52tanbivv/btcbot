version = "0.1 beta"
prompt = "(Cmd)"
histfile = "/tmp/history"


class global_vars(dict):
    def __init__(self, g_vars={}):
        self['api1'] = 'exsimu1'
        self['api2'] = 'exsimu2'
        self['prompt'] = prompt
        self['version'] = version
        self['histfile'] = histfile
        self.update(g_vars)
