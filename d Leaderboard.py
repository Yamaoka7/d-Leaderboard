def update_score(username, score):
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO scores (username, score) VALUES (?, ?)", (username, score))
    conn.commit()
    conn.close()

def display_leaderboard():
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()
    cursor.execute("SELECT username, MAX(score) AS max_score FROM scores GROUP BY username ORDER BY max_score DESC LIMIT 10")
    leaderboard = cursor.fetchall()
    print("Leaderboard:")
    for i, (username, max_score) in enumerate(leaderboard):
        print(f"{i+1}. {username}: {max_score}")
    conn.close()
