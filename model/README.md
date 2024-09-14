# Logistic Regression Model

This project is a logistic regression model trained on medical data to predict the presence of a disease (0 or 1).

## Table of Contents
- Installation
- Usage
- Docker
- Testing
- Contributing
- License

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Apxu2148/DiseasePredictionTest.git
    ```
2. Navigate to the project directory:
    ```bash
    cd C:\Python\HomeworkHeart
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the web interface:
```bash
python app.py
```

## Docker

To build the Docker image:

docker build -t homeworkheart:app .

To run the Docker container:

docker run -p 5000:5000 homeworkheart:app

## Testing

You can test the API endpoints using Postman or any other API testing tool. An example test request is provided in the file test_request.json.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.