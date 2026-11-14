# oppo_age_gap definition
Extracts a tennis player's information about their career matches from tennisabstract.com and plots their age against the age difference between them and their opponents

## Install process
```bash
pip install git+https://github.com/UCB-stat159-f26/hw03-3-canwang0425
```

## Usage Explanation 
```python
#import all the public functions
from oppo_age_gap import get_player_matches_data, plot_player_age_diff
   
#example of getting the plot of a tennis player
serena = get_player_matches_data("serena williams")
plot_player_age_diff(serena)   
#example of getting an error message of a non-tennis player                  
get_player_matches_data("cindywang")          
```
## Tests
`python -m pytest` includes test cases that run on mock examples of both female and male tennis player career match files

## Reflections
I really enjoyed the process of turning what I wrote from HW2 into functions and testing them through different test cases. I think the functions make my code cleaner and more organized. I found the hardest part to be thinking through how to make the test cases well-rounded. I found that raising a clear error message is very important because it shows the user possible reasons it can be wrong. One thing that surprised me was that female players' files store opponents' birthdays while male players' files store their ages, which taught me to always check the data format before assuming two similar files are the same.