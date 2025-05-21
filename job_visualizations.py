import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# Just setting up a nice vibe for the charts
sns.set(style="whitegrid", font="Comic Sans MS", palette="pastel")
plt.rcParams.update({'axes.titlesize':16, 'axes.labelsize':14})

def show_trends(data):
    """
    Show how the job demand changes over time for each industry.
    Because trends tell stories, right?
    """
    plt.figure(figsize=(11,7))
    sns.lineplot(data=data, x='Year', y='Demand', hue='Industry', marker='o', linewidth=2)
    plt.title("How Industries Are Growing (2019-2023)")
    plt.xlabel("Year")
    plt.ylabel("Demand (# of Jobs)")
    plt.legend(title="Industry", loc='upper left', bbox_to_anchor=(1,1))
    plt.tight_layout()
    plt.show()

def show_interest_fit(areas, scores):
    """
    Show how your interests line up with what's hot in the job market.
    Because your vibe attracts your tribe.
    """
    df = pd.DataFrame({'Field': areas, 'Fit Score': scores})
    plt.figure(figsize=(9,5))
    sns.barplot(data=df, x='Field', y='Fit Score', palette='coolwarm')
    plt.ylim(0,1)
    plt.title("Your Interest x Market Demand Match")
    plt.ylabel("Score (0 to 1)")
    plt.tight_layout()
    plt.show()

def show_salaries(jobs, salaries):
    """
    Money talks! Here’s what you could expect to earn.
    """
    df = pd.DataFrame({'Job Title': jobs, 'Expected Salary (RMB/month)': salaries})
    plt.figure(figsize=(9,5))
    sns.barplot(data=df, x='Job Title', y='Expected Salary (RMB/month)', palette='Set3')
    plt.title("Potential Paychecks 💰")
    plt.tight_layout()
    plt.show()

def show_3d_match(interests, skills, demands):
    """
    Let’s get fancy — 3D scatter plot to see how you stack up
    across your interests, skills, and market demand.
    """
    fig = plt.figure(figsize=(10,7))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(interests, skills, demands, c='purple', s=100, alpha=0.7)

    ax.set_xlabel('Interest Level')
    ax.set_ylabel('Skill Level')
    ax.set_zlabel('Job Market Demand')
    ax.set_title('3D Career Match Overview')
    plt.tight_layout()
    plt.show()

def grab_sample_data():
    """
    Quick grab for some fake industry data.
    Swap with real stuff when you got it.
    """
    industries = ['AI', 'Finance', 'Education', 'Healthcare', 'Manufacturing']
    years = list(range(2019, 2024))
    demands = [
        [120, 140, 160, 180, 200],
        [100, 105, 110, 130, 140],
        [90, 88, 95, 100, 110],
        [110, 115, 130, 135, 150],
        [70, 80, 85, 90, 100]
    ]
    records = []
    for ind_idx, industry in enumerate(industries):
        for yr_idx, year in enumerate(years):
            records.append({'Year': year, 'Industry': industry, 'Demand': demands[ind_idx][yr_idx]})
    return pd.DataFrame(records)
