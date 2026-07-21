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
                sh 'docker build -t aiops-assistant:latest .'
            }
        }

        stage('Verify Docker') {
            steps {
                sh 'docker images'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker stop aiops-container || true
                docker rm aiops-container || true

                docker run -d \
                --name aiops-container \
                -p 5000:5000 \
                aiops-assistant:latest
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                sleep 5
                docker ps | grep aiops-container
                '''
            }
        }
    }

    post {
        success {
            echo 'Deployment completed successfully!'
        }

        failure {
            echo 'Deployment failed.'
        }
    }
}