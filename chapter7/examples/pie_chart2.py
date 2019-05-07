# This program displays a simple pie chart.
import matplotlib.pyplot as plt

def main():
    # Create a list of values.
    values = [20, 60, 80, 40]

    # Create a list of labels for values.
    slice_labels = ['1st Qtr', '2nd Qtr', '3rd Qtr', '4th Qtr']

    # Create a pie chart from the values.
    plt.pie(values, labels=slice_labels)

    # Add a title.
    plt.title('Sales by the Quarter.')
    
    # Display the pie chart.
    plt.show()

# Call the main function.
main()