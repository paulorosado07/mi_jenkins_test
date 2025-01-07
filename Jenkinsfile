pipeline {
    agent any
    environment {
        FLASK_APP = 'main.py'
        PATH = "$PATH:/var/lib/jenkins/.local/bin"
    }
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Run Flask App') {
            steps {
                sh 'flask run --host=0.0.0.0 --port=5000'
            }
        }
    }
}
