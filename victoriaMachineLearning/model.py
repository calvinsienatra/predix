import numpy as np 
from sklearn.linear_model import LogisticRegressionCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
# from sklearn.preprocessing import LabelBinarizer

def convert_onehot(arr, max_val):
	result = np.zeros(shape=(max_val,))

	for index in arr:
		result[index] = 1

	return result

class Model:
	def __init__(self, train_X, train_y, test_X, test_y, num_attrib, model=None):
		train_X = [convert_onehot(train_X[i], num_attrib) for i in range(len(train_X))]
		test_X = [convert_onehot(test_X[i], num_attrib) for i in range(len(test_X))]
		self.train_X = train_X
		self.train_y = train_y
		self.test_X = test_X
		self.test_y = test_y
		self.predicted_y = None
		self.num_attrib = num_attrib
		
		if model == None:
			self.model = SVC(probability=True)
		else:
			self.model = model

	def set_model(self, new_model):
		self.model = new_model

	def fit(self):
		self.model.fit(self.train_X, self.train_y)

	def predict(self):
		self.predicted_y = self.model.predict(self.test_X)
		return self.predicted_y

	def predict_probabilities(self):
		return self.model.predict_proba(self.test_X)

	def compute_accuracy(self):
		return accuracy_score(self.test_y, self.predicted_y)

	def score(self):
		return self.model.score(self.test_X, self.test_y)

	def predict_instance(self, test_instance):
		test_instance = convert_onehot(test_instance, self.num_attrib)
		return self.model.predict([test_instance])[0]

	def predict_prob_instance(self, test_instance):
		test_instance = convert_onehot(test_instance, self.num_attrib)
		return self.model.predict_proba([test_instance])[0]

	def get_coef(self):
		return self.model.dual_coef_

	def find_closest_support_vector(self, test_instance, desired_label, get_distance=False):
		test_instance = convert_onehot(test_instance, self.num_attrib)
		sv = self.model.support_vectors_

		min_distance = self.num_attrib
		closest_vec = None

		for vector in sv:
			label = self.model.predict([vector])[0]

			if label == desired_label:
				diff = abs(test_instance-vector)
				distance = np.linalg.norm(diff)

				if distance < min_distance:
					min_distance = distance
					closest_vec = vector

		if get_distance:
			return closest_vec, min_distance
		else:
			return closest_vec

	def get_advice(self, test_instance, desired_label):
		closest_vec, min_distance = self.find_closest_support_vector(test_instance, desired_label, True)
		test_instance = convert_onehot(test_instance, self.num_attrib)

		diff_features = []

		for i in range(len(closest_vec)):
			if closest_vec[i] != test_instance[i]:
				diff_features.append(i)

		return diff_features


