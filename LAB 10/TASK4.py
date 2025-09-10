def process_scores(scores):
    avg = sum(scores) / len(scores)
    print("Average:", avg)
    print("Highest:", max(scores))
    print("Lowest:", min(scores))

process_scores([88, 92, 79, 93, 85])
