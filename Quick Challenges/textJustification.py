def textJustification(words, maxWidth):
        num_of_words = len(words)
        start_ind, end_ind, runner = 0, 0, 0
        len_of_line, word_num_line = 0, 0
        res = []

        while True:
            runner = start_ind
            if runner >= num_of_words:
                break
            len_of_line, word_num_line = 0, 0

            #find the start and end word indexes for one line
            while runner < num_of_words:
                len_of_line = len_of_line + len(words[runner])
                word_num_line = word_num_line + 1
                if runner != start_ind:
                    len_of_line = len_of_line + 1
                if len_of_line > maxWidth:
                    break
                runner = runner + 1

            #justify one line
            if runner != num_of_words:
                end_ind = runner - 1
                if start_ind == end_ind: #one word in a line
                    oneline = words[start_ind] + " "*(maxWidth-len(words[start_ind]))
                else: #many words in a line
                    len_of_line = len_of_line - len(words[runner]) - 1
                    word_num = end_ind - start_ind + 1
                    extra_spaces = maxWidth - (len_of_line - (word_num - 1))
                    basic_pad_spaces = extra_spaces // (word_num - 1)
                    addition_pad_spaces = extra_spaces % (word_num - 1)
                    oneline = ""
                    for ind in range(start_ind, runner-1):
                        oneline = oneline + words[ind] + " "*basic_pad_spaces
                        if ind - start_ind < addition_pad_spaces:
                            oneline = oneline + " "
                    oneline = oneline + words[runner-1]
            else: #last line
                oneline = ""
                for ind in range(start_ind, num_of_words-1):
                    oneline = oneline + words[ind] + " "
                oneline = oneline + words[num_of_words-1]
                pad_spaces = maxWidth - len(oneline)
                oneline = oneline + " "*pad_spaces

            res.append(oneline)        
            start_ind = runner

        return res
