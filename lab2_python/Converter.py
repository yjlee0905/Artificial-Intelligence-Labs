import re
import Constant

class Binary:
    def __init__(self, token1, op, token2):
        self.left = token1
        self.op = op
        self.right = token2

    def inorderTraversal(self, root, result):
        if isinstance(root, Binary) is False:
            print root
            result.append(root)
            return

        self.inorderTraversal(root.left, result)
        result.append(root.op)
        self.inorderTraversal(root.right, result)
        return



def remove_brackets(source, id):
    reg = '\(([^\(]*?)\)'
    m = re.search(reg, source)
    if m is None:
        return None, None
    new_source = re.sub(reg, str(id), source, count=1)
    return new_source, m.group(1)


class BNFtoCNFconverter:

    def __init__(self, target):
        self.stack = []
        self.sourceStr = target

        final = target
        while True:
            target, temp = remove_brackets(target, len(self.stack))
            if target is None:
                break
            final = target
            self.stack.append(temp)
        self.stack.append(final)

    def getResult(self):
        root = self.stack[-1]
        m = re.match('\s*([0-9]+)\s*$', root)
        if m is not None:
            root = self.stack[int(m.group(1))]
        reg = '(\d+)'
        while True:
            m = re.search(reg, root)
            if m is None:
                break
            new = '(' + self.stack[int(m.group(1))] + ')'
            root = re.sub(reg, new, root, count=1)
        return root

    def mergeItems(self, logic):
        reg0 = '(\d+)'
        reg1 = '!\s+(\d+)'
        flag = False
        for i in range(len(self.stack)):
            target = self.stack[i]
            if logic not in target:
                continue

            m = re.search(reg1, target)
            if m is None:
                continue

            m = re.search(reg0, target)
            if m is None:
                continue

            for j in re.findall(reg0, target):
                child = self.stack[int(j)]
                if logic not in child:
                    continue
                newReg = '(^|\s)' + j + '(\s|$)'
                self.stack[i] = re.sub(newReg, ' ' + child + ' ', self.stack[i], count=1)
                self.stack[i] = self.stack[i].strip()
                flag = True
        if flag:
            self.mergeItems(logic)

    def runConverter(self, fileName):
        sentences = self.parseAndFormatSentences(fileName)


    # parse files
    def parseAndFormatSentences(self, fileName):
        sentences = open(fileName, 'r').read().split('\n')

        parsedSentences = []
        for sentence in sentences:
            parsed = []
            parsedStr = ''
            tree = self.parse(sentence, Constant.OPERATORS)
            tree.inorderTraversal(tree, parsed)

            for idx in range(0, len(parsed)):
                if idx == len(parsed)-1:
                    parsedStr += parsed[idx]
                else:
                    parsedStr += parsed[idx] + ' '
            parsedSentences.append(parsedStr)
        print parsedSentences


    def parse(self, sentence, op):
        if not op:
            sentence = sentence.strip()
            if sentence[0] == '!':
                sentence = sentence.replace(' ', '')
            return sentence

        idx = sentence.rfind(op[0])
        if idx == -1:
            sentence = sentence.strip()
            if sentence[0] == '!':
                sentence = sentence.replace(' ', '')
            return self.parse(sentence, op[1:])
        return Binary(self.parse(sentence[:idx], op), op[0], self.parse(sentence[idx+len(op[0]):], op))

    # ordering
    def makeOrder(self):
        flag = False
        for i in range(0, len(self.stack)):
            newSrc = self.addBrackets(self.stack[i])
            if self.stack[i] != newSrc:
                self.stack[i] = newSrc
                flag = True
        return flag

    def addBrackets(self, source):
        reg = '\s+(&|\||=>|<=>)\s+'
        if len(re.findall(reg, source)) < 2:
            return source

        regAnd = '(!\s+)?\S+\s+&\s+(!\s+)?\S+'
        m = re.search(regAnd, source)
        if m is not None:
            return re.sub(regAnd, '(' + m.group(0) + ')', source, count=1)

        regOr = '(!\s+)?\S+\s+\|\s+(!\s+)?\S+'
        m = re.search(regOr, source)
        if m is not None:
            return re.sub(regOr, '(' + m.group(0) + ')', source, count=1)

        regImp = '(!\s+)?\S+\s+=>\s+(!\s+)?\S+'
        m = re.search(regImp, source)
        if m is not None:
            return re.sub(regImp, '(' + m.group(0) + ')', source, count=1)

        regIff = '(!\s+)?\S+\s+<=>\s+(!\s+)?\S+'
        m = re.search(regIff, source)
        if m is not None:
            return re.sub(regIff, '(' + m.group(0) + ')', source, count=1)
