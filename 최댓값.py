listing = [int(input()) for i in range(9)]
maxnum = max(listing)

print(maxnum, listing.index(maxnum)+1, sep='\n')