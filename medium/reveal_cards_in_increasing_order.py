"""
In a deck of cards, every card has a unique integer.  You can order the deck in any order you want.

Initially, all the cards start face down (unrevealed) in one deck.

Now, you do the following steps repeatedly, until all cards are revealed:

Take the top card of the deck, reveal it, and take it out of the deck.
If there are still cards in the deck, put the next top card of the deck at the bottom of the deck.
If there are still unrevealed cards, go back to step 1.  Otherwise, stop.
Return an ordering of the deck that would reveal the cards in increasing order.

The first entry in the answer is considered to be the top of the deck.
"""
import logging
import sys
import collections
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        if len(deck) == 1:
            return deck

        list.sort(deck)
        deq = collections.deque(deck)

        ans = collections.deque()
        ans.append(deq.pop())
        ans.appendleft(deq.pop())

        i = 1
        while deq:
            ans.rotate(-i)
            ans.appendleft(deq.pop())
            i += 1
        return ans


if __name__ == '__main__':
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    format = '%(asctime)s [%(levelname)s]: %(message)s'

    stream = logging.StreamHandler(sys.stdout)
    stream.setFormatter(logging.Formatter(format))
    stream.setLevel(logging.INFO)
    log.addHandler(stream)

    tes_pattern = [([17, 13, 11, 2, 3, 5, 7], [2, 13, 3, 11, 5, 17, 7]),
                   ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
                   ([1, 2, 3, 4], [1, 3, 2, 4]),
                   ([1, 2, 3, 4, 5, 6], [1, 4, 2, 6, 3, 5])]

    for deck, expected_result in tes_pattern:
        solution = Solution()
        myresult = solution.deckRevealedIncreasing(deck)
        assert myresult == expected_result, log.error(f'Expected result: {expected_result}, but received: {myresult}')

    while log.handlers:
        handler = log.handlers[0]
        handler.close()
        log.removeHandler(handler)
