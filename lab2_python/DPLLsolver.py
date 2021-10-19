import Constant

class DPLLsolver:
    # constants

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
        self.dpll(sentences, atoms, result)
        # TODO return dpll

    def dpll(self, sentences, atoms, result):
        # sentences: whole sentences, when assign delete for sentences

        assigned = result
        #check
        pureLiterals = self.findPureLiterals(sentences, atoms)

        # check single atom
        # simple
        oneAtomSentences = []
        for sentence in sentences:
            if len(sentence) == 1:
                oneAtomSentences.append(sentence)

        isOneAtomSentenceExist = True if len(oneAtomSentences) > 0 else False
        isSuccess = True if len(sentences) == 0 else False
        isFailure = True
        for i in range(0, len(sentences)):
            if len(sentences[i]) != 0:
                isFailure = False
                break

        while isOneAtomSentenceExist or isSuccess or isFailure or len(pureLiterals) != 0:
            if isSuccess:
                for atom in atoms:
                    if assigned[atom] == Constant.UNBOUNDED:
                        assigned[atom] = Constant.FALSE
                assigned[Constant.RESULT] = Constant.SUCCESS
                return assigned
            elif isFailure:
                assigned[Constant.RESULT] = Constant.FAILURE
                return assigned
            else:
                if isOneAtomSentenceExist:
                    # TODO implement
                    self.processEasyCaseSingle(assigned, oneAtomSentences)
                    print(assigned)
                elif len(pureLiterals) != 0:
                    self.processEasyCase(assigned, pureLiterals)
                    print(assigned)
                    self.deleteAssigned(sentences, pureLiterals)
                    print(sentences)





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
        elif oneAtoms[key] == Constant.POSITIVE:
            if result[key] == Constant.UNBOUNDED:
                result[key] = Constant.TRUE
        # TODO return check

    def processEasyCaseSingle(self, result, singleStateAtoms):
        for i in range(0, len(singleStateAtoms)):
            if singleStateAtoms[i][0][0] == '!':
                atom = singleStateAtoms[i][0]
                if result[atom[1:]] == Constant.INIT:
                    result[atom[1:]] = Constant.FALSE
            else:
                if result[atom] == Constant.INIT:
                    result[atom] = Constant.TRUE
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