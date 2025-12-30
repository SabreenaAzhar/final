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
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
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
                bat 'mkdir C:\\temp || exit 0'
                bat 'copy app.py C:\\temp\\'
            }
        }
    }
}
