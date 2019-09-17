Information Set Monte Carlo Tree Search
=======================================

Python 3 implementation of ISMCTS for the game of simplified Knockout Whist.

Based on Python 2.7 version from https://www.aifactory.co.uk/newsletter/2013_01_reduce_burden.htm

Strength of ISMCTS
==================
Compared with random move agent over 100 games.

100 iterations vs random move =  58 : 42

1000 iterations vs random move = 67 : 33

2000 iterations vs random move = 65 : 35

Rules of simplified Knockout Whist
==================================
from https://www.pagat.com/whist/kowhist.html

Two to seven players may play. From lowest to highest, the ranks are 2, .., 10, J, Q, K, A

In the first round, each player is dealt seven cards then a trump suit is
determine randomly.

Player 1 goes first to play a card, followed by player 2, 3, and so on. Until
everyone has played one card, this is one trick.

Each player must play a card with the same suit as the first card, otherwise
they may play any card. Each trick is won by the highest trump, otherwise by
the highest card of the first suit.

The player that wins the trick, will start the next trick.

Once all cards are played, the players that did not win any tricks in the round
are knocked out. Then the remaining players are dealt six cards in
the next round. Each subsequent round will have one less card.

The last player remaining is the winner.

Note: in the actual game, the player with the most tricks in the current
round decides the trump suit of the next round and there is an additional
"dog's life" condition
