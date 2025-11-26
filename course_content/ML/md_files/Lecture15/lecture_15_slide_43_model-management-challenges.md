# Slide 43 of Lecture 15 contains information about the Model Management Challenges.

• Model Definition: Difficult to define actual model to manage.
• Input data needs to be transformed into features expected by model.
• ML pipelines combines feature transformations and actual model in a single
abstraction.
• Model Validation: Ability to back-test accuracy performance of models over time (after
model gets update).
• Make use of same training, test and validation set including same evaluating
metrics.
• Model Retraining: Deciding when to retrain a model is challenging.
• Training is done offline and models are loaded at prediction in a system.
• If new events (new public holiday, a new promotional activity) occur that our models
have not been trained on, need to trigger retraining or even re-modelling.
