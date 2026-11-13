import matplotlib.pyplot as plt

def plot_player_age_diff(match_table):
    player_name = match_table['player'].iloc[0]
    win_matches = match_table[match_table['result'] == 'W']
    lose_matches = match_table[match_table['result'] == 'L']
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.scatter(win_matches['player_age'], win_matches['age_diff'], color='skyblue', label='Match won',s=15)
    ax.scatter(lose_matches['player_age'], lose_matches['age_diff'], color='purple', label='Match lost',s=15)
    ax.axhline(0, color='grey', linewidth = 1)
    ax.set_xlabel(f"{player_name}'s age")
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')
    ax.set_yticks(range(-20,21,10))
    ax.set_yticklabels(["-20years\n younger\n than\n opponent", "-10","same age","+10","+20years\n older\n than\n opponent"])
    ages = f"Age {int(match_table['player_age'].min())} to {int(match_table['player_age'].max())}"
    ax.set_title(f"{player_name}'s Professional Matches, {ages}",fontsize = 25,fontweight = "bold",loc = "left")
    ax.grid(color='lightgrey')
    ax.legend(loc = "upper center",fontsize = 12,frameon = False)
    return fig, ax