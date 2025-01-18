# Hex Code Image Processor

This project is a Flask-based web application that allows users to upload images and generate a hex color code table representing the colors in the image. Users can customize the level of granularity for the hex code table using a step size slider.

## Features

- **Image Upload**: Users can upload an image via a simple and intuitive web interface.
- **Hex Code Table Generation**: The application processes the image to display a table of hex color codes corresponding to the image pixels.
- **Step Size Customization**: Users can adjust the step size to control the resolution of the hex code table.
- **Dynamic Updates**: The hex table updates dynamically based on the selected step size.

## Live Demo

Access the live website here: [Hex Code Image Processor](https://hex-code-image.onrender.com/)&#8203;

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- PIL (Pillow)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/hex-code-image-processor.git
    cd hex-code-image-processor
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python app.py
    ```

4. Open the application in your browser at `http://127.0.0.1:5000`.

## Project Structure

- **app.py**: The main application file, including all Flask routes and image processing logic&#8203;.
- **templates/**:
  - **upload_page.html**: The homepage where users can upload an image&#8203;.
  - **hex_table.html**: Displays the hex code table and allows users to adjust the step size dynamically&#8203;.
- **static/**: Contains static files such as CSS for styling.
- **uploads/**: Directory for storing uploaded images.

## How It Works

1. Navigate to the homepage and upload an image.
2. The application processes the uploaded image to generate a hex code table with a default step size of 5.
3. Use the slider on the hex table page to adjust the step size and see the updated table.
4. The hex codes represent the colors in the image, and each table cell is styled with its respective color.

## Example Usage

1. Upload an image using the **Upload an Image to Get Hex Codes** form on the homepage.
2. View the generated hex code table.
3. Adjust the step size using the slider to refine the table resolution.

## Acknowledgments

- Flask: For creating a lightweight web framework.
- Pillow: For processing images.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

