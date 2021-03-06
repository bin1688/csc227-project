
class JSONGolferRoundScores(object):
    def __init__(self, tournGolferId, roundId):
        # Add needed code - note initialize all hole scores to 0
        self.model = "golfer.golferroundscores"
        self.fields = {"grs_tourn_golfer": tournGolferId,
                       "grs_round": roundId,
                       "grs_total_score": 0,
                       "grs_hole1_score": 0,
                       "grs_hole2_score": 0,
                       "grs_hole3_score": 0,
                       "grs_hole4_score": 0,
                       "grs_hole5_score": 0,
                       "grs_hole6_score": 0,
                       "grs_hole7_score": 0,
                       "grs_hole8_score": 0,
                       "grs_hole9_score": 0,
                       "grs_hole10_score": 0,
                       "grs_hole11_score": 0,
                       "grs_hole12_score": 0,
                       "grs_hole13_score": 0,
                       "grs_hole14_score": 0,
                       "grs_hole15_score": 0,
                       "grs_hole16_score": 0,
                       "grs_hole17_score": 0,
                       "grs_hole18_score": 0,
                       }


def main():
    # Add needed code
    standaloneDjango()
    jsonStr = getJSONstr()
    writeJSONstr(jsonStr)


def standaloneDjango():
    # Add needed code
    import os
    import django
    import json

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wgt_site.settings")
    django.setup()


def getTournID():
    # Add needed code
    from django.db import models
    from tournament.models import Tournament

    newTournObj = Tournament.objects.get(tourn_name="Oak City Championship")
    return newTournObj.tourn_id


def getGolferID(name_to_get):
    # Add needed code
    from django.db import models
    from golfer.models import Golfer

    newGolfer = Golfer.objects.get(golfer_name=name_to_get)

    return newGolfer.golfer_id


def getTournGolferID(golfer_id, tourn_id):
    # Add needed code
    global tourn_golfer_id
    from django.db import models
    from golfer.models import TournGolfer

    tourn_golfers = TournGolfer.objects.filter(tg_tourn=tourn_id)

    for tourn_golfer in tourn_golfers:
        if tourn_golfer.tg_golfer.golfer_id == golfer_id:
            tourn_golfer_id = tourn_golfer.tg_id
            break

    return tourn_golfer_id


def getRoundIDs(tourn_id):
    # Add needed code
    from golfer.models import Round

    round1_id = 0
    round2_id = 0

    tourn_rounds = Round.objects.filter(round_tourn_id=tourn_id)

    for round in tourn_rounds:
        if round.round_day == "Sat":
            round1_id = round.round_id

        else:
            round2_id = round.round_id

    return round1_id, round2_id


def readScores():
    import csv

    # Add needed code
    # This is the same code as in your
    # create_golfer_scores function from Project 1
    round_scores_list = []

    try:
        input_file = open("golferScores.csv", 'r')

        file_lines = csv.reader(input_file)

        golfer_scores_list = list(file_lines)

        input_file.close()

        for round_score in golfer_scores_list:
            round_scores_list.append(round_score)

    except IOError:
        print("File Not Found Error.")

    return round_scores_list


def getJSONstr():
    # Add needed code
    import json

    scores = readScores()
    tourn_id = getTournID()
    round1_id, round2_id = getRoundIDs(tourn_id)
    round_scores = []

    for score in scores:
        golfer_id = getGolferID(score[0])
        tourn_golfer_id = getTournGolferID(golfer_id, tourn_id)

        if score[2] == 'Sat':
            grs = JSONGolferRoundScores(tourn_golfer_id, round1_id)
        else:
            grs = JSONGolferRoundScores(tourn_golfer_id, round2_id)

        scores_list = list(map(int, score[3:]))

        round_score = 0
        j = 1
        for sc in scores_list:
            grs.fields["grs_hole{}_score".format(j)] = sc
            round_score = round_score + sc
            j = j + 1

        grs.fields["grs_total_score"] = round_score

        json_grs = json.dumps(grs.__dict__)
        round_scores.append(json_grs)

    jsonStr = str(round_scores).replace("'", '')

    return jsonStr


def writeJSONstr(jsonStr):
    # Add needed code
    outFile = open('golfer_round_scores_data.json', 'w')
    outFile.write(jsonStr)
    outFile.close()


main()
