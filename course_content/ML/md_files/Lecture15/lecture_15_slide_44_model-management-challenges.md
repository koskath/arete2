# Slide 44 of Lecture 15 contains information about the Model Management Challenges.

• Data Management Challenges: data integration, feature transformation, model
training apply different operations based on different abstractions.
• Querying model Metadata to select best model: To accelerate model lifecycle
management, need to understand metadata and lineage of models
(e.g., hyperparameters, trained and validated datasets).
• Centralized metadata store can accelerate learning processes (e.g., warm-
starting of hyperparameter search) and automate simple error checks.
• Multi-Language Code Bases
• Backwards Compatibility: Model that was trained (last month or last year) should still
be working today (required for production deployments).
