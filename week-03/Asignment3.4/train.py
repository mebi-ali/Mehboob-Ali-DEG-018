import fire
import mlflow
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def preprocess_data(df: pd.DataFrame):

    df = df[['alcohol', 'flavanoids', 'color_intensity', 'proline', 'target' ]]
    return df


# we use scikit-learn pipeline to package standarization into single object with model
def setup_logistic_pipeline(random_state):
    lr = LogisticRegression(random_state=random_state)
    pipe = make_pipeline(StandardScaler(), lr)
    return pipe


def split_data(df, random_state):
    target = df.columns[-1]
    y = df[target]
    X = df[df.columns[0:-1]]

    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size = 0.25, random_state = random_state)
    return X_train, X_test, Y_train, Y_test


def track_with_mlflow(model, X_test, Y_test, mlflow, model_metadata):
    mlflow.log_params(model_metadata)
    mlflow.log_metric("accuracy", model.score(X_test, Y_test))
    mlflow.sklearn.log_model(model, "lr", registered_model_name="Logistic_reg")


def main(file_name: str, random_state: int):
    df = preprocess_data(pd.read_csv(file_name))

    X_train, X_test, Y_train, Y_test = split_data(df, random_state)
    # let's check some other k
    rs_list = range(0, random_state)

    for rand in rs_list:
        with mlflow.start_run():
            lr_pipe = setup_logistic_pipeline(random_state)
            lr_pipe.fit(X_train, Y_train)
            model_metadata = {"random_state": random_state}
            track_with_mlflow(lr_pipe, X_test, Y_test, mlflow, model_metadata)


if __name__ == "__main__":
    fire.Fire(main)
