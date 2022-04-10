import argparse
import random 
import requests
import json
import numpy as np

def run_experiment(steps, method):
    """
        steps
            how many queries to make
        method
            an object that implements selectAd(), update(ad, ad_reward), and __str__()
    """
    mean_reward = []
    total_reward = 0
    for i in range(steps):
        ad = method.selectAd()
        ad_gen = "https://755vgi76zg.execute-api.us-east-1.amazonaws.com/prod"
        data = {
            "ad": ad
        }
        response = requests.post(ad_gen, json.dumps(data))
        resp = json.loads(response.content) 
        ad_reward = int(resp["body"][1])

        method.update(ad, ad_reward)
        total_reward += ad_reward
        mean_reward.append(total_reward / (i + 1))
    
    # x = [r for r in mean_reward]
    # y = [_ for _ in range(steps)]

    # plt.scatter(y, x)
    # plt.show()

    with open(f"historical_results{method.a}.txt", "a") as f:
        f.write(f"Method: {method} scored Mean Reward: {mean_reward[-1]} after {steps} steps\n")

    print(f"Total reward is: {total_reward}")


class AdData:
    mean_reward = 1
    num_success = 1
    total_times_shown = 1

    def __str__(self):
        return f"MeanReward: {self.mean_reward}, NumSuccess: {self.num_success}, TotalTimesShown: {self.total_times_shown}"

    def __gt__(self, other):
        return(self.mean_reward > other.mean_reward)


class ExpDecayGreedy:
    def __init__(self, a):
        self.ad_list = ['ad_1', 'ad_2', 'ad_3', 'ad_4', 'ad_5']
        self.ad_data = {ad: AdData() for ad in self.ad_list} 
        self.a = a
        self.steps = 0

    def selectAd(self):
        if np.random.uniform(0, 1) <= self.a ** self.steps:
            return random.choice(self.ad_list)
        else:
            return max(self.ad_data, key=self.ad_data.get)

    def update(self, ad, ad_reward):
        self.ad_data[ad].num_success += ad_reward
        self.ad_data[ad].total_times_shown += 1
        self.ad_data[ad].mean_reward = self.ad_data[ad].num_success / self.ad_data[ad].total_times_shown
        self.steps += 1

    def __str__(self):
        return f"ExpDecayGreedy(a={self.a})"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('a', action="store", metavar="<p>",
                        help="")
    args = parser.parse_args()

    run_experiment(1000, ExpDecayGreedy(float(args.a)))

main()