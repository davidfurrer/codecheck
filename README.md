# codecheck

- This is a python package that can be installed locally through `pip install -e path` where `path` is the absolute path to the local directory for this package
- If `pip` returns `Permission denied` warning messages, try change directory into the local directory for this package, and run `python setup.py install --user`.
- To check if installed sucessfully, run `pip list`. You should be able to see the *codecheck* listed if successfully installed. 

- All functions in the codecheck package are used to check string in basic level files

- Functions for video file format checking:
  - `check_ordinal_video(ordinal, total_lines = 0, ordinal_list = 0)`
  - `check_onset_video(onset)`
  - `check_offset_video(offset)`
  - `check_object_video(obj)`
  - `check_utterance_type_video(utterance_type, word = 0)`
  - `check_object_present_video(obj_pres, word = 0)`
  - `check_speaker_video(speaker, word = 0)`
  - `check_basic_level_video(basic_level, word = 0)`
  
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

- All functinos that check format would return a boolean.

- `spellcheck(word, freqN, suggestN)` is a function that can be used for *word*, *basic_level*, *labeled_object.object* and *labeled_object.basic_level* columns spell-checking.
  - *word* is a string that needs to be spell-checked
  - *freqN* is the number of words that *word* need to be compared with from the frequency-ordered word list
  - *suggestN* is the number of suggested words that would be given out as the words closest to *word*
  - if word is spelled correct, the function would return `true` and `0`; if the word is not in the word list, it would return `false` and list of suggested word
