pipeline {
    agent { label 'apps'}

    stages {
        stage('Scan') {
            steps{
                sh 'ifconfig'
                sh '/opt/sonar-scanner/bin/sonar-scanner -Dsonar.projectKey=Fluffy-python -Dsonar.sources=. -Dsonar.host.url=https://sonar.cube-bit.ml -Dsonar.login=dd1604b0db9d0531be5c5b9679470db5a2466dda'
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