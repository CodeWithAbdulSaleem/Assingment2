# 🎮 Grid World Game using Reinforcement Learning (Policy Iteration)

## 📌 Problem Statement

Design a small game where an agent learns to reach a goal while avoiding penalties using **Reinforcement Learning (Policy Iteration)**.

---

## 🧠 Concept Used

This project is based on:

* Markov Decision Process (MDP)
* Policy Iteration Algorithm

---

## 🏗️ Environment Design

### 🔹 Grid Layout (3x4)

```
[ S ][   ][   ][ +1 ]
[   ][ X ][   ][ -1 ]
[   ][   ][   ][   ]
```

---

### 🔹 States

* Each cell in grid = one state
* Total states = 12

---

### 🔹 Special States

| Type | Description    |
| ---- | -------------- |
| S    | Start          |
| +1   | Goal (Reward)  |
| -1   | Penalty        |
| X    | Wall (Blocked) |

---

### 🔹 Actions

* Up (0)
* Down (1)
* Left (2)
* Right (3)

---

### 🔹 Rewards

| Situation         | Reward    |
| ----------------- | --------- |
| Reach Goal        | +1        |
| Hit Penalty       | -1        |
| Move normally     | -0.04     |
| Hit wall/boundary | Stay same |

---

## 🔄 Policy Iteration Steps

1. Initialize random policy
2. Policy Evaluation
3. Policy Improvement
4. Repeat until optimal policy is found

---

## ⚙️ Requirements

```bash
pip install numpy
```

---

## ▶️ Run the Code

```bash
python gridworld_policy_iteration.py
```

---

## 📊 Output

* Optimal Policy (direction arrows)
* State Value Function

---

## 🧪 Example Policy Output

```
→ → → G
↑ X → P
↑ → → ↑
```

---

## 📚 Learning Outcome

* Understand agent-environment interaction
* Learn optimal decision-making
* Apply RL in game scenarios

---

## 👨‍💻 Author

Abdul Saleem
