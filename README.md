# CSC3015-DataAnalytics

## create your own venv
> "C:\Users\USER\AppData\Local\Programs\Python\Python310\python.exe" -m venv venv </br>
or 'python -m venv venv'

## main point is data preprocessing
### what ive done so far:
- data clean for uwb_dataset_part1.csv
- feature extraction to create MEAN and STD features
- RFC to find most important features
- apply PCA to reduce dimensions

### what i think we can try:
- mostly the same thing 
- but use lasso regression instead of rfc.
- can also try full dimension reduction for pca, since i only tried hybrid approach 
- ye feel free to experiment more!