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
                python3 -m venv venv
                ls
                '''
            }
        }

        
        stage('Run Python') {
            steps {
                sh 'bash -c "source venv/bin/activate && python script.py"'
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
