import random

global _15_PERCENT
_15_PERCENT = 0.15


def get_pos_classified_ids(prediction, threshold):
	
	def __higher_than_threshold(tupl):
		index, value = tupl
		return value >= threshold
		
	pos_classified = filter(
		lambda tupl: __higher_than_threshold(tupl), enumerate(prediction))
	indexes = [tupl[0] for tupl in pos_classified]
	return indexes

def get_total_err_pos_classified_ids(pos_classified_ids, target):
	return len(filter(lambda index: target[index] == 0, pos_classified_ids))

def get_total_err_neg_classified_ids(neg_classified_ids, target):
	return len(filter(lambda index: target[index] == 1, neg_classified_ids))

def get_total_correct_pos_classified_ids(pos_classified_ids, target):
	return len(filter(lambda index: target[index] == 1, pos_classified_ids))

def get_total_correct_neg_classified_ids(neg_classified_ids, target):
	return len(filter(lambda index: target[index] == 0, neg_classified_ids))

def get_total_pos_samples(target):
	return len(filter(lambda c: c == 1, target))

def get_total_neg_samples(target):
	return len(filter(lambda c: c == 0, target))

# Accuracy = proportion of correct classifications
def calc_accuracy(target, prediction, threshold):
	classz = map(lambda prob: 1 if prob >= threshold else 0, prediction)
	corect_classified = filter(
		lambda tupl: tupl[0] == tupl[1], zip(target, classz))
	total_corect_classified = len(corect_classified)
	return total_corect_classified * 1.0 / len(target)

	
# True Positive Rate = total of correct positive class / total of positive samples
def calc_TPR(target, prediction, threshold):
	pos_classified_indexes = get_pos_classified_ids(prediction, threshold)
	total_correct_pos_classified = get_total_correct_pos_classified_ids(pos_classified_indexes, target)
	total_pos_samples = get_total_pos_samples(target)
	return total_correct_pos_classified * 1.0 / total_pos_samples

# True Negative Rate = total of correct negative class / total of negative samples
def calc_TNR(target, prediction, threshold):
	pos_classified_indexes = get_pos_classified_ids(prediction, threshold)
	neg_classified_indexes = [i for i, c in enumerate(target) if i not in pos_classified_indexes]
	total_correct_neg_classified = get_total_correct_neg_classified_ids(pos_classified_indexes, target)
	total_neg_samples = get_total_neg_samples(target)
	return total_correct_neg_classified * 1.0 / total_neg_samples

# False Positive Rate = total erroneously classified as pos / total of negative samples
def calc_FPR(target, prediction, threshold):
	pos_classified_indexes = get_pos_classified_ids(prediction, threshold)
	total_err_pos_classified = get_total_err_pos_classified_ids(pos_classified_indexes, target)
	total_neg_samples = get_total_neg_samples(target)
	return total_err_pos_classified * 1.0 / total_neg_samples

# False Negative Rate = total erroneously classified as neg / total of positive samples
def calc_FNR(target, prediction, threshold):
	pos_classified_indexes = get_pos_classified_ids(prediction, threshold)
	neg_classified_indexes = [i for i, c in enumerate(target) if i not in pos_classified_indexes]
	total_err_neg_classified = get_total_err_neg_classified_ids(neg_classified_indexes, target)
	total_pos_samples = get_total_pos_samples(target)
	return total_err_neg_classified * 1.0 / total_pos_samples
	

def choose_threshold(target, prediction):	
	fprs_to_threshold = dict()
	tries_threshold = map(lambda x: x / 1000.0, range(0, 1010, 10))
	for try_threshold in tries_threshold:
		fpr = calc_FPR(target, prediction, try_threshold)
		diff = abs(_15_PERCENT - fpr)
		fprs_to_threshold[diff] = try_threshold
	min_fpr_diff = min(fprs_to_threshold.keys())
	threshold = fprs_to_threshold[min_fpr_diff]
	return threshold
	
def my_cross_tab(target, prediction):	
	threshold = choose_threshold(target, prediction)
	accuracy = calc_accuracy(target, prediction, threshold)
	TPR = calc_TPR(target, prediction, threshold)	
	TNR = calc_TNR(target, prediction, threshold)
	FPR = calc_FPR(target, prediction, threshold)
	FNR = calc_FNR(target, prediction, threshold)
	
	output = [threshold, accuracy, TPR, TNR, FPR, FNR]
	return output

if __name__ == "__main__":	
	
	target = map(int, raw_input().split())
	prediction = map(float, raw_input().split())
	output = my_cross_tab(target, prediction)
