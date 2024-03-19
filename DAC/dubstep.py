def song_decoder(song):
    """Return the words of the initial song that DJ used to make a dubsteb remix. Separate the words with a space.

    Args:
        song (string]): Upper case string e.g WUBWUBIWUBAMWUBWUBX
    Returns:
        string: Return the words of the initial song that DJ used to make a dubsteb remix. Separate the words with a space
    """
    song = song.upper()
    str = "WUB"

    if song.find(str) != -1:
        return " ".join(song.replace(str, " ").split())
    return song


remix = "WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"
output = "WE ARE THE CHAMPIONS MY FRIEND"

print(song_decoder(remix) == output)
print(song_decoder(remix))
