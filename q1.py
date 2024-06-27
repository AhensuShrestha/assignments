import numpy as np

#Average: Arithmetic mean (Average) is the sum of data divided by the number of data-points. It is a measure of the central location of data in a set of values which vary in range.
#Uses: Averages are used to summarize data and provide a simple measure of central tendency.
def compute_mean(data):
    """Compute the mean of a list of numbers."""
    return np.mean(data)

#Variance: variance is the squared deviation of a variable from its mean. Basically, it measures the spread of random data in a set from its mean or median value.
#Uses: Variance is used to quantify the dispersion or spread of data points.
def compute_variance(data):
    """Compute the variance of a list of numbers."""
    return np.var(data, ddof=1)

#Covariance: Covariance provides the measure of strength of correlation between two variable or more set of variables. 
#Uses: Covariance is used to determine the relationship between two variables. It’s a key component in statistical models and risk assessment.

def compute_covariance(data1, data2):
    """Compute the covariance between two lists of numbers."""
    return np.cov(data1, data2, ddof=1)[0, 1]

#Gaussian distribution: Gaussian distribution is a continuous probability distribution function which is symmetric about its mean and has a bell-shaped curve. It is one of the most used probability distributions.
#Uses: The Gaussian distribution is widely used in statistics to model real-valued random variables whose distributions are not known.
def gaussian_distribution(x, mean, variance):
    """Compute the Gaussian distribution value for a given x, mean, and variance."""
    return (1.0 / np.sqrt(2 * np.pi * variance)) * np.exp(-((x - mean) ** 2) / (2 * variance))


data = [15, 22, 28, 35, 42]
data1 = [11, 23, 34, 45, 56]
data2 = [18, 27, 36, 45, 54]

mean = compute_mean(data)
variance = compute_variance(data)
covariance = compute_covariance(data1, data2)
gaussian_value = gaussian_distribution(3, mean, variance)

print(f"Mean: {mean}")
print(f"Variance: {variance}")
print(f"Covariance: {covariance}")
print(f"Gaussian value at x=3: {gaussian_value}")

