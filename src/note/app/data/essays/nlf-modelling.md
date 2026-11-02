---
tags: [miscellanea, model]
---

# NLF Modelling

## Index

## Goal

NFL modeling aims to **predict, explain, or simulate aspects of football games**. Common goals include:

- **Player movement prediction**: Forecast where players will move on the field in the next few seconds.
- **Win probability**: Estimate the likelihood that a team will win at any point during a game.
- **Play success models**: Predict outcomes of a play (e.g., yards gained, first downs, touchdowns).
- **Injury risk modeling**: Predict likelihood of injuries for players based on movement, impact, and workload.
- **Team strategy optimization**: Identify optimal play-calling strategies based on opponents.

## Model Type

### a) Player Movement Models

- **Physics-based models**: Use kinematics to predict movement.
- **Deep learning**: RNNs, LSTMs, or Transformers to capture sequences of player positions.
- **Graph neural networks**: Model interactions between players as a dynamic graph.

### b) Win Probability Models

- **Logistic regression**: Classic model using score, time, down, distance.
- **Gradient boosting / XGBoost**: Handles non-linear interactions effectively.
- **Neural networks**: Can capture complex patterns in game state.

### c) Play Outcome Models

- **Expected Points Added (EPA)**: Quantifies the value of each play toward winning.
- **Success rate models**: Binary classification for play success (e.g., gaining a first down).

## References

- https://www.youtube.com/watch?v=3t6hM5tRlfA
- https://www.youtube.com/watch?v=uM9iLQJzMO0
- https://www.samford.edu/sports-analytics/fans/2023/How-I-Built-a-Competitive-NFL-Prediction-Model-with-Only-Five-Statistics
- https://medium.com/draftkings-engineering/modeling-football-combining-ml-models-and-monte-carlo-simulations-170fd58cbe11
- https://www.kaggle.com/competitions/nfl-big-data-bowl-2026-prediction/overview

## Provenance

- Notion export: `Modelo/Miscellanea/Miscellanea/NLF Modelling 27ac0f5171ec80bf86bcc7e406fe68af.md`
