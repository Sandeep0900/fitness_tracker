# Health and Fitness Analysis Web App

This repository contains a Flask-based web application designed to analyze health and fitness metrics, such as Body Mass Index (BMI) and calorie burn estimation, based on user input. It leverages a synthetic dataset to provide tailored fitness insights.

## Features
- **BMI Calculation**: Automatically calculates BMI based on height and weight.
- **Calorie Burn Prediction**: Estimates calories burned based on workout type and duration.
- **Health Status Assessment**: Classifies health status based on BMI values.
- **Simple and Intuitive UI**: User-friendly input forms and result display.

## Getting Started
### Prerequisites
1. Python 3.7+
2. Flask
3. Pandas
4. NumPy

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your_username/health-fitness-analysis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd health-fitness-analysis
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Dataset
Ensure the dataset file `gym_members_exercise_tracking_synthetic_data.csv` is present in the root directory. This file contains synthetic data to support predictions and analysis.

## Usage
1. Run the application:
   ```bash
   python app.py
   ```
2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```
3. Fill in the form with your details and submit to view your health analysis.

## File Structure
- `app.py`: Main application logic.
- `templates/`: Contains HTML templates for the web interface.
  - `index.html`: Form for user input.
  - `result.html`: Displays analysis results.
- `gym_members_exercise_tracking_synthetic_data.csv`: Dataset for analysis.

## Example Output
- **Input**:
  - Age: 25
  - Gender: Male
  - Weight: 70 kg
  - Height: 1.75 m
  - Workout Type: Cardio
  - Duration: 1 hour

- **Output**:
  - BMI: 22.86
  - Calories Burned: 560 kcal
  - Health Status: Healthy

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For questions or suggestions, feel free to reach out:
- GitHub: [Sandeep0900](https://github.com/Sandeep0900)
- Email: sandeesharma09@gmail.com

