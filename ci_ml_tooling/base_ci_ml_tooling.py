'Base class providing a common structure for calling the single tools and methods'

DATA_NEEDED_FOR_TOOLING = {
    'weigthwatcher': False,
    'giskard': True,
    'deepchecks': True,
    'SHAP': True
}

class MlModel:
    def __init__(
            self,
            model_instance = None
    ):
        self.model_instance = model_instance


class BaseCiMlTooling:
    '''
    Class for providing a base for the interaction of data, model and tooling.
    '''
    def __init__(
            self,
            models: list(MlModel),
            data = None,
            tools: list(str) = ['all'],
    ):
        self.data = data
        self.models = models
        self.tools = tools


    def _check_models(self):
        for model in self.models:
            if model.model_instance is None:
                raise ValueError
            
    
    def _check_data(self):
        if self.data is None and any([
           [DATA_NEEDED_FOR_TOOLING[x] for x in self.tools]
        ]):
            raise ValueError
