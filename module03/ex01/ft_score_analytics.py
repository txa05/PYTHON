#! /usr/bin/env python3

import sys

def	score_analytics() -> None:
	if len(sys.argv) == 1:
		print(f"No score provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
		return
	scores = []
	invalid_count = 0
	
	for item in sys.argv[1:]:
		try:
			nbr = int(item)
			scores.append(nbr)
		except:
			invalid_count += 1

	if invalid_count == len(sys.argv[1:]):
		for value in sys.argv[1:]:
			print(f"Invalid parameter: '{value}'")
	if len(scores) == 0:
		print(f"No score provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
		return
	print(f"Scores processed: {scores}")
	print(f"Total Players: {len(scores)}")
	print(f"Total score: {sum(scores)}")
	print(f"Average score: {sum(scores) / len(scores)}")
	print(f"High score: {max(scores)}")
	print(f"Low score: {min(scores)}")
	print(f"Score range: {max(scores) - min(scores)}")
	print("")

def	main() -> None:
	print("=== Player Score Analytics ===")
	score_analytics()

if __name__ == "__main__":
	main()	
	
