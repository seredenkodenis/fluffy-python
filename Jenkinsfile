pipeline {
    agent { label 'apps'}

    stages {
        stage('Scan') {
             withCredentials([usernameColonPassword(credentialsId: 'jenkins-sonar-qube', variable: 'sonar')]) {
                 sh """
                /opt/sonar-scanner/bin/sonar-scanner -Dsonar.projectKey=Fluffy-python -Dsonar.sources=. -Dsonar.host.url=https://sonar.cube-bit.ml -Dsonar.login=$sonar
                """
                }
        }
        stage('start') {
            steps {
                sh 'cd bitcoin-warner'
                sh 'python3 warning.py'
            }
        }
    }
}