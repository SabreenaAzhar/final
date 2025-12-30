pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Upgrade pip first
                bat 'python -m pip install --upgrade pip'
                // Install all packages including pytest
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run pytest after installation
                bat 'python -m pytest'
            }
        }

        stage('Build') {
            steps {
                bat 'echo Build completed'
            }
        }

        stage('Deploy') {
            steps {
                // Create folder if it doesn't exist
                bat 'mkdir C:\\temp || exit 0'
                // Copy app.py to temp folder
                bat 'copy app.py C:\\temp\\'
            }
        }
    }
}
