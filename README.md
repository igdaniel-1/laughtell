# laughtell
Probabilist Map Grapher for One Piece's Laugh Tell Location

-- Premise
There exists a treasure island hidden so that its location can only be 
determined by the coordinates of 4 other islands. 

The problem? You only have the coordinates to 3 of those islands.

Instead of looking for that last set of coordinates, could a pirate
with a laptop find the last hidden island?


-- Context
There's a TV show called One Piece where the protagonist is searching
for the aforementioned hidden island. He has the coordinates to 3 of
the 4 islands, and is visibly struggling to find the 4th. Once he has 
four, he can connect the islands on the map to find the King of the 
Pirates treasure, pretty awesome stuff.


-- Locating the 5th island
What this program does is display a map of the most 'probable' locations 
where the 5th island could be. It's probable and not the exact location 
because this program throws a dart at each latitude and logitude on the map...


[like this set of 5 islands, A, B, C, and a guess position of D, and the 
possible position of X]

0     0     0     0     0     0     0     0     

0    [A]    0     0     0    [C]    0     0     

0     0     \     0     /     0     0     0     

0     0     0    [X]    0     0     0     0     

0     0     /     0     \     0     0     0     

0    [B]    0     0     0    [D]    0     0     


... and using all of those hypothetical locations [represented by 0] for the 4th island, 'D', 
I've used matplotlib to draw the two diagonal lines between the top-leftmost 
corner with the bottom-right, likewise with the bottom-left to the top-right.

All of these potential locations for the 5th island, 'X', are tallied up. 
Then, the locations are displayed according to their likelihoods.