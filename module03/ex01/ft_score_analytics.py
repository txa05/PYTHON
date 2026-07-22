#! /usr/bin/env python3

import sys

def	score_analytics() -> None:
	if len(sys.argv) == 1:
		print(f"No score provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
		return
	scores = [int(n) for n in sys.argv[1:]]
	print(f"Scores processed:", scores)

score_analytics()