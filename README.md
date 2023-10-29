# ci_tooling_for_ml

Repository with tooling for continuous integration (CI) of Machine Learning (ML) models.

Assessing the performance inside a CI pipeline of a ML model poses a challenge in comparison to CI pipelines for pure code. In the case of ML we have three degress of freedom (data, ML model, code) which may change from one CI pipeline execution to the other compared to the one degree of freedom in classical software enginnering where only the source code may change and needs to be tested.

This repository gives an overview of packages available for specialized CI tooling for ML use cases and functionality for seamlessly integrating these tooling in CI pipelines.

## Methods and packages

Overview about the used methods and packages in this repository. Data agnostic methods (wokring only on the model itself), methods evaluating data and model combined and, as a special case, the usage of eXplainable AI methods as a tool for continuous integration for Machine Learning models.

### Data agnostic

Data agnostic methods try to assess the ML model performance solely on the model itself.

Packages:
- [weightwatcher](https://pypi.org/project/weightwatcher/)

### Data and model combination evaluation

These methods use the combination of data and the model to assess the model performance by identifying shortcomings in the data itself.

Packages:
- [Giskard](https://pypi.org/project/giskard/)
- [deepchecks](https://pypi.org/project/deepchecks/)

#### Adveserial methods

Adveserial methods are a peculiarity for evaluating a ML model and the data used training it. By 

### Explainable AI (XAI)

XAI methods aim at explaining the predictions of a ML model. Indepent of the used methods the result is an estimation of the importance of features for the model prediction which can be used as a CI tool. Here, the ML model can be checked against domain expertise or if the ML model focuses on outlier data points.

Packages:
- [SHAP](https://pypi.org/project/shap/)
