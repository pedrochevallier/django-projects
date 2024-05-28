# My Django Project

This Django project contains three main features: a QR code generator, a URL shortener, and a map game. Below you will find a brief description of each feature, how to set up the project, and how to contribute.

## Features

### 1. QR Code Generator
The QR code generator allows users to generate QR codes for any input text. It uses the `qrcode` library to create the QR codes.

### 2. URL Shortener
The URL shortener enables users to create shortened URLs that redirect to longer URLs. It is useful for sharing links more conveniently.

### 3. Map Game
The map game is an interactive game where users are given two random points representing countries. The user needs to guess where a third point (country) is located.

## Setup Instructions

Follow these steps to set up the project on your local machine.

### Prerequisites
- Python 3.x
- Django 3.x or later
- Redis

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the migrations:**

    ```sh
    python manage.py migrate
    ```


6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

7. Open your browser and go to `http://127.0.0.1:8000/` to see the project running.

## Usage

### QR Code Generator
- Navigate to `/qr-generator/`.
- Enter the text you want to encode.
- Click "Generate QR Code" to create and display the QR code.

### URL Shortener
- Navigate to `/url-shortener/`.
- Enter the long URL you want to shorten.
- Click "Shorten URL" to get the shortened URL.

### Map Game
- Navigate to `/map-game/`.
- You will be presented with two points representing countries.
- Guess where the third point (country) is located by clicking on the map.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

