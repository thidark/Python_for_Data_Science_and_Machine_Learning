votes=["Bob","Alice","Bob","Charlie","Alice","Alice"]

vote_counts={}


for name in votes:
    if name in vote_counts:
        vote_counts[name] += 1
    else:
        vote_counts[name] = 1
            
for name, count in vote_counts.items():
    print(f"{name}: {count}")


    
   