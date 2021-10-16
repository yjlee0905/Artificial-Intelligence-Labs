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

    def dpll(self, sentences, atoms):
        print("hello")

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















