def integer_formatter(x, pos):
    """
    Format the x-axis tick labels as integers.

    Parameters:
    - x (float): The tick value to be formatted. This is the position on the x-axis
      where the label will be displayed.
    - pos (int): The position index of the tick label. While this parameter is
      required by the formatter function's signature, it is not used in this function.

    Returns:
    - str: The formatted tick label as an integer (string format).
    """
    return f'{int(x)}'

def sumSameParity(n, k):

  """
    Determines if it is possible to express the integer 'n' as the sum of 'k' positive integers,
    all having the same parity (either all odd or all even). If possible, it returns "YES" followed
    by the integers, otherwise returns "NO".

    Parameters:
    n (int): The integer to be expressed as the sum of 'k' integers. It must be a positive integer (1 <= n <= 10^9).
    k (int): The number of terms in the sum. All terms must share the same parity (1 <= k <= 100).

    Returns:
    str: A string "YES" followed by the integers that sum to 'n', if such a representation is possible.
         Otherwise, it returns "NO" if it is not possible to represent 'n' as the sum of 'k' integers
         with the same parity.
  """

  """
    The first check evaluates three conditions where it is impossible to represent 'n' as the sum of 'k' addends with the same parity:
    1. If 'k' is greater than 'n', then it's impossible to represent 'n' as a sum of 'k' positive integers because the minimum sum of 'k' positive integers is at least 'k'.
    2. If 'n' is odd and 'k' is even, it's impossible to represent 'n' as the sum of 'k' numbers with the same parity because the sum of an even number of odd integers is always
       even, and 'n' is odd.
    3. If 'n' is even and 'k' is odd, and 'k' is greater than 'n/2', it's impossible to represent 'n' as a sum of 'k' even integers. The minimum sum of 'k' even integers is '2*k',
       which would exceed 'n' if 'k > n/2'. Also, 'n' cannot be the sum of 'k' odd integers because the sum of an odd number of odd integers is always odd, but 'n' is even.
  """
  if (k > n or (n % 2 != 0 and k % 2 == 0) or (n % 2 == 0 and k % 2 != 0 and k > n / 2)):
    return("NO")

  # This list will store the 'k' addends that sum up to 'n' with the same parity.
  addends = []

  # If 'k' equals 'n', the only possible way to represent 'n' as a sum of 'k' numbers is by using 'k' ones (i.e., 'n' 1's), since the sum of 'k' ones equals 'n'.
  if (k == n):
    addends = [1] * k
    """
    The following condition handles two cases where 'n' can be represented as a sum of 'k' odd integers:
    Case 1: If 'n' is odd and 'k' is odd, and 'k < n' (which is ensured by the initial check), it's always possible to represent 'n' as a sum of 'k' odd integers.
    Case 2: If 'n' is even, 'k' is even, and 'k > n / 2', it's possible to represent 'n' as the sum of 'k' odd integers. This is because the sum of an even number of odd integers is
            even, and since 'k' exceeds 'n / 2', the minimum sum of 'k' even integers would exceed 'n'. Hence, we need to use odd integers instead.
    In both cases, the strategy is to use (k-1) ones, which are odd, and set the final addend as 'n - (k-1)' to ensure that the total sum equals 'n'.
    The number 'n - (k-1)' will always be odd because subtracting an odd number (i.e., (k-1)) from a number 'n', either odd or even, results in an odd number.
    """
  elif((n % 2 != 0 and k % 2 != 0) or (n % 2 == 0 and k % 2 == 0 and k > n / 2)):
    addends = [1] * (k - 1)
    addends.append(n - (k - 1))
    """
    Finally, this condition handles the case where 'n' is even and 'k' is less than or equal to 'n / 2'.
    Regardless of whether 'k' is even or odd, 'n' can always be written as the sum of 'k' even numbers. This is because the sum of any number of even integers is always even.
    The strategy here is to use (k-1) numbers equal to 2, and set the final addend as 'n - 2 * (k-1)' to ensure the total sum equals 'n'.
    The value 'n - 2 * (k-1)' will always be even, so the sum of the numbers will maintain the correct parity.
    """
  else:
    addends = [2] * (k - 1)
    addends.append(n - 2 * (k - 1))

  # Return "YES" to indicate that the solution exists, followed by the addends that sum up to 'n'.
  return("YES\n" + " ".join(map(str, addends)))

def get_season(month: int) -> str:
    """
    Determine the season for a given month.

    Parameters:
    ----------
    month : int
        The month as an integer, where 1 = January, 2 = February, ..., 12 = December.

    Returns:
    -------
    str
        The season corresponding to the provided month, as one of 
        'Winter', 'Spring', 'Summer', or 'Fall'.

    Notes:
    ------
    - The function assigns months to seasons based on the following rules:
        - Winter: December (12), January (1), February (2)
        - Spring: March (3), April (4), May (5)
        - Summer: June (6), July (7), August (8)
        - Fall: September (9), October (10), November (11)
    - This approach is based on meteorological seasons, where seasons are divided evenly into three months each.
    
    Example:
    -------
    >>> get_season(5)
    'Spring'
    >>> get_season(12)
    'Winter'
    """
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Fall'
    
def plot_time_intervals(time_intervals: list) -> dict:
    """
    Plot the number of reviews for each specified time interval and return counts.

    Parameters:
    ----------
    time_intervals : list of tuples
        A list of tuples where each tuple represents a time interval.
        Each tuple contains two strings: the start and end times in 'HH:MM:SS' format.

    Returns:
    -------
    dict
        A dictionary with each time interval as a key (formatted as 'start - end') 
        and the corresponding count of reviews as the value.

    Example:
    -------
    >>> plot_time_intervals([("00:00:00", "02:59:59"), ("03:00:00", "05:59:59")])
    
    - This will plot the number of reviews within each specified time interval.
    - It also returns a dictionary with the review counts for each interval.

    Notes:
    ------
    - Converts time intervals to `datetime.time` objects for efficient comparison.
    - Uses a single loop to apply boolean masks to the DataFrame for each interval, 
      avoiding repeated filtering operations for improved performance.
    - The plot displays each time interval on the x-axis with corresponding review counts, 
      and an average line is added to highlight the mean number of reviews.
    - The y-axis format is adjusted for readability, displaying review counts with commas.

    Plot Style:
    -----------
    - The plot uses Seaborn's 'colorblind' palette for accessibility.
    - An average line (in red) is added to indicate the mean review count across intervals.
    
    """
    # Convert time intervals to datetime.time objects outside the loop for efficiency
    interval_times = [(pd.to_datetime(start).time(), pd.to_datetime(end).time()) for start, end in time_intervals]
    interval_counts = {}
    import matplotlib.ticker as mtick 
    import seaborn as sns
    import matplotlib.pyplot as plt
    # Use a single loop to create boolean masks and count reviews in each interval
    for (start, end), label in zip(interval_times, [f'{start} - {end}' for start, end in time_intervals]):
        interval_mask = (df['timestamp_created'].dt.time >= start) & (df['timestamp_created'].dt.time <= end)
        interval_counts[label] = interval_mask.sum()  # Faster to sum the boolean mask than filtering the DataFrame

    # Plotting the number of reviews for each interval
    plt.figure(figsize=(16, 8))
    sns.barplot(x=list(interval_counts.keys()), y=list(interval_counts.values()), palette='colorblind', hue=list(interval_counts.keys()),
                legend=False, edgecolor='black', linewidth=1)
    plt.title('Number of Reviews by Time Interval')
    plt.xlabel('Time Intervals')
    plt.ylabel('Number of Reviews')
    plt.gca().yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: '{:,.0f}'.format(x)))
    plt.xticks(rotation=45)
    
    # Adding the mean line
    mean_reviews = sum(interval_counts.values()) / len(interval_counts)
    plt.axhline(y=mean_reviews, color='darkred', linestyle='--', label=f'Mean: {mean_reviews:,.0f}')
    plt.legend(loc='upper right')  
    plt.tight_layout()
    plt.show()

    return interval_counts




def sentiment_score(sentiment):
    value = 0
    if sentiment > 0.05:
        value = 4  # positive comment
    elif sentiment <= -0.05:
        value = 0  # negative comment
    else:
        value = 2  # neutral comment
    return value 
    '''Determines the sentiment score by attributing to the value of score a number which can be 4 0 or 2. 4 representing a 
positive comment, 0 a negative comment and 2 a neutral comment'''

def translatee(txt):

    if txt is None or txt.strip() == '':
        return ''  # Return an empty string for None or empty inputs
    try:
        translation = translator.translate(txt, dest="en")
        return translation.text  # Return only the translated text
    except Exception as e:
        return str(txt)  # Ensure that original text is returned as a string
        ''' Translates a given text in english'''
    