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
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }

        stage('Build') {
            steps {
                bat 'echo Build completed'
            }
        }

        stage('Deploy') {
            steps {
                bat 'copy app.py C:\\temp\\'
            }
        }
    }
}
