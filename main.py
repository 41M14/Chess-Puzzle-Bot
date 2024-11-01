import random
import time

time = int(time.strftime("%H"))
if 5 <= time < 12:
    greeting = "Good morning Aarush ji"
elif time==12:
    greeting = "Good noon Aarush ji"
elif 12 <= time < 16:
    greeting = "Good afternoon Aarush ji"
elif 16 <= time < 22:
    greeting = "Good evening Aarush ji"
else:
    greeting = "Good night Aarush ji"
    print(f"{greeting}")

puzzles = {
    "beginner": [
        "8/8/8/8/4k3/3r1K2/8/8 w - - 0 1",
        "8/8/8/8/8/2k5/8/1Q6 w - - 0 1",
        "8/5p2/5p2/5p2/4k3/3r1K2/8/8 w - - 0 1",
        "8/8/3p4/8/8/8/3K4/4R3 w - - 0 1",
        "8/5p2/5p2/5p2/8/8/3K4/4R3 w - - 0 1",
        "6k1/6pp/8/8/5B2/8/8/6K1 w - - 0 1",
        "8/5p2/5p2/5p2/8/8/5B2/6K1 w - - 0 1",
        "8/5p2/5p2/5p2/8/8/4B3/6K1 w - - 0 1",
        "8/5p2/5p2/5p2/8/8/3B4/6K1 w - - 0 1",
        "8/6pp/8/8/5k2/8/8/6K1 w - - 0 1",
        "8/8/5k2/8/5B2/8/8/6K1 w - - 0 1",
        "8/8/8/8/8/8/5k2/6K1 w - - 0 1",
        "8/8/8/8/8/8/6k1/6K1 w - - 0 1",
        "8/6pp/8/8/5k2/8/5K2/8 w - - 0 1",
        "8/8/6pp/8/5k2/8/6K1/8 w - - 0 1",
        "8/8/6pp/8/8/8/6K1/5k2 w - - 0 1",
        "8/8/8/8/8/4k3/8/4K3 w - - 0 1",
        "8/8/5k2/8/5K2/8/6R1/8 w - - 0 1",
        "8/8/8/8/8/5R2/6k1/6K1 w - - 0 1",
        "8/5ppp/8/8/8/5R2/6k1/6K1 w - - 0 1",
        "8/6pp/8/8/5R2/6k1/6K1/8 w - - 0 1",
        "8/6pp/8/8/8/6k1/6R1/6K1 w - - 0 1",
        "8/6pp/8/8/5R2/8/6k1/6K1 w - - 0 1",
        "8/6pp/8/8/5R2/8/6k1/8 w - - 0 1",
        "8/6pp/8/8/5R2/8/6k1/8 w - - 0 1",
        "8/6pp/8/8/8/8/6k1/8 w - - 0 1",
        "8/6pp/8/8/5R2/8/6k1/8 w - - 0 1",
        "8/6pp/8/8/5R2/8/6k1/8 w - - 0 1",
        "8/8/8/8/8/4k3/8/4K3 w - - 0 1",
        "8/5ppp/8/8/8/5R2/6k1/6K1 w - - 0 1",
        "8/6pp/8/8/8/5R2/6k1/6K1 w - - 0 1",
        "8/6pp/8/8/5R2/8/6k1/6K1 w - - 0 1",
        "8/6pp/8/8/8/6k1/6R1/6K1 w - - 0 1",
        "8/6pp/8/8/5R2/8/6k1/8 w - - 0 1",
        "8/8/8/8/8/4k3/8/4K3 w - - 0 1",
        "8/6pp/8/8/8/8/6k1/6K1 w - - 0 1",
        "8/6pp/8/8/8/8/6k1/8 w - - 0 1",
        "8/6pp/8/8/8/8/6k1/8 w - - 0 1",
        "8/5ppp/8/8/8/5R2/6k1/6K1 w - - 0 1",
        "8/6pp/8/8/8/6k1/6R1/6K1 w - - 0 1",
        "8/5ppp/8/8/8/5R2/6k1/6K1 w - - 0 1",
        "8/6pp/8/8/8/8/6k1/6K1 w - - 0 1",
        "8/8/8/8/8/5R2/6k1/6K1 w - - 0 1",
        "8/6pp/8/8/8/6k1/6R1/6K1 w - - 0 1",
        "8/8/8/8/8/5R2/6k1/6K1 w - - 0 1",
        "8/8/8/8/8/4k3/8/4K3 w - - 0 1",
        "8/6pp/8/8/8/5R2/6k1/6K1 w - - 0 1",
        "8/6pp/8/8/8/5R2/6k1/8 w - - 0 1",
        "8/8/8/8/8/4k3/8/4K3 w - - 0 1",
        "8/8/8/8/8/8/5k2/6K1 w - - 0 1" 
    ],
    "intermediate": [
        "8/5p2/5pk1/8/8/5R2/7P/6K1 w - - 0 1",
        "5r1k/6p1/6qp/3P1p2/3PpP2/8/1Q3K2/8 w - - 0 1",
        "6k1/1R6/6p1/8/2r5/8/5PPP/6K1 w - - 0 1",
        "5r1k/pp1n1ppp/8/8/2n5/1PNP4/1P1N1PPP/5RK1 w - - 0 1",
        "6k1/5ppp/8/8/1Q6/8/5PPP/6K1 w - - 0 1",
        "3r2k1/pb1q1p1p/1p1b1Pp1/4p3/2B1P3/2N2B2/PPP3PP/R3Q1K1 w - - 0 1",
        "4r1k1/pp1q1ppp/4p3/3nPb2/1P1N4/P2B1N2/2Q2PPP/5RK1 w - - 0 1",
        "r4rk1/ppp2ppp/8/8/3q4/8/PB2NPPP/R2Q1RK1 w - - 0 1",
        "4rrk1/ppp2pp1/8/8/3P4/1P3P2/4B1PP/2R1R1K1 w - - 0 1",
        "r4rk1/pp1bqpp1/2p1p2p/8/3P4/1P3NP1/P1Q2P1P/R1BR2K1 w - - 0 1",
        "r3r1k1/ppp2pp1/8/2b1p1q1/3P4/1P3P2/P3B1PP/1R1QR1K1 w - - 0 1",
        "2r3k1/p5p1/3P2qp/8/3Q4/2P2P2/P4PK1/8 w - - 0 1",
        "r4rk1/1pp1qppp/p2b1n2/8/4N3/2P3P1/PP1N1PBP/R2Q1RK1 w - - 0 1",
        "r4rk1/pp1q1ppp/2n1p3/8/4P3/2N3P1/PP3PBP/R1Q1R1K1 w - - 0 1",
        "r1b1r1k1/ppp1qppp/2n5/3n4/2Pp4/3B1NP1/PPQNPPBP/R3R1K1 w - - 0 1",
        "r3r1k1/ppp2ppp/8/2b1p1q1/3P4/1P2PP2/P3B1PP/1R1QR1K1 w - - 0 1",
        "r4rk1/pp1bqppp/2n1pn2/3p4/3P4/2P1PN2/PP3PPP/RNBQR1K1 w - - 0 1",
        "r2q1rk1/pppb1pp1/3p3p/3P4/2P5/2N2P2/PP2Q1PP/2KR2B1 w - - 0 1",
        "r1bq1rk1/ppp1ppbp/6p1/4P3/2P5/2N1B3/PP3PPP/R2Q1RK1 w - - 0 1",
        "r1bq1rk1/ppp1ppbp/6p1/4P3/2P5/2N1B3/PP1QBPPP/R2R2K1 w - - 0 1",
        "r1bq1rk1/pp1nppbp/6p1/4P3/3P4/2N1B3/PP2BPPP/R1BQ1RK1 w - - 0 1",
        "r1bq1rk1/ppp1ppbp/6p1/3P4/2P5/2N1B3/PP1QBPPP/R3R1K1 w - - 0 1",
        "r2q1rk1/pppb1ppp/3p3n/3P4/2P5/2N2P2/PP3NPP/2KR1Q1B w - - 0 1",
        "r1bq1rk1/ppp1ppbp/2n3p1/8/2P5/2N1B3/PP3PPP/R2Q1RK1 w - - 0 1",
        "r2q1rk1/pppb1ppp/6n1/3P4/2P5/2N2P2/PPQ1N1PP/2KR3B w - - 0 1",
        "r2q1rk1/pppb1ppp/6n1/3P4/2P5/2N2P2/PPQ1N1PP/2KR3B w - - 0 1",
        "r1bq1rk1/ppp1ppbp/6p1/4P3/2P5/2N1B3/PP1QBPPP/R2R2K1 w - - 0 1",
        "r1bq1rk1/pp1nppbp/6p1/4P3/3P4/2N1B3/PP2BPPP/R2R2K1 w - - 0 1",
        "r1bq1rk1/ppp1ppbp/6p1/8/2P5/2N1B3/PP3PPP/R2Q1RK1 w - - 0 1",
        "r1bq1rk1/ppp1ppbp/6p1/3P4/2P5/2N1B3/PP1QBPPP/R2R2K1 w - - 0 1",
        "r1bq1rk1/ppp1ppbp/6p1/3P4/3n4/2N1B3/PP1QBPPP/R2R2K1 w - - 0 1",
        "r1bq1rk1/ppp1ppbp/2n3p1/8/2P5/2N1B3/PP3PPP/R2Q1RK1 w - - 0 1",
        "r1bq1rk1/ppp1ppbp/6p1/4P3/3n4/2N1B3/PP3PPP/R2Q1RK1 w - - 0 1",
        "r1bq1rk1/ppp1ppbp/2n3p1/8/2P5/2N1B3/PP3PPP/R2Q1RK1 w - - 0 1",
        "r1bq1rk1/ppp1ppbp/6p1/4P3/3n4/2N1B3/PP1QBPPP/R2R2K1 w - - 0 1",
        "r1bq1rk1/ppp1ppbp/6p1/3P4/2P5/2N1B3/PP1QBPPP/R2R2K1 w - - 0 1",
        "r1bq1rk1/pp1nppbp/6p1/4P3/3P4/2N1B3/PP2BPPP/R2R2K1 w - - 0 1",
        "r1bq1rk1/ppp1ppbp/6p1/3P4/3n4/2N1B3/PP1QBPPP/R2R2K1 w - - 0 1",
        "r1bq1rk1/ppp1ppbp/6p1/3P4/3n4/2N1B3/PP1QBPPP/R2R2K1 w - - 0 1",
        "r1bq1rk1/ppp1ppbp/6p1/3P4/3n4/2N1B3/PP1QBPPP/R2R2K1 w - - 0 1",
        "r1bq1rk1/ppp1ppbp/6p1/3P4/3n4/2N1B3/PP1QBPPP/R2R2K1 w - - 0 1",
        "r1bq1rk1/ppp1ppbp/6p1/3P4/3n4/2N1B3/PP1QBPPP/R2R2K1 w - - 0 1",
        "r1bq1rk1/ppp1ppbp/6p1/3P4/3n4/2N1B3/PP1QBPPP/R2R2K1 w - - 0 1",
        "r1bq1rk1/ppp1ppbp/6p1/3P4/3n4/2N1B3/PP1QBPPP/R2R2K1 w - - 0 1"
    ],
    "advanced": [
        "r1bq1rk1/ppp1bppp/2n5/3np3/4P3/2P2N1P/PP1NBPP1/R1BQR1K1 w - - 0 10",
        "2r2rk1/1pqbbppp/p2ppn2/4n3/2P5/2N1PN2/PPQ1BPPP/R1B2RK1 w - - 1 12",
        "r1bqr1k1/pp2bppp/2n1p3/3nP3/2Pp4/2N1BN2/PP2BPPP/R2QR1K1 w - - 0 13",
        "r1bqr1k1/ppp1bppp/3p1n2/3P4/2P1P3/5N2/PP3PPP/R1BQRBK1 w - - 0 12",
        "2r1r1k1/1pqnbppp/p2p4/4p3/2P1N3/1P2PP2/PBQ3PP/3RR1K1 w - - 1 16",
        "3r1rk1/1pq2ppp/2n2b2/3pn3/2P5/2N1PN2/1P2BPPP/3RR1K1 w - - 1 14",
        "r1bqr1k1/ppp1bppp/2n2n2/3p4/3P4/2NBPN2/PP2BPPP/R2QR1K1 w - - 1 10",
        "r2qr1k1/1ppbbppp/3p1n2/4p3/2P1P3/2N2P2/PP1Q2PP/R1B1NRK1 w - - 0 12",
        "r1bqr1k1/pp3pbp/3p2p1/2pPp3/4P3/2P2N1P/PP1NBPP1/R2QR1K1 w - - 0 12",
        "r1bq1rk1/pppnbppp/3p4/3Pp3/4P3/2N1BN2/PPP2PPP/R2QR1K1 w - - 0 10",
        "r1bqr1k1/ppp2ppp/2n5/3p4/3Pn3/2NBBP2/PPP3PP/R2Q1RK1 w - - 1 10",
        "r2qr1k1/ppp2ppp/2n2b2/3p4/3Pn3/2N1PN2/PPP2PPP/R1BQR1K1 w - - 0 11",
        "r1bq1rk1/pp1n1ppp/2p1pn2/3p4/3P4/2P1PN2/PP3PPP/RNBQR1K1 w - - 1 10",
        "r1bqr1k1/pppn1ppp/4p3/3P4/2P5/5N2/PP2BPPP/R2QR1K1 w - - 1 11",
        "r1bq1rk1/pppn1ppp/4pn2/3p4/3P4/2P1PN2/PP3PPP/RNBQR1K1 w - - 1 9",
        "r1bqr1k1/pppn1ppp/4p3/3P4/2P5/5N2/PP2BPPP/R2QR1K1 w - - 0 11",
        "r1bq1rk1/pppn1ppp/4pn2/3p4/3P4/2P1PN2/PP3PPP/RNBQR1K1 w - - 0 9"
    ]
}

def get_puzzle(level):
    """
    Returns a random puzzle FEN from the specified difficulty level.
    """
    return random.choice(puzzles[level])

def main():
    print("Itz UR Friend Mayank")
    print("Welcome to the Chess Puzzle Bot!")
    print("Choose difficulty level:")
    print("1. Beginner (400-800 ELO)")
    print("2. Intermediate (800-1800 ELO)")
    print("3. Advanced (1800-2800 ELO)")
    print("4. Quit")

    while True:
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            fen = get_puzzle("beginner")
            print(f"Beginner puzzle FEN: {fen}")
        elif choice == "2":
            fen = get_puzzle("intermediate")
            print(f"Intermediate puzzle FEN: {fen}")
        elif choice == "3":
            fen = get_puzzle("advanced")
            print(f"Advanced puzzle FEN: {fen}")
        elif choice == "4":
            print("Thank you for using the Chess Puzzle Bot. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
