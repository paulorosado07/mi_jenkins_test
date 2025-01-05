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

        stage('Run Virtual Enviroment & Pip & App Flask') {
            steps {
                sh 'bash -c "source venv/bin/activate && pip install blinker click Flask Flask-Cors itsdangerous Jinja2 MarkupSafe Werkzeug && python3 main.py"'
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
