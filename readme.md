# Beat Saber Backup Converter
A simple program that cleans your Beat Saber files folder backup and converts the custom songs data (Scores, favourites and so on) to the new format used with RSL (1.14.0).

# The steps for usage are as follows (for fixing song duplicates and scores):
1. Upload all your songs again and run BeatSaber for RSL to make the cache (assuming duplicates are there) 
2. Get the backup of your game (using SideQuest), then backup that 
3. Copy the RSL cache (which is in your RSL config folder, e.g `ModData/SongLoader.json` into the original backup folder)
4. Run the program
5. Copy the existing files manually into the BS folder `sdcard/Android/data/com.beatgames.beatsaber/files` (do not restore the backup through SideQuest)
6. Delete your custom_level_ maps in your RSL folder (`sdcard/ModData/com.beatgames.beatsaber/Mods/SongLoader/CustomLevels`) now that they're not needed (assuming your newly uploaded songs are there)
