import sys
import csv

# Functions to check for video files
acceptable_utterance_types = ['s', 'n', 'd', 'r', 'q', 'i', 'o', 'u']
comment = "%com:"

# video ordinal column format checking
def check_ordinal_video(ordinal, total_lines = 0, ordinal_list = 0):
    digit_list = ['0']
    for y in ordinal:
        if y.isdigit():
            digit_list.append(y)
    string_digits = ''.join(digit_list)
    int_digits = int(string_digits)
    
    try:
        if ordinal_list:
            #Check for repeat values
            assert(not (ordinal in ordinal_list))
        #Check for non-digit characters
        assert(x.isdigit() for x in ordinal)
        if total_lines:
            #Check that ordinal value is from 1 to total_lines-1, inclusive
            assert(int_digits >= 0 and int_digits <= total_lines - 1)

    except AssertionError:
        return False

    return True
    
# video onset column format checking
def check_onset_video(onset):
    try:
        assert(x.isdigit() for x in onset)
    except AssertionError:
        return False

    return True

# video offset column format checking
def check_offset_video(offset):
    try:
        assert(x.isdigit() for x in offset)
    except AssertionError:
        return False
        
    return True

# video object column format checking
def check_object_video(obj):
    try:
    	if not obj.startswith(comment):
	        for char in obj:
	            assert (char.isalpha() or char == "+" or char == "'")
    except AssertionError:
        return False

    return True

# video utterance_type column format checking
def check_utterance_type_video(utterance_type, word = NA):
    try:
    	if word.startswith(comment):
    		assert (utterance_type == "NA")
    	else:
        	assert (utterance_type in acceptable_utterance_types)
    except AssertionError:
        return False
        
    return True

# video object_present column format checking
def check_object_present_video(obj_pres, word = NA):
    try:
    	if word.startswith(comment):
    		assert (obj_pres == "NA")
    	else:
        	assert(obj_pres == "y" or obj_pres == "n" or obj_pres == "o" or obj_pres == "u")
    except AssertionError:
        return False
        
    return True

# check if a speaker is valid
def isValid(speaker):
    if len(speaker) != 3: 
        return False
    if speaker[0].isalpha() and speaker[0].isupper():
        if speaker[1].isalpha() and speaker[1].isupper():
            if speaker[2].isalpha() and speaker[2].isupper():
                return True
            elif speaker[2].isdigit():
                return True
    return False

# video speaker column format checking
def check_speaker_video(speaker, word = NA):
    try:
        if word.startswith(comment):
            assert (speaker == "NA")
        else:
            assert(isValid(speaker))
    except AssertionError:
        return False
        
    return True

# video basic_level column format checking
def check_basic_level_video(basic_level, word = NA):
    try:
    	if word.startswith(comment):
    	    assert (basic_level == "NA")
    	else:
            for char in basic_level:
                assert (char.isalpha() or char == "+" or char == "'" or char == " " or char == "*")
    except AssertionError:
        return False
        
    return True


#Functions to check for audio files

acceptable_tier = ['*CHF', '*CHN', '*CXF', '*CXN', '*FAF', '*FAN', '*NOF',
                   '*MAF', '*MAN', '*NON', '*OLF', '*OLN', '*SIL', '*TVF', '*TVN']

# audio tier column format checking
def check_tier_audio(tier):
    try:
        assert(tier in acceptable_tier)
    except AssertionError:
        return False
        
    return True

# audio word column format checking
def check_word_audio(word):
    try:
        for char in word:
            assert (char.isalpha() or char == "+" or char == "'")
    except AssertionError:
        return False
        
    return True

# audio utterance_type column format checking
def check_utterance_type_audio(utterance_type):
    try:
        assert (utterance_type in acceptable_utterance_types)
    except AssertionError:
        return False
        
    return True

# audio object_present column format checking
def check_object_present_audio(obj_pres):
    try:
        assert(obj_pres == "y" or obj_pres == "n" or obj_pres == "u" or obj_pres == "o")
    except AssertionError:
        return False
        
    return True

# audio speaker column format checking
def check_speaker_audio(speaker):
    try:
        #currently no comment in audio file for word column, so no check on it
 #        if word.startswith(comment):
	#     assert (speaker == "NA")
	# else:
	    assert(isValid(speaker))
    except AssertionError:
        return False
        
    return True

# audio timestamp column format checking
def check_timestamp_audio(timestamp):
    underscore_index = timestamp.find("_")

    if underscore_index != -1:
        try:
            for x in range(len(timestamp)):
                if x != underscore_index:
                    assert(timestamp[x].isdigit())
        except AssertionError:
            return False
    else:
        try:
            assert(underscore_index != -1)
        except AssertionError:
            return False

    return True
               
    
# audio basic_level column format checking
def check_basic_level_audio(basic_level):
    try:
        for char in basic_level:
            assert (char.isalpha() or char == "+" or char == "'" or char == " " or char == "*")
    except AssertionError:
        return False
        
    return True



