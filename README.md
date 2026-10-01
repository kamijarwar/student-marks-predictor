# student-marks-predictor
A simple ML project that predicts student marks from study and sleep hours using Linear Regression.
# Student Marks Predictor

A simple machine learning project that predicts a student's marks based on daily **study hours** and **sleep hours**, using **Linear Regression**.

Built as a beginner-friendly project while learning Machine Learning with Python.

---

## Features

- Takes study hours and sleep hours as input
- Trains a Linear Regression model on sample student data
- Predicts marks out of 100
- Gives a short motivational message based on the predicted marks

---

## How It Works

1. **Data:** a small dataset of `[study hours, sleep hours]` and the marks scored.
2. **Training:** `LinearRegression` from scikit-learn learns the best-fit formula:

```
   marks = (a x study_hours) + (b x sleep_hours) + c
```

3. **Prediction:** the user enters their own hours and the model applies the learned formula.
4. **Output:** predicted marks (kept between 0 and 100) with a feedback message.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/student-marks-predictor.git
cd student-marks-predictor
```

Install the requirements:

```bash
pip install -r requirements.txt
```

---

## Usage

```bash
python marks_predictor.py
```

### Example

```
Daily Studying Hours: 6
Daily Sleeping Hours: 5

Predicted Marks: 72.4/100
Good, but you need to improve.
```

---

## Project Structure

```
student-marks-predictor/
├── marks_predictor.py   # main program
├── requirements.txt     # dependencies
├── README.md            # project documentation
└── .gitignore
```

---

## Tech Stack

- Python 3
- NumPy
- scikit-learn

---

## Limitations

- The training data is small and sample-based, so predictions are only estimates.
- Only two features are used (study hours and sleep hours).

---

## Future Improvements

- [ ] Use real quiz/exam data
- [ ] Add more features such as attendance
- [ ] Plot a graph of the data and the fitted line
- [ ] Show the learned coefficients (`model.coef_`, `model.intercept_`)
- [ ] Build a simple web interface

---

## Author

**Kamran Jarwar (Kami)**
IT Student, Quaid-e-Awam University of Engineering, Science and Technology

Feel free to fork this project and improve it.
