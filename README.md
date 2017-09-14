# melo
A multiplayer Elo scale, specifically designed for use in math contests.

The traditional Elo rating scale gives scores to competitors based on the aggregation of competitior-vs-competitor games. However, it does not work for multiplayer competitions, such as math contests. This algorithm computes a multiplayer Elo score by predicting how many competitors an individual should beat based on their present Elo and adjusting based on the number of competitors actually beat. It accounts for ties, with special consideration to ties at the maximum possible score of a contest. Furthermore, it takes the relative difficulty and quality of a competition to weight the scores accurately. 

In future commits, the algorithm will be cleaned up and data will be stored in a separate file.
