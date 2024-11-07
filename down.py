from flask import Flask, request, render_template, send_file
from pytube import YouTube
import os

app = Flask(__name__)

# Route to display the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle the video download
@app.route('/download', methods=['POST'])
def download_video():
    # Get the YouTube URL from the form
    video_url = request.form['video_url']
    
    try:
        # Create a YouTube object using the URL
        yt = YouTube(video_url)
        
        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()
        
        # Set the download path to the current working directory
        download_path = os.getcwd()
        
        # Download the video
        stream.download(download_path)
        
        # Return a success message
        return f"Download complete! The video '{yt.title}' has been downloaded successfully."

    except Exception as e:
        # Return an error message if something goes wrong
        return f"An error occurred: {str(e)}"

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
