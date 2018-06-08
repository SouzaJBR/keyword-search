# encoding: utf-8
import csv
import re
import argparse


# Source: https://stackoverflow.com/a/5320179 by Hugh Bothwell
def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search


def find_word(w, t):
    return w.lower() in t.lower()


if __name__ == '__main__':


    parser = argparse.ArgumentParser()

    parser.add_argument('queryFile', help='File containing the query', type=str)
    parser.add_argument('scopusFile',
                        help='CSV File containing the Scopus result exported to CSV. Before export please select "Citation Information" and "Abstract & keywords" only',
                        type=str)

    parser.add_argument('--detailed', action='store_true', default=False)

    args = parser.parse_args()

    with open(args.scopusFile) as csvFile:
        csvData = csv.reader(csvFile)

        query = ''
        with open(args.queryFile) as queryFile:
            query = queryFile.read()

        query = re.sub(r'[()"]', '', query)
        temp = query.split('OR')
        tokens = []
        papers = []

        for token in query.replace(' AND ', ' OR ').split(' OR '):
            tokens.append(tuple((token.strip(), [])))

        for row in csvData:

            paperTitle = row[0]

            if paperTitle == '':
                print 'vazio'

            tokenMatch = []

            for (token, matches) in tokens:
                for attribute in row:
                    if find_word(token, attribute):
                        matches.append(paperTitle)
                        tokenMatch.append(token)
                        break

                    #csvRows = [r for r in csvRowData]



            papers.append((paperTitle, tokenMatch))

        print('==================== TOKENS - PAPERS COUNT ==================')
        tokens = sorted(tokens, key=lambda matches: len(matches[1]))
        for token, matches in tokens:
            print(token + ' => ' + str(len(matches)) + ' papers')


        print('\n\n')

        if args.detailed:
            print('==================== TOKENS - PAPERS LIST ==================')

            for token, matches in tokens:
                print(token)

                for match in matches:
                    print('\t' + match)

                print ('\n')

            print('\n\n')
            print('==================== PAPERS - TOKENS COUNT ==================')
            papers.sort(key=lambda tup: len(tup[1]))
            for paper, matches in papers:
                print(paper + ' => ' + str(len(matches)) + ' tokens')

            print('\n\n')
            print('==================== PAPERS - TOKENS LIST ==================')
            for paper, matches in papers:
                print(paper)

                for match in matches:
                    print('\t' + match)

                print('\n')

        # print findWholeWord('based')('“Android-based Disease Monitoringn')
        # for row in csvData:
        # '(\sOR\s)|(\sAND\s)'     print(row[1])
