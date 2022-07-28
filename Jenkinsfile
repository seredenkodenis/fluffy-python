pipeline {
    agent { label 'apps'}
    environment {
        sonar = credentials('jenkins-sonar-qube')
    }
    stages {
        stage('Scan') {
            steps{
                 sh """
                /opt/sonar-scanner/bin/sonar-scanner -Dsonar.projectKey=Fluffy-python -Dsonar.sources=. -Dsonar.host.url=https://sonar.cube-bit.ml -Dsonar.login=$sonar
                """
            }
        }
        stage('start') {
            steps {
                sh 'pwd'
                dir('/opt/agent/workspace/sonar/bitcoin-warner') {
                    sh 'pwd'
                    sh 'ls'
                    sh "python3 warning.py"
                }
            }
        }
    }
}