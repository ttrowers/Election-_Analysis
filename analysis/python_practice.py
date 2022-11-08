counties=["Arapahoe","Denver","Jefferson"]
if counties[1]=='Denver':
    print(counties[1])
    counties= ["Arapahoe","Denver","Jefferson"]

    if "El Paso" in counties:
        print("El Paso is in the list of counties.")
    else:
            print("El paso is not the list of counties.")

for county in counties:
    print(county)

    counties_dict={"Arapahoe":422829, "Denver":463353, "Jefferson":432438}
    for county, voters in counties_dict.items():
        print(county + "county has" +str(voters) + " registered voters.")

        for county,voters in counties_dict.items():
            print("F {county} county has {voters} registered voters")

candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes =int(input("What is the total number of votes in the election?"))
message_to_candidate= (
    f"You received {candidate_votes} number of votes."
    f"The total number of votes in the election was {total_votes}."
    f"You received {candidate_votes/ total_votes * 100}% of the total votes.")

print(message_to_candidate)
message_to_candidate =(
    f"You received {candidate_votes:,} number of votes."
    f"The total number of votes in the election was {total_votes:,}."
    f"You received{candidate_votes/ total_votes * 100:2f}% of the total votes.") 


 
