# recordX: Student Record Management System
<p align="center">
  <img src="https://i.imgur.com/9N3nALp.jpg" align="center">
</p>

<br />
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#-introduction">Introduction</a></li>
    <li><a href="#-technologies-used">Technologies Used</a></li>
    <li><a href="#-project-structure">Project Structure</a></li>
    <li><a href="#-installation">Installation</a></li>
    <li><a href="#-usage">Usage</a></li>
    <li><a href="#-contributing">Contributing</a></li>
    <li><a href="#-licensing">Licensing</a></li>
  </ol>
</details>
<br />

## 🚀 Introduction
Welcome to RecordX, a tool built to provide efficient management and organisation of academic records in educational institutions. Engineered for simplicity and effectiveness, RecordX offers a user-friendly environment to seamlessly handle all create, delete, read, and update operations related to academic records.

<p align="center">
  <img src="https://i.imgur.com/yLx0D1p.png" align="center">
</p>

### ✨Key Features:
* **Intuitive Interface**: Navigate academic data effortlessly with our user-friendly interface.
* **Effortless Operations**: Perform create, delete, read, and update operations with ease.
* **Data Organisation**: Streamline the management and organisation of academic records effortlessly.
* **Enhanced Efficiency**: Save time and resources by leveraging RecordX's powerful capabilities.

Whether you're an administrator, teacher, or staff member, RecordX is designed to empower you in your daily tasks related to academic data management.

### 🌐 Deployed Site
Visit the [Deployed Site](https://scottandee.github.io/recordX/) to experience the Student Record Management System in action. Explore its features and see how it can revolutionise student record management for your institution.

### 🧠 The Team
* **Olayinkascott Andee**
  * Role: Developer
  * [Andee's LinkedIn](https://www.linkedin.com/in/olayinkascott-andee/)
<!-- ### Blogpost
For more in-depth information about the development journey, challenges, and insights gained during the creation of the Student Record Management System, check out the Project Blog Post. -->

<br />

## 💻 Technologies Used
### Frontend
![jQuery](https://img.shields.io/badge/jquery-%230769AD.svg?style=for-the-badge&logo=jquery&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
### Backend
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

<br />

## 📂 Project Structure
### Backend `/backend`
This folder contains all backend-related logic, including:
* `/app`: The main Flask application.
  * `api`: API controllers for handling client requests and responses 
  * `/models`: Data declaration for each of the resources.
  * `/utils`: Reusable functions used throughout the app.
* `run_app.py`: Script for creating and running the Flask application.
* `config.py`: Configuration settings for the Flask application.
* `/tests`: Unit tests for the backend application.
### Frontend `/frontend`
This folder contains all frontend-related files, including:
* `/scripts`: JavaScript files for rendering dynamic content
* `/styles`: Stylesheets for styling HTML elements.
* `/images`: Images and SVGs used in the project.
* `*.html`: HTML files that define the structure and content of the web pages.
### Docs `/docs`
This folder contains the deployed version of the frontend, which makes API calls to the deployed backend server at `https://www.scottandee.tech/api/v1/`.
### Others
* `requirements.txt`: Contains the project's dependencies.
* `LICENSE.txt`: Contains the MIT license for the project.
* `README.md`: Provides vital information about the project.

<br /> 

## 🔨 Installation
### Setup Virtual Environment (Optional)
1. Install `virtualenv`
   ```bash
   pip3 install virtualenv
   ```
2. Create a virtual environment with `virtualenv`

   ```bash
   virtualenv recordX
   ```
3. Activate the virtual environment
   * First off, cd into the virtual environment you just created
     ```bash
     cd recordX/
     ```
   * Now activate the virtual environment with this command
     ```bash
     source bin/activate
     ```
     Your terminal prompt should look like ```(recordX) scottandee@scottandee-VirtualBox:~/recordX$```

### Clone the Repository and Install all Dependencies
4. Clone the repository.
   ```bash
   git clone git@github.com:scottandee/recordX.git
   ```
   You can now cd into this cloned repository
   ```bash
   cd recordX/
   ```
5. Install the requirements.
   ```bash
   pip3 install -r requirements.txt
   ```
### Start the Backend Server
6. Start the backend server.
   * cd into the backend directory
     ```bash
     cd backend/
     ```
   * run the start-up script
     ```bash
     python3 run_app.py
     ```
<p align="center">
  <img src="https://i.imgur.com/PcGyHrQ.png" align="center">
</p>

### Open the `dashboard.html` File
7. In another window, open the frontend dashboard
    * cd into the frontend directory
      ```bash
      cd ../frontend
      ```
    * Open the dashboard in your default browser
      ```bash
      open dashboard.html
      ```
<p align="center">
  <img src="https://i.imgur.com/8ElTFfX.png" align="center">
</p>

<br />

## 🎮 Usage
### Create a New Record
* Navigate to any of the student, course, faculty, or department sections of the navbar.
* Click on the Create button.
* Fill in the required information
* Submit the form to add a new record.

### View Detailed Information about a Record
* Click on the cards representing each record to access detailed information about it.

### Search for a Record
* Click on the search bar.
* Use the search bar to enter keywords related to the resource you're looking for.
* Refine your search by applying filters as necessary

### Update an Existing Record
* Click on the vertical ellipsis icon at the top right corner of the record to be updated.
* Update the values as desired in the edit form
* Submit the form to save the updated information.

### Delete an Unwanted or Irrelevant Record
* Click on the vertical ellipsis icon at the top right corner of the record to be deleted.
* Select "Delete" and confirm the action in the confirmation message.

### Monitor Records at Dashboard
* Navigate to the dashboard section
* View the count of the different records

<br />

## 🤝 Contributing
Here are some steps to follow when contributing to this project:
1. Fork the repository
2. Clone the repository into your machine
3. Install all dependencies from the `requirements.txt` file
4. Run the tests
5. Make your changes
6. Write tests for your changes and make sure they pass
7. Commit your changes
8. Push your changes to your fork
9. Create a pull request to the original repository

<br />

## 📜 Licensing
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

Copyright (c) 2023 Olayinkascott Andee.

See the LICENSE file for more information.
