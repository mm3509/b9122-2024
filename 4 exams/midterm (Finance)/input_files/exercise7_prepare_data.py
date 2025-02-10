import numpy as np


import exercise8_data


URL = "https://github.com/SandeepHonnali/Loan-Approval-Prediction-using-Machine-Learning/raw/refs/heads/main/1Copy%20of%20loan.csv"  # noqa: E501


def prepare_data(url=URL):

    # Lazy importing, because you don't run this on your system and it
    # only serves once.
    import pandas
    import io

    txt = exercise8_data.get_html(url)
    with open("loans.txt", "w+") as f:
        f.write(txt)

    df = pandas.read_csv(io.StringIO(txt))

    # Clean the data: only 1-year loans, and drop NA's.
    df.drop(df[df["Loan_Amount_Term"] != 360.0].index, inplace=True)

    outcome = "Loan_Status"
    features = ["ApplicantIncome", "LoanAmount"]

    df = df[[outcome] + features]
    for f in features:
        df[outcome] = np.log(df[outcome])
    df.dropna(inplace=True)

    with open("y.txt", "w+") as f:
        np.savetxt(f, df[outcome] == "Y")

    with open("x.txt", "w+") as f:
        np.savetxt(f, df[features])

if "__main__" == __name__:
    prepare_data()
