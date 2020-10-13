import sys
import helpers

LENGTH = 364.4

def main():
    if len(sys.argv) < 2:
        print("Usage: python race.py <datafile.csv>")
        sys.exit()
        
    data = helpers.import_data(sys.argv[1])
    cleaned = helpers.clean_data(data)
    
    stats = list()
    for row in cleaned:
        vf = helpers.final_velocity(row["Acceleration"], LENGTH - row["Distance"], row["Velocity"])
        time = row["Time"] + helpers.time(LENGTH - row["Distance"], row["Velocity"], vf)
        stats.append({
            "Person": row["Person"],
            "Time": time,
            "AvgV": LENGTH / time,
            "FinalV": vf
        })
                          
    helpers.print_winner(stats)
    helpers.export_data(stats, "stats.csv")

if __name__ == "__main__":
    main()
