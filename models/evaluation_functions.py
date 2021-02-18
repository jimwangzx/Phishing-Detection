import matplotlib.pyplot as plt
from sklearn import metrics
import seaborn as sns


def print_accuracies(model, x_train, y_train, x_cross, y_cross, x_test, y_test):
    print("Caclulating Accuracies ...")
    train_predicts = model.predict(x_train)
    print('\nTraining f1 Score:', metrics.f1_score(y_train, train_predicts))
    print('Training Accuracy:', metrics.accuracy_score(y_train, train_predicts))

    cross_predicts = model.predict(x_cross)
    print('\nCross Validation f1 Score:',
          metrics.f1_score(y_cross, cross_predicts))
    print('Cross Validation Accuracy:',
          metrics.accuracy_score(y_cross, cross_predicts))

    test_predicts = model.predict(x_test)
    print('\nTesting f1 Score:', metrics.f1_score(y_test, test_predicts))
    print('Testing Accuracy:', metrics.accuracy_score(y_test, test_predicts))
    return train_predicts, cross_predicts, test_predicts


def confusion_matrix_plot(y_true, y_predict, title='Confusion Matrix'):
    confusion_data = metrics.confusion_matrix(
        y_true, y_predict, normalize='true')

    fig, ax = plt.subplots(figsize=(5, 5))

    # annot=True to annotate cells
    sns.heatmap(confusion_data, cmap='Greens', annot=True)

    plt.title(title)
    plt.xlabel('Predicted Labels')
    plt.ylabel('True Labels')
    ax.set_xticklabels(['Non-Phishing', 'Phishing'])
    ax.set_yticklabels(['Non-Phishing', 'Phishing'])
    plt.show()
