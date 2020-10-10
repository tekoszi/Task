from django.shortcuts import render
import re
import math
from scipy.stats import chisquare


def index(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        data = myfile.read()
        data = data.decode("utf-8").split('\n')
        targetColumn = []

        for row in data[:1]:
            row = row.replace('\r', '').replace('\n', '')
            fileHeaders = re.findall(r"(\w+)", row, 0)
            try:
                columnNumber = fileHeaders.index('7_2009')
            except Exception as e:
                print(e)
                return render(request, 'Homepage/index.html', {'targetColumnMissing': 1})

        # staighting up the file columns, cutting only words and numbers from the file to align column count.
        for row in data[1:]:
            row = row.replace('\r', '').replace('\n', '')
            sub = re.sub(r"[^A-Za-z0-9. ()'-/]+", ", ", row, 0, re.MULTILINE).split(', ')
            try:
                if sub[columnNumber]:
                    targetColumn.append(sub[columnNumber])
            except IndexError:
                targetColumn.append(0)

        # calculating percentage of provided number occurring on first position of every number provided in a data
        def countRatio(listOfNumbers, number):
            counter = 0
            if len(listOfNumbers) > 10:
                for x in listOfNumbers:
                    if str(x)[0] == str(number):
                        counter += 1
                return round(counter / len(listOfNumbers) * 100, 1)
            else:
                print('Provide a list containing more than 10 records!')

        realValues = []
        expectedValues = []
        for x in range(1, 10):
            realValues.append(countRatio(targetColumn, x))
            expectedValues.append(round(math.log10(1 + (1 / x)) * 100, 1))

        # calculating if data obey the law using chisquare test.
        powerDivergence = float(
            str(chisquare(realValues, f_exp=expectedValues)).split('pvalue=')[1].replace(')', '')) * 100
        print(powerDivergence)

        templateDict = {'powerDivergence': powerDivergence, 'realValues': realValues, 'expectedValues': expectedValues}
        if powerDivergence > 95:
            success = 'Data in file ' + myfile.name + ' obeys Benford\'s Law.'
            templateDict['success'] = success
        else:
            failure = 'Data in file ' + myfile.name + ' does not obey Benford\'s Law.'
            templateDict['failure'] = failure

        return render(request, 'Homepage/index.html', templateDict)

    return render(request, 'Homepage/index.html')

