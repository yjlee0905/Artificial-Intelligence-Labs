import re
import Constant

def remove_brackets(source, id):
    reg = '\(([^\(]*?)\)'
    m = re.search(reg, source)
    if m is None:
        return None, None
    new_source = re.sub(reg, str(id), source, count=1)
    return new_source, m.group(1)

def merge(source):
    old = source.getResult()
    source.mergeItems('|')
    source.mergeItems('&')
    return old != source.getResult()

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
            if m is not None:
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

    def runConverter(self, sentence):
        # make order
        zero = BNFtoCNFconverter(sentence)
        while zero.makeOrder():
            zero = BNFtoCNFconverter(zero.getResult())
        merge(zero)

        one = BNFtoCNFconverter(zero.getResult())
        one.runReplaceIff()
        merge(one)

        two = BNFtoCNFconverter(one.getResult())
        two.runReplaceImplication()
        merge(two)

        three, four = None, None
        three = BNFtoCNFconverter(two.getResult())
        while three.runDeMorgan():
            pass
        merge(three)
        threeHalf = BNFtoCNFconverter(three.getResult())
        threeHalf.runSimplify()

        four = BNFtoCNFconverter(threeHalf.getResult())
        while four.runDistributive():
            pass
        merge(four)

        five = BNFtoCNFconverter(four.getResult())
        five.runSimplify()

        converted = []
        converted.append(five.getResult())

        return converted


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


    # Replace if and only if
    def runReplaceIff(self):
        final = len(self.stack) - 1
        flag = self.replaceAllIff()
        self.stack.append(self.stack[final])
        return flag


    def replaceAllIff(self):
        flag = False
        for i in range(0, len(self.stack)):
            ans = self.replaceIffInner(self.stack[i], len(self.stack))
            if ans is None:
                continue
            self.stack[i] = ans[0]
            self.stack.append(ans[1])
            self.stack.append(ans[2])
            flag = True
        return flag

    def replaceIffInner(self, source, id):
        reg = '^(.*?)\s+<=>\s+(.*?)$'
        m = re.search(reg, source)
        if m is None:
            return None
        a, b = m.group(1), m.group(2)
        return (str(id) + ' & ' + str(id+1), a + ' => ' + b, b + ' => ' + a)


    # Replace Implication
    def runReplaceImplication(self):
        flag = False
        for idx in range(0, len(self.stack)):
            ans = self.replaceImplicationInner(self.stack[idx])
            if ans is None:
                continue
            self.stack[idx] = ans
            flag = True
        return flag


    def replaceImplicationInner(self, source):
        reg = '^(.*?)\s+=>\s+(.*?)$'
        m = re.search(reg, source)
        if m is None:
            return None
        a, b = m.group(1), m.group(2)
        if '!' in a:
            return a.replace('! ', '') + ' | ' + b
        return '! ' + a + ' | ' + b


    # Apply De Morgan's Law
    def runDeMorgan(self):
        reg = '!\s+(\d+)'
        flag = False
        final = len(self.stack) - 1
        for i in range(0, len(self.stack)):
            target = self.stack[i]
            m = re.search(reg, target)
            if m is None:
                continue
            flag = True
            child = self.stack[int(m.group(1))]
            self.stack[i] = re.sub(reg, str(len(self.stack)), target, count=1)
            self.stack.append(self.demorganInner(child))
            break
        self.stack.append(self.stack[final])
        return flag


    def demorganInner(self, source):
        items = re.split('\s+', source)
        newItems = []
        for item in items:
            if item == '|':
                newItems.append('&')
            elif item == '&':
                newItems.append('|')
            elif item == '!':
                newItems.append('!')
            elif len(item.strip()) > 0:
                newItems.append('!')
                newItems.append(item)

        for idx in range(0, len(newItems)-1):
            if newItems[idx] == '!':
                if newItems[idx+1] == '!':
                    newItems[idx] = ''
                    newItems[idx+1] = ''
        return ' '.join([i for i in newItems if len(i) > 0])


    # Distributive
    def runDistributive(self):
        flag = False
        reg = '(\d+)'
        final = len(self.stack) - 1
        for i in range(0, len(self.stack)):
            target = self.stack[i]
            if '|' not in self.stack[i]:
                continue
            m = re.search(reg, target)
            if m is None:
                continue

            for j in re.findall(reg, target):
                child = self.stack[int(j)]
                if '&' not in child:
                    continue
                newReg = "(^|\s)" + j + "(\s|$)"
                items = re.split('\s+&\s+', child)
                tmpLst = [str(j) for j in range(len(self.stack), len(self.stack) + len(items))]

                for item in items:
                    self.stack.append(re.sub(newReg, ' '+item+' ', target).strip())
                self.stack[i] = ' & '.join(tmpLst)
                flag = True
            if flag:
                break
        self.stack.append(self.stack[final])
        return flag


    # simplification
    def runSimplify(self):
        old = self.getResult()
        for i in range(0, len(self.stack)):
            self.stack[i] = self.reduceOr(self.stack[i])
        final = self.stack[-1]
        self.stack[-1] = self.reduceAnd(final)
        return len(old) != len(self.getResult())

    def reduceAnd(self, target):
        if '&' not in target:
            return target

        items = set(re.split('\s+&\s+', target))
        for item in list(items):
            if ('! ' + item) in items:
                return ''
            if re.match('\d+$', item) is None:
                continue
            value = self.stack[int(item)]
            if self.stack.count(value) > 1:
                value = ''
                self.stack[int(item)] = ''
            if value == '':
                items.remove(item)
        return ' & '.join(list(items))

    def reduceOr(self, target):
        # TODO check 'or'
        if 'or' not in target:
            return target

        items = set(re.split('\s+\|\s+', target))
        for item in list(items):
            if ('! ' + item) in items:
                return ''
        return ' |'.join(list(items))