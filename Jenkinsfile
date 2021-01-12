pipeline{
    agent any
    stages{
        stage("Build"){
            steps{
                echo "========executing A========"
                //Set the version
                sh ''"VERSION=$BUILD_NUMBER" > .env'
                sh 'cat .env'
                //Build the application
                sh 'docker-compose build module'
            }
            post{
                always{
                    echo "========always========"
                }
                success{
                    echo "========A executed successfully========"
                }
                failure{
                    echo "========A execution failed========"
                }
            }
        }
        stage("Test"){
            steps{
                echo "========executing Test========"
                sh 'docker build -f Test/Dockerfile -t test-image .'
            }
            post{
                always{
                    echo "========always========"
                }
                success{
                    echo "========A executed successfully========"
                }
                failure{
                    echo "========A execution failed========"
                }
            }
        }
    }
    post{
        always{
            echo "========always========"
        }
        success{
            echo "========pipeline executed successfully ========"
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
}