
from stable_baselines3 import DQN
from env_simulator import PhilosophyEnv

def train_agent():
    env = PhilosophyEnv()
    model = DQN("MlpPolicy", env, verbose=0)
    model.learn(total_timesteps=5000)
    return model, env

def run_simulation(model, env, steps=50):
    obs = env.reset()
    history = {"H": [], "A": [], "E": []}

    for _ in range(steps):
        action, _ = model.predict(obs)
        obs, _, _, _ = env.step(action)
        H, A, V = obs
        E = A * V
        history["H"].append(H)
        history["A"].append(A)
        history["E"].append(E)

    return history
