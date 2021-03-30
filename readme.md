# Beat Saber Backup Converter
A simple program that cleans your Beat Saber files folder backup and converts the custom songs data (Scores, favourites and so on) to the new format used with RSL (1.14.0).

# The steps for usage are as follows (for fixing song duplicates and scores):
1. Get the backup of your game (using SideQuest), then backup that 
2. Run the program with the back up window
3. Copy the new files manually into the BS folder `sdcard/Android/data/com.beatgames.beatsaber/files` (do not restore the backup through SideQuest)
4. Delete your custom_level_ maps in your RSL folder (`sdcard/ModData/com.beatgames.beatsaber/Mods/SongLoader/CustomLevels`) now that they're not needed (assuming your newly uploaded songs are there)
