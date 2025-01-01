pipeline {
    agent any

    environment {
        VENV = 'venv'
        FLASK_APP = 'main.py'
    }

    stages {
        stage('version') {
            steps {
                sh 'python3 --version'
            }
        }
        
        stage('Setup Environment') {
            steps {
                sh '''
                python3 -m venv $VENV
                source $VENV/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        
        stage('Start Application') {
            steps {
                sh '''
                source $VENV/bin/activate
                python3 main.py
                '''
            }
        }
    }


    post {
        success {
            echo 'Flask app is running successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
