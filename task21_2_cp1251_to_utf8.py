# Imagine, you've downloaded a Bulgarian subtitles file, encoded in Windows-1251:
#  Silicon.Valley.sampleBGsubs.srt
# But you have to convert it in UTF8, as your player recognise only Unicode encoded subtitles
# Write a program: cp1251_to_utf8.py, which will receive an input file name as argument and
# will create an UTF encoded file with the same name, but with sufix "_utf8_" added.

input_file="Silicon.Valley.sampleBGsubs.srt"
output_file="Silicon.Valley.sampleBGsubs_utf8_.srt"

with open(input_file, "r+b") as f:
    bytestring = f.read()
    decoded_string = bytestring.decode(encoding="cp1251")

    with open(output_file, encoding='utf-8', mode='w') as new_utf_file:
        new_utf_file.write(decoded_string)
    
    print(decoded_string)
