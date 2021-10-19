import Constant

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

    def runDPLL(self, sentences, atoms):
        result = {}
        for i in range(0, len(atoms)):
            result[atoms[i]] = Constant.UNBOUNDED
        return self.dpll(sentences, result, atoms)

    def dpll(self, set, oAssign, atoms):
        # sentences: whole sentences, when assign delete for sentences

        assign = oAssign.copy()
        check = self.findPureLiterals(set, atoms)

        # check single atom
        # simple
        simple = []
        for sentence in set:
            if len(sentence) == 1:
                simple.append(sentence)

        isSimple = True if len(simple) > 0 else False
        isSuccess = True if len(set) == 0 else False
        isFailure = True
        for i in range(0, len(set)):
            if len(set[i]) != 0:
                isFailure = False
                break

        while isSimple or isSuccess or isFailure or len(check) != 0:
            if isSuccess:
                for atom in atoms:
                    if assign[atom] == Constant.UNBOUNDED:
                        assign[atom] = Constant.FALSE
                assign[Constant.RESULT] = Constant.SUCCESS
                return assign
            elif isFailure:
                assign[Constant.RESULT] = Constant.FAILURE
                return assign
            else:
                if isSimple:
                    # TODO implement
                    self.processEasyCaseSingle(assign, simple)
                    #temp = set

                    set = self.propagate(set, assign)
                    #print(set)
                elif len(check) != 0:
                    self.processEasyCase(assign, check)
                    #print(assign)
                    # TODO delete from set
                    self.deleteAssigned(set, check)
                    #print(set)

                simple = []
                for sentence in set:
                    if len(sentence) == 1:
                        simple.append(sentence)
                #TODO ordering?

                isSimple = True if len(simple) > 0 else False
                isSuccess = True if len(set) == 0 else False
                isFailure = True
                for i in range(0, len(set)):
                    if len(set[i]) != 0:
                        isFailure = False
                        break
                check = self.findPureLiterals(set, atoms)

        # start Guess
        remaining = filter(lambda atom: assign[atom] == Constant.UNBOUNDED, assign)
        remaining = sorted(remaining)
        result = {}
        e = remaining[0]
        assign[e] = Constant.TRUE
        print "hard case, guess: " + e + "=true"

        # map
        # TODO delete from set

        tempSet = []
        for a in set:
            tempSet.append(a)

        tempSet = self.propagate(tempSet, assign)
        result = self.dpll(tempSet, assign, atoms)
        if result[Constant.RESULT] == Constant.SUCCESS:
            return result
        assign[e] = Constant.FALSE
        print "hard case, guess: " + e + "=false"

        tempSet = self.propagate(set, assign)
        result = self.dpll(tempSet, assign, atoms)
        return result

    def findPureLiterals(self, sentences, atoms):
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

    def processEasyCase(self, result, oneAtoms):
        sortedAtoms = sorted(list(oneAtoms.keys()))
        key = sortedAtoms[0]
        if oneAtoms[key] == Constant.NEGATE:
            if result[key] == Constant.UNBOUNDED:
                result[key] = Constant.FALSE
                print "easyCase " + key + " = false"
        elif oneAtoms[key] == Constant.POSITIVE:
            if result[key] == Constant.UNBOUNDED:
                result[key] = Constant.TRUE
                print "easyCase " + key + " = true"
        # TODO return check

    def processEasyCaseSingle(self, result, singleStateAtoms):
        # TODO make in order
        for i in range(0, len(singleStateAtoms)):
            atom = singleStateAtoms[i][0]
            if atom[0] == '!':
                if result[atom[1:]] == Constant.UNBOUNDED:
                    result[atom[1:]] = Constant.FALSE
                    print "easyCase " + atom[1:] + " = false"
            else:
                if result[atom] == Constant.UNBOUNDED:
                    result[atom] = Constant.TRUE
                    print "easyCase " + atom + " = true"
        # TODO return check

    # delete assigned
    def deleteAssigned(self, sentences, curAssigned):
        sortedAtoms = sorted(list(curAssigned.keys()))
        key = sortedAtoms[0]
        toBeDeleted = '!'+key if curAssigned[key] == Constant.NEGATE else key

        idx = 0
        while idx < len(sentences):
            if toBeDeleted in sentences[idx]:
                sentences.remove(sentences[idx])
                idx -= 1
            idx += 1

        print(sentences)

    def propagate(self, sentences, curAssigned):
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
        for sentence in sentences:
            print sentence
            # for atom in sentence:
            #     print(atom)
        return sentences