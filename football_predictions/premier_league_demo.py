''' Premier League DEMO '''
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from football_predictions.data import premier_league as pl
import football_predictions.data.tools.encoding as enc
import football_predictions.data.tools.rolling_averages as rolling
import football_predictions.build_features as bf

premier_league_df = pl.download_premier_league_base_data()

# List of columns to keep for training
columns_to_keep = [
    'Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR',
    'HS', 'AS', 'HST', 'AST', 'HC', 'AC', 'HF', 'AF', 'HY', 'AY', 'HR', 'AR', 'AvgH', 'AvgD',
    'AvgA',
]

# Filter the DataFrame to keep only the columns of interest
pl_useful_df = premier_league_df[columns_to_keep]

# Preprocess base data
pl_useful_encoded_df = enc.encode_base_data(pl_useful_df)

# Add columns with rolling columns
columns_for_rolling_averages = [
    'FTHG', 'FTAG', 'HTHG', 'HTAG',
    'HS', 'AS', 'HST', 'AST', 'HC', 'AC',
    'HF', 'AF', 'HY', 'AY', 'HR', 'AR', 'FTR_code', 'HTR_code'
]

new_rolling_columns = [f'rolling_{col}' for col in columns_for_rolling_averages]
window_sizes = [2,3,4]
pl_final_df = pl_useful_encoded_df.groupby("HomeTeam").apply(
    lambda x:
        rolling.rolling_averages_for_window_sizes(x,columns_for_rolling_averages,window_sizes))

# Split data
train_df, test_df = train_test_split(pl_final_df, test_size=0.2, random_state=42)

# Create features and target
rolling_features = bf.generate_rolling_features(columns_for_rolling_averages, window_sizes)
X_train = bf.create_features_from_data_frame(train_df,rolling_features)
X_test = bf.create_features_from_data_frame(test_df,rolling_features)
y_train = bf.create_target_from_df(train_df)
y_test = bf.create_target_from_df(test_df)

# Train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions for each class with probabilities
y_pred_prob = model.predict_proba(X_test)

# Assign predictions to test data frame
test_df['PHW'] = y_pred_prob[:, 2]
test_df['PD'] = y_pred_prob[:, 1]
test_df['PAW'] = y_pred_prob[:, 0]
test_df['PR'] = model.predict(X_test)

# Create data frame with data useful for evaluation
predictions_df = test_df[['Date','HomeTeam','AwayTeam','FTR','FTR_code','AvgH', 'AvgD',
                          'AvgA','PHW','PD','PAW','PR']]

raw_prediction_evaluation_report = classification_report(
    predictions_df['FTR_code'], predictions_df['PR'])
print(raw_prediction_evaluation_report)
