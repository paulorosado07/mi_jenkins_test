pipeline {
    agent any
    environment {
        FLASK_APP = 'main.py'
    }
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Run Flask App') {
            steps {
                sh 'nohup flask run --host=0.0.0.0 --port=5000 &'
            }
        }
    }
}
