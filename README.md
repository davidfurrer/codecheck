# codecheck

- This is a python package that can be installed locally through `pip install -e path` where `path` is the absolute path to the local directory for this package

- All functions in the codecheck package are used to check string in basic level files

- Functions for video file format checking:
  - `check_ordinal_video(ordinal, total_lines = 0, ordinal_list = 0)`
  - `check_onset_video(onset)`
  - `check_offset_video(offset)`
  - `check_object_video(obj)`
  - `check_utterance_type_video(utterance_type, word = NA)`
  - `check_object_present_video(obj_pres, word = NA)`
  - `check_speaker_video(speaker, word = NA)`
  - `check_basic_level_video(basic_level, word = NA)`
  
- Functions for audio file format checking:
  - `check_tier_audio(tier)`
  - `check_word_audio(word)`
  - `check_utterance_type_audio(utterance_type)`
  - `check_object_present_audio(obj_pres)`
  - `check_speaker_audio(speaker)`
  - `check_timestamp_audio(timestamp)`
  - `check_basic_level_audio(basic_level)`

- Most functions for format checking accept one string parameter and return boolean as checking result.

- `check_ordinal_video` function can accept up to three parameter, with the second and third being a integer and a list; those two parameters would be set to `0` by default and checking related to those two parameters would be ignored. 

- All functions that accept a second parameter *word* are checking if the word column contains a column. If so, an NA would be valid format. If no *word* is passed in, this test would be ignored. 

- `spellcheck(word, n)` is a function that can be used for *word*, *basic_level*, *labeled_object.object* and *labeled_object.basic_level* columns spell-checking.
  - *word* is a string that needs to be spell-checked
  - *n* is the number of words that *word* need to be compared with from the frequency-ordered word list
