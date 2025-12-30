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
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build') {
            steps {
                sh 'echo "Build step done"'
            }
        }

        stage('Deploy') {
            steps {
                sh 'cp app.py /tmp/'
            }
        }
    }
}
