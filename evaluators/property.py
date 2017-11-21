import re

"""
Class to get the properties used for labeling
"""
class LabelingProperties:
    def __init__()

    def run(self, data):
        labeling_properties = self.analyze(data)
        print labeling_properties


    def analyze(self, data):
        labeling_properties = {}

        with open(data) as infile:
            for line in infile:
                tmp = line.split('\t')

                # use all datatype string
                if '^^<http://www.w3.org/2001/XMLSchema#string>' in tmp[2]:
                    if not tmp[1] in labeling_properties:
                        labeling_properties[tmp[1]] = 1
                    else:
                        labeling_properties[tmp[1]] += 1

                pattern = re.compile("<.*>")
                if not pattern.match(tmp[2]) and not 'XMLSchema' in tmp[2]:
                    if not tmp[1] in labeling_properties:
                        labeling_properties[tmp[1]] = 1
                    else:
                        labeling_properties[tmp[1]] += 1

        return labeling_properties