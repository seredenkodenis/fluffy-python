pipeline {
    agent { label 'apps'}

    stages {
        stage('Scan') {
            def scannerHome = tool 'sonar';
            withSonarQubeEnv() {
                sh "${scannerHome}/bin/sonar-scanner"
            }
        }
        stage('start') {
            steps {
                sh 'cd bitcoin-warner'
                sh 'python warning.py'
            }
        }
    }
}