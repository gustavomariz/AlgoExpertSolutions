def tournamentWinner(competitions, results):
    # Write your code here
    teams = {}
    winner = "nowin"
    teams["nowin"] = 0
    
    for i in range(len(results)):
        w = abs(results[i]-1)
        if competitions[i][w] in teams:
            teams[competitions[i][w]] = teams[competitions[i][w]] + 3
        else:
            teams[competitions[i][w]] = 3

        if teams[competitions[i][w]] > teams[winner]:
            winner = competitions[i][w]
            
    return winner
    
