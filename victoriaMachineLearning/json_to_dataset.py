import json
import random
from model import *
import pickle
from sklearn.externals import joblib

class Indexer:
	def __init__(self, mylist=[]):
		self.list = mylist

	def get_index(self, object):
		return self.list.index(object)

	def get_object(self, index):
		if index < len(self.list):
			return self.list[index]
		else:
			return ''

	def add(self, new_list):
		for element in new_list:
			if element not in self.list:
				self.list.append(element)

	def __len__(self):
		return len(self.list)

	def __repr__(self):
		string = ''
		for i, obj in enumerate(self.list):
			string += str(i) + ': ' + obj + '\n'

		return string


# input: a dictionary of profiles
def feature_extractor(profile, indexer):
	keys = profile.keys()
	features = []

	for key in keys:
		if 'Name' not in key: # bypass name
			value = profile[key]

			if 'list' in str(type(value)): # value is list
				for element in value:
					element = element.replace(' ', '_')
					feature_name = key + ':' + element
					features.append(feature_name.lower())

			else:
				element = value.replace(' ', '_')
				feature_name = key + ':' + element
				features.append(feature_name.lower())

	indexer.add(features)
	return features

def get_class_indexer(raw_data, indexer):
	# convert class to index
	classes = []
	for profile in raw_data:
		feature_extractor(profile, indexer)

		for key in profile.keys():
			if key == 'currentCompany':
				if profile[key] not in classes:
					classes.append(profile[key])

	class_indexer = Indexer(classes)
	return class_indexer

# =======================================================
# convert a JSON profile to a list of indices
# =======================================================
def convert_profile(profile, indexer):
	keys = profile.keys()
	mylist = []
	label = ''

	for key in keys:
		value = profile[key]
		if 'Name' not in key and 'current' not in key:
			feature_name = ''

			if 'list' in str(type(value)): # value is list
				for element in value:
					element = element.replace(' ', '_')
					feature_name = key + ':' + element
					feature_name = feature_name.lower()

					index = indexer.get_index(feature_name)
					mylist.append(index)

			else:
				element = value.replace(' ', '_')
				feature_name = key + ':' + element
				feature_name = feature_name.lower()

				index = indexer.get_index(feature_name)
				mylist.append(index)

		elif 'currentCompany' in key:
			label = class_indexer.get_index(value)
	
	return mylist, label

# =======================================================
# X = original data
# y = original label
# indexer = feature indexer
# num_data = number of data to be generated
# =======================================================
def generate_synthetic_data(X, y, indexer, num_data):
	new_X = []
	new_y = []

	attributes_class = {}
	attributes_meta = {}

	for i in range(len(X)):
		data = X[i]
		label = y[i]

		# group into class
		if label in attributes_class.keys():
			for feature in data:
				if feature not in attributes_class[label]:
					attributes_class[label].append(feature)
		else:
			attributes_class[label] = list(data)

		# extract meta
		for feature in data:
			feature_name = indexer.get_object(feature)
			meta = feature_name.split(':')[0]

			if meta in attributes_meta.keys():
				if feature not in attributes_meta[meta]:
					attributes_meta[meta].append(feature)
			else:
				attributes_meta[meta] = [feature]

	# start generating synthetic data
	# class proportion
	proportion = int(num_data / len(attributes_class.keys()))

	for label in attributes_class.keys():
		for j in range(proportion):
			sample_x = []
			sample_y = label

			for meta in attributes_meta.keys():
				attributes = set(attributes_class[label]).intersection(attributes_meta[meta])

				if meta == 'skills':
					random_number = 10
				elif 'univ' in meta or 'major' in meta:
					random_number = 1
				else:
					random_number = 3

				if len(attributes) > random_number:
					chosen = random.sample(attributes, random_number)
				else:
					chosen = list(attributes)
				sample_x.extend(chosen)

			if sample_x not in new_X:
				new_X.append(sample_x)
				new_y.append(sample_y)

	return new_X, new_y


def generate_data():
	filename = 'schema.json'
	f = open(filename, 'r')
	raw_data = json.loads(f.read())

	indexer = Indexer()
	class_indexer = get_class_indexer(raw_data, indexer)

	# for i in range(len(indexer)):
	# 	print(indexer.get_object(i),end=',')

	# for i in range(len(class_indexer)):
	# 	print(class_indexer.get_object(i),end=',')

	dataset_x = []
	dataset_y = []

	for profile in raw_data:
		mylist, label = convert_profile(profile, indexer)
		dataset_x.append(mylist)
		dataset_y.append(label)

	new_X, new_y = generate_synthetic_data(dataset_x, dataset_y, indexer, 100000)
	dataset_x.extend(new_X)
	dataset_y.extend(new_y)

	zipped = list(zip(dataset_x, dataset_y))
	random.shuffle(zipped)

	dataset_x, dataset_y = zip(*zipped)

	train_X = []
	train_y = []

	test_X = []
	test_y = []

	for i, sample in enumerate(dataset_x):
		label = dataset_y[i]

		if i % 2 == 0 or i % 5 == 0 or i % 7 == 0:
			train_X.append(sample)
			train_y.append(label)
		else:
			if sample not in train_X:
				test_X.append(sample)
				test_y.append(label)

	train_file = open('training.csv','w')
	test_file = open('test.csv', 'w')

	for i in range(len(train_X)):
		train_file.write(str(train_X[i]) + ', ' + str(train_y[i])+'\n')

	for i in range(len(test_X)):
		test_file.write(str(test_X[i]) + ', ' + str(test_y[i])+'\n')

# generate_data()

def read_file_to_data(filename):
	f = open(filename, 'r')
	lines =  f.readlines()

	X = []
	y = []

	for line in lines:
		split = line.split('], ')
		data = [int(xx) for xx in split[0][1:].split(', ')]
		label = int(split[1].strip())

		X.append(data)
		y.append(label)

	return X, y

def main():
	arr_indexer = open('indexer.csv', 'r').readline().split(',')
	indexer = Indexer(arr_indexer)

	arr_class = open('class_indexer.csv', 'r').readline().split(',')
	class_indexer = Indexer(arr_class)

	train_X, train_y = read_file_to_data('training.csv')
	test_X, test_y = read_file_to_data('test.csv')

	new_model = joblib.load('model.pkl')
	model = Model(train_X, train_y, test_X[:10000], test_y[:10000], len(indexer), model=new_model)
	# model.fit()
	predicted = model.predict()
	prob = model.predict_probabilities()
	# accuracy = model.compute_accuracy()
	# coef = model.get_coef()

	# print(predicted)
	# print(prob)
	# print("accuracy", accuracy)
	# print(coef.shape)

	# print(model.predict_instance(test_X[-1]))
	# print(sum(model.predict_prob_instance(test_X[-1])))
	# print(model.model.support_vectors_.shape)
	# print(test_X[-1])
	# advice = model.get_advice(test_X[-1], 8)
	# arr = sorted([indexer.get_object(i) for i in advice])

	# for x in arr:
	# 	print(x)

	# joblib.dump(model.model, 'model.pkl')
	# 
	print("something")
