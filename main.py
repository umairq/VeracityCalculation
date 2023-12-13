import json

from algorithms.jaccard.jaccard_coeff2 import jaccard_coeff
from algorithms.adamic_adar.adamic_adar import adamic_adar
import logging as log
WTFN = 'logdegree'

measure_map = {
	'jaccard': {
		'measure': jaccard_coeff,
		'tag': 'JC'
	}
    ,
	'adamic_adar': {
		'measure': adamic_adar,
		'tag': 'AA'
	}
	# ,
	# 'degree_product': {
	# 	'measure': preferential_attachment,
	# 	'tag': 'PA'
	# },
	# 'katz': {
	# 	'measure': katz,
	# 	'tag': 'KZ'
	# },
	# 'simrank': {
	# 	'measure': c_simrank,
	# 	'tag': 'SR'
	# },
	# 'pathent': {
	# 	'measure': pathentropy,
	# 	'tag': 'PE'
	# }
}

# Function to parse the JSONL file, extract triples, call jaccard_coeff function, and store results in a new JSONL file
def process_and_store_scores(input_file, output_file,measure,processed_claims):
    with open(input_file, 'r') as infile:
        for line in infile:
            data = json.loads(line)  # Using eval to parse JSONL lines (if this is safe in your context)
            triple = (data['triple'][1:-1].split("', '"))
            print("triple: ", triple)
            subject, predicate, obj = triple
            if data['claim'] in processed_claims:
                continue
            # Call jaccard_coeff function here with subject, predicate, and obj
            score = measure(subject.split("/")[-1], predicate.split("/")[-1], obj.split("/")[-1], linkpred=True)
            
            # Add the score to the existing data
            data["jaccard_score"] = score
            # exit(1)
            # data = json.loads(data)
            # Write the updated data (with score) to the output file
            with open(output_file, 'a') as outfile:
                json.dump(data, outfile)
                outfile.write("\n")





# def main(args=None):
selected_measure = 'jaccard'
# compute closure
measure_name = measure_map[selected_measure]['tag']
measure = measure_map[selected_measure]['measure']
s,p,o = "Q76", "P2860", "Q13133"
log.info('Computing {} for {} triples..'.format(measure_name, len(s)))


# Example usage
input_file_path = '/local/upb/users/u/uqudus/profiles/unix/cs/jaccord/VeracityCalculation/data/data_dev/output_triples_IRIs.jsonl'  # Replace with your input JSONL file path
# output_file_path = '/local/upb/users/u/uqudus/profiles/unix/cs/jaccord/VeracityCalculation/data/output_triples_IRIs_with_v_scores.jsonl'    # Replace with the desired output JSONL file path
output_file_path = '/local/upb/users/u/uqudus/profiles/unix/cs/jaccord/VeracityCalculation/data/data_dev/output_triples_IRIs_with_v_scores.jsonl'    # Replace with the desired output JSONL file path

with open(output_file_path, 'r') as file:
    lines2 = file.readlines()
processed_claims = []
processed_triples = []
for ll in lines2:
    claim1 = json.loads(ll)['claim']
    processed_triples.append(json.loads(ll))
    processed_claims.append(claim1)
    print("processed claim:"+claim1)


process_and_store_scores(input_file_path, output_file_path, measure,processed_claims)

# score = measure(s, p, o, linkpred=True)
# print("Score: ", score)
