#! /bin/env python


class MeterTransfer:
    def __init__(self):
        self.units = {}
        self.operations = ('+', '-', '*', '/')

    def addUnit(self, regular):
        #print regular
        if regular[1] == 'foot':
            self.units[regular[1]] = float(regular[3])/float(regular[0])
            self.units['feet'] = float(regular[3])/float(regular[0])
        elif regular[1] == 'foot':
            self.units[regular[1]] = float(regular[3])/float(regular[0])
            self.units['feet'] = float(regular[3])/float(regular[0])
        elif regular[1] == 'inch':
            self.units[regular[1]] = float(regular[3])/float(regular[0])
            self.units['inches'] = float(regular[3])/float(regular[0])
        else:
            self.units[regular[1]] = float(regular[3])/float(regular[0])
            self.units[regular[1] + 's'] = float(regular[3])/float(regular[0])



    def printUnits(self):
        print self.units

    def calUnit(self, expression):
        result = 0
        lastNum = 0
        lastOper = ''
        isOper = False
        converExp = []
        #print expression
        for exp in expression:
            try :
                float(exp)
                lastNum = float(exp)
            except ValueError:
                if self.units.has_key(exp):
                    lastNum = lastNum * self.units[exp]
                    converExp.append(lastNum)
                if exp in self.operations:
                    converExp.append(exp)

        for exp in converExp:
            try:
                float(exp)
                if isOper:
                    if lastOper == '+':
                        lastNum = lastNum + float(exp)
                    elif lastOper == '-':
                        lastNum = lastNum - float(exp)
                    isOper = False
                else:
                    lastNum = float(exp)
            except ValueError:
                if exp in self.operations:
                    lastOper = exp
                    isOper = True
        return lastNum

if __name__ == "__main__":
    transfer = MeterTransfer()
    infile = open('input.txt', 'r')
    outfile = open('output.txt', 'w')
    try:
        outfile.write('djy1989418@126.com\n')
        outfile.write('\n')
        inContent = infile.readlines()
        #read regular from input.txt
        i = 0
        for line in inContent:
            line = line.strip()
            if len(line) == 0:
                break
            i += 1
            regular = line.split(' ')
            transfer.addUnit(regular)
        #transfer.printUnits()
        #begin to transfer
        for i in range(i, len(inContent)):
            if not inContent[i].strip():
                continue;
            line = inContent[i].strip().split(' ')
            num = transfer.calUnit(line)
            outfile.write('%0.2f m\n' % num)
    finally:
        infile.close()
        outfile.close()

