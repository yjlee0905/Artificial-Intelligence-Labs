import Constant
import copy

class DPLLsolver:

    def parseAtoms(self, sentences):
        atoms = set()
        for i in range(0, len(sentences)):
            for j in range(0, len(sentences[i])):
                atom = sentences[i][j]
                if atom[0] == '!':
                    atom = atom[1:]
                atoms.add(atom)
        return list(atoms)

    def runDPLL(self, atoms, sentences, isVerbose):
        if isVerbose:
            for sentence in sentences:
                for atom in sentence:
                    print atom,
                print

        result = {}
        for i in range(0, len(atoms)):
            result[atoms[i]] = Constant.UNBOUNDED
        return self.dpll(atoms, sentences, result, isVerbose)

    def dpll(self, atoms, sentences, assigned, isVerbose):
        assign = assigned.copy()
        pureLiterals = self.findPureLiterals(atoms, sentences)

        # check single atoms
        singleAtoms = []
        for sentence in sentences:
            if len(sentence) == 1:
                singleAtoms.append(sentence)

        isSingleAtoms = True if len(singleAtoms) > 0 else False
        isSuccess = True if len(sentences) == 0 else False
        isFailure = True
        for i in range(0, len(sentences)):
            if len(sentences[i]) != 0:
                isFailure = False
                break

        while isSingleAtoms or isSuccess or isFailure or len(pureLiterals) != 0:
            if isSuccess:
                for atom in atoms:
                    if assign[atom] == Constant.UNBOUNDED:
                        assign[atom] = Constant.FALSE
                        if (isVerbose):
                            print "unbound " + atom + "=false"
                assign[Constant.RESULT] = Constant.SUCCESS
                return assign
            elif isFailure:
                assign[Constant.RESULT] = Constant.FAILURE
                return assign
            else:
                if isSingleAtoms:
                    self.processEasyCaseSingle(assign, singleAtoms, isVerbose)
                    self.propagate(sentences, assign, isVerbose)
                elif len(pureLiterals) != 0:
                    self.processEasyCase(assign, pureLiterals, isVerbose)
                    self.deleteAssigned(sentences, pureLiterals, isVerbose)

                singleAtoms = []
                for sentence in sentences:
                    if len(sentence) == 1:
                        singleAtoms.append(sentence)
                #TODO ordering?

                isSingleAtoms = True if len(singleAtoms) > 0 else False
                isSuccess = True if len(sentences) == 0 else False
                isFailure = True
                for i in range(0, len(sentences)):
                    if len(sentences[i]) != 0:
                        isFailure = False
                        break
                pureLiterals = self.findPureLiterals(atoms, sentences)

        # start Guess
        remaining = filter(lambda atom: assign[atom] == Constant.UNBOUNDED, assign)
        remaining = sorted(remaining)
        guess = remaining[0]

        assign[guess] = Constant.TRUE
        if isVerbose:
            print "hard case, guess: " + guess + "=true"
        tempSentences = copy.deepcopy(sentences)
        tempSentences = self.propagate(tempSentences, assign, isVerbose)
        result = self.dpll(atoms, tempSentences, assign, isVerbose)
        if result[Constant.RESULT] == Constant.SUCCESS:
            return result

        assign[guess] = Constant.FALSE
        if isVerbose:
            print "fail|hard case, try: " + guess + "=false"
        tempSentences = self.propagate(sentences, assign, isVerbose)
        result = self.dpll(atoms, tempSentences, assign, isVerbose)
        return result

    def findPureLiterals(self, atoms, sentences):
        marks = {}
        for atom in atoms:
            marks[atom] = Constant.INIT

        for i in range(0, len(sentences)):
            for j in range(0, len(sentences[i])):
                atom = sentences[i][j]

                if atom[0] == '!':
                    atom = atom[1:]
                    if marks[atom] != Constant.CHECKED and marks[atom] == Constant.INIT:
                        marks[atom] = Constant.NEGATE
                    elif marks[atom] != Constant.CHECKED and marks[atom] == Constant.POSITIVE:
                        marks[atom] = Constant.CHECKED
                else:
                    if marks[atom] != Constant.CHECKED and marks[atom] == Constant.INIT:
                        marks[atom] = Constant.POSITIVE
                    elif marks[atom] != Constant.CHECKED and marks[atom] == Constant.NEGATE:
                        marks[atom] = Constant.CHECKED

        pure = {}
        for key in marks:
            if marks[key] == Constant.POSITIVE or marks[key] == Constant.NEGATE:
                pure[key] = marks[key]
        return pure

    def processEasyCase(self, result, oneAtoms, isVerbose):
        sortedAtoms = sorted(list(oneAtoms.keys()))
        key = sortedAtoms[0]
        if oneAtoms[key] == Constant.NEGATE:
            if result[key] == Constant.UNBOUNDED:
                result[key] = Constant.FALSE
                if isVerbose:
                    print "easyCase " + key + " = false"
        elif oneAtoms[key] == Constant.POSITIVE:
            if result[key] == Constant.UNBOUNDED:
                result[key] = Constant.TRUE
                if isVerbose:
                    print "easyCase " + key + " = true"

    def processEasyCaseSingle(self, result, singleStateAtoms, isVerbose):
        # TODO make in order
        for i in range(0, len(singleStateAtoms)):
            atom = singleStateAtoms[i][0]
            if atom[0] == '!':
                if result[atom[1:]] == Constant.UNBOUNDED:
                    result[atom[1:]] = Constant.FALSE
                    if isVerbose:
                        print "easyCase " + atom[1:] + " = false"
                        for singleAtoms in singleStateAtoms:
                            if atom[1:] in singleAtoms:
                                print atom[1:] + ' contradiction'
            else:
                if result[atom] == Constant.UNBOUNDED:
                    result[atom] = Constant.TRUE
                    if isVerbose:
                        print "easyCase " + atom + " = true"
                        for singleAtoms in singleStateAtoms:
                            if '!' + atom in singleAtoms:
                                print '!' + atom + ' contradiction'

    def deleteAssigned(self, sentences, curAssigned, isVerbose):
        sortedAtoms = sorted(list(curAssigned.keys()))
        key = sortedAtoms[0]
        toBeDeleted = '!'+key if curAssigned[key] == Constant.NEGATE else key

        idx = 0
        while idx < len(sentences):
            if toBeDeleted in sentences[idx]:
                sentences.remove(sentences[idx])
                idx -= 1
            idx += 1

        # Verbose
        if isVerbose:
            for sentence in sentences:
                for atom in sentence:
                    print atom,
                print

    def propagate(self, sentences, curAssigned, isVerbose):
        for atom in curAssigned:
            if curAssigned[atom] == Constant.TRUE:
                idx = 0
                while idx < len(sentences):
                    if atom in sentences[idx]:
                        sentences.remove(sentences[idx])
                        idx -= 1
                    elif '!'+atom in sentences[idx]:
                        sentences[idx].remove('!'+atom)
                    idx += 1
            elif curAssigned[atom] == Constant.FALSE:
                idx = 0
                while idx < len(sentences):
                    if '!'+atom in sentences[idx]:
                        sentences.remove(sentences[idx])
                        idx -= 1
                    elif atom in sentences[idx]:
                        sentences[idx].remove(atom)
                    idx += 1
        # Verbose
        if isVerbose:
            for sentence in sentences:
                for atom in sentence:
                    print atom,
                print
        return sentences