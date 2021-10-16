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
            result[atoms[i]] = Constant.UNSURE
        # TODO return dpll

    def dpll(self, sentences, atoms, result):
        #check
        pure = self.findPureLiterals(sentences, atoms)

        # simple
        oneAtomSentence = []
        for sentence in sentences:
            if len(sentence) == 1:
                oneAtomSentence.append(sentence)

        isOneAtomSentenceExist = True if len(oneAtomSentence) > 0 else False
        isSuccess = True if len(sentences) > 0 else False
        isFailure = False
        for i in range(0, len(sentences)):
            if len(sentences[i]) != 0:
                isFailure = True
                break

        while isOneAtomSentenceExist or isSuccess or isFailure or len(pure) != 0:
            if isSuccess:
                for atom in atoms:


            print(":")




    def findPureLiterals(self, sentences, atoms):
        marks = {}
        for atom in atoms:
            marks[atom] = 0

        for i in range(0, len(sentences)):
            for j in range(0, len(sentences[i])):
                atom = sentences[i][j]

                if atom[0] == '!':
                    atom = atom[1:len(atom)-1]
                    if atom in marks and marks[atom] == 0:
                        marks[atom] = -1
                    elif atom in marks and marks[atom] == 1:
                        del marks[atom]
                else:
                    if atom in marks and marks[atom] == 0:
                        marks[atom] = 1
                    elif atom in marks and marks[atom] == -1:
                        del marks[atom]

        pure = []
        for key in marks:
            if marks[key] == 0:
                pure.append(key)

        return pure

    def processEasyCaseSingle(self, result, oneAtoms):
        sortedAtoms = list(oneAtoms.keys())
        key = sortedAtoms[0]
        if oneAtoms[key] == -1:
            if result[key] == Constant.UNSURE:
                result[key] = Constant.FALSE
        else:
            if result[key] == Constant.UNSURE:
                result[key] = Constant.TRUE
        # TODO return check

    def processEasyCase(self, result, singleStateAtoms):
        for i in range(0, len(singleStateAtoms)):
            if singleStateAtoms[i][0][0] == '!':
                atom = singleStateAtoms[i][0]
                if result[atom[1:]] == Constant.UNSURE:
                    result[atom[1:]] = Constant.FALSE
            else:
                if result[atom] == Constant.UNSURE:
                    result[atom] = Constant.TRUE
        # TODO return check

    # assign 한거 삭제
    def deleteAssigned(self, sentences, curAssigned):
        keys = list(curAssigned.keys())














