# Project Structure
```
Volleyball-Objects-Tracking
├── requirements
│   └── base.txt - all basic requirements for the project
├── videos
│   ├── akcja2.mp4
│   └── akcja3.mp4
├── .gitignore
├── VolleballObjectDetection.ipynb - jupyter notebook containing code to train the model
├── adjust_labels.py - script to adjust labels in datasets
├── best7.pt - trained model 
└── main.py - script to run the model and watch the results
```

# User's guide

The model is trained to detects players in a volleyball match. If you want to run the model on your custom video you will need to do serveral thinks:
- Clone the repository on your local machine using `git clone https://github.com/KacperST/Volleyball-Objects-Tracking.git`,
- Upload your video in mp4 format into `videos` directory,
- In `main.py` in line 16 change the "akcja2.mp4" to name of your video,
- In terminal, run the script using `python main.py` command.
