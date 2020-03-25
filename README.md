# Dominant-strategy-equilibrium
Displays all dominant strategy equilibriums for a n-player game

## Language and modules  
**Language:** python3  
**Modules imported:**  
* sys
* numpy
* itertools

## Solution approach  
The approach uses brute-force method. It iterates over each player one by one. 
In the i<sup>th</sup> iteration it finds the best action s<sub>i</sub> for all possible values of the strategy S<sub>-i</sub> of all other players. If the interesction of s<sub>i</sub> for all possible S<sub>-i</sub> is null for any player then no dominant strategy equilibrium exists else atleast one exists.

## Time Complexity  
The complexity is O(N * A).  
where N is the number of players  
and A is the product of the number of actions available to each player

## Author  
Atirek Kumar  
Roll no: 20171060  
Team number: 7  
