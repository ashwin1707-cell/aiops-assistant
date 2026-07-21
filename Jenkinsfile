pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking project...'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t aiops-assistant:latest .'
            }
        }

        stage('Verify Docker') {
            steps {
                bat 'docker images'
            }
        }
    }

    post {
        success {
            echo 'Build completed successfully!'
        }
        failure {
            echo 'Build failed.'
        }
    }
}